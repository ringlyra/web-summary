<!-- metadata -->

- **title**: 音楽生成AI 「Suno」でAWSの曲を作って楽しく資格勉強できないだろうか #SUNOAI - Qiita
- **source**: https://qiita.com/Takenoko4594/items/38e50a607ce2dad2ab06
- **author**: qiita.com
- **published**: 2025-06-03T14:47:30Z
- **fetched**: 2025-06-04T12:43:43Z
- **tags**: codex, suno, aws, music
- **image**: https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-v4.9f790b4dcf003500eb01.png?auto=format&bg=fff&fit=fill&fill=blur&w=1200&h=630&q=100&s=63164cc85fd254d91d216087b2a78c3f

## 要約

**Suno**という音楽生成AIを使い、**AWS**サービスをテーマにしたオリジナル曲で資格学習を盛り上げようという記事。Claude 4を用いて歌詞を作り、Sunoで曲を生成する手順を紹介。試作曲として"Foundation of Tomorrow"など3曲を掲載し、Sunoの無料枠情報も触れている。

## 本文 / Article

# はじめに

最近、音楽が簡単に作れる 「Suno」という生成AIを知りまして、AWSサービスを曲にしたら資格の勉強が捗るでは？という思い付きです。

youtubeとか学習コンテンツでもいいんですが、通勤中とかはテンション上げたいなーと思い、自部でいい感じの曲を作ってみることにしました。

### 作った曲

というわけで下記に作った曲を載せます。

### 1曲目：Foundation of Tomorrow

Amazon Bedrockの曲です

### 2曲目：Edge of the World

Amazon CloudFrontの曲です

### 3曲目：Chronos Chronicles

Amazon Timestreamの曲です

# Sunoとは

無料枠もありまして1日に5曲？くらいは作れるようなので、気になった方はぜひ！

# 作ってみる

## 題材を決める

今回は、「Amazon Bedrock」をテーマに音楽を作ります。

## 歌詞を用意する

音楽を作る上で歌の歌詞が必要となります。  
今回は、Claude 4 Sonnet にAmazon Bedrockの歌詞を書いてもらいます。

プロンプト1回目

```
Amazon Bedrockの歌詞を考えてください。目的は学習に利用するので、正しい内容でお願いします。

```

プロンプト2回目

```
歌っぽくなくていいので、概要から詳細までブレイクダウンするような歌詞をお願いします。

```

生成結果

```
# Amazon Bedrock学習用テキスト

## 第1章：概要と基本概念

Amazon Bedrockは何なのか
AWSの生成AI基盤サービス
Foundation Modelsへの統一アクセス
サーバーレスでスケーラブル

基盤モデルとは何を意味するか
大規模データで事前学習済み
テキスト、画像、コードを理解
汎用性高い推論能力を持つ

なぜBedrockが必要なのか
AIモデル構築は複雑で困難
インフラ管理、スケーリングの課題
マネージドサービスで解決

## 第2章：アーキテクチャと技術基盤

APIベースのアクセス方法
REST APIとSDKを提供
boto3、CLI、コンソールから利用
リアルタイムとバッチ処理対応

セキュリティアーキテクチャ
データはAWS内で処理される
顧客データでモデル訓練しない
暗号化、アクセス制御、監査ログ

リージョンとアベイラビリティ
複数リージョンでサービス展開
高可用性とディザスタリカバリ
レイテンシ最適化の地理的配置

## 第3章：利用可能なモデルプロバイダー

Anthropic Claude シリーズ
高度な推論と安全性重視
会話、分析、コード生成に強み
複数バージョンとサイズ展開

Amazon Titan モデル群
テキスト生成と埋め込み提供
AWSネイティブで最適化
多言語対応とカスタマイズ性

AI21 Labs Jurassic モデル
創造的テキスト生成に特化
長文コンテンツ作成に適している
ビジネス文書生成で実績

Cohere Command と Embed
企業向けNLP機能に特化
分類、要約、検索拡張に強み
多言語サポートと安定性

Meta Llama モデル群
オープンソース系の選択肢
カスタマイズ性と透明性
研究開発での利用実績

Stability AI 画像生成
Stable Diffusion アクセス
テキストから画像生成
高品質な視覚コンテンツ作成

## 第4章：主要機能とサービス

テキスト生成機能の詳細
プロンプトエンジニアリング重要
温度パラメータで創造性調整
トークン制限とコンテキスト管理

カスタムモデル作成機能
ファインチューニングで性能向上
独自データセットでの学習
継続事前学習も可能

モデル評価とベンチマーク
人間評価とAI評価の組み合わせ
タスク固有の評価指標
A/Bテストでの性能比較

知識ベース統合機能
RAG（検索拡張生成）実装
ベクトルデータベース連携
リアルタイム情報更新対応

## 第5章：実装と開発手法

APIコール基本パターン
認証情報の設定方法
リクエスト形式とレスポンス処理
エラーハンドリングのベストプラクティス

SDK利用による開発効率化
Python、Java、JavaScript対応
高レベル抽象化で開発簡素化
非同期処理とストリーミング対応

プロンプトエンジニアリング手法
システムプロンプトの設計
Few-shot学習の活用方法
Chain-of-Thought推論の実装

パフォーマンス最適化戦略
バッチ処理でのスループット向上
キャッシュ戦略による応答時間短縮
並列処理での処理能力拡張

## 第6章：セキュリティとコンプライアンス

データプライバシー保護
顧客データの分離保証
処理後のデータ自動削除
GDPR、CCPA準拠対応

アクセス制御機能
IAMポリシーによる細粒度制御
リソースベースポリシー設定
一時的認証情報の活用

監査とログ機能
CloudTrailによる API呼び出し記録
CloudWatchでの利用状況監視
コンプライアンスレポート生成

セキュリティ認証取得状況
SOC、ISO27001認証済み
HIPAA、PCI DSS対応
業界固有のコンプライアンス要件

---

## 学習ポイント解説

この歌詞に含まれる重要なAmazon Bedrockの概念：

- **基盤モデル（Foundation Models）**: 大規模な事前学習済みAIモデル
- **API経由でのアクセス**: プログラムから簡単に利用可能
- **複数のモデル提供**: Claude、Amazon Titan等の選択肢
- **ファインチューニング**: 独自データでモデルをカスタマイズ
- **セキュリティ**: 企業レベルの安全性
- **RAG（Retrieval-Augmented Generation）**: 外部知識との組み合わせ
- **従量課金**: 使用量に応じた料金体系
- **AWSとの統合**: 既存のAWSサービスとの連携

```

