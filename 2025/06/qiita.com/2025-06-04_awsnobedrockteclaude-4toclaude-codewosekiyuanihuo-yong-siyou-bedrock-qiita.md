<!-- metadata -->
- **title**: AWSのBedrockでClaude 4とClaude Codeをセキュアに活用しよう！ #bedrock - Qiita
- **source**: https://qiita.com/moritalous/items/9da3e2538c9507890e40
- **author**: moritalous
- **published**: 2025-06-04T02:37:57Z
- **fetched**: 2025-06-04T03:04:30Z
- **tags**: codex, bedrock, claude4, claudecode, aws
- **image**: https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.0.0%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkY0MTU3NCUyRjRlZjYzODMyOTNiYTllNmNlZmJiOThmYzhjNjViZDRjZjZjYjM4YTIlMkZ4X2xhcmdlLnBuZyUzRjE1OTU2NDI5ODU_aXhsaWI9cmItNC4wLjAmYXI9MSUzQTEmZml0PWNyb3AmbWFzaz1lbGxpcHNlJmZtPXBuZzMyJnM9ZTFlNGUwZGIzYzk1NWIxYjQxY2VjZjJkNGFmZDI5ZWM%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3Dde1fbbe710093376a1e4ee9e4ec36763?ixlib=rb-4.0.0&w=1200&fm=jpg&mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjAuMCZ3PTk2MCZoPTMyNCZ0eHQ9QVdTJUUzJTgxJUFFQmVkcm9jayVFMyU4MSVBN0NsYXVkZSUyMDQlRTMlODElQThDbGF1ZGUlMjBDb2RlJUUzJTgyJTkyJUUzJTgyJUJCJUUzJTgyJUFEJUUzJTgzJUE1JUUzJTgyJUEyJUUzJTgxJUFCJUU2JUI0JUJCJUU3JTk0JUE4JUUzJTgxJTk3JUUzJTgyJTg4JUUzJTgxJTg2JUVGJUJDJTgxJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9MDdhYTY1NTRiNDUxNGVkYmI2NTUxY2QyMmMxNmQ2OTU&mark-x=120&mark-y=112&blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjAuMCZ3PTgzOCZoPTU4JnR4dD0lNDBtb3JpdGFsb3VzJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9NTE5MDJlZTJlOTExNTEzZmVhMTBjNzY4YjZmNjRkM2I&blend-x=242&blend-y=480&blend-w=838&blend-h=46&blend-fit=crop&blend-crop=left%2Cbottom&blend-mode=normal&s=339106f4048fb0135986594e1af31ce8

## 要約
**AWSのBedrock**で**Claude 4**と**Claude Code**を安全に導入する方法を解説。利点と制約、利用時のポイントを端的にまとめている。

## 本文 / Article
[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F7cf985a8-7134-408b-a197-cf566a0d133d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c674351ddc39dc70f708b5026ccba7cb)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F7cf985a8-7134-408b-a197-cf566a0d133d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c674351ddc39dc70f708b5026ccba7cb)

---

自己紹介
----

```
profile:
  name: 森田 和明
  company: 富士ソフト株式会社
  position:
    title: 主任 / フェロー
    specialization: アーキテクト・エバンジェリスト
  
  AWS Certifications:
      - AWS Ambassador (2023, 2024)
      - Japan AWS Top Engineer (2020-2024)
      - Japan All AWS Certifications Engineer (2024)
      - AWS Community Builder (2024, 2025)
  
  professional_focus: 
      - AWS関係のアーキテクトとエバンジェリスト（生成AIを含む）
  
  social:
    X: https://x.com/moritalous
    Qiita: https://qiita.com/moritalous
    GitHub: https://github.com/moritalous

```

---

まだまだイケる！Bedrockの入門書！
--------------------

[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F92d00a43-11ed-472b-8cc1-31161f3f08a8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=1d9f4a104ec4e281e34fd291d0abfa5d)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F92d00a43-11ed-472b-8cc1-31161f3f08a8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=1d9f4a104ec4e281e34fd291d0abfa5d)

---

Claude 4をAmazon Bedrockで使おう
===========================

---

Claude 4はAWS上でも使えます
-------------------

モデルを有効化して

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fbd35579c-ccb2-4e14-b477-762ba4418ba3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=51bcfdff009166a0e0072b51cb3327ed)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fbd35579c-ccb2-4e14-b477-762ba4418ba3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=51bcfdff009166a0e0072b51cb3327ed)

