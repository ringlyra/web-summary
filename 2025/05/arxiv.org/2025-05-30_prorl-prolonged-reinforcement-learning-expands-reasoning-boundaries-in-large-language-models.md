<!-- metadata -->
- **title**: ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models
- **source**: https://arxiv.org/abs/2505.24864
- **author**: Liu, Mingjie, Diao, Shizhe, Lu, Ximing, Hu, Jian, Dong, Xin, Choi, Yejin, Kautz, Jan, Dong, Yi
- **published**: 2025/05/30T00:00:00Z
- **fetched**: 2025-06-04T03:35:18Z
- **tags**: codex, ai
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png


## 概要 / Summary
**ProRL**は**長時間の強化学習**によって、基盤モデルでは到達できない推論境界を拡張する手法。KL制御や多様なタスクで訓練し、pass@k評価で一貫して基盤モデルを上回ることを示す。

## 本文 / Article
Abstract:Recent advances in reasoning-centric language models have highlighted reinforcement learning (RL) as a promising method for aligning models with verifiable rewards. However, it remains contentious whether RL truly expands a model's reasoning capabilities or merely amplifies high-reward outputs already latent in the base model's distribution, and whether continually scaling up RL compute reliably leads to improved reasoning performance. In this work, we challenge prevailing assumptions by demonstrating that prolonged RL (ProRL) training can uncover novel reasoning strategies that are inaccessible to base models, even under extensive sampling. We introduce ProRL, a novel training methodology that incorporates KL divergence control, reference policy resetting, and a diverse suite of tasks. Our empirical analysis reveals that RL-trained models consistently outperform base models across a wide range of pass@k evaluations, including scenarios where base models fail entirely regardless of the number of attempts. We further show that reasoning boundary improvements correlates strongly with task competence of base model and training duration, suggesting that RL can explore and populate new regions of solution space over time. These findings offer new insights into the conditions under which RL meaningfully expands reasoning boundaries in language models and establish a foundation for future work on long-horizon RL for reasoning. We release model weights to support further research: [this https URL](https://huggingface.co/nvidia/Nemotron-Research-Reasoning-Qwen-1.5B)
