---
title: Qwen3 Embedding
source: https://simonwillison.net/2025/Jun/8/qwen3-embedding/
author: Simon Willison
published: '2025-06-08T04:22:29Z'
fetched: '2025-06-08T15:59:46Z'
tags:
- codex
- ai
- embeddings
- qwen
- llm
- huggingface
image: https://static.simonwillison.net/static/2025/qwen3-mteb.jpg
---

## 要約

Qwenが公開した新しい埋め込みモデル「Qwen3 Embedding」は0.6B、4B、8Bの3サイズで、Text EmbeddingとText Rerankingの2種類があります。最小モデルは639MBのGGUFで、`llm-sentence-transformers`プラグインを使ったテストでは1024次元のベクトルが得られました。これらのモデルはMTEBリーダーボードで最も高く評価され、Apache 2.0ライセンスで提供されています。また、Transformers.jsによるブラウザ上のデモもあり、560MBのモデルファイルを読み込んでクラスタ可視化を行うことができます。

## 本文

**[Qwen3 Embedding](https://qwenlm.github.io/blog/qwen3-embedding/)** ([via](https://twitter.com/xenovacom/status/1931082176788906006 "@xenovacom")) New family of embedding models from Qwen, in three sizes: 0.6B, 4B, 8B - and two categories: Text Embedding and Text Reranking.

The full collection [can be browsed](https://huggingface.co/collections/Qwen/qwen3-embedding-6841b2055b99c44d9a4c371f) on Hugging Face. The smallest available model is the 0.6B Q8 one, which is available as a 639MB GGUF. I tried it out using my [llm-sentence-transformers](https://github.com/simonw/llm-sentence-transformers) plugin like this:

```
llm install llm-sentence-transformers
llm sentence-transformers register Qwen/Qwen3-Embedding-0.6B
llm embed -m sentence-transformers/Qwen/Qwen3-Embedding-0.6B -c hi | jq length

```

This output 1024, confirming that Qwen3 0.6B produces 1024 length embedding vectors.

These new models are the highest scoring open-weight models on the well regarded [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) - they're licensed Apache 2.0.

![Table showing ranking of embedding models with columns for Rank, Model name, Zero-shot performance, Memory Usage, Number of Parameters, Embedding Dimensions, and Max Tokens. Top models include gemini-embedding-001 at rank 1 with 99% zero-shot and 3072 embedding dimensions, Qwen3-Embedding-8B at rank 2 with 99% zero-shot and 4096 embedding dimensions, and several other Qwen3 variants. Most models show 99% zero-shot performance with green highlighting, except gte-Qwen2-7B-instruct at rank 6 which shows "NA" with red highlighting and a warning triangle icon.](https://static.simonwillison.net/static/2025/qwen3-mteb.jpg)

You can also try them out in your web browser, thanks to a [Transformers.js](https://huggingface.co/docs/transformers.js/en/index) port of the models. I loaded ![this page in Chrome](https://static.simonwillison.net/static/2025/qwen3-web.jpg) and it fetched 560MB of model files and gave me an interactive interface for visualizing clusters of embeddings like this:

![Screenshot of a text embedding web application interface showing a "Sentences" panel on the left with various sample sentences about topics like cooking, technology, sports, finance, music, and history, a "Labels" section below listing these categories, and a "Scatterplot" visualization on the right displaying colored clusters of data points representing the embedded sentences grouped by topic, with an "Embed & Plot" button at the bottom and instructions to "Done! Hover over points to see sentences."](https://static.simonwillison.net/static/2025/qwen3-web.jpg)
