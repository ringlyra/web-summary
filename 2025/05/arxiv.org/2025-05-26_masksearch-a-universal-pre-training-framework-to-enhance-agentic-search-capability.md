<!-- metadata -->
- **title**: MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability
- **source**: https://arxiv.org/abs/2505.20285
- **author**: Wu, Weiqi; Guan, Xin; Huang, Shen; Jiang, Yong; Xie, Pengjun; Huang, Fei; Cao, Jiuxin; Zhao, Hai; Zhou, Jingren
- **published**: 2025-05-26T00:00:00Z
- **fetched**: 2025-06-04T01:16:34Z
- **tags**: codex, article
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約
外部検索を利用する**RALM**の弱点を補うため、新しい事前学習法**MaskSearch**を提案。検索ツールでマスク領域を補完するRAMPを導入し、SFTとRLでさらに強化。多段質問応答で性能向上を確認。

## 本文 / Article
[Submitted on 26 May 2025 (

[v1](https://arxiv.org/abs/2505.20285v1)

), last revised 27 May 2025 (this version, v2)]

Title:MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability
=========================================================================================

View a PDF of the paper titled MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability, by Weiqi Wu and 8 other authors

[View PDF](/pdf/2505.20285)
[HTML (experimental)](https://arxiv.org/html/2505.20285v2)
> Abstract:Retrieval-Augmented Language Models (RALMs) represent a classic paradigm where models enhance generative capabilities using external knowledge retrieved via a specialized module. Recent advancements in Agent techniques enable Large Language Models (LLMs) to autonomously utilize tools for retrieval, planning, and reasoning. While existing training-based methods show promise, their agentic abilities are limited by inherent characteristics of the task-specific data used during training. To further enhance the universal search capability of agents, we propose a novel pre-training framework, MaskSearch. In the pre-training stage, we introduce the Retrieval Augmented Mask Prediction (RAMP) task, where the model learns to leverage search tools to fill masked spans on a large number of pre-training data, thus acquiring universal retrieval and reasoning capabilities for LLMs. After that, the model is trained on downstream tasks to achieve further improvement. We apply both Supervised Fine-tuning (SFT) and Reinforcement Learning (RL) for training. For SFT, we combine agent-based and distillation-based methods to generate training data, starting with a multi-agent system consisting of a planner, rewriter, observer, and followed by a self-evolving teacher model. While for RL, we employ DAPO as the training framework and adopt a hybrid reward system consisting of answer rewards and format rewards. Additionally, we introduce a curriculum learning approach that allows the model to learn progressively from easier to more challenging instances based on the number of masked spans. We evaluate the effectiveness of our framework in the scenario of open-domain multi-hop question answering. Through extensive experiments, we demonstrate that MaskSearch significantly enhances the performance of LLM-based search agents on both in-domain and out-of-domain downstream tasks.

Submission history
------------------

From: Xin Guan [

[view email](/show-email/a02aa2d1/2505.20285)

]

**[[v1]](/abs/2505.20285v1)**

Mon, 26 May 2025 17:58:50 UTC (1,077 KB)

**[v2]**

Tue, 27 May 2025 06:46:24 UTC (1,077 KB)
