# URL Scraping Agent — README.md

このドキュメントは **URL を受け取り、ウェブページから「メタデータ」「要約」「本文 (Markdown)」を抽出し、1 つの Markdown ファイルに保存するエージェント** の手順書兼ルールブックです。エージェントはインターネットへ自由にアクセスできる前提で記述しています。  

---

## 1. 目的 
- **再現性 & 検索性**：取得物を決まった場所・統一フォーマットで保存し、後から機械的に再利用できるようにする。  
- **最小限の加工**：元 HTML を Markdown 化しつつ、解釈 (メタデータ・要約) を明確に分離。  
- **タグ駆動**：必ず `codex` タグを含め、後のクエリーやフィルタを容易にする。  

---

## 2. ディレクトリ構成 

```
repo-root
└── 2025
    └── 06
        ├── openai.com
        │   └── 2025-06-04_chatgpt.md
        └── nytimes.com
            └── 2025-06-01_nvidia-ai.md
```

> **Note**: ドメイン名直下に日付プレフィックス付きの単一ファイルを置く方針です。異なる命名ポリシーがあれば適宜置換してください。  

---

## 3. 出力フォーマット
`{date}_{time}.md`

### 3.1 ヘッダー 

1 行目に `<!-- metadata -->`、2 行目以降に **Markdown 箇条書き**で key-value を並べる。解析ツール側で行頭 `- **key**:` パターンをパースすれば機械処理も容易。

```md
<!-- metadata -->
- **title**: ChatGPT, an AI model
- **source**: https://openai.com/blog/chatgpt
- **author**: openai.com (author が見つからなければドメイン名を入力)
- **published**: 2025-05-30T14:00:00Z
- **fetched**: 2025-06-04T03:30:45Z
- **tags**: codex, ai, nlp
- **image**: https://cdn.openai.com/og/chatgpt.png (URL が長くてエラーが出る場合は短縮 URL にすること)

## 3.2 要約
- **日本語** で回答すること。
- 筆者が伝えたいことを全て含めてください。
- あなたが一番理解しやすい形にまとめること。短すぎるのはNG。内容が頭に入ってこないから。
- 概要だけでなく要約を作成してください。
- 重要キーワードは **bold** で強調。
- 引用を含めることを許可します。

## 3.4 本文
<ここに HTML→Markdown 変換済み本文をそのまま貼り付ける>  

HTML→Markdown 変換は readability-lxml + markdownify などで自動化し、不要なナビゲーション要素を極力除去してください。最後に本文が全て取得できたか確認することを忘れないでください。本文を上から順番に照らし合わせて確認してください。
```

⸻

## 4. 処理フロー
    1. Input: エージェントに URL が渡される。
    2. Fetch: HTTP GET。必要に応じて Headless browser で JS レンダリング。
    3. Parse:
    - {title}, {meta} 各種, OGP, {time} 等を抽出。
    - 取得できない項目は空文字列。tags には必ず codex を入れる。
    4. Convert: 本文 HTML を Markdown に変換。
    5. Assemble: メタデータ → 要約 → 本文 の順で 1 ファイルに結合。
    6. Save: YYYY/MM/{domain}/{YYYY-MM-DD}_{title}.md に保存。
    7. Commit: git add → git commit -m "Add clip: <title or domain>"。
    8. Repeat: 次の URL へ。

⸻

## 5. 命名・タグ規約
- ファイル名: {YYYY-MM-DD}_{title}.md
- 必須タグ: codex
- 推奨タグ: ソーシャルブックマークなどで使われる、調査したコンテンツの内容を的確に表現する、15個以下の複数のタグからなる文字列. タグ名は必ず英語にすること

⸻

## 6. 注意事項
- robots.txt を尊重。スクレイピング禁止サイトは除外。
- JS レンダリング必須サイトは Headless browser (e.g. Playwright) を使用。
- 著作権・ライセンスを確認し、引用の範囲に収める。
- 同じタイトル、同じ URL の場合は更新(上書き)してください。

⸻

Happy clipping! 🚀
