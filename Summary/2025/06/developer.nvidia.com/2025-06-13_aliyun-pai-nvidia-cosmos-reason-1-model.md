---
title: Alibaba Cloud PAI が NVIDIA Cosmos Reason-1 を提供
source: https://developer.nvidia.com/ja-jp/blog/aliyun-pai-nvidia-cosmos-reason-1-model/
author:
- developer.nvidia.com
published: '2025-06-13T02:53:19+00:00'
fetched: '2025-06-13T10:47:07.871712+00:00'
tags:
- codex
- ai
- robotics
image: https://developer-blogs.nvidia.com/ja-jp/wp-content/uploads/sites/6/2025/06/image001.png
---

## 要約

Alibaba Cloud PAI-Model Gallery に NVIDIACosmos Reason-1-7B が統合され、ワンクリックでデプロイ可能になった。Reason-1は動作理解に特化したマルチモーダル AI で、視覚入力を連鎖思考推論により解釈し、物理環境に基づいた最適行動を導く。PAI の APIを用いればエンタープライズ向けにセキュアな推論サービスを利用でき、SFTとRLを組み合わせたポストトレーニング用スクリプトも公開されている。これによりユーザーは自社データでモデルをカスタマイズし、高速な推論基盤を活用できる。また、サンプル動画を用いた推論テストでは牛乳を注ぐ行動の次に取るべきステップを解析するなど、時空間関係を考慮した出力が確認された。今後PAIでもポストトレーニング機能を統合予定で、独自のフィジカルAI開発が容易になる。

## 本文

Reading Time: 2 minutes

