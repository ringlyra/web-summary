---
title: '【インターンレポート】OpenAI Agents SDK (Python版) でコールセンター風音声対話型マルチエージェントデモを作ってみた(おまけ付き) - Insight Edge Tech Blog'
source: https://techblog.insightedge.jp/entry/tech-blog-intern-1
author:
  - techblog.insightedge.jp
published: '2025-07-10T00:00:00Z'
fetched: '2025-07-11T23:52:21.477686+00:00'
tags:
  - codex
  - insightedge
image: https://cdn.image.st-hatena.com/image/scale/160935e92c70756fde208424f53d8ca4a32bc30f/backend=imagemagick;version=1;width=1300/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20250710%2F20250710102051.png
---

## 要約

サッカー映像分析を研究する東京科学大学院生の筆者が、昨年のインターンをきっかけに再びInsight Edgeでアルバイトし、OpenAI Agents SDK（Python版）を利用したコールセンター風音声対話型マルチエージェントデモを開発。AIエージェント普及の変遷や音声対話モデルの利点、主要リアルタイムAPIや各社開発キットを整理し、SDKのハンドオフ・MCP・ツール機能を組み合わせたデモ構成と実装を詳説した。ガードレールなしでも機能を再現できたが応答遅延が10秒以上と大きいため、Speech-to-Speechアーキテクチャへの移行やカスタムボイスによるアバターベース展開を模索したいと締めくくる。

## 本文

