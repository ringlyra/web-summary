<!-- metadata -->

- **title**: Claude Pro（$20）プランでゼロから始めるClaude Code
- **source**: https://zenn.dev/asap/articles/700168965fdb7b
- **author**: zenn.dev
- **published**: 2025-06-06T02:56:51.366+09:00
- **fetched**: 2025-06-05T18:59:52Z
- **tags**: codex, ai
- **image**: https://res.cloudinary.com/zenn/image/upload/s--o927mcY9--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Pro%25EF%25BC%2588%252420%25EF%25BC%2589%25E3%2583%2597%25E3%2583%25A9%25E3%2583%25B3%25E3%2581%25A7%25E3%2582%25BC%25E3%2583%25AD%25E3%2581%258B%25E3%2582%2589%25E5%25A7%258B%25E3%2582%2581%25E3%2582%258BClaude%2520Code%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:asap%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3plbm4tdXNlci11cGxvYWQvYXZhdGFyL2VhYjVhYTQ1MTkuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png

## 要約

Claude Proプラン(月額 $20)で利用できる **Claude Code** の導入方法を解説。環境構築からテトリス制作、**Playwright MCP** での自動テスト、レート制限の検証まで実践的にまとめている。

1. 契約手順と利用可能モデル（Claude Sonnet 4）の紹介
2. macOS Sequoia環境でNode.jsをインストール
3. `npm install -g @anthropic-ai/claude-code` でCLIを導入し、ログイン手順を解説
4. `/init` 実行で `CLAUDE.md` を作成、日本語応答の設定を書き込む
5. Next.js + TypeScriptでテトリスを開発し、ファイル書き込み承認を確認
6. `.mcp.json` を追加し、Playwright MCP経由でGUIテストを実行
7. コスト試算ツールでAPI利用料を確認し、総額$22.44で約5時間のレート制限を体験
8. Claude Codeは簡単に導入でき、Proプランでも趣味開発には十分

## 本文

# はじめに

ClaudeのProプラン（月額$20）からClaude Codeが利用できるようになったと聞きまして、早速試してみます。（後数日来なかったらMaxプラン契約してたかもしれない・・・）

<https://x.com/_catwu/status/1930307574387363948>

ちなみに、Claude Code初心者なので、下記の資料を参考にして進めました。例によっていつもありがとうございます。  
<https://x.com/schroneko/status/1930089588053422137>

備忘録的につらつら書いていこうと思います。  
まだ使ったことない人が、なんとなく使えるくらいには書く予定です。

なお、Proプランでは「Claude Sonnet 4」モデルしか利用できないそうです。  
今回の記事も「Claude Sonnet 4」の利用が前提となります。

今回の記事では、実際に環境をセットアップし、簡単にテトリスゲームを作成し、Playwright MCPを使った自動テストまで一通り実施してみました。  
その後、レート制限が来るまでひたすら利用して、Proプラン利用の場合、どの程度でレート制限がくるか確認しました。

これから初めて使ってみようかなという方の手助けになれば幸いです。

# 環境

M4 Max MacBook Pro  
macOS Sequoia 15.2

# 事前準備

## Claudeの契約

ClaudeのProプラン（もしくはMaxプラン）を契約しましょう。  
APIで利用したい場合はそれでも良いですが、月額$20くらいなので、とりあえず一ヶ月だけ課金するのはアリかなと思います。

<https://claude.ai/>  
こちらからアカウント登録し、Proプランへのアップグレードをしてください。  
年間契約だと安いですが、Xで断末魔が聞こえてきているので、おすすめしません。

