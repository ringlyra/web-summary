<!-- metadata -->

- **title**: ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models
- **source**: https://arxiv.org/abs/2505.24864
- **author**: Liu, Mingjie, Diao, Shizhe, Lu, Ximing, Hu, Jian, Dong, Xin, Choi, Yejin, Kautz, Jan, Dong, Yi
- **published**: 2025-05-30T00:00:00Z
- **fetched**: 2025-06-04T03:45:06Z
- **tags**: codex, reinforcement learning, reasoning, llm
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

長時間の**ProRL**訓練によりLLMの推論能力を拡張できるか検証。**KL制御**や参照ポリシーのリセットを導入し、幅広いタスクで基盤モデルを上回る性能を示した。

## 本文

[Submitted on 30 May 2025]

# Title:ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models

Authors:[Mingjie Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+M), [Shizhe Diao](https://arxiv.org/search/cs?searchtype=author&query=Diao,+S), [Ximing Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+X), [Jian Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+J), [Xin Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+X), [Yejin Choi](https://arxiv.org/search/cs?searchtype=author&query=Choi,+Y), [Jan Kautz](https://arxiv.org/search/cs?searchtype=author&query=Kautz,+J), [Yi Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+Y)

View a PDF of the paper titled ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models, by Mingjie Liu and 7 other authors

[View PDF](/pdf/2505.24864)
[HTML (experimental)](https://arxiv.org/html/2505.24864v1)

> Abstract:Recent advances in reasoning-centric language models have highlighted reinforcement learning (RL) as a promising method for aligning models with verifiable rewards. However, it remains contentious whether RL truly expands a model's reasoning capabilities or merely amplifies high-reward outputs already latent in the base model's distribution, and whether continually scaling up RL compute reliably leads to improved reasoning performance. In this work, we challenge prevailing assumptions by demonstrating that prolonged RL (ProRL) training can uncover novel reasoning strategies that are inaccessible to base models, even under extensive sampling. We introduce ProRL, a novel training methodology that incorporates KL divergence control, reference policy resetting, and a diverse suite of tasks. Our empirical analysis reveals that RL-trained models consistently outperform base models across a wide range of pass@k evaluations, including scenarios where base models fail entirely regardless of the number of attempts. We further show that reasoning boundary improvements correlates strongly with task competence of base model and training duration, suggesting that RL can explore and populate new regions of solution space over time. These findings offer new insights into the conditions under which RL meaningfully expands reasoning boundaries in language models and establish a foundation for future work on long-horizon RL for reasoning. We release model weights to support further research: [this https URL](https://huggingface.co/nvidia/Nemotron-Research-Reasoning-Qwen-1.5B)

|           |                                                                                               |
| --------- | --------------------------------------------------------------------------------------------- |
| Comments: | 26 pages, 17 figures                                                                          |
| Subjects: | Computation and Language (cs.CL); Artificial Intelligence (cs.AI)                             |
| Cite as:  | [arXiv:2505.24864](https://arxiv.org/abs/2505.24864) [cs.CL]                                  |
|           | (or [arXiv:2505.24864v1](https://arxiv.org/abs/2505.24864v1) [cs.CL] for this version)        |
|           | <https://doi.org/10.48550/arXiv.2505.24864> Focus to learn more arXiv-issued DOI via DataCite |
