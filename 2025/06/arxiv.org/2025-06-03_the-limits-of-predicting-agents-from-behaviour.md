<!-- metadata -->

- **title**: The Limits of Predicting Agents from Behaviour
- **source**: https://arxiv.org/abs/2506.02923
- **author**: Alexis Bellot, Jonathan Richens, Tom Everitt
- **published**: 2025-06-03
- **fetched**: 2025-06-10T11:18:07Z
- **tags**: codex, ai, agents, safety
- **image**: /static/browse/0.3.4/images/arxiv-logo-fb.png

## 要約

論文はAIエージェントがもつ世界モデルを構造的因果モデルとして記述し、行動データのみからその信念や計画を完全に推定するのは不可能だと論じる。合理性と最適性を前提に観測行動が未知環境での選択をどの程度絞り込むかを数学的に解析し、未知環境での行動を囲い込む上界・下界を導出する。これにより、公正性や安全性などエージェントの意図が関わる指標をどこまで信頼できるかの理論的限界を明示する。さらに世界モデルを明示的に扱う枠組みを拡張することで分布シフト下の推論や公平性評価に応用できると述べ、安全で予測可能なAI設計にはこうした因果的視点が欠かせないと主張する。加えて理論的な境界を実例に適用し、行動データから得られる推定区間を計算する手順を提示しており、AI安全研究の基盤となる知見を提供する。

## 本文

arXiv:2506.02923v1 [cs.AI] 3 Jun 2025
The Limits of Predicting Agents from Behaviour
Alexis Bellot1, Jonathan Richens1and Tom Everitt1
1Google DeepMind
As the complexity of AI systems and their interactions with the world increases, generating explanations
for their behaviour is important for safely deploying AI. For agents, the most natural abstractions for
predicting behaviour attribute beliefs, intentions and goals to the system. If an agent behaves as if it
has a certain goal or belief, then we can make reasonable predictions about how it will behave in novel
situations, includingthosewherecomprehensivesafetyevaluationsareuntenable. Howwellcanweinfer
an agent’s beliefs from their behaviour, and how reliably can these inferred beliefs predict the agent’s
behaviour in novel situations? We provide a precise answer to this question under the assumption that
the agent’s behaviour is guided by a world model. Our contribution is the derivation of novel bounds on
the agent’s behaviour in new (unseen) deployment environments, which represent a theoretical limit for
predicting intentional agents from behavioural data alone. We discuss the implications of these results
for several research areas including fairness and safety.

1. Introduction
   Humans understand each other through the use of abstractions. We explain our intentions by
   appealing to our “goals” and “beliefs” about the world around us without knowing the underlying
   cognition going on inside our heads. According to Dennett (1989, 2017), the same is true of our
   understanding of other systems. For example, a bear hibernates during winter as ifit believes that
   the lower temperatures cause food scarcity. This is a useful description of the bear’s behaviour, with
   real predictive power. For example, it gives us (human observers) the ability to anticipate how bears
   might act as the climate changes. There is a correspondence between beliefs and behaviour that is
   foundational to rational agents (Davidson, 1963).
   Artificial Intelligence (AI) systems appear to have similarly general capabilities, not totally unlike
   that of humans and animals. They can generate text that is fluent and accurate in response to a very
   diverse set of questions. Whenever they display consistent types of behaviour across many different
   tasks, we are tempted to apply our own mentalistic language more or less at face value (Shanahan,
   2024), taking seriously questions such as: What do the AIs know? What do they think, and believe?
   Taking the analogy further, it is as ifthey learn “world models” that mirror the causal relationships of
   theenvironmenttheyaretrainedon, guidingtheirfutureplansandbehaviour1. Andasaconsequence,
   their interactions with an environment will leave clues that might give us the ability to predict their
   future behaviour in novel domains. This possibility engages with a core AI Safety problem: how to
   guarantee and predict whether AI systems will act safely and beneficially?
   The main result of this paper is to offer a new perspective on this problem by showing that:
   With an assumption of competence and optimality, the behaviour of AI systems partially
   determines their actions in novel environments.
   1Recent research suggests that an AI’s behaviour, to the extent that it is consistent with rationality axioms, can be
   formally described by a (causal) world model (Halpern and Piermont, 2024). The same conclusion can also be obtained
   for AIs capable of solving tasks in multiple environments (Richens and Everitt, 2024). For large language models, there
   is increasing empirical evidence for the “world model” hypothesis, see e.g., Goldstein and Levinstein, 2024; Gurnee and
   Tegmark, 2023; Li et al., 2022; Toshniwal et al., 2022 and Vafa et al., 2024.
   Corresponding author(s): abellot@google.com
   ©2025 Google DeepMind. All rights reserved
   The Limits of Predicting Agents from Behaviour
   Here behaviour means our observations of the decisions made by the AI system, contextual
   variables, and utility or reward values in some environment. The “partial” determination of actions
   in new environments is a consequence of our lack of knowledge about the AI’s actual world model
   (different models may induce different optimal actions). However, even though we can’t uniquely
   identify the AI’s future behaviour and beliefs, we can narrow it down to a range of possible outcomes.