なんなら、Proプラン契約後「設定」→「請求」→「プランを調整」から、契約を解除しても、支払った1ヶ月分は利用できるので、解約しても良いと思います。  
![](https://storage.googleapis.com/zenn-user-upload/b2f216af757e-20250605.png)

1ヶ月使ってみて、また継続して使いたくなった時に再度契約すれば良いのです。

## Node.jsをインストールする

macなら

でインストールできます。今後`npm`コマンドを利用する上で必要になります。

# Claude Codeを実行してみる

## Claude Codeのインストール

ターミナルで下記のコマンドを実行しましょう。  
とりあえず、以降フォルダの移動はしたくないので、作業用の`sample`ディレクトリで実行するものとします。

./sample

```
npm install -g @anthropic-ai/claude-code

```

![](https://storage.googleapis.com/zenn-user-upload/45c18ff200f9-20250605.png)

下記のように表示されれば、成功です。  
![](https://storage.googleapis.com/zenn-user-upload/85292c5c6f97-20250605.png)

## Claude Codeのログイン

続いて、下記のコマンドでログインを行います。

![](https://storage.googleapis.com/zenn-user-upload/95eb7883a64e-20250605.png)

すると、まずは下記のようにテキストスタイルの選択画面が表示されるので、好きなものを選びましょう。  
私は1にしました。  
![](https://storage.googleapis.com/zenn-user-upload/4ce24373e739-20250605.png)

続いて、ログイン方法の選択です。今回はProプラン経由でClaude Codeを利用するため、上の選択肢でEnterを押します。  
![](https://storage.googleapis.com/zenn-user-upload/b275d0a4e7f1-20250605.png)

すると下記のようにブラウザが立ち上がります。ブラウザにログイン情報が残っている場合は、しばらく待つと勝手にログインが行われます。  
![](https://storage.googleapis.com/zenn-user-upload/53ed793d1204-20250605.png)

ログインに成功すると下記のように承認依頼が表示されるので、承認してください。  
![](https://storage.googleapis.com/zenn-user-upload/195e3f6cc470-20250605.png)

下記の画面が表示されたら、再びターミナルに戻りましょう  
![](https://storage.googleapis.com/zenn-user-upload/efc82ba8fc0d-20250605.png)

ターミナル上では下記にようになっているはずですので、Enterを押しましょう  
![](https://storage.googleapis.com/zenn-user-upload/3bd27a191800-20250605.png)

セキュリティに関しての注意事項が記載されています。  
![](https://storage.googleapis.com/zenn-user-upload/47e4350626d4-20250605.png)

記載内容は下記です。読んだらEnterを押しましょう

```
 セキュリティに関する注意事項:

 1. Claudeは誤りを犯す可能性があります
    Claudeの応答は常に確認してください。特に
    コードを実行する際は注意が必要です。

 2. プロンプト注入のリスクのため、信頼できるコードのみで使用してください
    詳細については以下のリンクを参照してください:
    https://docs.anthropic.com/s/claude-code-security

 Enterキーを押して続行してください…

```

続いてターミナルの設定について聞かれています。  
![](https://storage.googleapis.com/zenn-user-upload/d00bcbee8473-20250605.png)

```
 Claude Codeのターミナル設定を使用しますか？

 最適なコーディング体験のため、ターミナルの推奨設定を有効にします
 改行にはShift+Enterを使用

 ❯ 1. はい、推奨設定を使用します
   2. いいえ、後で/terminal-setupで設定します

```

こちらもとりあえず1で設定しておきます。Enterを押しましょう。

フォルダ内のファイルを全て読んでしまうが問題ないかを確認しています。  
Claude Codeを実行したディレクトリ以下のフォルダやディレクトリはClaudeが読みにいくので、不適切な文章を置かないでくださいという意味です。  
![](https://storage.googleapis.com/zenn-user-upload/8f47bb9ee5b7-20250605.png)

```
このフォルダー内のファイルを信頼しますか？

/use_claudecode/sample

Claude Codeはこのフォルダー内のファイルを読み込む可能性があります。信頼できないファイルを読み込むと、Claude Codeが予期しない動作をする可能性があります。

ご承諾いただければ、Claude Codeはこのフォルダー内のファイルを実行する可能性があります。信頼できないコードを実行することは危険です。
https://docs.anthropic.com/s/claude-code-security
 ❯ 1. はい、続行
   2. いいえ、終了

```

さてこれで、Claude Codeが利用できるようになりました。  
![](https://storage.googleapis.com/zenn-user-upload/a56e56fb14e6-20250605.png)

# なんか作ってみる

## /initを実行する

さて、なんか作ってもらおうと思いますが、まずは`/init`を実行してみましょう。  
これを実行することで、ディレクトリの中身をClaudeが読み込んで、CLAUDE.mdに情報を書き込んでくれます。  
これを読むことでClaudeはリポジトリの概要をすぐに理解できるわけです。  
加えて、ここに記載されている制約を守って実装してくれるようになります。

まずは実行してみましょう

すると下記のように`ls`コマンドの実行をするので許可してくださいという表示が出ます。  
![](https://storage.googleapis.com/zenn-user-upload/f9e2f2f45215-20250606.png)

普通に許可する場合は1でEnterを押せば良いです。  
また、今後このコマンドは確認しなくて良いと思った場合は、2でEnterを押してください。  
拒否する場合は3です。  
ここでは一旦1にします。

続いては、ファイルの書き込みの承認依頼がきました。  
こちらも承認します。  
![](https://storage.googleapis.com/zenn-user-upload/43b2b50efd24-20250606.png)

## 日本語で出力させる

さて、下記のような`CLAUDE.md`が作られました。  
ただ、このままだと英語なのでちょっと不便ですね。  
![](https://storage.googleapis.com/zenn-user-upload/9b1cb473eb08-20250606.png)

そこで、この`CLAUDE.md`に下記の文言を追加しましょう。

> 必ず日本語で回答してください。

![](https://storage.googleapis.com/zenn-user-upload/865ac556e814-20250606.png)  
このようにすることで、今後Claudeの出力が日本語になります。

## テトリスでも作ってみる

### 早速プロンプトを入れてみる

下記のようなプロンプトを試してみました

すると下記のように、タスクを作って作り始めてくれました。  
![](https://storage.googleapis.com/zenn-user-upload/c49d3ab266c7-20250606.png)

### やっぱ変えたい！そんな時は

さて、ここで私、pythonじゃなくてNext.jsで作って欲しくなりました。  
そんな時は、まずは現在の実行を停止するために「Esc」ボタンを押しましょう。

すると実行が止まって下記のような画面になります。  
![](https://storage.googleapis.com/zenn-user-upload/d690096b0f5a-20250606.png)

その際、入力ボックスが復活しているので、下記のように入力すればNext.jsで再度実装を開始してくれます。

![](https://storage.googleapis.com/zenn-user-upload/920c72067819-20250606.png)

```
やっぱり、Next.jsとTypeScriptで実装してください。

```

すると、下記のように、Next.jsによる実装のタスクを作成してくれました。  
![](https://storage.googleapis.com/zenn-user-upload/9793d262b1d1-20250606.png)

そのまま、プロジェクトの作成も実施してくれます。  
何かするたびに承認が要求されますので、都度承認するか、2を押してオートモードにするのも良いです。（ただし、初出のコマンドは毎回承認要求されます）  
![](https://storage.googleapis.com/zenn-user-upload/68a3e2afbf77-20250606.png)

ファイルの出力などもオートで進むのを眺めているといつの間にか、完成していて、実際に動くかどうかをサーバを立ち上げて確かめてくれるらしいです。  
![](https://storage.googleapis.com/zenn-user-upload/c737b166b124-20250606.png)

どうやら完成したようです。実際に起動してみましょう！  
![](https://storage.googleapis.com/zenn-user-upload/68a3e2afbf77-20250606.png)

### 動作確認

新しいターミナルを立ち上げて、下記のコマンドを入力します。

するとちゃんと動くテトリスが表示されました。  
![](https://storage.googleapis.com/zenn-user-upload/6a673dace5f1-20250606.png)

ついでに、「コミットしといて」と伝えると、勝手にコミットメッセージとかも作ってcommitしておいてくれます。ありがたいですね。

もしエラーなどがあって動作しない場合は、入力欄にエラーの詳細を記述して「しっかり考えて」と追加して依頼すれば大体直してくれると思います。

### CLAUDE.mdを更新する

改めて`/init`コマンドを実行してみましょう。  
`CLAUDE.md`が更新されて、先ほど作成したテトリスゲームの概要が書き出されるはずです。

下記をClaude Codeで実行してみましょう。

このように、中身を更新してくれて、作成したコードを簡単に解説してくれるようになりました。  
また、日本語で出力してほしいという指示は残したままにしてくれています。  
したがって、「どんな技術を使うか」、「どんな制約下で実装するか」などはこちらに追記しておくことで、上書きされず常に参照してくれるようになります。  
![](https://storage.googleapis.com/zenn-user-upload/97fc167cbfac-20250606.png)

また、余談ですが、コンソールのログを見ると、`.github/copilot-instructions.md`や`/.cursorrules`、`/.cursor/rules/**`なども参照してくれるっぽいです。  
おそらくですが、ここに記載されている制約やルールも反映してくれるのだと思います。  
![](https://storage.googleapis.com/zenn-user-upload/641be32c36fd-20250606.png)

## Claude Codeを停止する

`/exit`コマンドを実行することで、停止してコンソールに抜けることができます。  
![](https://storage.googleapis.com/zenn-user-upload/8e7256e7e5ed-20250606.png)

# MCPと接続させてみる

さて、せっかくWebアプリができたので、PlayWrite MCPを接続してテストも自動でしてもらいましょう。

MCPに接続させる方法はとても簡単です。  
リポジトリに`.mcp.json`というファイルを作成して、下記を書き込むだけです。

.mcp.json

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}

```

下記の記事を参考にさせていただきました。  
<https://izanami.dev/post/0b13ae65-d420-47cd-b8a0-d4ef9d301508>

## PlayWrite MCPでテトリスゲームをテストする

いつも通り`claude`コマンドでClaude Codeを立ち上げてください。  
すると、下記のようにMCPを実行してよいかの承認依頼が来るはずです。  
![](https://storage.googleapis.com/zenn-user-upload/f4e90c0eb941-20250606.png)

これを承認後下記のようにclaude Codeに依頼してみます。

```
playwrite mcpを利用してテトリスゲームをテストしてください。

```

するとそのうち下記のように、Tool Useの承認依頼が飛んできます。これがMCPを使い始めた証拠です。  
![](https://storage.googleapis.com/zenn-user-upload/a18023620967-20250606.png)

さて、実際にPlayWrite MCPがテストしている様子を動画でご覧ください。

<https://youtu.be/JKeU6b9RVSI>  
Web画面のスクリーンショットを撮りながら、画面をクリックして一時停止してみたり、キーボード入力を試してミノが動くかどうかを確かめたりしながら、動作確認をしてくれています。

最終的にテストを完了できました！  
![](https://storage.googleapis.com/zenn-user-upload/c4cb7b59fe25-20250606.png)

## かかったコストは？

Proプランから利用しているため、月額$20以上にはかかっていないですが、どうやらClaude Codeではかかったトークン数を保存してるらしく、そこからAPI利用時のコストを見積もってくれるツールを開発してくださった方がいるようです。

使い方などは下記の記事をご覧ください。  
<https://zenn.dev/ryoppippi/articles/6c9a8fe6629cd6>

こちらを見ると、今回の処理でかかったコストは$2.39らしいです。  
![](https://storage.googleapis.com/zenn-user-upload/b6bb462fb64d-20250606.png)

ちょっとしか使っていない割には結構かかったなという印象ですね・・・  
やはり定額利用が正義だ・・・

# Proプランの制限

その後、開発中のWebアプリの機能追加などに利用していたところ、上記の$2.39に加えて、$20.05、つまり合計$22.44使ったところでレート制限に達しました。  
![](https://storage.googleapis.com/zenn-user-upload/26d59b19c2d1-20250606.png)  
![](https://storage.googleapis.com/zenn-user-upload/5d01cc437a7b-20250606.png)

AM2:30ごろに制限を受けて、AM6:00ごろまでということなので、以下のProプランの制限が5時間でリセットされるというのは正しそうです。  
<https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan>  
[https://support.anthropic.com/ja/articles/8325612-claude-proには使用制限がありますか](https://support.anthropic.com/ja/articles/8325612-claude-pro%E3%81%AB%E3%81%AF%E4%BD%BF%E7%94%A8%E5%88%B6%E9%99%90%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%81%8B)

感覚としては、「思ったよりたくさん使えたな」という印象です。  
ただ、大きいリポジトリの機能追加などに利用すると、1タスクくらいですぐに制限が来る感じです。  
（それでも5時間待てば再開できるのだから、かなり良心的だと思う。趣味で使う分には十分すぎると思いました。）

# まとめ

今回はClaudeのProプラン（月額 $20）を利用してClaude Codeを試してみました。

実際に環境をセットアップし、簡単にテトリスゲームを作成し、Playwright MCPを使った自動テストまで一通り実施しました。

Claude Codeは手軽に使えて、初心者から上級者まで十分に活用できるツールです。興味がある方は一度試してみてはいかがでしょうか！

# 参考文献

下記の記事で勉強させていただきました。ありがとうございました。

<https://docs.anthropic.com/en/docs/claude-code/overview>

<https://speakerdeck.com/schroneko/getting-started-with-claude-code>

<https://zenn.dev/schroneko/articles/code-with-claude>

<https://note.com/nike_cha_n/n/nee3503e7a617>

<https://qiita.com/eiji-noguchi/items/a45dbb94ad7544d1c1b4>

<https://izanami.dev/post/0b13ae65-d420-47cd-b8a0-d4ef9d301508>