## Sunoで音楽を作る

### サインアップまたはサインイン

以下にアクセスし、サインアップまたはサインインします。

### 音楽を作成する

左のメニューから「Create」を選択します。曲の作成方法は「Custom」を選択します。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2Fa6aee2e0-d5bd-4051-95a1-8129e297c4c3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a7a73119a635788254653cb256e7d13f)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2Fa6aee2e0-d5bd-4051-95a1-8129e297c4c3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a7a73119a635788254653cb256e7d13f)

Lyrics欄に先ほどClaude 4で生成した歌詞を入力します。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F76217e63-a666-4b8f-a9ee-242a5bbd3400.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9fcac28c2543391346aa73f00a8f9b42)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F76217e63-a666-4b8f-a9ee-242a5bbd3400.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9fcac28c2543391346aa73f00a8f9b42)

Syles欄は、好きな曲のジャンルを選択します。今回は「electonic」を選択しました。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2Fa3c7a03d-7ca8-4913-9cd6-d2f7dc4ac7fa.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=462cdd87b53fce1495812808ed1fddb7)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2Fa3c7a03d-7ca8-4913-9cd6-d2f7dc4ac7fa.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=462cdd87b53fce1495812808ed1fddb7)

Persona欄は、歌手のペルソナを指定できるようなのですが、今回は空欄です。  
曲を生成するたびに歌手を固定したい場合などに利用するようです。

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F52641bd8-e2d1-41bc-98e4-29d4bdcfed13.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ba0bf61a7c24864b1a6087af9cb90158)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F52641bd8-e2d1-41bc-98e4-29d4bdcfed13.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ba0bf61a7c24864b1a6087af9cb90158)

Song Title欄は、任意の曲タイトルを入力します。今回は別途生成AIに考えてもらった「Foundation of Tomorrow」とします。  
(基盤モデルの「Foundation」と未来への架け橋という意味を込めて。らしいです)

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F39cea7cc-c2d4-4085-a0b1-79137efcefff.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9c3983787fd9bafa1e4900c49767475a)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F39cea7cc-c2d4-4085-a0b1-79137efcefff.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9c3983787fd9bafa1e4900c49767475a)

最後に「Create」ボタンを押してみます。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F6e9dcb87-703e-4fad-8c9c-e678a8943d7c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e2a97e707822ee6c2863954db8218cf4)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F6e9dcb87-703e-4fad-8c9c-e678a8943d7c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e2a97e707822ee6c2863954db8218cf4)

多分出来ました！これだけで曲からボーカルまで作ってくれます！  
ちなみに1度に2曲作ってくれるみたいです  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F5b5d211c-9660-4579-b816-a8791143182a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fafac52836e26f24b9bf2ac897ab535e)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F560123%2F5b5d211c-9660-4579-b816-a8791143182a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fafac52836e26f24b9bf2ac897ab535e)

# 所感

最近は、こんな簡単に音楽作れちゃうんだなぁとしみじみと感じました。  
無茶ぶりで依頼してもいい感じの曲にしてくれるので、単純に曲を作っても楽しそうですね。

今回の主題としては、音楽+AWSサービスでAWSの試験勉強を楽しくできないかな？という内容でしたが、ラップとかポップな曲でなければ、いい感じに勉強になりそうな気がします。

ただ流石に、テンポが速いと聞き取れないですね...ジャンル選択は大事そうです

作った曲については、実際に通勤中とかに聞いてみて、資格勉強に役立ててみたいと思います！