[2025-07-10](https://techblog.insightedge.jp/archive/2025/07/10)

[【インターンレポート】OpenAI Agents SDK (Python版) でコールセンター風音声対話型マルチエージェントデモを作ってみた(おまけ付き)](https://techblog.insightedge.jp/entry/tech-blog-intern-1)
=========================================================================================================================================

[AIエージェント](https://techblog.insightedge.jp/archive/category/AI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88)
[OpenAI Agents SDK](https://techblog.insightedge.jp/archive/category/OpenAI%20Agents%20SDK)
[生成AI](https://techblog.insightedge.jp/archive/category/%E7%94%9F%E6%88%90AI)
[音声解析](https://techblog.insightedge.jp/archive/category/%E9%9F%B3%E5%A3%B0%E8%A7%A3%E6%9E%90)

目次
--

* [【インターンレポート】OpenAI Agents SDK (Python版) でコールセンター風音声対話型マルチエージェントデモを作ってみた(おまけ付き)](#%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%B3%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88openai-agents-sdk-python%E7%89%88-%E3%81%A7%E3%82%B3%E3%83%BC%E3%83%AB%E3%82%BB%E3%83%B3%E3%82%BF%E3%83%BC%E9%A2%A8%E9%9F%B3%E5%A3%B0%E5%AF%BE%E8%A9%B1%E5%9E%8B%E3%83%9E%E3%83%AB%E3%83%81%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%83%87%E3%83%A2%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%E3%81%8A%E3%81%BE%E3%81%91%E4%BB%98%E3%81%8D)
  + [はじめに](#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB)
  + [1.AIエージェント✖️音声 = 音声エージェント](#1-ai%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%EF%B8%8F%E9%9F%B3%E5%A3%B0--%E9%9F%B3%E5%A3%B0%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88)
    - [1.1 普及してきたAIエージェントについて](#11-%E6%99%AE%E5%8F%8A%E3%81%97%E3%81%A6%E3%81%8D%E3%81%9Fai%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)
    - [1.2 音声エージェントの恩恵について考える](#12-%E9%9F%B3%E5%A3%B0%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%81%A9%E6%81%B5%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E8%80%83%E3%81%88%E3%82%8B)
    - [1.3 リアルタイム音声対話API・音声エージェント開発ツールの紹介](#13-%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E9%9F%B3%E5%A3%B0%E5%AF%BE%E8%A9%B1api%E9%9F%B3%E5%A3%B0%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E9%96%8B%E7%99%BA%E3%83%84%E3%83%BC%E3%83%AB%E3%81%AE%E7%B4%B9%E4%BB%8B)
  + [2. OpenAI Agents SDK (Python版)で作る音声対話型マルチエージェントツール](#2-openai-agents-sdk-python%E7%89%88%E3%81%A7%E4%BD%9C%E3%82%8B%E9%9F%B3%E5%A3%B0%E5%AF%BE%E8%A9%B1%E5%9E%8B%E3%83%9E%E3%83%AB%E3%83%81%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%83%84%E3%83%BC%E3%83%AB)
    - [2.1 OpenAI Agents SDKとは](#21-openai-agents-sdk%E3%81%A8%E3%81%AF)
    - [2.2 2種類の音声エージェントの構造](#22-2%E7%A8%AE%E9%A1%9E%E3%81%AE%E9%9F%B3%E5%A3%B0%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E9%80%A0)
    - [2.3 デモの紹介](#23-%E3%83%87%E3%83%A2%E3%81%AE%E7%B4%B9%E4%BB%8B)
    - [2.4 今後の展望](#24-%E4%BB%8A%E5%BE%8C%E3%81%AE%E5%B1%95%E6%9C%9B)
  + [おわりに](#%E3%81%8A%E3%82%8F%E3%82%8A%E3%81%AB)
  + [参考資料](#%E5%8F%82%E8%80%83%E8%B3%87%E6%96%99)

はじめに
----

こんにちは！！！

Insight Edgeでアルバイトをしております、東京科学大学大学院 修士2年の田中です。大学院では、経営工学系の研究室で、サッカーの試合映像分析に関する研究をしています。私の研究室では、(知識)グラフやLLM、強化学習を用いた、金融や自動運転などのあらゆる産業領域への応用研究が活発になされており、様々な領域の研究を知ることができます。

Insight Edgeさんとは、昨年に行われた1ヶ月間のインターンシップから関わらせていただいております。そのインターンでは視覚言語モデルのPoCに参加させていただきました。そのようなご縁もあり、来年度からはデータサイエンティストとしてお仕事させていただけることとなりましたので、今後ともお付き合いよろしくお願いいたします🔥🔥🔥

さて、前置きが長くなりましたが、本記事ではタイトルにもある通り、OpenAI Agents SDK(Python版)で作成したコールセンター風音声対話型マルチエージェントのデモについてご紹介したいと思います。用いた技術スタックや実際に使ってみた使用感を中心に、デモ映像なども交えてご紹介します。

第1章では、まずは背景として、なぜ音声エージェントが最近注目されているかということを理解していただけるように、AIエージェント/音声対話モデル/音声エージェントの現状についてそれぞれ紹介していきます。

第2章では、今年の3月に公開されたOpenAI Agents SDK (Python版)のコア機能を紹介します。これらの機能を用いて作成した音声マルチエージェントの作成過程を通して、そのリアルな使用感や作成時の注意点を明らかにし、最後に今後の展望をお伝えします。

それでは行ってみましょう！！

(※) 本記事はこれを執筆した2025年6月下旬時点でのお話となります。またこの記事の筆者は現場経験に乏しい大学院生である点をご理解いただき、それを踏まえた上で温かい心で一読いただけると幸いです。

1.AIエージェント✖️音声 = 音声エージェント
-------------------------

本章では、まずAIエージェントの定義...というよりかは、AIエージェントの普及の変遷をたどるような形で、AIエージェントの開発を後押しする様々な道具をご紹介します。次に音声エージェントについて、従来のテキストベースのAIエージェントとの違いを明確にしながら、使用用途や、使用する上で留意しておくべきことを紹介します。最後に、音声エージェントを開発する上では外せないリアルタイム対話型モデルと、開発キットをいくつかまとめたのでご紹介します。本章を通して、音声エージェントに少しでも親しみを持っていただければと思います。

### 1.1 普及してきたAIエージェントについて

「2025年はAIエージェントの年だ」という言葉をよく耳にします。確かにその活用事例は今年から爆発的に見られるようになってきました。しかし、その下地は2年ほど前からありました。2023年のLangChainのようなフレームワークの開拓が1つ目の下地です。これはLLMを1つのエージェントと見立て、複数のエージェントが連鎖的に回答を思考するフローを構築できます。そして他方では、昨年から今年にかけて提唱された、外部ツールや異なる規約を持つエージェント同士の連携への需要に応えるためのインフラ整備がなされてきました。これまではエージェントの脳みそとしての役割を担うLLMの内部知識のみで完結するような、一般的なタスクへのエージェント構築に留まっていた。しかし、MCPやA2Aといった新しいプロトコル(規約、取り決め)によって、メールアプリ処理やローカルファイル処理など、外部ツール操作や外部ベンダーエージェントとの協調が必要となる、専門性の高いタスクへのエージェント構築が可能となりました (下図参照)。

これは、LLMの内部知識にはない情報にアクセスできる権限をエージェントへ与えることで、これまでのRAG的な検索機能に加えて、これまで人間が行っていたようなアプリケーションの操作する機能もエージェントに備わったことを意味します。

* **Model Context Protcol(MCP)**: Ahthropicが2024年11月に提唱、AIツールにローカルまたはインターネット上のサーバーとの情報のやり取りのルールのこと
* **Agent to Agent(A2A)**: Googleが2025年4月に提唱、別々の役割が与えられたAIエージェントに共有させるルールのこと

![A2AやMCPの説明](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090013.png)


A2AとMCPの概要図 (参照: A2A Protcol
(<https://a2aproject.github.io/A2A/latest/#why-a2a-matters>))

この流れを受けるかのように、OpenAI・Google・AWSのような大手AI・クラウドプロバイダーが、それぞれが持つサービスや、外部ツール・エージェントとの簡易的な統合を目的として、OpenAI Agents SDK (Python版は25年3月)・Agent Development kit(25年4月)・Strands Agents SDK(25年5月)のようなエージェント開発キットを公開しています。

これら以外にもすでにさまざまなAIエージェントの開発キットが続々と登場してきています。実際にAIエージェントを作る際は、自分達の課題と開発環境に適したものを選定する必要があるでしょう。

### 1.2 音声エージェントの恩恵について考える

現在、対話型マルチエージェントと称されるものの多くが、テキストベースのものです。テキストベースのエージェントを使用する際は、ユーザーがキーボードでクエリを入力し、そのクエリに応じた回答をエージェントがテキストで返し、その回答に応じて再びユーザーがクエリを入力し...というようなループが続きます。それに対して、今後はユーザーの入力とエージェントの出力が音声に置き換えられるような音声対話型マルチエージェントの事例が増えてくるのではないかと予想しています。なぜなら、音声機能を持ったエージェントは以下のような恩恵をもたらしてくれるからです。

1. **ハンズフリーで伝達が楽で早い**：人同士の対話も、キーボードで入力するよりかは発話形式で行った方が早いですし、楽ですよね。そもそもキーボードが手元にない場面や、打っている時間がない場面、キーボードの扱いが難しい場合でも役立ちそうです
2. **感情の伝達ができる**：たとえばカスタマーセンターのように、ユーザー側の感情をAIに理解させた上で対応してもらった方がいい場面があるかもしれません。また、エージェント側に感情豊かに話してもらうことで、聴きやすさが増すかもしれません。NotebookLMの音声機能が特にわかりやすい事例ですね
3. **新しいユーザー体験の提供**：テキストベースではどうしても、「AIを道具として使用している感」が強かったのです。しかし、音声での会話は「AIを仕事仲間として・友達として使用している感」が強まります(筆者の体感に基づく)

音声ベースでのエージェントは、テキストベースのエージェントに比べて、情報の入出力の伝達速度が早いことや伝達が簡易であること、さらに人間のように感情表現の伝達ができるという点で恩恵があります。音声エージェントとのやりとりをする際に求められることは、テキストベースで求められていた、**いかにして正しい情報を早く引き出すか**という要素に加えて、いかにして人間同士のやりとりに近づけるかがあります。つまり、**人間的な会話の間合いや相槌、言語特有のイントネーションや息継ぎのタイミング、相手の感情など理解した上での柔軟な言葉選びや対応の仕方の再現**が重要な要素になっているのです。

AIエージェントの使用用途は様々ですが、音声機能を持ったエージェントならではの応用事例は、以下のようなものが挙げられます。

* カスタマーセンター：リアルタイムで顧客に対応し、顧客の情報を処理しながら、適切に社内のナレッジを参照して回答を提供したり、人間のオペレーターに引き継いだりする
* 会議のファシリテーターや書記：会議のサポート機能全般を担う。議事録作成、リマインダー機能など
* ナビゲーションシステム：PCやスマホ、車に搭載し、料理や機械操作、道案内など、あらゆる用途でナビゲーションさせる
* エンタメ：カスタム音声(ボイスクローニング)機能などを用いて、特定のキャラクターを模したAIと会話させる (マルチエージェント要素は少ない)

人間が対応する場合と比較して、音声エージェントを使用するメリットはどのようなことが挙げられるでしょうか？たとえば以下のようなことが挙げられます。

* 24時間365日稼働可能
* オペレータの負担削減
* 人件費削減
* 多言語対応可能

このようなメリットがある一方で、以下のようなデメリットもあります。

* 聞き間違えと言い間違え：特定の言語に対する音声認識性能や音声合成性能が低いと、実用化できません
* 全対応の難しさ：これまで人間が行なっていたことを形式知化した上でプロンプトと機構で再現し、フルコミットさせることの難しさ
* 作業量と遅延のトレードオフ：音声マルチエージェントのマルチエージェント部分で行う作業量が増えるほど、返答速度が低下してしまう

したがって、音声エージェントを構築していく際は、このようなデメリットを考慮しつつ、これらをなるべく軽減できるような環境やモジュールの選定・構築が必要となるでしょう。
とりわけ、聞き間違え・言い間違え・遅延は音声を扱う上では、かなりセンシティブにならなければならない課題であることを確認しておきましょう。

### 1.3 リアルタイム音声対話API・音声エージェント開発ツールの紹介

音声エージェントの耳、そして口(喉？)の役割を果たすのが、音声認識 (Speech-To-Text)と音声合成 (Text-To-Speech)です。それぞれ、多言語に対応したツールや、日本語特化ツール、ローカルツールなど非常にたくさんあり、ここで紹介しきれませんが、どちらの技術も日進月歩で大きく進歩しています。
例えば音声合成に関して、2025年5月に公開された、Googleの多言語対応音声合成モデル(gemini-2.5-flash-preview-tts)の使用事例が以下の記事で紹介されています。このモデルはマルチスピーカーでの発話設定が可能で(執筆時点で最大２名)、この記事では2人の日本人による漫才スクリプトをこのモデルに発話させた結果を聞くことができます。聞いてみると、思っている以上に自然なイントネーションの日本語が発話されていることを確認できるかと思います。

[Gemini API TTS（Text-to-Speech）で漫才音声を生成してみた](https://zenn.dev/sonicmoov/articles/bd862039bcba46)

さらにAIと直接リアルタイムで会話することを目的とした、Speech-to-Speech型のモデルも増えてきています。
Speech-to-Speechとは、音声認識、回答生成、音声合成を一貫して行うモデル構造のことで、低遅延で、より人間らしい自然な会話を実現することを目指しています。これまでのような、複数の固有のモデルを組み合わせたモデル構造と異なり、Speech-to-Speech型のモデルでは、認識した音声をテキスト化せずそのまま特徴量として使用しているため、テキスト化する際に欠落してしまう発話者の感情やトーンのような非言語的特徴を回答生成や音声合成に有効に利用できます。
以下に、6月時点でSpeech-to-Speechモデルを使用できる代表的なAPIとその特徴をまとめています。基本的にどのモデルもToolCallに対応しており、エージェント的な使用も可能です。

| API | 公開日 | 6月中旬時点での使用可能モデル | 競合と比較した際の特徴 |
| --- | --- | --- | --- |
| OpenAI Realtime API | 2024.10 (WebSocket)   2024.12 (WebRTC) | gpt-4o-realtime-preview-2025-06-03   gpt-4o-mini-realtime-preview-2025-06-03 | WebRTCでの利用が可能 |
| Google LiveAPI | 2025.4 (Preview) | gemini-2.0-flash-live-001   gemini-live-2.5-flash-preview   gemini-2.5-flash-preview-native-audio-dialog (イントネーション改善、感情認識)   gemini-2.5-flash-exp-native-audio-thinking-dialog (Deep think版) | PCカメラやスクリーン共有など、画像や動画を介したリアルタイム会話に特化 |
| Azure Voice LiveAPI | 2025.5 (Preview) | gpt-4o-realtime-preview gpt-4o-mini-realtime-preview phi4-mm-realtime | Azure内の音声ツール(ビルトイン/カスタムのアバター、音声)との統合が可能 |
| AWS SDK Bedrock API | 2025.4 | Amazon Nova Sonic | AWS上での利用に特化 |

今後は、どのエージェント開発フレームワークにも、リアルタイム対話モデルが組み込めるようになると思われます。LiveKitのようなWebRTCでの通信を前提としたユーザー・サーバー間やサーバー間の低遅延通信を行いつつ、Speech-to-Speech型のモデルと、外部ツールや異なるベンダーのエージェントとの連携によって遅延の少ないような、音声対話型マルチエージェントを構築していくようなイメージです。その際、使用する可能性がある、大手AIベンダーが提供しているエージェント開発キットも下の表にまとめています。基本的には、先ほど紹介したリアルタイム音声エージェントも組み込むことができ、MCPやA2Aプロトコルでの外部連携機能も備わっています。

| SDK | 公開日 |
| --- | --- |
| OpenAI Agents SDK | 2025.3 (Python版)   2025.6 (TypeScript版) |
| Google Agent Development Kit (ADK)   Google Vertex AI Agents | ADK: 2025.4 |
| Azure AI Foundry Agent Service | 2025.5 (一般提供開始) |
| AWS Strands Agents | 2025.5 |

以上で、第１章はおわりです。本章を通じて、音声エージェント関連の背景知識や便益、現状公開されているツールの一部をお伝えできたかと思います。次章では、音声エージェント技術的な部分をもう少し深掘りするため、上の表で紹介したエージェント開発キットを用いて実際に作成したデモをお見せし、開発キットの使用感や、基本的な技術、音声エージェントの雰囲気を少しでも理解していただければと思います。

2. OpenAI Agents SDK (Python版)で作る音声対話型マルチエージェントツール
--------------------------------------------------

この章では、実際にエージェント開発キットを利用して作成した音声対話型マルチエージェントのデモの様子をお見せします。今回は、1.3節で紹介した開発キッドの中で、比較的早くから利用可能だったOpenAI Agents SDK(Python版)を使用しています。始めに、OpenAI Agents SDKの基本的な情報と機能を紹介します。次に、一般的な音声エージェントの構造として2つ、Chained ArchitectureとSpeech-to-Speech Architectureをそれぞれ紹介します。続いて、デモの紹介として、実際のコードとマルチエージェントの全体像、そしてデモを動かしている動画をお見せします。最後に残る課題と今後の展望についてお伝えします。

### 2.1 OpenAI Agents SDKとは

OpenAI Agents SDKとは、OpenAIによって提供されているオープンソースのPython/TypeScript用のライブラリのことで、AIエージェントの開発を簡素化するために設計されています。
OpenAI Agents SDKで提供されている基本的な機能として以下のようなものがあります。

* **ハンドオフ (Handoffs)**  
  あるエージェントが自分の役割を超えるタスクに遭遇した際、専門エージェントに委譲する仕組み。  
  複雑なワークフローを円滑に進めることができます。  
  *この開発キットは A2A が提唱される前に公開されたものですが、考え方は共通です。*
* **エージェントのツール化 (Agent as a tool)**  
  他のエージェントをツールとして利用し、LLMへの問い合わせを**関数呼び出し形式**で行えます。
* **MCP**  
  エージェントが外部ツールへアクセスしたり、特定機能を実行したりするための**拡張機能**。
* **関数呼び出し (Function calling / Tools)**  
  開発者が定義した **Python 関数**をAIエージェントにツールとして提供し、必要に応じて実行可能。
* **組み込みツール**  
  Web検索・ファイル検索・コンピューター操作など、標準で備わっているツール群。
* **ガードレール (Guardrails)**  
  エージェントの入力・出力を検証／制御し、安全性と品質を確保する機能。
* **トレーシング (Tracing)**  
  エージェントの実行フローを時系列で可視化・記録し、デバッグや性能分析を容易にします。
* **ストリーミング生成**  
  エージェント実行中の出力やイベントを**チャンク単位**で順次受け取る仕組み。

今回の作成したデモは、特にハンドオフ・MCP・Tools・ガードレール・ストリーミング生成がコア技術となります。これらの機能を組み合わせて、音声機能を持ったマルチエージェントを構築していきます。

### 2.2 2種類の音声エージェントの構造

OpenAI PlatformのWebサイトのVoice agentsページでは、２種類の音声マルチエージェントの構造が紹介されています。
1つ目のSTT, TTS組み込み型のChained Architectureは、テキストベースのマルチエージェントを個別のSTTモデルとTTSモデルで挟み込んだ構造をとっています。それぞれの入出力の管理がしやすいことや、構築のしやすさが利点としてあげられます。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090015.png)


Chained architecture: STT, TTS組み込み型のエージェント構造
(参照: OpenAI platform, "Voice agents"
(<https://platform.openai.com/docs/guides/voice-agents?voice-agent-architecture=speech-to-speech>))

一方、2つ目のSpeech-to-Speech Architectureは、1.3節で紹介したSpeech-to-Speechモデルの使用を前提としたマルチエージェントのことを指しています。Chained Architectureと比較し、遅延が少ないこと、感情や声のトーンのような非言語的な要素も伝達可能であることが利点としてあげられます。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090015.png)


Speech-to-speech (realtime) architecture: Speech-to-Speech型のエージェント構造
(参照: OpenAI platform, "Voice agents"
(<https://platform.openai.com/docs/guides/voice-agents?voice-agent-architecture=speech-to-speech>))

どちらの構造を取るかは、その用途に応じて考える必要があるでしょう。OpenAI Agents SDKはPython版とTypeScript版があり、現在Python版では1つ目のChained Architectureのみをサポートしています。TypeScript版はSpeech-to-Speech構造のエージェントを作成できるとのことですが、この記事を書いている2,3週間ほど前に、出たばかりということもあり、残念ながら今回は紹介できません。今回は、Python版の開発キットを用いて、Chained-Architecture構造のマルチエージェントを作成しています。

### 2.3 デモの紹介

それでは早速デモの作成の順序を説明していきます。まず、コードを書く前にする作業としてコールセンターの設定を考えます。たとえば以下のような設定です。

* 会社名: 任意
* 取扱製品・サービス: 10種類のデジタル製品
* 質問タイプ:　商品注文・商品取扱・クレーム・全く関係のない質問
* その他: 対応マニュアル(最初に名前を伺うなど？今回はエージェントごとのプロンプトで代用)

マルチエージェントとしてエージェントを複数用意するのであれば、質問タイプごとに用意することが1つの方法です。今回の例では、以下のエージェント構成が考えられます。まず、電話対応を行い質問タイプを認識するトリアージエージェントです。次に、商品注文・商品取扱・クレーム・無関係な質問をそれぞれ担当する専門エージェントです。特に、全く関係のない質問を担当するエージェントとして、2.1節で紹介したガードレールが役に立ちます。ガードレールは特別なエージェントで、質問が状況に相応しくない場合においてトリガーとしてエラーを吐き出す入力ガードレールと、エージェントによる出力が状況に相応しくない場合においてエラーを吐き出す出力ガードレールの2種類が用意されています。

今回は、たとえば「20+30はなんですか？」「月面に初めて到着した宇宙飛行士は誰？」といった状況に相応しくない質問がなされることを想定して、このような質問を弾くようなプロンプトをガードレールエージェントへ与えています。
これらを踏まえて、各エージェントの役割と関連を以下のように決めました。

* トリアージエージェント: 最初に質問者の名前と質問を聞き、質問からは質問タイプを類推する。質問タイプに応じて、担当のエージェントに質問者の名前・質問タイプをコンテキストとして渡し、対応を委譲(ハンドオフ)する。今回はコンテキストを更新する関数として、質問者が名前と質問を言った場合にそれらを記憶する関数を用意し、ToolCallに設定した。全く関係のない質問に関しては、取り付けたガードレールエージェントを呼び出し、「この質問には答えられない」といった旨の内容を出力する
* 商品注文エージェント: 質問者が買いたい製品を確認し、productsという名前のフォルダにそれぞれまとめた、製品情報テキストファイルの名前から該当する製品を探す。該当商品があれば、最後にもう一度確認して、質問者の同意を得たら注文完了メールをSlackに送信し、トリアージエージェントに仕事を再び受け渡す
* 商品取扱エージェント: 質問者が指摘している製品に関する情報を、productsフォルダ内の個別の製品情報テキストファイルから検索し、回答になりそうな部分を抽出し、回答を作成する。回答できない場合は、「申し訳ありませんが、回答できません」と回答させ、トリアージエージェントに仕事を再び受け渡す (人間のオペレータに繋ぎ直すという方法も考えられる)
* エラー・トラブル・クレーム対応エージェント: 質問者の指摘に対応する。製品に関してであれば、製品情報テキストから検索を行い回答を考える。答えられない場合は、「申し訳ありませんが、回答できません」と回答させ、トリアージエージェントに仕事を再び受け渡す

今回用いた、ToolとMCPは以下の通りです。

* Tool: update\_customer\_info (トリアージエージェントで質問者の名前を更新し、他のエージェントに受け渡す)
* MCP: Filesystem Server MCP (指定したフォルダの中身を操作できるようにする), SSE Slack API Server (自分で用意したSlackチャネルにBot招待し、Botが色々と話せるようにする)

最後に、音声モデルのパイプラインに統合し、ストリーミングでの再生を行えるように設定します。
これで以上となります。それでは、私が最初に作成したエージェントの概観図とコードをみていきましょう。

![最初の音声エージェントの概観図](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090022.png)


最初の音声対話型マルチエージェントの概観図

```
# 製品情報テキストファイルの一例 (Claudeで作成)

商品ID: PROD_004

【基本情報】
商品名: スマートスピーカー D47 Air
モデル番号: スD-6658
発売年: 2022
メーカー: イノベーション工房
工場住所: 北海道札幌市中央区架空町1-5-6

【寸法】
高さ: 7.9 cm
幅: 7.2 cm
奥行き: 2.9 cm
重量: 625 g

【カラーオプション】
- シルバー
- ホワイト
- グリーン

価格: 114,800円
保証期間: 36ヶ月

【取扱説明書の概要】
1. 初期設定：製品の電源を入れ、画面の指示に従って初期設定を完了してください。
2. 基本操作：スマートスピーカー D47 Airの主要な機能と操作方法について説明します。
3. 充電方法：付属の専用充電器または推奨される充電方法で充電してください。バッテリー寿命を延ばすためのヒントも含まれます。
4. トラブルシューティング：簡単な問題解決のためのステップバイステップガイド。
5. 安全上の注意：製品を安全にご利用いただくための重要な情報。

【サポート情報】
■ よくある質問
Q: スマートスピーカー D47 Airの電源が入らない場合の対処法は？
A: まず、製品が十分に充電されているか確認してください。次に、電源ボタンを10秒以上長押しして強制再起動をお試しください。それでも解決しない場合はサポートセンターにご連絡ください。

Q: スマートスピーカー D47 Airの保証期間は？
A: 通常、スマートスピーカー D47 Airの保証期間はご購入日から12ヶ月です。詳細は保証書をご確認ください。

■ エラーコード
E301: ネットワーク接続エラー。接続設定を確認してください。
E302: ストレージ容量不足。不要なデータを削除してください。
E203: バッテリー残量低下。充電してください。

■ サポートセンター
電話: 0120-12x-26x (受付時間: 平日9:00-18:00)
メール: support.d-6658@example-company.co.jp
ウェブサイト: http://www.example-company.co.jp/support/スd-6658

```

```
# config.py

import numpy as np
from pydantic import BaseModel

MODEL = "gpt-4o-mini"
SAMPLE_RATE = 24000
FORMAT = np.int16
CHANNELS = 1
VOICE_INSTRUCTION = "あなたは、コールセンターのエージェントです。丁寧な日本語で話してください。"
VOICE_SPEED = 1.0

PRODUCTS_LIST = [
    "タブレット A68 Air", 
    "スマートウォッチ B27 Max", 
    "スマートフォン C82 Lite", 
    "スマートスピーカー D47 Air",
    "スマートフォン E51 Mini",
    "スマートスピーカー F29 Pro",
    "スマートフォン G81 Standard",
    "ワイヤレスイヤホン H61 Air",
    "ワイヤレスイヤホン I79 Pro",
    "ゲーム機 J87 Max"
]

JA_RECOMMENDED_PROMPT_PREFIX = """
#システムコンテキスト\n
あなたは、エージェントの協調と実行を簡単にするために設計されたマルチエージェントシステム「Agents SDK」の一部です。
Agentsは主に2つの抽象概念、**Agent**と**Handoffs**を使用します。エージェントは指示とツールを含み、適切なタイミングで会話を他のエージェントに引き継ぐことができます。
ハンドオフは通常 transfer_to_<agent_name> という名前のハンドオフ関数を呼び出すことで実現されます。エージェント間の引き継ぎはバックグラウンドでシームレスに処理されます。
ユーザーとの会話の中で、これらの引き継ぎについて言及したり、注意を引いたりしないでください。\n"""

# CONTEXT
class CallCenterAgentContext(BaseModel):
    customer_name: str | None = None
    question_type: str | None = None

```

```
# my_workflow.py

from __future__ import annotations

import os
import uuid
from collections.abc import AsyncIterator
from typing import Callable

from agents import (Agent, GuardrailFunctionOutput,
                    InputGuardrailTripwireTriggered, RunContextWrapper, Runner,
                    TResponseInputItem, function_tool, input_guardrail, trace)
from agents.mcp import MCPServerStdio
from agents.voice import VoiceWorkflowBase, VoiceWorkflowHelper
from config import JA_RECOMMENDED_PROMPT_PREFIX, MODEL, CallCenterAgentContext
from pydantic import BaseModel, Field

# TOOLS

@function_tool
async def update_customer_info(
    context: RunContextWrapper[CallCenterAgentContext], customer_name: str, question_type: str
) -> None:
    """
    Update the customer information.

    Args:
        customer_name: The name of the customer.
        question_type: The type of question being asked.
    """
    # Update the context based on the customer's input
    context.context.customer_name = customer_name
    context.context.question_type = question_type

# Guardrails

class AbnormalOutput(BaseModel):
    reasoning: str | None = Field(
        default=None, description="異常な質問かどうかの理由"
    )
    is_abnormal: bool = Field(default=False, description="異常な質問かどうか")

guardrail_agent = Agent(
    name="Guardrail check",
    instructions=(
        "カスタマーがコールセンターにしないような質問をしているかどうかを確認してください。"
        "たとエバ、「あなたの好きな色は何ですか？」や「あなたの趣味は何ですか？」などの質問は、コールセンターにするべきではありません。"
        "他にも「210たす4は？」といった計算問題や、「今日の経済ニュースは？」といった一般的な雑談もコールセンターにするべきではありません。"
        "このような質問を見つけたら、is_abnormalをTrueにしてください。"
    ),
    output_type=AbnormalOutput,
    model=MODEL,
)

@input_guardrail
async def abnormal_guardrail(
    context: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    """This is an input guardrail function, which happens to call an agent to check if the input
    is a abnormal question.
    """
    result = await Runner.run(guardrail_agent, input, context=context.context)
    final_output = result.final_output_as(AbnormalOutput)

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.is_abnormal,
    )

# Voice Call Center Workflow
class VoiceCallCenterWorkflow(VoiceWorkflowBase):
    def __init__(self, on_start: Callable[[str], None], tts_output: Callable[[str], None], on_agent_change: Callable[[str], None] = None, on_context_change: Callable[[CallCenterAgentContext], None] = None):
        """
        Args:
            on_start: A callback that is called when the workflow starts. The transcription
                is passed in as an argument.
            tts_output: A callback that is called when the TTS output is generated.
            on_agent_change: A callback that is called when the agent changes.
            on_context_change: A callback that is called when the context changes.
        """
        self._input_history: list[TResponseInputItem] = []
        self._context = CallCenterAgentContext()
        self._conversation_id = uuid.uuid4().hex[:16]
        self._on_start = on_start
        self._tts_output = tts_output
        self._on_agent_change = on_agent_change
        self._on_context_change = on_context_change
        self._current_agent = None
        self._agents_initialized = False

    async def _initialize_agents(self):
        """MCPサーバーを初期化してエージェントを設定"""
        if self._agents_initialized:
            return

        try:
            # MCPサーバーの初期化
            self.file_mcp_server = MCPServerStdio(
                name="Filesystem Server, via npx",
                params={
                    "command": "npx",
                    "args": [
                        "-y", 
                        "@modelcontextprotocol/server-filesystem", 
                        "path/to/products"
                    ]
                }
            )
            
            self.slack_mcp_server = MCPServerStdio(
                name="SSE Slack API Server",
                params={
                    "command": "npx",
                    "args": [
                        "-y", 
                        "@modelcontextprotocol/server-slack"
                    ],
                    "env": {
                        "SLACK_BOT_TOKEN": os.environ.get("SLACK_BOT_TOKEN"),
                        "SLACK_TEAM_ID": os.environ.get("SLACK_TEAM_ID"),
                        "SLACK_CHANNEL_IDS": os.environ.get("SLACK_CHANNEL_ID"),
                    }
                }
            )

            # MCPサーバーを開始
            await self.file_mcp_server.__aenter__()
            await self.slack_mcp_server.__aenter__()

            # エージェントの初期化
            self.error_trouble_agent = Agent[CallCenterAgentContext](
                name="エラー・トラブル・クレーム対応エージェント",
                handoff_description="エラー・トラブル・クレーム対応エージェントは、商品のエラーやトラブル、クレームに関する質問に対応できます。",
                instructions=f"""{JA_RECOMMENDED_PROMPT_PREFIX}
                あなたはエラー・トラブル・クレーム対応エージェントです。もし顧客と話している場合、あなたはおそらくトリアージエージェントから仕事を委譲されました。
                コールセンターマニュアルと、以下のルーチンに従って顧客の質問に対応してください。
                # ルーチン
                1. 顧客がどの商品の、どのようなエラーやトラブルについて質問しているかを確認します。クレームであれば、どのようなクレームかを確認し、マニュアルに従って対応してください。
                2. 特定の商品に関するものである場合、file_mcp_serverで提供されているディレクトリのファイルの中に、一致するテキストファイルがあるかどうかを確認します。
                3. ある場合、そのテキストファイルの中から、顧客の質問に答えられる情報を抽出し、回答してください。質問の内容が答えれらない場合は、「申し訳ありませんが、それついてはお答えできません。」と伝えます。
                4. サポートセンターの電話番号やメールアドレスが書かれている場合は、顧客にその情報を伝え、Slackのチャンネルにその内容を送信してください。
                5. ない場合、「申し訳ありませんが、そのエラーやトラブルについてはお答えできません。」と伝えます。
                もし顧客がルーチンに関連しない質問をした場合、や「もう大丈夫です」という内容があった場合は、トリアージエージェントに引き継ぎます。
                """,
                mcp_servers=[self.file_mcp_server, self.slack_mcp_server],
            )

            self.how_to_agent = Agent[CallCenterAgentContext](
                name="商品取り扱いエージェント",
                handoff_description="商品取り扱いエージェントは、商品に関する質問に答えることができます。",
                instructions=f"""{JA_RECOMMENDED_PROMPT_PREFIX}
                あなたは商品取り扱いエージェントです。もし顧客と話している場合、あなたはおそらくトリアージエージェントから仕事を委譲されました。
                顧客をサポートするために、以下のルーチンを使用してください。
                # ルーチン
                1. 顧客がどのような商品について質問しているかを確認します。
                2. file_mcp_serverで提供されているディレクトリのファイルの中に、一致するテキストファイルがあるかどうかを確認します。
                3. ある場合、そのテキストファイルの中から、顧客の質問に答えられる情報を抽出し、回答してください。質問の内容が答えれらない場合は、「申し訳ありませんが、それついてはお答えできません。」と伝えます。
                4. ない場合、「申し訳ありませんが、その商品は取り扱っておりません。」と伝えます。
                もし顧客がルーチンに関連しない質問をした場合、や「もう大丈夫です」という内容があった場合は、トリアージエージェントに引き継ぎます。
                """,
                mcp_servers=[self.file_mcp_server],
            )

            self.order_agent = Agent[CallCenterAgentContext](
                name="商品注文・購入対応エージェント",
                handoff_description="商品注文・購入に関する質問に答えるエージェントです。",
                instructions=f"""{JA_RECOMMENDED_PROMPT_PREFIX}
                あなたは商品注文・購入対応エージェントです。もし顧客と話している場合、あなたはおそらくトリアージエージェントから仕事を委譲されました。
                顧客をサポートするために、以下のルーチンを使用してください。
                # ルーチン
                1. 顧客がどのような商品を購入したいかを確認します。
                2. file_mcp_serverで提供されているディレクトリのファイルの中に、一致する、もしくは類似するテキストファイルがあるかどうかを確認します。たとえば、「スマホ」のようにスマートフォンの略称を使っている場合や、商品名の一部が異なる場合などです。
                3. ある場合、一度顧客に確認のため「<商品>ですね。注文してもよろしいですか？」と尋ねます。同意を得たら、slack_file_mcp_serverで#注文管理に「<商品名>を注文しました。」と送信してください。拒否されたら、トリアージエージェントに引き継ぎます。
                4. ない場合、「申し訳ありませんが、その商品は取り扱っておりません。」と伝えます。少しだけでも似ている名前の商品がある場合は、「<似ている商品名>はありますが、<商品名>はありません。」と伝えます。
                もし顧客がルーチンに関連しない質問をした場合や、「もう大丈夫です」「わかりました」という内容があった場合は、トリアージエージェントに引き継ぎます。
                """,
                mcp_servers=[self.file_mcp_server, self.slack_mcp_server],
            )

            self.triage_agent = Agent[CallCenterAgentContext](
                name="トリアージエージェント",
                instructions=(
                    f"{JA_RECOMMENDED_PROMPT_PREFIX} "
                    "あなたは優秀なトリアージエージェントです。 あなたは、顧客のリクエストを適切なエージェントに委任することができます。\n"
                    "顧客の質問がコールセンターにしないような質問をしているかもしれない場合は、ガードレールエージェントを使用してください。\n"
                    "顧客の名前より先に質問が来た場合、質問を記憶しつつ、名前を聞き、update_customer_infoを呼び出してください。\n"
                    "顧客の質問は、以下の3つのカテゴリに分けられます。\n"
                    "1. 商品の取り扱いに関する質問\n"
                    "2. 商品の注文・購入に関する質問\n"
                    "3. エラー・トラブル・サポートに関する質問\n"
                    "適切なエージェントに引き継いでください。"
                ),
                handoffs=[
                    self.how_to_agent,
                    self.order_agent,
                    self.error_trouble_agent,
                ],
                input_guardrails=[abnormal_guardrail],
                tools=[update_customer_info],
            )

            # 再びトリアージエージェントに戻るためのハンドオフ
            self.order_agent.handoffs.append(self.triage_agent)
            self.how_to_agent.handoffs.append(self.triage_agent)
            self.error_trouble_agent.handoffs.append(self.triage_agent)
            
            self._current_agent = self.triage_agent
            self._agents_initialized = True

        except Exception as e:
            print(f"エージェント初期化エラー: {e}")

    async def run(self, transcription: str) -> AsyncIterator[str]:
        self._on_start(transcription)

        # エージェントの初期化(基本的には一度だけ)
        await self._initialize_agents()

        # Add the transcription to the input history
        self._input_history.append(
            {
                "role": "user",
                "content": transcription,
            }
        )

        try:
            with trace("Customer service", group_id=self._conversation_id):
                # Run the agent
                current_context_customer = self._context.customer_name
                current_context_question_type = self._context.question_type
                result = Runner.run_streamed(self._current_agent, self._input_history, context=self._context)
                full_response = ""
                async for chunk in VoiceWorkflowHelper.stream_text_from(result):
                    full_response += chunk
                    yield chunk
                
                self._tts_output(full_response)
                if self._context.customer_name != current_context_customer or self._context.question_type != current_context_question_type:
                    if self._on_context_change:
                        self._on_context_change(self._context.customer_name, self._context.question_type)
                # Update the input history and current agent
                self._input_history = result.to_input_list()
                if self._current_agent != result.last_agent:
                    self._current_agent = result.last_agent
                    if self._on_agent_change:
                        self._on_agent_change(self._current_agent.name)

        except InputGuardrailTripwireTriggered as e:
            message = "すみません。この質問にはお答えできません。"
            self._tts_output(message)
            # ガードレール作動の通知
            if self._on_agent_change:
                self._on_agent_change("ガードレール作動")

            self._input_history.append(
                {
                    "role": "assistant",
                    "content": message,
                }
            )
            self._current_agent = self.triage_agent
            if self._on_agent_change:
                self._on_agent_change(self._current_agent.name)

            yield message
            
        except Exception as e:
            error_message = f"申し訳ありません。システムエラーが発生しました: {str(e)}"
            self._tts_output(error_message)
            yield error_message

    async def cleanup(self):
        """リソースのクリーンアップ"""
        try:
            if hasattr(self, 'file_mcp_server'):
                await self.file_mcp_server.__aexit__(None, None, None)
            if hasattr(self, 'slack_mcp_server'):
                await self.slack_mcp_server.__aexit__(None, None, None)
        except Exception as e:
            print(f"クリーンアップエラー: {e}")

```

```
# main.py

from __future__ import annotations

import asyncio
import shutil

import sounddevice as sd
from agents.voice import (StreamedAudioInput, StreamedAudioResult,
                          STTModelSettings, TTSModelSettings, VoicePipeline,
                          VoicePipelineConfig)
from config import (CHANNELS, FORMAT, SAMPLE_RATE, VOICE, VOICE_INSTRUCTION,
                    VOICE_SPEED)
from dotenv import load_dotenv
from my_workflow import VoiceCallCenterWorkflow
from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, RichLog, Static
from typing_extensions import override

load_dotenv()

# UI Components

class Header(Static):
    """A header widget."""

    session_id = reactive("")
    current_agent = reactive("トリアージエージェント")

    @override
    def render(self) -> str:
        return f"音声コールセンター | 現在のエージェント: {self.current_agent}"

class AudioStatusIndicator(Static):
    """A widget that shows the current audio recording status."""

    is_recording = reactive(False)

    @override
    def render(self) -> str:
        status = (
            "🔴 録音中... (Kキーで停止)"
            if self.is_recording
            else "⚪ Kキーで録音開始 (Qキーで終了)"
        )
        return status

# Main Application

class VoiceCallCenterApp(App[None]):
    CSS = """
        Screen {
            background: #1a1b26;  /* Dark blue-grey background */
        }

        Container {
            border: double rgb(91, 164, 91);
        }

        Horizontal {
            width: 100%;
        }

        #input-container {
            height: 5;  /* Explicit height for input container */
            margin: 1 1;
            padding: 1 2;
        }

        Input {
            width: 80%;
            height: 3;  /* Explicit height for input */
        }

        Button {
            width: 20%;
            height: 3;  /* Explicit height for button */
        }

        #bottom-pane {
            width: 100%;
            height: 82%;  /* Reduced to make room for session display */
            border: round rgb(205, 133, 63);
            content-align: center middle;
        }

        #status-indicator {
            height: 3;
            content-align: center middle;
            background: #2a2b36;
            border: solid rgb(91, 164, 91);
            margin: 1 1;
        }

        #session-display {
            height: 3;
            content-align: center middle;
            background: #2a2b36;
            border: solid rgb(91, 164, 91);
            margin: 1 1;
        }

        Static {
            color: white;
        }
    """

    should_send_audio: asyncio.Event
    audio_player: sd.OutputStream
    last_audio_item_id: str | None
    connected: asyncio.Event

    def __init__(self) -> None:
        super().__init__()
        self.last_audio_item_id = None
        self.should_send_audio = asyncio.Event()
        self.connected = asyncio.Event()
        self.workflow = VoiceCallCenterWorkflow(
            on_start=self._on_transcription,
            tts_output=self._tts_output,
            on_agent_change=self._on_agent_change,
            on_context_change=self._on_context_change,
        )
        self.voice_config = VoicePipelineConfig(
            tts_settings=TTSModelSettings(
                speed=VOICE_SPEED,
                instructions=VOICE_INSTRUCTION,
            ),
            stt_settings=STTModelSettings(
                turn_detection={
                    "type": "server_vad",
                    "threshold": 0.5,
                    "prefix_padding_ms": 300,
                    "silence_duration_ms": 1000,
                }
            ),

        )

        self.pipeline = VoicePipeline(workflow=self.workflow, config=self.voice_config)
        self._audio_input = StreamedAudioInput()
        self.audio_player = sd.OutputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=FORMAT,
        )

    def _on_transcription(self, transcription: str) -> None:
        try:
            self.query_one("#bottom-pane", RichLog).write(
                f"あなた: {transcription}"
            )
        except Exception:
            pass

    def _tts_output(self, text: str) -> None:
        try:
            self.query_one("#bottom-pane", RichLog).write(f"エージェント応答: {text}")
        except Exception:
            pass

    def _on_agent_change(self, agent_name: str) -> None:
        try:
            header = self.query_one("#session-display", Header)
            header.current_agent = agent_name
            self.query_one("#bottom-pane", RichLog).write(f"🔄 エージェント切り替え: {agent_name}")
        except Exception:
            pass
    
    def _on_context_change(self, customer_name: str, question_type: str) -> None:
        try:
            self.query_one("#bottom-pane", RichLog).write(
                f"📝 コンテキスト変更: 顧客名={customer_name}, 質問タイプ={question_type}"
            )
        except Exception:
            pass

    @override
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with Container():
            yield Header(id="session-display")
            yield AudioStatusIndicator(id="status-indicator")
            yield RichLog(id="bottom-pane", wrap=True, highlight=True, markup=True)

    async def on_mount(self) -> None:
        self.run_worker(self.start_voice_pipeline())
        self.run_worker(self.send_mic_audio())

    async def start_voice_pipeline(self) -> None:
        try:
            self.audio_player.start()
            self.result: StreamedAudioResult = await self.pipeline.run(
                self._audio_input
            )
            async for event in self.result.stream():
                bottom_pane = self.query_one("#bottom-pane", RichLog)
                if event.type == "voice_stream_event_audio":
                    self.audio_player.write(event.data)  # Play the audio
                elif event.type == "voice_stream_event_lifecycle":
                    bottom_pane.write(f"ライフサイクルイベント: {event.event}")
        except Exception as e:
            bottom_pane = self.query_one("#bottom-pane", RichLog)
            bottom_pane.write(f"エラー: {e}")
        finally:
            self.audio_player.close()
            # クリーンアップ
            await self.workflow.cleanup()

    async def send_mic_audio(self) -> None:
        device_info = sd.query_devices()
        print(device_info)

        read_size = int(SAMPLE_RATE * 0.02)

        stream = sd.InputStream(
            channels=CHANNELS,
            samplerate=SAMPLE_RATE,
            dtype="int16",
        )
        stream.start()

        status_indicator = self.query_one(AudioStatusIndicator)

        try:
            while True:
                if stream.read_available < read_size:
                    await asyncio.sleep(0)
                    continue

                await self.should_send_audio.wait()
                status_indicator.is_recording = True

                data, _ = stream.read(read_size)

                await self._audio_input.add_audio(data)
                await asyncio.sleep(0)
        except KeyboardInterrupt:
            pass
        finally:
            stream.stop()
            stream.close()

    async def on_key(self, event: events.Key) -> None:
        """Handle key press events."""
        if event.key == "enter":
            self.query_one(Button).press()
            return

        if event.key == "q":
            await self.workflow.cleanup() # クリーンアップしてから終了
            self.exit()
            return

        if event.key == "k":
            status_indicator = self.query_one(AudioStatusIndicator)
            if status_indicator.is_recording:
                self.should_send_audio.clear()
                status_indicator.is_recording = False
            else:
                self.should_send_audio.set()
                status_indicator.is_recording = True

if __name__ == "__main__":
    if not shutil.which("npx"):
        raise RuntimeError("npx is not installed. Please install it with `npm install -g npx`.")
    app = VoiceCallCenterApp()
    app.run()

```

main.pyのVoicePipelineに、my\_workflow.pyで作成したVoiceCallWorkflowを挟み込んでいます。また、フロントエンドの部分はPythonでターミナル上に作れるTextualというフレームワークを用いています。

それでは、このコードを実際に動かしてみたデモの様子を3つみていきましょう。
1つ目の動画は製品の取り扱いの質問を行なっている例です。返答が遅くて気掛かりですが、しっかりとMCPが機能しているようですね。

2つ目の動画は製品の注文を行なっている例です。MCPで製品情報を整理しつつ、商品の注文メール送信までを行えています。

3つ目はガードレールをあえて起動させようとしている例です...が失敗していますね。どうしてなのでしょうか？

この原因は、ストリーミング生成と入力ガードレールの相性が良くないためと考えられます。以下の図を用いて説明します。入力ガードレールは音声認識が全て終了してから行うのに対し、音声合成の部分では、音声認識が徐々になされていく中でエージェントのLLMが回答生成し、その回答をチャンクごとに出力しようとします。すると、入力ガードレールが異常検知する前に出力が生成されてしまうため、先にLLMが好き勝手に回答する挙動をしてしまったわけなのです。

![ガードレールがストリーミング生成でうまく機能しないことを表した図](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090019.png)


ガードレールがストリーミング生成でうまく機能しないことを表した図

したがって、ストリーミング生成での音声マルチエージェントを構築する場合は、入力ガードレールエージェントは使用しない方がいいということがわかりました。対策として、そのままトリアージエージェントにプロンプトとしてガードレールを再現してしまう方法が考えられます。実際にトリアージエージェントからガードレールエージェントを取り外し、プロンプトを変更した後の、エージェントの概観図と、変更した部分のみのコードを掲載します。

![変更後の音声エージェントの概観図](https://cdn-ak.f.st-hatena.com/images/fotolife/i/insightedge/20250710/20250710090025.png)


変更後の音声対話型マルチエージェントの概観図

```
# my_workflow.pyのガードレール部分を消し、トリアージエージェントとの紐付けを削除し代わりにプロンプトを修正しました

self.triage_agent = Agent[CallCenterAgentContext](
                name="トリアージエージェント",
                instructions=(
                    f"{JA_RECOMMENDED_PROMPT_PREFIX} "
                    "あなたは優秀なトリアージエージェントです。 あなたは、顧客のリクエストを適切なエージェントに委任することができます。\n"
                    "顧客の質問がコールセンターにしないような質問をした場合は、「すみません。この質問には答えられません」と伝えてください。"
                    "コールセンターにしないような質問は、一般的な知識や雑談、計算問題などです。\n"
                    "たとえば、「あなたの好きな色は何ですか？」と言った質問や「210たす4は？」といった質問は、コールセンターにするべきではありません。\n"
                    "会社に関する質問でも、「この会社の設立年はいつですか？」といった質問は、コールセンターにするべきではありません。\n"
                    "顧客の質問に答えるために、顧客の名前と質問のタイプをupdate_customer_infoを呼び出して保存してください。\n"
                    "顧客の名前のみ分かった場合でも、update_customer_infoを呼び出し、質問はNoneとして保存してください。\n"
                    "顧客の名前より先に質問が来た場合、update_customer_infoを呼び出し、顧客の名前はNoneとして保存してください。さらに顧客の名前を聞き出してください。\n"
                    "質問タイプが話の途中から変わる場合も、update_customer_infoを呼び出して更新してください。\n"
                    "顧客の質問は、以下の4つのカテゴリに分けられます。\n"
                    "1. 商品の取り扱いに関する質問\n"
                    "2. 商品の注文・購入に関する質問\n"
                    "3. エラー・トラブル・クレームに関する質問\n"
                    "4. その他の回答不可能・専門知識が必要な質問\n"
                    "適切なエージェントに引き継いでください。\n"
                ),
                handoffs=[
                    self.how_to_agent,
                    self.order_agent,
                    self.error_trouble_agent,
                ],
                tools=[update_customer_info],
            )

```

以上の変更を加えた後のデモの様子を見てみましょう。

ガードレールエージェントなしでも、うまくガードレールの機能は再現できていますね！

残る課題としては、やはりレイテンシーが挙げられます。最初の回答までに10秒以上、2回目以降の回答までに体感6,7秒ほどの待ち時間があるので、使用感は正直良くないです。
しかし、Chained ArchitectureではなくSpeech-to-Speech Architectureに変更することで、そのレイテンシーは改善できる見込みがあります。
人間が行なっているコールセンターで実際にどれくらいの遅延であれば許容できるかを踏まえた上で、レイテンシーを減らす・もしくは感じさせないような作りを考え、実用化に向けてさまざまな意見を取り入れながら設計していく必要があると思いました。

### 2.4 今後の展望

前節では、Chained Architectureの音声対話型マルチエージェントの性能と課題をお伝えしました。この構造での音声エージェントが持つ課題を明確にできたのが今回の収穫だったかなと思います。前節でも述べたように、遅延を減らす対策として、構造をリアルタイム対話型モデルを基盤としたSpeech-to-Speech Architectureに変えることが考えられます。もし、機会があればこの構造に変えたとき、どれだけ遅延が改善されたかをご紹介できればと思います。

話が少し大きくなりますが、本章の最後に、AIエージェントのこれからの展望について少し話させてください。私自身、AIエージェントを今回のアルバイトで初めて作ってみたのですが、テキストベースのものに音声が付くだけで一気に「向こう側に相手がいる」ような感覚が強まるのを感じました。AIエージェントはこれから、より人間性を帯びてくるのではないかと私は考えています。具体的な例として、人間やキャラクターを模したアバターベースのAIエージェントや、ロボットベースのAIエージェントの応用が活発化する可能性があります。その後、カスタマイズによる会社独自のデジタルヒューマンが会社の新しいブランドを形成したり、ロボット同士が協力して仕事をサポートするような未来が訪れるかもしれません。それを楽しみにしつつ、いかにして人間とAIが協調していくかという議論を継続して行う必要があると考えます。

おわりに
----

今回のアルバイトのテーマでもありました、「音声エージェント関連サーベイ」で得た知見の一部を本記事でまとめさせていただきました。
本アルバイトを通して、初めて音声とエージェント両面の技術に触れることができ、どちらとも関心を高めることができました。
今後は、Speech-to-Speechモデルでのマルチエージェントの構築や、カスタムボイスを利用したアバターベースでの音声エージェントの可能性を探っていきたいと思います。
今回のアルバイトでお世話になりましたInsight Edgeの社員の方々、特にチューターとして日頃からアルバイトのサポートをしてくださいました須賀さんに、心から感謝を申し上げたいと思います。
ここまで読んでいただき、ありがとうございました！！

参考資料
----

* Google Cloud, "Agent2Agent プロトコル（A2A）を発表：エージェントの相互運用性の新時代", <https://cloud.google.com/blog/ja/products/ai-machine-learning/a2a-a-new-era-of-agent-interoperability>
* Agent2Agent (A2A) Protocol, Home, <https://a2aproject.github.io/A2A/latest/#why-a2a-matters>
* Google AI Developers, "音声生成(テキスト読み上げ)", <https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja>
* AWS, "Amazon Nova Documentation", <https://docs.aws.amazon.com/nova/>
* taku\_sid,「うさぎでもわかるAmazon Nova Sonic入門」, <https://zenn.dev/taku_sid/articles/20250413_nova_sonic>
* OpenAI, "Voice agents", <https://platform.openai.com/docs/guides/voice-agents?voice-agent-architecture=speech-to-speech>
* OpenAI Agents SDK, <https://openai.github.io/openai-agents-python/ja/>
* takemo101, 株式会社ソニックブーム,「Gemini API TTS（Text-to-Speech）で漫才音声を生成してみた」, <https://zenn.dev/sonicmoov/articles/bd862039bcba46>

[![リクルートサイト](https://insightedge.jp/wp-content/uploads/2024/09/bottombanner2_A.png)](https://recruit.insightedge.jp/)

[![リクルートサイト](https://insightedge.jp/wp-content/uploads/2024/09/bottombanner2_A.png)](https://recruit.insightedge.jp/)

[#LLM](https://d.hatena.ne.jp/keyword/LLM)

[#大規模言語モデル](https://d.hatena.ne.jp/keyword/%E5%A4%A7%E8%A6%8F%E6%A8%A1%E8%A8%80%E8%AA%9E%E3%83%A2%E3%83%87%E3%83%AB)

[#音声解析](https://d.hatena.ne.jp/keyword/%E9%9F%B3%E5%A3%B0%E8%A7%A3%E6%9E%90)

keiichisuga
[2025-07-10 09:00](https://techblog.insightedge.jp/entry/tech-blog-intern-1)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/techblog.insightedge.jp/entry/tech-blog-intern-1 "この記事をはてなブックマークに追加")

関連記事

* [![Amazon Bedrock Agentsで化粧品推薦AIを作ってみた！実際に使って月2500円節約できた話](https://cdn.image.st-hatena.com/image/square/859fc3841fc3b2ce486b61b227867e9863e82c05/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20250707%2F20250707123619.png "Amazon Bedrock Agentsで化粧品推薦AIを作ってみた！実際に使って月2500円節約できた話")](https://techblog.insightedge.jp/entry/cosme-recommend-agent)

  [2025-07-07](https://techblog.insightedge.jp/archive/2025/07/07)

  [Amazon Bedrock Agentsで化粧品推薦AIを作ってみた！実際に使って月2500円節約…](https://techblog.insightedge.jp/entry/cosme-recommend-agent)

  アジャイル開発チームの塚越です。2023年にInsight Edge(以下、…
* [![LibreChatとBedrock Knowledge Bases MCPでかんたん社内文書検索エージェント](https://cdn.image.st-hatena.com/image/square/5998f869dcc85bb78dc53901e23b6ba8a3ded584/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20250702%2F20250702080039.png "LibreChatとBedrock Knowledge Bases MCPでかんたん社内文書検索エージェント")](https://techblog.insightedge.jp/entry/librechat-mcp)

  [2025-07-02](https://techblog.insightedge.jp/archive/2025/07/02)

  [LibreChatとBedrock Knowledge Bases MCPでかんたん社内文書検索エー…](https://techblog.insightedge.jp/entry/librechat-mcp)

  こんにちは！アジャイル開発チームの筒井です！ 最近の生成AIツ…
* [![世界は新たな時代を迎えようとしている](https://cdn.image.st-hatena.com/image/square/8aaa77a22d94fb0c414fd0b3ae3e2fc4e219c628/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20250527%2F20250527100023.png "世界は新たな時代を迎えようとしている")](https://techblog.insightedge.jp/entry/ai-agent)

  [2025-05-27](https://techblog.insightedge.jp/archive/2025/05/27)

  [世界は新たな時代を迎えようとしている](https://techblog.insightedge.jp/entry/ai-agent)

  こんにちは。CINO(Chief Innovation Officer)の森です。 ここ最…
* [![LM Studio を使ってローカルでLLMを実行する方法](https://cdn.image.st-hatena.com/image/square/bbba8be3b80ee498facc25fd2536042499775aaa/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20250310%2F20250310093019.jpg "LM Studio を使ってローカルでLLMを実行する方法")](https://techblog.insightedge.jp/entry/local-llm)

  [2025-03-10](https://techblog.insightedge.jp/archive/2025/03/10)

  [LM Studio を使ってローカルでLLMを実行する方法](https://techblog.insightedge.jp/entry/local-llm)

  こんにちは、Insight Edgeでリードデータサイエンティストを務…
* [![Prompt flowを用いた自律型エージェントの作成](https://cdn.image.st-hatena.com/image/square/2d88c671b98aa5fe7b1931a8bde5c76423034ab0/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fi%2Finsightedge%2F20240415%2F20240415073027.png "Prompt flowを用いた自律型エージェントの作成")](https://techblog.insightedge.jp/entry/promptflow-agent)

  [2024-04-15](https://techblog.insightedge.jp/archive/2024/04/15)

  [Prompt flowを用いた自律型エージェントの作成](https://techblog.insightedge.jp/entry/promptflow-agent)

  こんにちは！Lead Engineerの筒井です。 このテックブログでも…