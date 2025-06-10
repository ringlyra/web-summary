<!-- metadata -->
- **title**: v0 APIのアーキテクチャ: Chat Completion API自作界隈
- **source**: https://blog.lai.so/v0-api/
- **author**: laiso
- **published**: 2025-06-07T10:15:05.000Z
- **fetched**: 2025-06-07T20:39:04Z
- **tags**: codex, v0-api, autofix, workers-ai, cli
- **image**: https://blog.lai.so/content/images/2025/03/my-github-icon-2024-2.png

## 要約
Vercelが提供する **v0 API** は、OpenAI互換のエンドポイントを備え、**Chat Completion API** を拡張して高品質なコード生成を実現するサービスです。記事では、v0 APIが**複合モデルアーキテクチャ**を採用し、前処理でRAGを行い、既存LLMでコード生成後、**AutoFix**で修正する仕組みを詳しく解説。さらに、自分で同様のAPIプロキシを構築する手順を紹介し、HonoとWorkersを使った実装例や、Cloudflare **Workers AI** を利用したモデル切り替え方法、ストリーミングレスポンスの変換など、実践的なノウハウがまとめられています。

## 本文 / Article
## はじめに

先日、Vercelがv0 APIという興味深いサービスを発表しました。[v0.dev](https://v0.dev/?ref=blog.lai.so)は、アプリのプロトタイピングからデプロイまでをWebブラウザ上のチャットで行えるサービスです。v0 APIは、この機能を外部から利用可能にする有料プラン向けのAPIサービスとして提供されています。

[v0 API

Access the model behind v0.](https://vercel.com/docs/v0/api?ref=blog.lai.so)

現在、CursorやClineなどのエディタでコード生成のバックエンドとしてv0 APIを利用することができます。くわえて、Vercel ProユーザーはAI SDKの[AI Playground](https://ai-sdk.dev/playground/vercel:v0-1.0-md?ref=blog.lai.so)からこの機能を試すこともできます。

## 利用方法

v0 APIは、OpenAIの**Chat Completions API**の仕様に準拠したエンドポイントを提供しています。そのため、既存のOpenAIモデル対応アプリケーションでは、ベースURLの設定を変更するだけでv0 APIを利用することができます。

ユーザーにとっては、AIエディタに設定を追加するだけで、Next.jsアプリなどのモダンなWebアプリケーション開発において、コード生成の品質が大幅に向上するという利点があります。

Clineでの設定方法が以下のページにあります。 Base URL: `https://api.v0.dev/v1`とAPIキーを設定するだけで使えます。

[v0 in Cline

Use the v0 model inside Cline.](https://vercel.com/docs/v0/cline?ref=blog.lai.so)

## LLMをコード生成に使う時の課題

現在のフロンティアモデル（ClaudeやGemini）は知識カットオフにより2024年前半頃の技術スタックで学習が停止しており、2024年後半以降にリリースされたReact 19、Next.js 15、Tailwind CSS 4.0、shadcn/ui、AI SDKなどの最新アップデートに対応していません。このため、新規にアプリケーションのコードを生成する際、最新のフレームワークバージョンと組み合わせると動作に問題が発生することがあります。

[React Router v7でコードを書いてくれSonnet

Claude 3.7 Sonnetに代表される現在の主力なコーディングモデルやソフトウェア開発タスクの自動化に利用されるLLMは、知識のカットオフにより2024年後半頃までにネット上に存在する情報をもとにしたソースコードしか書くことができない。例えばAnthropicのAPIを直接利用して確認すると、「React Routerの最新バージョンはv6です」と返答が来る。しかし、最新版はv7だ。v7.0.0はちょうどこの時期にリリースされたため境界にあり、つまりv7の実践的な知識はない。これに限らず、LLMの世界ではNext.jsはv14、Flaskはv2、Railsはv7と一世代遅れたバージョンを認識していることになっている。 これらのアップデートによって入った変更は、既存のソースコードに記述していればLLMが空気を読んで従う。加えて、ユーザーがカスタムルールとしてエディタ側で追加情報を設定したり、外部ドキュメントをその場で参照して補正することもできる。エージェントのfetchツールでWeb検索できる範囲の情報は適切に処理されるが、完全ではないので、我々は都度最新ドキュメントを読んで差](https://blog.lai.so/sonnet-cutoff/)

また、v0のようなモダンなWebアプリのコード生成というユースケースに、LLMは特化して設計されているわけではありません。LLMの性能評価で使用されるベンチマークは、Pythonのデータサイエンスやアルゴリズム問題が中心であり、最も活躍が期待される場面はチャットアシスタントでのコードサンプル提供です。

自然言語による指示でアプリのプロトタイピングを行うv0では、生成されたコードの品質がすべてです。しかし、従来のLLMはエージェントのようにエラー修正を自律的に行うことができません。そのため、v0ユーザーはエラーを発見した際に、手動で修正指示を入力する必要がありました。

このような課題を解決するため、Vercelは複合モデルアーキテクチャを開発したというのが、以下のブログ記事の内容です。

[Introducing the v0 composite model family - Vercel

Learn how v0’s composite AI models combine RAG, frontier LLMs, and AutoFix to build accurate, up-to-date web app code with fewer errors and faster output.](https://vercel.com/blog/v0-composite-model-family?ref=blog.lai.so)

## v0 APIのアーキテクチャ

Vercelはv0 APIを「v0モデル」という新たなLLMのような名称でマーケティングしています。"v0-1.0-md"や"v0-1.5-md"のようにバージョンごとに専用のモデル名が付けられていますが、実際にはv0モデルは独立したLLMではありません。

v0モデルは内部でClaude（Anthropic Sonnet 3.7やSonnet 4）などの既存のLLMのAPIを呼び出し、それらの結果を活用する仕組みになっています。Vercelはこのアプローチを**複合モデルアーキテクチャ（Composite Model Architecture）**と呼んでいます。

この複合モデルアーキテクチャでは、LLMの呼び出しプロセスが下図のようにいくつかの段階に分けられています。

![](https://blog.lai.so/content/images/2025/06/image-10.png)

[https://vercel.com/blog/v0-composite-model-family](https://vercel.com/blog/v0-composite-model-family?ref=blog.lai.so)

### 前処理（Pre-processing）

まず前処理として、Vercelはv0ユーザーが送信したクエリを受け取り、自社データセットから最適なドキュメントを検索してLLMの入力コンテキストに追加します。Vercel内部のDBなどからも情報を取得しているようです。これをRAG（Retrieval-Augmented Generation）の文脈で説明していました。

### メインのコード生成

次にメインのコード生成では、ベースLLMとしてClaude Sonnet（v0-1.0-mdではSonnet 3.7、v0-1.5-mdではSonnet 4）を使用していることが言及されています。ここが普段私たちが意識しているコード生成のレイヤーです。

### 後処理（AutoFix）

後処理として、LLMが生成したコードをレスポンスとして返す前に自動修正を行います。Vercelはこれを**AutoFix**と呼んでおり、過去にはGemini Flash 2.0を使用していましたが、現在は独自にファインチューニングした言語モデル「vercel-autofixer-01」をFireworks AI上でホストして使用しています（基盤モデルは非公表）。

このAutoFixモデルは、コード生成中にリアルタイムでエラーや不整合を修正します。AIエディタ側で行われていたようなフィードバックループがサーバー側に来ているということですね。

### アーキテクチャの特徴

このように、v0 APIは既存のLLMを単純にラップするのではなく、前処理・後処理や複数のモデルを組み合わせることで、最新のフレームワークやツールに対応したコード生成を実現しています。

OpenAI互換エンドポイントとして提供されているため、既存のAIエディタやツールへの統合も容易です。MCPサーバーでコンテキストを追加する方法と比較すると、メッセージデータに直接介入している点に特徴があります。

AIエディタが用意したカスタマイズ設定を活用してサービスを提供するという設計思想もユニークだと思いました。

## Chat Completions API を自作しよう

このように、v0 APIはLLMの応答に前処理・後処理を組み合わせることで、コード生成の品質を大幅に改善する仕組みを採用しています。

LLMをコード生成に使用する際の課題は、私たちが日常的にAIエディタでコーディングを行う場面でも同様に発生します。

そこで、v0 APIの仕組みを参考に、私たちも独自のChat Completions APIプロキシを構築し、ClineやCursorなどのAIエディタから呼び出せるようにしてみましょう。

### API設計と基本実装

自作APIは、クライアント（VSCodeやCursor）とLLMサービスの間に立つプロキシとして機能します。Chat Completions API互換のREST APIとして実装し、POST `/chat/completions` エンドポイントでリクエストを受け取り、ストリーミング対応でレスポンスを返します。デバッグ用に非ストリーミングオプションを用意しておきますが、現在のAIエディタからの呼び出しはほぼストリームです。

実装は段階的に進めます。まずモックレスポンスで動作確認を行い、次にOpenAI SDKを使って真の（？）LLM呼び出しに置き換えます。フレームワークにはHonoと[create-cloudflare](https://www.npmjs.com/package/create-cloudflare?ref=blog.lai.so)を採用し、ボイラープレートを最小限に抑えた軽量な実装を目指します。詳細なコードサンプルは以下のGistリンクを参照してください。

[Custom AI editor tool override API with OpenAI Chat Completion compatibility

Custom AI editor tool override API with OpenAI Chat Completion compatibility - README.md](https://gist.github.com/laiso/2ddc2076583d30c9f20c4e89f7b9aa9a?ref=blog.lai.so)

モックレスポンス版（mock.ts）は単に"Hello, I'm Mock Streaming!"という返事のみの固定のJSONデータをストリーミングで返します。HonoのAPIによって以下のように簡単に書けますね。

![](https://blog.lai.so/content/images/2025/06/image-2.png)

これをwrangler devで立ち上げたローカルサーバーのエンドポイント[http://localhost:8787/mock/v1](http://localhost:8787/mock/v1?ref=blog.lai.so) でアクセスできるようClineに設定します。

![](https://blog.lai.so/content/images/2025/06/Screenshot-2025-06-07-at-14.49.33.png)

モックレスポンス版をClineに組み込むと、APIは常に固定のメッセージを返します。ローカルサーバーによりClineの応答速度が格段に向上するので、通常の利用時はLLMのAPI呼び出しのレイテンシがボトルネックだったことを実感できました。

そしてClineはモックAPIの単調な応答に対して「インテリジェンスが足りないためClaude Sonnetへの置き換えを検討してください」と促してきます。このメッセージも初めて見ました。

次にOpenAI版（openai.ts）です。差分は単に入力→出力をそのままOpenAIのSDKに渡すだけで、完全なプロキシサーバーになります。

![](https://blog.lai.so/content/images/2025/06/image-3.png)

これを先ほどのモックAPIのエンドポイントと入れ替え [http://localhost:8787/openai/v1](http://localhost:8787/openai/v1?ref=blog.lai.so) にモデルIDをgpt-4o などに指定するといつものClineのように動作します。ただここまでだとリクエストをそのまま流して何が嬉しいのか？　と思いますよね。次の段階ではv0 APIのように前処理工程を加えてゆきます。

### LLMのコンテキストを動的に注入する

OpenAI APIでコード生成するの前処理として、v0 APIのように私たちのAPIでも、フレームワークのベストプラクティスをメッセージオブジェクトとして追加してみましょう。たとえば以下のようにファイルに保存したプロンプトを追加で上乗せします。Clineから見ると自身の知らぬところで勝手に設定コンテキストが追加されていることになります。

![](https://blog.lai.so/content/images/2025/06/image-4.png)

### レスポンスのチャンクを書き換える

生成されたコードをユーザーに返却する前に、ストリーミングレスポンスのチャンクを書き換えることで、AIエディタの挙動を動的に制御できます。

たとえば、レスポンスのメッセージ配列の中にあるファイル編集ツールの呼び出しを検知します。その内部のスニペットを探索し、古いメソッドを使っていたら新しいメソッドに置換するというシンプルなパイプラインが構築できます。

これは以下のようにストリームデータを逐次受信しつつ、必要な変換処理を挟みながらクライアントに転送していくことで実現できます。

![](https://blog.lai.so/content/images/2025/06/image-5.png)![](https://blog.lai.so/content/images/2025/06/image-6.png)

app.post('/v1/chat/completions'

### モデルをWorkers AIへの置き換える

v0 APIの複合モデルアーキテクチャは、内部で呼び出すLLMを動的に切り替える仕組みを備えています。これと同様の機能を実現するため、先ほど実装したOpenAI APIの呼び出し部分をCloudflareの[Workers AI](https://www.cloudflare.com/developer-platform/products/workers-ai/?ref=blog.lai.so)に置き換えてみます。

Workers AIはCloudflareが提供するサーバーレスでAIモデルを実行できるサービスで、Cloudflare Workersから簡単に呼び出せます。LlamaやMistralなどの最新のオープンなモデルにできます。ローカルPCでパラメータサイズの大きいモデルを動作させるより遥かに高速で、無料枠で試せますので多様なモデルを切り替えて呼び出したい本記事のケースに最適です。

ただし、Workers AIはwrangler devで立ち上げたローカルサーバーにも対応していますが、実際にはCloudflare内のサービスをリモートで呼び出しているため、利用枠（Neurons）を消費する点に注意が必要です。

[Pricing

Workers AI is included in both the Free and Paid Workers plans and is priced at $0.011 per 1,000 Neurons.](https://developers.cloudflare.com/workers-ai/platform/pricing/?ref=blog.lai.so)

### モデル選択の考慮点

モデルの選択については、Workers AIで現在Function Calling（tools）に対応したモデルはいくつかあり、その中でも[`llama-4-scout-17b-16e-instruct`](https://developers.cloudflare.com/workers-ai/models/llama-4-scout-17b-16e-instruct/?ref=blog.lai.so)が最も忠実にツール呼び出しの応答がされることを確認しました。

他のモデルは正常なデータ構造やテキストの応答を返さないことが多く、動作検証に耐えられません。

`llama-4-scout-17b-16e-instruct`は十分な性能を備えていますが、残念ながらこのモデルは日本語での出力に対応していません。

各モデルの応答は[Playground](https://playground.ai.cloudflare.com/?ref=blog.lai.so)から試すことができます。日々新しいモデルが追加されているので、今後より動作に適したモデルが追加されるかもしれません。

![](https://blog.lai.so/content/images/2025/06/image-7.png)

2025年06月時点

## Workers AIへの実装

先程実装したOpenAIのAPI呼び出し部分をWorkers AI用に置き換えます。

Workers AIのレスポンスはOpenAIとは異なるため変換処理が必要であり、この変換パイプラインは「レスポンスのチャンクを書き換える」で説明したv0の後処理フローと同じ仕組みです。

![](https://blog.lai.so/content/images/2025/06/image-8.png)

workersai.ts

[streamWorkersAI2OpenAI](https://gist.github.com/laiso/2ddc2076583d30c9f20c4e89f7b9aa9a?ref=blog.lai.so#file-workersai-ts-L73) の工程はかなり骨が折れる作業でした。基本的にデータ構造の移し替えなのですが、Workers AIのレスポンス仕様→OpenAIのレスポンス仕様→Clineのクライアント仕様の階層を辿るのでデバッグを人間が真心を込めて行う必要がありました。筆者はHTTPクライアントツールなどを駆使して各リクエストの中身の値を観察してロジックを組みました。

![](https://blog.lai.so/content/images/2025/06/image-9.png)

ストリーミングのデバッグは重労働

エンドポイントを[http://localhost:8787/workersai/v1](http://localhost:8787/workersai/v1?ref=blog.lai.so) に差し替えClineのエージェントが無事に機能することを確認しました。

![](https://blog.lai.so/content/images/2025/06/Screenshot-2025-06-07-at-14.53.05.png)

## おわりに

本記事では、Chat Completions API互換の自作APIを設計・実装し、OpenAIやWorkers AIなど複数のLLMサービスに対応させる方法を解説しました。モック実装から始めて段階的に機能を拡張し、ストリーミングレスポンスやレスポンス変換、動的なコンテキスト注入などのポイントを紹介しました。

Clineでの動作に焦点を当てましたが、筆者は他のエディタでも動作確認ができています。

CursorではCloudflare Workersにデプロイしたオンラインのエンドポイントが必要になります。これはCursorの仕様で[Cursor社の内部インフラを経由する](https://docs.cursor.com/settings/api-keys?ref=blog.lai.so#will-my-api-key-be-stored-or-leave-my-device%3F)ためです。そのため、アクセスを制限するために、アクセスを制限するには自前のAPIキー認証の実装が必要になります。

また、GitHub Copilot Chatはv1.99以降で[Ollamaエンドポイント設定に対応](https://code.visualstudio.com/docs/copilot/language-models?ref=blog.lai.so)しており、Ollamaのモデル情報を返すエンドポイントの追加が必要ですがClineと同じく動作します。こちらはローカルホストのAPIを想定した機能のためAPIキー設定は不要です。

![](https://blog.lai.so/content/images/2025/06/Screenshot-2025-06-07-at-15.01.45.png)

Copilot Chatでの動作例

これらの実装も以下のソースコードに含まれています。

[Custom AI editor tool override API with OpenAI Chat Completion compatibility

Custom AI editor tool override API with OpenAI Chat Completion compatibility - README.md](https://gist.github.com/laiso/2ddc2076583d30c9f20c4e89f7b9aa9a?ref=blog.lai.so)

v0 APIの複合モデルアーキテクチャはv0と似たシステムを構築したいケースでの応用が考えられます。たとえばデザインシステムや社内ドキュメントを活用したコードプロトタイプ生成があります。これはMCPサーバーの活用方法として開発の現場で検証されているような領域で、業界の関心も高いです。

本記事が、独自のChat Completions APIプロキシや複合モデルアーキテクチャの設計・実装に取り組む際の参考になれば幸いです。