NVIDIA は最近、Cosmos Reason-1 の 2 つのマルチモーダル大規模言語モデル (MLLM)、7B ([GitHub](https://github.com/nvidia-cosmos/cosmos-reason1)) と 56B バージョンをリリースしました。 これらは、フィジカル AI の教師ありファインチューニング (SFT) とフィジカル AI の強化学習 (RL) の 2 段階で学習されます。 さらに、7B モデルはオープンソース化されており、物理法則と具現化された推論データを使用して Qwen2.5-VL で事後トレーニングされています。

Alibaba Cloud PAI-Model Gallery は Cosmos Reason-1-7B を統合し、エンタープライズ グレードのデプロイ ソリューションを提供しています。この投稿では、Alibaba Cloud PAI (AI プラットフォーム) に Cosmos Reason-1-7B を迅速にデプロイし、使用する方法を探ります。

## NVIDIA Cosmos プラットフォーム

[NVIDIA Cosmos](https://www.nvidia.com/ja-jp/ai/cosmos/)™ は、最先端の生成[世界基盤モデル](https://www.nvidia.com/ja-jp/glossary/world-models/?ncid=so-nvsh-459205) (WFM)、高度なトークナイザー、ガードレール、加速データ処理とキュレーション パイプラインで構成されるプラットフォームです。 世界モデルのトレーニングを強化し、[自動運転車](https://www.nvidia.com/ja-jp/use-cases/autonomous-vehicle-simulation/) (AV) および[ロボット](https://www.nvidia.com/ja-jp/use-cases/robotics-simulation/)向けの[フィジカル AI](https://www.nvidia.com/ja-jp/glossary/generative-physical-ai/) 開発を加速するために構築されています。

Cosmos は、世界生成とポストトレーニングのための Cosmos Predict 、制御可能でフォトリアルな合成データのための Cosmos Transfer、フィジカル AI による推論のための Cosmos Reason、安全でない入力をフィルタリングするための事前ガードと一貫性のある安全な出力のための事後ガードを備えた Cosmos Guardrail など、開発者がそのまま使用できる事前トレーニング済みマルチモーダル モデルファミリを提供しています。

NVIDIA Cosmos Reason-1 は、動き、オブジェクト相互作用、時空関係を理解するために特別に開発された、完全にカスタマイズ可能なマルチモーダル AI 推論モデルです。 このモデルは、思考の連鎖 (CoT) 推論を使用して視覚入力を解釈し、与えられたプロンプトに基づいて結果を予測し、最適な意思決定に報酬を与えるものです。

実世界の物理学に基づいて推論し、自然言語で明確で文脈を認識した応答を生成します。 Cosmos Reason-1 は、他のフィジカル AI モデルに対するデータ批判および品質フィルタリング コンポーネントとして、また具現化されたエージェントの次の行動を推論する計画モデルとしても使用できます。

## Alibaba Cloud PAI-Model Gallery への Cosmos Reason-1-7B の統合

PAI-Model Gallery は、オープンソース AI コミュニティの高品質な事前トレーニング済みモデルを統合する Alibaba Cloud PAI のコンポーネントです。これにより、ユーザーはコーディング不要でオープンソース モデルのトレーニング (ファインチューニング)、圧縮、評価、展開を行い、モデルを推論に使用することができます。 これにより、AI 技術をより迅速、効率的、便利に活用できるようになります。  さらに、PAI-Model Gallery は、すぐに使える API を提供し、エンタープライズ グレードのデータ セキュリティをサポートします。

Cosmos Reason-1-7B を Alibaba Cloud PAI-Model Gallery に統合することで、「AI+Cloud」パラダイムに基づく事前トレーニング済みモデルのシームレスな準備とモジュラー設計により、マルチモーダル テクノロジ スタックの複雑さとモデル適応コストを最小限に抑えます。

企業や開発者は、クラウドネイティブ プラットフォーム上で生の視覚入力から物理的制約による高度な推論出力まで、エンドツーエンドの開発を実施することで、フィジカル AI のライフサイクル全体を加速化できます。

## Alibaba Cloud PAI への Cosmos Reason-1-7B のワンクリック デプロイ

![](https://developer-blogs.nvidia.com/ja-jp/wp-content/uploads/sites/6/2025/06/JP-screenshot-1-1024x470.jpg)

画像ソース: Alibaba Cloud

本章では、Alibaba Cloud PAI への Cosmos Reason-1-7B のワンクリック デプロイと、モデル パフォーマンス テストについて紹介します。

1. PAI-Model Gallery の Web サイトで Cosmos Reason-1-7B モデルを検索してください。以下のリンクをクリックしてください:  
   <https://pai.console.aliyun.com/?regionId=ap-northeast-1#/quick-start/models/Cosmos-Reason1-7B/intro>

![](https://developer-blogs.nvidia.com/ja-jp/wp-content/uploads/sites/6/2025/06/JP-screenshot-2-1-1024x465.png)

画像ソース: Alibaba Cloud

2. モデルの詳細ページの右上隅にある「デプロイ」ボタンをクリックし、コンピューター リソースを選択すると、クラウドへのモデル デプロイをワンクリックで実行できます。

![](https://developer-blogs.nvidia.com/ja-jp/wp-content/uploads/sites/6/2025/06/JP-screenshot-3-1024x539.jpg)

画像ソース: Alibaba Cloud

3. デプロイが正常に完了したら、サービス ページで「呼び出し情報を表示」をクリックしてエンドポイントとトークンを取得します。 サービスの呼び出し方法については、「事前学習済みモデル」のリンクをクリックしてモデル概要ページに戻り、詳細な呼び出し手順を確認してください。

![](https://developer-blogs.nvidia.com/ja-jp/wp-content/uploads/sites/6/2025/06/JP-Screenshot-4-1024x576.jpg)

画像ソース: Alibaba Cloud

4. 推論サービスを使用: API を介してモデル サービスを呼び出すことも、PAI プラットフォームが提供する Web ベースの UI を介してモデルとやりとりすることもできます。

## モデル性能テスト

このテストでは、[NVIDIA Research Web サイト](https://research.nvidia.com/labs/dir/cosmos-reason1/) のサンプル動画をモデル入力として使用しています。

動画では、人が牛乳をカップに注いでいます。 「人が牛乳をカップに注いだ後、次の行動は何が最も合理的ですか?」という質問を入力します。

モデルの応答は、その人の次の行動におけるさまざまな可能性を考慮したことを示しています。 牛乳を注いだ後に牛乳瓶を置き、スプーンで牛乳とコーヒーをかき混ぜるといったシナリオも構成しました。 徹底的に分析した後、モデルは次の論理的なステップは「牛乳瓶をカウンターに戻す」ことであると結論付けました。

このケースから、モデルは人の行動を正確に解釈し、正しい予測を提供しました。

予測推論に伴う動き、オブジェクト相互作用、時空関係を理解するこの能力は、一般に達成するのは困難です。 さらに、モデルは完全な一連の思考プロセスを出力し、思考プロセス全体を明確に理解することを可能にします。

以下は、参考用の動画、入力質問、モデル出力です。

- 質問: 全体的な目標は、「エージェントが牛乳をカップに注ぐ」ことです。 動画内のエージェントは、現在、この指示を完了するために多くのサブタスクの中の 1 つを実行しています。 動画内のエージェントにとって、最も可能性の高い次のサブタスクは何ですか?
- モデル出力: エージェントは現在、コップに牛乳を注いでいます。 注いた後の次のサブタスクは、論理的には期待する量になったら注ぐのを止めることです。 そして、エージェントは牛乳瓶をカウンターに戻す必要があります。 その後、こぼれないようにボトルのキャップを閉めるかもしれません。 最後に、スプーンで牛乳とコーヒーをかき混ぜ、完全に混ぜることもできます。 しかし、現在の行動は注ぐことです。そのため、注いだ後の次のステップは注ぐのを止め、瓶を置くことになります。 ただ、この質問は、最も可能性の高い次のサブタスクを要求していることです。 注いでいる動作は継続中なので、注いだ後の次のステップは牛乳瓶をカウンターに戻すことです。 あるいは、注いでいる動作がまだ進行中の場合、牛乳を全部注ぎ切るために角度を調整するかもしれません。 しかし、状況を考えると、エージェントは積極的に注いでいるため、それが完了したら瓶を下に置くことは理にかないます。 しかしながら、答えは注ぐのを止めて瓶を横に置くことかもしれません。 しかし、注いだ後の正確な次のステップは、ボトルを元の場所に戻すことです。 あるいは、エージェントはカップがいっぱいかどうかを確認する必要があるかもしれません。 しかし、注いだ後の最も論理的な次のステップは、注ぐのを止めてボトルを置くことです。 したがって、答えはおそらく「牛乳瓶をカウンターに戻す」ということです。

## 近日公開: NVIDIA Cosmos Reason-1 ツールを基盤とするモデル ポストトレーニングのベスト プラクティス

NVIDIA はまた、Cosmos Reason-1 ベンチマークでのモデルのトレーニングと評価に関連するスクリプトを使用して、Cosmos Reason-1 ツールをオープンソース化しました。

企業や開発者は、自社データに基づいて Cosmos Reason-1 モデルをカスタマイズし、提供されたポストトレーニングのスクリプト (SFT + RL) を活用して独自のフィジカル AI モデルを構築できます。

Alibaba Cloud PAI チームがテストした Cosmos Reason-1 ツールのパフォーマンスは以下の通りです。ポストトレーニングのテストでは、Cosmos Reason-1 ツールは Qwen2.5-32B-Instruct モデルと gsm8k データセット (バッチ サイズ = 2,048) の組み合わせに基づいて、小規模クラスターでオープンソース フレームワークの 1 ～ 2 倍の高速化を達成することが示されています。 **PAI は近日中に、Cosmos-Reason1 ツールのポストトレーニングの機能を統合する予定です。**

## Alibaba Cloud PAI で NVIDIA Cosmos Reason-1-7B モデルを始める

Cosmos Reason-1-7B を PAI 上で開始するには、Alibaba Cloud の日本国内のノードをご利用ください。Cosmos のその他のリソースをご覧ください。
