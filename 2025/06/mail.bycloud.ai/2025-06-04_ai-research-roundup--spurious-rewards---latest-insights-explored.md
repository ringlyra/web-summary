<!-- metadata -->
- **title**: AI Research Roundup: Spurious Rewards & Latest Insights Explored
- **source**: https://mail.bycloud.ai/p/a-shocking-rlvr-revelation-for-llm-just-dropped-dacd425f175077f9
- **author**: mail.bycloud.ai
- **published**: 
- **fetched**: 2025-06-04T11:10:30.676110Z
- **tags**: codex, ai, research
- **image**: https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/6d21e855-ca01-459a-b19b-a8b5c4cfbb2b/issue_58.jpg?t=1748980487

## 要約
最新のAI研究ニュースレターでは、**DeepSeek**モデルの強化版や、画像編集に強い**FLUX.1 Kontext**など業界動向を紹介。注目論文は、**RLVR**でランダムや誤った報酬でも計算能力が向上するという衝撃の事実を報告し、特に**Qwen**系列はコード生成への嗜好が精度向上に寄与していると指摘。他にも、Transformerが系統的探索を苦手とする問題や、外部報酬を使わず自己確信度で学習する**RLIF/INTUITOR**手法の効果を解説。全体としてLLMの推論能力を高める新たなアプローチが議論された。

## 本文 / Article

###### *May 26th ~ June 2nd* *#58 Latest AI Research Explained Simply*

🗞️ Industry News in 1 Line
--------------------------

1. ♥ 9.8k DeepSeek released DeepSeek-R1-0528, a version 2 for its R1 model. Around 10~20% performance increase compared to R1v1. It is currently the SoTA open source model, and they also distilled a DeepSeek-R1-0528-Qwen3-8B. You can watch [my video](https://youtu.be/_5Xv3kXyBDE) for a brief overview. Weights are now available on [Huggingface](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528).

   ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/84b61904-b493-4b7f-b47f-b6e231a116db/GsHZfE_aUAEo64N.png?t=1748978442)

   DeepSeek-R1-0528 Benchmarks
2. ♥ 2.5k Black Forest Labs, founded by the key people behind Stable Diffusion, has released FLUX.1 Kontext. Unlike traditional text-to-image models, Kontext understands both text AND images as input, enabling true in-context generation and editing. Currently SoTA in image editing with text.

   ![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/427e5156-afca-4796-a069-5afc7abd913c/GsIi2ydXYAAbfjw.jpg?t=1748978693)

   FLUX.1 Kontext text-based image editing demo
