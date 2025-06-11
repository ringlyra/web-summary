<!-- metadata -->

- **title**: SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models
- **source**: https://arxiv.org/abs/2506.01062
- **author**: Pham, Thinh, Nguyen, Nguyen, Zunjare, Pratibha, Chen, Weiyuan, Tseng, Yu-Min, Vu, Tu
- **published**: 2025-06-01T00:00:00Z
- **fetched**: 2025-06-04T04:44:39Z
- **tags**: codex, llm, benchmark, reasoning, search
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

SealQAは、検索拡張言語モデルの推論力を測る難関ベンチマークで、Seal-0、Seal-Hard、LongSealの3種類があり、最先端モデルでも正答率が低い点を指摘。ノイズに弱く計算増加も効果が薄い。

## 本文

> Abstract:We introduce SealQA, a new challenge benchmark for evaluating SEarch-Augmented Language models on fact-seeking questions where web search yields conflicting, noisy, or unhelpful results. SealQA comes in three flavors: (1) Seal-0 (main) and (2) Seal-Hard, which assess factual accuracy and reasoning capabilities, with Seal-0 focusing on the most challenging questions where chat models (e.g., GPT-4.1) typically achieve near-zero accuracy; and (3) LongSeal, which extends SealQA to test long-context, multi-document reasoning in "needle-in-a-haystack" settings. Our evaluation reveals critical limitations in current models: Even frontier LLMs perform poorly across all SealQA flavors. On Seal-0, frontier agentic models equipped with tools like o3 and o4-mini achieve only 17.1% and 6.3% accuracy, respectively, at their best reasoning efforts. We find that advanced reasoning models such as DeepSeek-R1-671B and o3-mini are highly vulnerable to noisy search results. Notably, increasing test-time compute does not yield reliable gains across o3-mini, o4-mini, and o3, with performance often plateauing or even declining early. Additionally, while recent models are less affected by the "lost-in-the-middle" issue, they still fail to reliably identify relevant documents in LongSeal when faced with numerous distractors. To facilitate future work, we release SealQA at [this http URL](http://huggingface.co/datasets/vtllms/sealqa).
