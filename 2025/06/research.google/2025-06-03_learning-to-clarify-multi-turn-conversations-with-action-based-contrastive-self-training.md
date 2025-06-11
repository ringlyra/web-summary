<!-- metadata -->

- **title**: Learning to clarify: Multi-turn conversations with Action-Based Contrastive Self-Training
- **source**: https://research.google/blog/learning-to-clarify-multi-turn-conversations-with-action-based-contrastive-self-training/
- **author**: research.google
- **published**: 2025-06-03
- **fetched**: 2025-06-04T10:37:51Z
- **tags**: codex, ai
- **image**: https://storage.googleapis.com/gweb-research2023-media/images/Open_Graph.width-800.format-jpeg.jpg

## 要約

マルチターンシミュレーションがなければ、私たちのアプローチは、IRPOのようなポリシーでのDPOバリアントと同様に見ることができますが、会話アクションとタスクヒューリスティックを説明する会話固有の報酬信号を使用します。「シミュレーション付きのサンプリングw/サンプリング」では、この軌跡レベルのシミュレーションは、マルチターンパフォーマンス、特に独自の明確化の質問について推論するポリシーモデルの能力を改善するために重要であることがわかります。主な実験の基本モデルであるZephyrは、ミストラルを調整することにより得られます。

## 本文 / Article

**_Are action-based preferences necessary?_** One of the key factors of ACT is that the contrastive pairs highlight differences between conversational actions. In “ACT w/ Random Actions”, we additionally examine the importance of action selection by randomly sampling both the winning and losing action when constructing the preference pair, and observe this underperforms normal ACT.

**_Do we need on-policy sampling?_** In “ACT w/o on-policy sampling”, we examine the importance of on-policy sampling by evaluating normal off-policy DPO on the dataset as constructed in Phase 1. While we do observe some improvements over SFT (e.g., from 69.0 to 74.8 Macro F1), the overall improvements are much larger when using on-policy sampling as with full ACT. This may be due to the fact that the off-policy negative responses are not guaranteed to lie in the language manifold of the policy model, and distribution shift may be too difficult to overcome with off-policy learning.

**_Is trajectory simulation necessary?_** ACT is better-aligned with multi-turn conversations due to its trajectory simulation. Without multi-turn simulation, our approach can be viewed similarly to on-policy DPO variants like IRPO, but with a conversation-specific reward signal which accounts for conversation actions and task heuristics. In “ACT w/ sampling w/o simulation”, we find that this trajectory-level simulation is critical to improving multi-turn performance, especially the policy model’s ability to reason about its own clarification questions.

**_Is ACT model agnostic?_** The base model in our main experiments, [Zephyr](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta), is obtained by aligning [Mistral](https://mistral.ai/news/announcing-mistral-7b). In “ACT with unaligned foundation models” we observe a performance gap of 6.5 Action F1 and 4.3 Trajectory F1 after ACT tuning for the two models. However, our results demonstrate ACT can improve performance regardless of pre-existing alignment with human feedback, although it can help as an improved model initialization. Overall, we find that improving base model performance with ACT is model agnostic.
