<!-- metadata -->
- **title**: Frankentext: Stitching random text fragments into long-form narratives
- **source**: https://arxiv.org/abs/2505.18128
- **author**: Pham, Chau Minh; Russell, Jenna; Pham, Dzung; Iyyer, Mohit
- **published**: 2025-05-23T00:00:00Z
- **fetched**: 2025-06-04T04:40:56Z
- **tags**: codex, ai
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 概要 / Summary
LLM を使い、文章の 90% 以上を他文書から直接引用しつつ、一貫した物語を生成する **Frankentexts** を提案。Gemini-2.5-Pro で検証したところ、品質と指示適合度は高く、**AI 文章判定** では最大 59% が人間作と誤判定された。

## 本文 / Article
[Submitted on 23 May 2025 (

[v1](https://arxiv.org/abs/2505.18128v1)

), last revised 29 May 2025 (this version, v2)]

Title:Frankentext: Stitching random text fragments into long-form narratives
============================================================================

View a PDF of the paper titled Frankentext: Stitching random text fragments into long-form narratives, by Chau Minh Pham and Jenna Russell and Dzung Pham and Mohit Iyyer

[View PDF](/pdf/2505.18128)
[HTML (experimental)](https://arxiv.org/html/2505.18128v2)
> Abstract:We introduce Frankentexts, a new type of long-form narratives produced by LLMs under the extreme constraint that most tokens (e.g., 90%) must be copied verbatim from human writings. This task presents a challenging test of controllable generation, requiring models to satisfy a writing prompt, integrate disparate text fragments, and still produce a coherent narrative. To generate Frankentexts, we instruct the model to produce a draft by selecting and combining human-written passages, then iteratively revise the draft while maintaining a user-specified copy ratio. We evaluate the resulting Frankentexts along three axes: writing quality, instruction adherence, and detectability. Gemini-2.5-Pro performs surprisingly well on this task: 81% of its Frankentexts are coherent and 100% relevant to the prompt. Notably, up to 59% of these outputs are misclassified as human-written by detectors like Pangram, revealing limitations in AI text detectors. Human annotators can sometimes identify Frankentexts through their abrupt tone shifts and inconsistent grammar between segments, especially in longer generations. Beyond presenting a challenging generation task, Frankentexts invite discussion on building effective detectors for this new grey zone of authorship, provide training data for mixed authorship detection, and serve as a sandbox for studying human-AI co-writing processes.

Submission history
------------------

From: Chau Minh Pham [

[view email](/show-email/0993d44a/2505.18128)

]

**[[v1]](/abs/2505.18128v1)**

Fri, 23 May 2025 17:38:47 UTC (29,653 KB)

**[v2]**

Thu, 29 May 2025 01:43:46 UTC (9,724 KB)
