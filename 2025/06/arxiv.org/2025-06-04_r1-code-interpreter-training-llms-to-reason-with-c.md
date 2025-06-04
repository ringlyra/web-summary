<!-- metadata -->
- **title**: R1-Code-Interpreter: Training LLMs to Reason with Code via Supervised and Reinforcement Learning
- **source**: https://arxiv.org/abs/2505.21668
- **author**: Chen, Yongchao
- **published**: 2025/05/27
- **fetched**: 2025-06-04T04:41:14Z
- **tags**: codex, arxiv, llm, code-interpreter, reinforcement
- **image**: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png

## 概要 / Summary
**LLM** にコード実行能力を組み合わせ、強化学習で訓練することで、計算やアルゴリズム推論を改善。Despite advances in reasoning and planning of R1-like models, Large Language Models (LLMs) still struggle with tasks requiring...

## 本文 / Article
[Submitted on 27 May 2025]

Title:R1-Code-Interpreter: Training LLMs to Reason with Code via Supervised and Reinforcement Learning
======================================================================================================

Authors:[Yongchao Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y), [Yueying Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Y), [Junwei Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+J), [Yilun Hao](https://arxiv.org/search/cs?searchtype=author&query=Hao,+Y), [Jingquan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+J), [Yang Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Y), [Chuchu Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+C)

View a PDF of the paper titled R1-Code-Interpreter: Training LLMs to Reason with Code via Supervised and Reinforcement Learning, by Yongchao Chen and 6 other authors

[View PDF](/pdf/2505.21668)
> Abstract:Despite advances in reasoning and planning of R1-like models, Large Language Models (LLMs) still struggle with tasks requiring precise computation, symbolic manipulation, optimization, and algorithmic reasoning, in which textual reasoning lacks the rigor of code execution. A key challenge is enabling LLMs to decide when to use textual reasoning versus code generation. While OpenAI trains models to invoke a Code Interpreter as needed, public research lacks guidance on aligning pre-trained LLMs to effectively leverage code and generalize across diverse tasks. We present R1-Code-Interpreter, an extension of a text-only LLM trained via multi-turn supervised fine-tuning (SFT) and reinforcement learning (RL) to autonomously generate multiple code queries during step-by-step reasoning. We curate 144 reasoning and planning tasks (107 for training, 37 for testing), each with over 200 diverse questions. We fine-tune Qwen-2.5 models (3B/7B/14B) using various SFT and RL strategies, investigating different answer formats, reasoning vs. non-reasoning models, cold vs. warm starts, GRPO vs. PPO, and masked vs. unmasked code outputs. Unlike prior RL work on narrow domains, we find that Code Interpreter training is significantly harder due to high task diversity and expensive code execution, highlighting the critical role of the SFT stage. Our final model, R1-CI-14B, improves average accuracy on the 37 test tasks from 44.0\% to 64.1\%, outperforming GPT-4o (text-only: 58.6\%) and approaching GPT-4o with Code Interpreter (70.9\%), with the emergent self-checking behavior via code generation. Datasets, Codes, and Models are available at [this https URL](https://github.com/yongchao98/R1-Code-Interpreter) and [this https URL](https://huggingface.co/yongchao98).

|  |  |
| --- | --- |
| Comments: | 33 pages, 8 figures |
| Subjects: | Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Symbolic Computation (cs.SC) |
| Cite as: | [arXiv:2505.21668](https://arxiv.org/abs/2505.21668) [cs.AI] |
|  | (or  [arXiv:2505.21668v1](https://arxiv.org/abs/2505.21668v1) [cs.AI] for this version) |
|  | <https://doi.org/10.48550/arXiv.2505.21668> Focus to learn more  arXiv-issued DOI via DataCite |