3. ♥ 4.9k [Anthropic has open-sourced its circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing) for their mechanistic interpretability research. These tools utilize cross-layer transcoders to construct interpretable graphs, allowing for interventions on model features to observe changes in output. The interactive Neuronpedia platform supports visualization and annotation of these graphs, helping studies on behaviors such as multi-step reasoning and hallucination suppression in models like Gemma-2-2B and Llama-3.2-1B.

   ![]()

   An overview of the interactive graph explorer UI on Neuronpedia.

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/bfba51a0-ee8e-42d5-8b45-51ddfd5ebe33/image.png?t=1748369227)](https://www.findmypapers.ai?=newsletter)

papers preview, go give it a spin!

While we are improving the retrieval quality for finding AI research papers, we still want to make the search experience a bit less boring.

So now, we are able to display the papers that are being searched on! (truly a new tiny feature lol)

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b33452d0-4484-4fe0-aa6b-68f337e064b3/image.png?t=1748369486)](https://www.findmypapers.ai?=newsletter)

and a nicer citation section

Spurious Rewards: Rethinking Training Signals in RLVR
-----------------------------------------------------

*Shao et al. [University of Washington, Allen Institute for Artificial Intelligence, University of California]*

♥ 1.7k   LLM RLVR   bycloud’s pick

### Reinforcement Learning's Surprising Math Boost

**Reinforcement learning with verifiable rewards (RLVR)** has become the default method for improving mathematical reasoning in language models. But what if the rewards guiding this learning are completely disconnected from actual correctness?

This study tells us that certain models improve dramatically even when trained on random or deliberately incorrect rewards. This discovery challenges assumptions about how RLVR works and highlights critical differences in model pretraining.

### The Mechanism Behind Reward Resilience

The researchers of this study tested the RLVR method across multiple reward types on mathematical benchmarks like MATH-500. For Qwen models, rewards ranged from ground-truth labels to "spurious" signals like random binary assignments or incentives for incorrect answers. Surprisingly, all rewards (even those with zero correlation to correctness) gave significant accuracy gains.

After analyzing this behavior, the researchers analyzed that Qwen models frequently use "code reasoning" to generate Python-like pseudocode to structure solutions without execution. Before training, this appeared in 66.7% of responses. After RLVR with *any* reward, it surged past 90%. This shift correlated strongly with performance improvements, suggesting RLVR amplifies pretrained capabilities rather than imparting new knowledge.

For non-Qwen models like Llama or OLMo, spurious rewards failed. These models lack Qwen’s pretrained affinity for code reasoning. When they attempted code generation, accuracy often dropped.

### Performance Gains and Implications

The tests on RLVR approach with Qwen2.5-Math-7B achieved 21-26% accuracy gains on MATH-500 using spurious rewards (random, format-based, or incorrect labels) which is quite close to the 28.8% gain from ground-truth rewards. However, Llama and OLMo models saw minimal or negative changes with identical rewards. For example, OLMo2-7B only improved with ground-truth supervision.

Forcing Qwen models to generate code via prompts improved accuracy by 11-25%, while suppressing it reduced gains. However, when Non-Qwen models were prompted for code, they performed worse. This confirms code reasoning as a primary driver behind Qwen’s reward-agnostic improvements, and that a handful of RLVR research may need to be re-evaluated as a lot of them **only validated their performance Qwen model families, thus their results may fail to generalize**.

Reasoning LLMs are Wandering Solution Explorers
-----------------------------------------------

*Lu et al. [NUS AI Institute]*

♥ 361   LLM Reasoning Search

### Introduction to the Reasoning LLMs

LLMs don’t have very good reasoning skills but they try to keep up by using techniques like chain-of-thought prompting to tackle complex problems. But under the hood, these reasoning LLMs (RLLMs) often wander aimlessly through solution spaces rather than exploring them systematically.

This paper shows that as problems grow more complex, RLLMs stumble and produce invalid steps, redundant explorations, or unfaithful conclusions. Current benchmarks might hide these problems on simpler tasks, but as the tasks get more complex, the performance of models suffer severely.

### Why Transformers Suck at Systematic Exploration

Systematic exploration requires three steps:

* **Validity** means each reasoning step follows the problem’s rules, like staying within bounds during a grid search.
* **Effectiveness** ensures the model reaches a valid solution.
* **Necessity** means no wasted steps. i.e. every action must directly contribute to solving the problem or ruling out dead ends.

For instance, in depth-first search tasks, a systematic explorer would backtrack correctly after hitting dead ends, avoiding redundant paths. Current RLLMs violate these principles repeatedly. They commit boundary violations, like hallucinating array indices beyond actual limits. Procedure omission occurs when models skip essential substeps, halting prematurely. Incorrect backtracking leads them to restore outdated states, corrupting the search.

Unnecessary explorations can lead to state revisitation or infinite loops which repeat failed approaches until resources exhaust. Evaluation errors exacerbate these issues, such as using stale data in dynamic programming or miscomputing values mid-reasoning.

These failures are mainly caused due to architectural gaps. Transformers lack built-in mechanisms for state tracking or structured backtracking. Without explicit memory management or loop-exit heuristics, RLLMs rely on local context, overlooking global constraints. For example, in permutation tasks, smaller models degrade faster, but even top-tier systems like Anthropic-Sonnet-3.7 eventually falter as complexity mounts.

### Evaluating Transformers on Complex Problems

The researchers conducted experiments on tasks like permutation generation and all tested RLLMs show exponential performance decay as problem size increases. In one test, models created permutations of lists with duplicates. Additionally, the ratio of valid solutions found plummeted for larger inputs across all models, including commercial giants like OpenAI-O3. Smaller open-source models deteriorated fastest, but none of them achieved systematicity.

The findings signal three urgent shifts for AI research.

1. First, architectures need components like symbolic modules or search controllers to enforce structured exploration.
2. Second, training must prioritize process supervision, rewarding valid step-by-step reasoning over final-output mimicry.
3. Third, evaluation should evolve beyond accuracy metrics to audit reasoning traces for validity and efficiency.

Learning to Reason without External Rewards
-------------------------------------------

*Zhao et al. [UC Berkeley, Yale University]*

### Introduction to Reasoning in LLMs

Training large language models for complex reasoning often requires reinforcement learning with verifiable rewards (RLVR), which requires costly domain-specific supervision like gold-standard solutions or test cases. This limitation makes it hard to generalize this approach to broader applications.

This paper introduces Reinforcement Learning from Internal Feedback (RLIF) which is a new approach that enables models to learn from intrinsic signals without external oversight. The researchers have developed the INTUITOR method, an RLIF implementation that leverages a model's self-certainty as the sole reward signal. This approach eliminates the need for labeled data or verifiers, and offers a scalable path for autonomous AI systems where traditional rewards are impractical.

### Working Mechanism of INTUITOR Framework

INTUITOR uses the Group Relative Policy Optimization (GRPO), a reinforcement learning framework. Instead of using external rewards, it substitutes them with self-certainty scores derived from the model’s token-level predictions. Self-certainty is calculated as the average KL divergence between the model’s output distribution and a uniform distribution over the vocabulary.

Higher values of this divergence indicate greater confidence in generated tokens. During training, multiple candidate responses are sampled for each query. Their self-certainty scores are normalized to compute advantages, guiding policy updates toward high-confidence outputs. This process creates a self-reinforcing loop: the model iteratively refines responses to maximize its own confidence. For example, when encountering uncertain reasoning chains, INTUITOR encourages detailed step-by-step explanations until confidence rises.

The KL divergence penalty acts as a regularizer and prevents excessive deviation from the reference model. Additionally, self-certainty operates token-by-token, which makes it inherently process-aware rather than outcome-focused. This continuous signal helps the model build internal coherence without external validation.

### Benchmark Performance of INTUITOR Framework

The researchers conducted experiments with Qwen2.5 models (1.5B and 3B parameters) trained on mathematical datasets that show INTUITOR matches GRPO’s in-domain performance. On MATH500 and GSM8K benchmarks, accuracy differences were barely noticeable. For instance, Qwen2.5-3B scored 79.2% (INTUITOR) versus 82.6% (GRPO) on GSM8K. Additionally, INTUITOR excels in generalization: it achieved a 65% relative improvement on LiveCodeBench code generation and a 76% gain on CRUXEval-O, outperforming GRPO’s 44%.

The Online self-certainty method used an approach where rewards are computed using the evolving policy. This prevented reward hacking, unlike static offline versions. Tests showed that the KL penalty’s role in balancing generalization, especially for out-of-domain tasks.