---

Claude 4はAWS上でも使えます
-------------------

プレイグラウンドで実行

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F2ff70e6c-3919-468f-966a-22af91d07159.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=51eccf5d4b57e0f3c30bd3387ac93260)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F2ff70e6c-3919-468f-966a-22af91d07159.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=51eccf5d4b57e0f3c30bd3387ac93260)

---

AWS準拠のセキュリティ
------------

Bedrock提供モデルとモデル開発元のAPIは別もの。同じモデルを使用する場合でも物理的に隔離

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F5d847415-8c54-4fb7-b981-2b94faab0eb7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=0da2558d7c8f09168198401c26f25068)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F5d847415-8c54-4fb7-b981-2b94faab0eb7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=0da2558d7c8f09168198401c26f25068)

---

リージョン情報
-------

Claude 4モデルはすべてクロスリージョン推論（※１）での提供  
Sonnet 4はローンチのタイミングで東京・大阪でも利用できます！

| クロスリージョン（※１） | Claude Sonnet 4 | Claude Opus 4 |
| --- | --- | --- |
| **米国** ：バージニア北部、オハイオ、オレゴン | ✅ 提供 | ✅ 提供 |
| **アジアパシフィック** ：東京、大阪、ムンバイ、ソウル、シンガポール、シドニー、ハイデラバード（※２） | ✅ 提供 | ❌ 未提供 |

（※１）クロスリージョン推論：複数のリージョンのどこかで処理されます  
（※２）ハイデラバードはオプトインリージョン（デフォルトで無効化）

---

Anthropic APIとBedrockの比較
------------------------

モデルそのものは同じでもAPIで提供されている機能は異なります

| 機能 | Anthropic API | Amazon Bedrock |
| --- | --- | --- |
| SDK | Anthropic SDK | AWS SDK / Anthropic SDK |
| 認証・認可 | APIキー | AWS認証情報 |
| バッチ処理 (Batch processing) | ✅ 利用可能 | ✅ 利用可能 |
| 引用 (Citations) | ✅ 利用可能 | ❌ 利用不可 Bedrockナレッジベースで代用 |
| コード実行 (Code execution) | ✅ 利用可能 (パブリックベータ) | ❌ 利用不可 Bedrockエージェントで代用 |
| コンピュータ使用 (Computer use) | ✅ 利用可能 (パブリックベータ) | ✅ 利用可能 (ベータ) |
| ファイル API (Files API) | ✅ 利用可能 (パブリックベータ) | ❌ 利用不可 |
| MCPコネクタ (MCP connector) | ✅ 利用可能 (パブリックベータ) | ❌ 利用不可 |
| PDFサポート | ✅ 利用可能 | ❌ 利用不可 Converse APIで代用 |
| プロンプトキャッシング (Prompt caching) | ✅ 利用可能 | ✅ 利用可能 |
| └1時間キャッシュ期間 (1-hour cache duration) | ✅ 利用可能 (ベータ) | ❌ 利用不可 |
| トークンカウント (Token counting) | ✅ 利用可能 | ❌ 利用不可 |
| ツール使用 (Tool use) | ✅ 利用可能 | ✅ 利用可能 |
| ウェブ検索 (Web search) | ✅ 利用可能 | ❌ 利用不可 |

---

Bedrockではモデル以外の機能も充実
--------------------

複数のモデルを組み合わせて生成AIアプリ開発ができるプラットフォーム  
もちろん生成AI以外のAWSサービスとの組み合わせも

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fc9e0e7ce-d23a-44bf-87c6-13586454354a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=68d8e021ee7d9f3a7ddf2dd95be1596a)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fc9e0e7ce-d23a-44bf-87c6-13586454354a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=68d8e021ee7d9f3a7ddf2dd95be1596a)

---

Claude CodeもAmazon Bedrockで使おう
==============================

---

Bedrockで使うための設定
---------------

環境変数をひとつ足すだけでOK

```
export CLAUDE_CODE_USE_BEDROCK=1
claude

```

---

Claude Code ?
-------------

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fd57a1836-8531-4d2d-859a-704863397009.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a828e8193e3b51a2bc3bcc757d4696c7)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fd57a1836-8531-4d2d-859a-704863397009.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a828e8193e3b51a2bc3bcc757d4696c7)

