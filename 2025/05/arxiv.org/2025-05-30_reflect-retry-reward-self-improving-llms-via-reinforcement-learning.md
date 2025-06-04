<!-- metadata -->
- **title**: Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning
- **source**: https://arxiv.org/abs/2505.24726
- **author**: Shelly Bensal, Umar Jamil, Christopher Bryant, Melisa Russak, Kiran Kamble, Dmytro Mozolevskyi, Muayad Ali, Waseem AlShikh
- **published**: 2025-05-30T00:00:00Z
- **fetched**: 2025-06-04T15:32:38Z
- **tags**: codex, llm, reinforcement-learning, self-improvement
- **image**: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png

## 概要 / Summary
大型言語モデルが誤答した際に**自己反省**を行い、その後の試行で成果を出した場合に報酬を与える**強化学習**手法を提案。抽象的なタスクでも自己改善が可能で、比較的小さなモデルで大幅な性能向上を確認。

## 本文 / Article
> Abstract:We explore a method for improving the performance of large language models through self-reflection and reinforcement learning. By incentivizing the model to generate better self-reflections when it answers incorrectly, we demonstrate that a model's ability to solve complex, verifiable tasks can be enhanced even when generating synthetic data is infeasible and only binary feedback is available. Our framework operates in two stages: first, upon failing a given task, the model generates a self-reflective commentary analyzing its previous attempt; second, the model is given another attempt at the task with the self-reflection in context. If the subsequent attempt succeeds, the tokens generated during the self-reflection phase are rewarded. Our experimental results show substantial performance gains across a variety of model architectures, as high as 34.7% improvement at math equation writing and 18.1% improvement at function calling. Notably, smaller fine-tuned models (1.5 billion to 7 billion parameters) outperform models in the same family that are 10 times larger. Our novel paradigm is thus an exciting pathway to more useful and reliable language models that can self-improve on challenging tasks with limited external feedback.
