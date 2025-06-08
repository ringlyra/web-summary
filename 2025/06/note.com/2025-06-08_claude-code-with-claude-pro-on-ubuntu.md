<!-- metadata -->
- **title**: Claude Code with Claude Pro on リモート Ubuntu 環境で安価に常在戦場モバイルポチポチ開発
- **source**: https://note.com/hi_noguchi/n/n53fbc5f23be4
- **author**: Hi-Noguchi | 株式会社きみより代表
- **published**: 2025-06-08T21:14:30+09:00
- **fetched**: 2025-06-08T16:17:31Z
- **tags**: codex, ubuntu, github, claude, aicoding, claudeCode, greptile, byobu
- **image**: https://assets.st-note.com/production/uploads/images/194956419/45af9a15393574684e6ac9ee8b90ecf3.png

## 要約
Claude Pro を利用して、リモートの Ubuntu サーバーに Claude Code を導入し、モバイル端末から常時開発できる環境を構築する手順を解説。セッション制限を活用すれば 24 時間連続で作業でき、休憩も自動的に挟める。Ubuntu 上で Node.js を `n` で管理し、Byobu でターミナルを保持しつつ GitHub CLI を使って認証・リポジトリ取得を行い、`claude` コマンドで開発を進める。モバイル開発における利点やコスパの高さ、他ツールとの比較にも触れている。

## 本文
はじめに
----

### 要約

### 対象読者

### Claude Code ?

### Claude Code with GitHub Actions ?

### 常在戦場モバイルポチポチ開発？

* Claude Pro は Claude Pro 利用のセッション開始から 5 時間内で「定額利用」になる

  + たとえば 11:30 に開始したら、そのセッション内で利用上限に達した場合、次に使えるようになるのは 16:00 となる（分の判定が Claude Code 以外のところと比べて若干緩い）
  + で、 16:00 台に使い始めて上限がくると、次の再開は 21:00
  + 21:00 台に使い始めて……再開は 26:00 ( 02:00 )
* ……という感じで、サラリーマン的に労働時間に縛られない開発が可能なのであれば、これで 24 時間ずーっと Claude Pro の使える間は開発を続けられるというわけ
* ポモドーロならぬ Claude Code タイマーが切れるまでが作業時間。切れたら強制的にお休みに入れる。適度に休憩できる！　これでみんなハムスターのごとく車輪くるくる開発ライフ！（ぐるぐる目）
* ……取り乱しましたが、セルゲーム前の悟空のように、モバイルデバイスから開発していることが平常状態、という境地に至れれば、精神的な疲労も感じなくなりましょう
* なおネットワーク帯域的にも必要なのは SSH 接続のみか GitHub 閲覧くらいなので、

### 本記事が合わなそうな人

* CLI は一切見たくない人
* Ubuntu / Linux なんて触りたくもないという人
* 常在戦場でモバイルデバイスから開発なんてとてもでないけれどやってられんという人
* リモート Ubuntu 環境なんてけしからん！　漢ならローカル環境一択！　という人

事前準備
----

### Claude Pro 加入

* Claude Pro は 20 ドル ～ 加入できるのでまずはオススメ
* MAX 100 ドル ～ でも構いませんが、最初は Pro からでいいんじゃないかな
* Claude Code に限らず Claude Desktop やら WEB やらモバイルアプリやら、とにかく Anthropic Claude 謹製サービスが定額で使えるので、入っていて損はないです

### リモート Ubuntu 環境の用意

### SSH クライアントの用意

Ubuntu 環境への Claude Pro の設定
--------------------------

### まずは root ユーザで

### 基本パッケージ更新

```
apt update
apt upgrade -y

shutdown -r now
```

### ユーザ作成して sudo 権限付与

* 再起動が終わったらユーザ作成
* それから sudo 権限を付与
* 最後に設定反映

```
adduser user-desuyo

usermod -aG sudo user-desuyo
```

### ユーザを切り替え

### node.js 環境用意

```
apt install make build-essential -y
curl -L https:
```

```
n
```

![](https://assets.st-note.com/img/1749381515-aDdHUxFAY1P9MCNGizB5pnjW.png?width=1200)

n

```
n 24
```

![](https://assets.st-note.com/img/1749381585-78lnuaCosRhFjUweHrgk2OZN.png?width=1200)

ふたたび n

```
npm install -g pnpm
```

```
pnpm setup
```

### Claude Code インストール

```
pnpm install -g @anthropic-ai/claude-code
pnpm approve-builds -g
```

```
claude
```

### Byobu を使う

Claude Pro を GitHub 連携して使う
--------------------------

### 前置き

### gh のインストールと GitHub 認証

```
sudo apt install gh -y
```

```
gh auth login
```

### GitHub からリポジトリを持ってくる

```
gh repo clone OrganizationName or UserName/RepoName
```

### カレントディレクトリを移動して Claude Code 起動

```
cd RepoName
```

```
claude
```

Claude Code で開発する際の基本的な流れ
-------------------------

動作確認どうするの？
----------

おわりに
----

### 雑感

* こんな感じで最近モバイルポチポチ開発やり始めてますが、中毒めいたものがあるので、くれぐれも健康を損なわないように……
* Claude Code は何が嬉しいの？　という点について、個人的に GitHub Copilot / Cursor / Windsurf / Cline / RooCode あたりのエディタ型のものと比べて一番のメリットは、モバイルデバイスでの開発親和性ですかねー
* Devin との比較でいうと、圧倒的コスパの良さ。ほんと十数分の一で済む
* ニーズがあれば、Claude Code のもう少し具体的なところも書くかなー

### 関連記事

### 自己紹介