---

Claude Code !!
--------------

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F748715b8-fef5-40c1-a06c-05c13410ed5a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d9c73422c254d7ae4ad1b80eea178653)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F748715b8-fef5-40c1-a06c-05c13410ed5a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d9c73422c254d7ae4ad1b80eea178653)

---

`/status`コマンドで設定をチェック
---------------------

バージニア北部リージョンのClaude 3.7 Sonnet（とClaude 3.5 Haiku）が使用されます

[![スクリーンショット 2025-05-30 213137.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F5c7a6551-4148-4a30-8fec-f3e16c51032c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=65ce333de958a162408c5be7e65e9926)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F5c7a6551-4148-4a30-8fec-f3e16c51032c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=65ce333de958a162408c5be7e65e9926)

---

モデルやリージョンを変更する方法
----------------

* モデルを変更したい

  ```
  export CLAUDE_CODE_USE_BEDROCK=1
  export ANTHROPIC_MODEL=us.anthropic.claude-sonnet-4-20250514-v1:0
  export ANTHROPIC_SMALL_FAST_MODEL=us.anthropic.claude-3-5-haiku-20241022-v1:0
  claude

  ```
* リージョンを変更したい

  ```
  export CLAUDE_CODE_USE_BEDROCK=1
  export AWS_REGION=us-west-2
  claude

  ```

---

東京/大阪リージョンに設定もできるが、、
--------------------

Claude 3.5 Haikuが未提供なので工夫が必要

---

Claude以外のモデルは諦めよう
-----------------

Amazon Novaはだめでした

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fc0faf3d5-70ab-4945-bc85-5a6404ba80b1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d700d25007801c49b5fc881c1bf71fc4)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fc0faf3d5-70ab-4945-bc85-5a6404ba80b1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d700d25007801c49b5fc881c1bf71fc4)

---

BedrockでClaudeを使うTips
=====================

---

利用状況を人ごとに管理したい
--------------

アプリケーション推論プロファイルを作成することでコストを分けて管理

```
aws bedrock create-inference-profile \
  --inference-profile-name claude-code-user1 \
  --model-source copyFrom=arn:aws:bedrock:us-east-1:123456789012:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0

```

```
# 出力
{
  "inferenceProfileArn": "arn:aws:bedrock:us-east-1:123456789012:application-inference-profile/ua2srtupytga",
  "status": "ACTIVE"
}

```

`inferenceProfileArn`をANTHROPIC\_MODELに指定

---

モデル呼び出しログを確認
------------

有効化するとモデル呼び出しログが見られます！自分の環境で見てみよう！（Claude Codeのプロンプトも見られるよ）

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F917e2e8d-660a-4ac6-88fe-daa717828637.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3ee716e5103184c593af6a4dc8de0867)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F917e2e8d-660a-4ac6-88fe-daa717828637.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3ee716e5103184c593af6a4dc8de0867)

---

Bedrockのいいところ・残念なところ
====================

---

Bedrockのいいところ
-------------

* AWSのサービスとしてのセキュリティ
  + IAMによる権限管理
  + 会社でのサービス利用までの説明が楽（AWSがすでに認められてるケース）
* AWSのサービスとしての請求
  + 事前のチャージ不要で使った分だけの課金
  + 請求が他のAWS利用料と合算
* Claude以外のモデルも利用可能
  + 埋め込みモデル、リランキングモデル、画像生成モデル

---

Bedrockの残念なところ
--------------

* APIキーでサクッとができない
* 使いすぎ防止が難しい
  + 想定よりも使ってしまうかも
  + アラート設定などはあるがリアルタイムで使えなくなる仕組みではない
* クォータ制限がきびし目
  + 緩和申請！！！  
    [![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fd4f8817e-4945-46a8-aaf9-2b2b393a1677.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a9a795608ad6eb0fff91644e572374da)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2Fd4f8817e-4945-46a8-aaf9-2b2b393a1677.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a9a795608ad6eb0fff91644e572374da)

---

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F82c9b7ae-4613-4f93-b125-2fcd4010fcb1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c13d214f1a1f369b874b97675b34fcf9)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F41574%2F82c9b7ae-4613-4f93-b125-2fcd4010fcb1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c13d214f1a1f369b874b97675b34fcf9)
