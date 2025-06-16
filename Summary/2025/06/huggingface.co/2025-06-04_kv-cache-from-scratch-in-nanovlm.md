---
title: KV Cache from scratch in nanoVLM
source: https://huggingface.co/blog/kv-cache
author:
- Aritra Roy Gosthipaty
- Kashif Rasul
- Luis Wiedmann
- Andres Marafioti
- Pedro Cuenca
published: '2025-05-28T00:00:00Z'
fetched: '2025-06-04T13:30:57Z'
tags:
- codex
- ai
- performance
- pytorch
- llm
image: https://huggingface.co/blog/assets/kv-cache/thumbnail.png
---

## 要約

nanoVLMリポジトリで**KVキャッシュ**をゼロから実装し、生成速度を**38%**向上させた経験を紹介する。文章生成では過去のトークン列を毎回再計算する必要があるが、各層のSelf-Attentionで使用するKey/Valueを保存することで計算を省略できる。実装では入力処理の**prefill**とキャッシュを使う**decode**の二段階に分け、位置エンコーディングを管理する`start_pos`で整合性を保つ。手法の要点と効率化のメリットを、小規模コードベースを用いて学ぶ狙いが語られている。

## 本文

# KV Cache from scratch in nanoVLM

We have implemented KV Caching from scratch in our [nanoVLM](https://github.com/huggingface/nanoVLM) repository (a small code base to train your own Vision Language Model with pure PyTorch). This gave us a **38%** of speedup in generation. In this blog post we cover KV Caching and all our experiences while implementing it. The lessons learnt are general and can be applied to all autoregressive language model generations. Implementing from scratch on a small codebase is a great learning experience, come along for the ride!

[![bar plot showcasing improvement in generation speed](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/kv-cache/speed_improved.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/kv-cache/speed_improved.png)

## Introduction

Autoregressive language models generate text by sampling _one token at a time_. During inference, the model processes a given input sequence, predicts the next token, appends it to the sequence, and repeats this process until some stopping criterion:

[![diagram for autoregression](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/kv-cache/autoregression.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/kv-cache/autoregression.png)

This step-by-step generation is inherently sequential:

- To generate token ti+1 t\_{i+1} ti+1​, the model must consider the entire sequence from t0 t_0 t0​ to ti t_i ti​. From the first instance in the above example ti+1 t\_{i+1} ti+1​ would be `the` , while all the previous tokens t0 t_0 t0​ to ti t_i ti​ would be `[What, is, in,]`.
- Although transformers are internally parallel, each new prediction requires a full forward pass through all transformer layers, which incurs a quadratic memory/compute in terms of the sequence length.

This repetition also leads to computational **redundancy**. In this post, we explore **KV Caching**, an optimisation technique that mitigates this inefficiency.

Table of contents:

## Revisiting the Transformer Architecture

Before diving into caching, let’s revisit how attention operates in transformer models. A Transformer language model consists of stacked layers, each composed of:

- Multi-head self-attention
- Feed-forward network (MLP)
- Residual connections and layer normalisation

To understand **where KV Caching helps**, we focus on the **self-attention** mechanism, specifically within a single attention head.

Let’s walk through a simple PyTorch implementation to visualise the key computations.

```
import torch

input_seq_length = 5
dim_model = 10

input_ids_emb = torch.randn(input_seq_length, dim_model)
W_q = torch.randn(dim_model, dim_model)
W_k = torch.randn(dim_model, dim_model)
W_v = torch.randn(dim_model, dim_model)

Q = input_ids_emb @ W_q
K = input_ids_emb @ W_k
V = input_ids_emb @ W_v

```

### Self-Attention Computation

For a sequence of T T T input embeddings represented as X∈RT×D X \in \mathbb{R}^{T \times D} X∈RT×D, self-attention is computed as:

- Q=XWQ Q = XW_Q Q=XWQ​, with WQ∈RD×Dq W_Q \in \mathbb{R}^{D \times D_q} WQ​∈RD×Dq​
- K=XWK K = XW_K K=XWK​, with WK∈RD×Dk W_K \in \mathbb{R}^{D \times D_k} WK​∈RD×Dk​
- V=XWV V = XW_V V=XWV​, with WV∈RD×Dv W_V \in \mathbb{R}^{D \times D_v} WV​∈RD×Dv​
- Causal mask M M M to prevent future token access

The final output is:

Attention(X;Q,K,V)=softmax(QK⊤⋅Mdk)V
\text{Attention}(X; Q, K, V) = \text{softmax}\left( \frac{QK^\top \cdot M}{\sqrt{d_k}} \right)V
Attention(X;Q,K,V)=softmax(dk​​QK⊤⋅M​)V

Here’s a minimal PyTorch equivalent using a causal mask:

```
import torch.nn.functional as F

attention_scores = Q @ K.T


causal_mask = torch.tril(torch.ones(input_seq_length, input_seq_length))
masked_scores = attention_scores.masked_fill(causal_mask == 0, float('-inf'))

attention_weights = F.softmax(masked_scores, dim=-1)
output = attention_weights @ V

```

## Where Redundancy Creeps In

In autoregressive generation, the model generates one token at a time. With each step, it recomputes Q Q Q, K K K, and V V V for **the entire sequence**, even though the earlier tokens haven’t changed.

```
new_token_emb = torch.randn(1, dim_model)
extended_input = torch.cat([input_ids_emb, new_token_emb], dim=0)

Q_ext = extended_input @ W_q
K_ext = extended_input @ W_k
V_ext = extended_input @ W_v



```

To confirm the redundancy:

```
torch.testing.assert_close(K, K_ext[:input_seq_length])
torch.testing.assert_close(V, V_ext[:input_seq_length])

```

These checks show that for all but the newest token, K K K and V V V are identical to previously computed values.

```
Original (5×5):         Extended (6×6):
■ ■ ■ ■ ■              ■ ■ ■ ■ ■ □
■ ■ ■ ■ ■              ■ ■ ■ ■ ■ □
■ ■ ■ ■ ■    →         ■ ■ ■ ■ ■ □
■ ■ ■ ■ ■              ■ ■ ■ ■ ■ □
■ ■ ■ ■ ■              ■ ■ ■ ■ ■ □
                       □ □ □ □ □ □

```

- **■** = Already computed and reused
- **□** = Recomputed unnecessarily

Most of the attention computation is repeated needlessly. This gets more expensive as sequences grow.

## How KV Caching Fixes It

To eliminate this inefficiency, we use **KV Caching**:

- After processing the initial prompt, we **cache** the computed keys ( K K K ) and values ( V V V ) for each layer.
- During generation, we **only compute** K K K **and** V V V **for the new token**, and **append** them to the cache.
- We compute Q Q Q for the current token and use it with the **cached K K K and V V V** to get the output.

This changes generation from full-sequence re-computation to a lightweight, incremental update.

> ✅ In practice, this cache is a per-layer dictionary with keys "key" and "value", each of shape (`batch_size`, `num_heads`, `seq_len_cached`, `head_dim`).

This is the foundation of how modern LLMs can generate long outputs efficiently.

## KV Caching in nanoVLM: From Theory to Practice

Now that we understand the theory behind KV Caching, let’s see how it’s implemented in practice inside our [nanoVLM](https://github.com/huggingface/nanoVLM) repository. This is an ideal testbed, as it's a super concise and self-contained codebase.

KV caching is enabled across three key components in our model:

1. The **Attention block** that uses and updates the KV cache
2. The **Language model** that tracks cache per layer
3. The **Generation loop** that separates **prefill** (the initial pass with the input prompt) and sequential **decode** phases

### 1. Updating KV Cache in the Attention Block

In the `LanguageModelGroupedAttention` class, we modify the `forward` function to accept and update a cache of keys and values (`block_kv_cache`).

Previously, the model recomputed K K K and V V V at every generation step. Now we only compute Knew K\_{\text{new}} Knew​, Vnew V\_{\text{new}} Vnew​ for the current token, and append them to the cached values.

```
def forward(self, x, cos, sin, attention_mask=None, block_kv_cache=None):
    is_prefill = block_kv_cache is None
    B, T_curr, C = x.size()


    q_curr, k_curr, v_curr = project_current_tokens(x)
    q, k_rotated = apply_rotary_pos_embd(q_curr, k_curr, cos, sin)

    if not is_prefill and block_kv_cache['key'] is not None:

        k = torch.cat([block_kv_cache['key'], k_rotated], dim=2)
        v = torch.cat([block_kv_cache['value'], v_curr], dim=2)
    else:

        k, v = k_rotated, v_curr

    block_kv_cache = {'key': k, 'value': v}
    return attention_output, block_kv_cache

```

### 2. Tracking Cache Across Layers

In the `LanguageModel` class, we introduce **layer-wise cache tracking**. The `start_pos` argument helps the model compute correct **rotary positional encodings** for newly generated tokens.

```
def forward(self, x, kv_cache=None, start_pos=0):
    T_curr = x.size(1)
    position_ids = torch.arange(start_pos, start_pos + T_curr, device=x.device)
    cos, sin = self.rotary_embd(position_ids)

    for i, block in enumerate(self.blocks):

        x, kv_cache[i] = block(x, cos, sin, attention_mask, kv_cache[i])

    return x, kv_cache

```

- `kv_cache`: A list of dictionaries, one per transformer layer, holding previous keys and values.
- `start_pos`: Ensures that rotary embeddings are aligned with current generation index.

### 3. Prefill vs Decode in the Generation Loop

The biggest architectural change is in the `generate()` method of the `VisionLanguageModel`.

We **split generation into two stages**:

- **PREFILL PHASE:** Encode the full prompt and build the initial cache.
- **DECODE PHASE:** Generate tokens one at a time using cached keys/values.

```
PREFILL PHASE (cache construction)
[Prompt: "What is"] → [Transformer] → [Cache: K, V for all layers]

DECODE PHASE (token-by-token)
[Token: "the"] → [Q("the") + cached K/V] → [next token: "?"] → ...

```

Here’s the corresponding code:

```

prompt_output, kv_cache_list = self.forward(
    inputs,
    kv_cache=None,
    start_pos=0
)


for i in range(max_new_tokens):
    next_token = sample_from(prompt_output)

    decode_output, kv_cache_list = self.forward(
        next_token,
        kv_cache=kv_cache_list,
        start_pos=current_position
    )

    prompt_output = decode_output

```

> By separating these phases, we avoid redundant computation and dramatically speed up inference, especially for long prompts.

### Summary of Changes

| Module                                  | Original Behaviour                           | New Behaviour                                  |
| --------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| `LanguageModelGroupedAttention.forward` | Recomputes Q Q Q, K K K, V V V on every step | Uses and updates KV cache                      |
| `LanguageModel.forward`                 | No memory of previous state                  | Tracks per-layer KV cache, handles `start_pos` |
| `VisionLanguageModel.generate`          | One-phase generation loop                    | Split into **prefill** and **decode** phases   |

## Summary: Why KV Caching Matters

| Benefit                     | Explanation                                                       |
| --------------------------- | ----------------------------------------------------------------- |
| **Incremental growth**      | Cache grows by one row per new token                              |
| **Position-aware decoding** | `start_pos` ensures correctness of position encoding calculations |
| **Efficiency**              | Reduces per-token inference to O(`seq len`) instead of quadratic  |

KV caching eliminates unnecessary computation during autoregressive generation, enabling faster and more efficient inference, especially in long sequences and real-time applications. This is a trade-off between speed and memory, and its drawbacks can be more complex code and restricting fancier inference schemes, like beam-search, etc. KV caching is a popular method for speeding up LLM inference, making it possible to run them on consumer hardware, and now you know how it works too!
