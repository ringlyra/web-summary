# URL Scraping Agent — README.md

このドキュメントは **URL を受け取り、ウェブページから「クリッピング (スクレイピングした生データ)」「メタデータ」「要約」を抽出して GitHub リポジトリに整理・保存するエージェント** のための手順書兼ルールブックです。エージェントはインターネットに自由にアクセスできる前提で書かれています。

---

## 1. 目的 / Purpose  
- **再現性 & 検索性**：すべての取得物を決まった場所に置き、後から機械的に再利用できるようにする。  
- **最小限の加工**：クリッピングは “元の HTML そのまま” を保存し、解釈はメタデータと要約に分離する。  
- **タグ駆動**：`codex` タグを必須にし、後のクエリーフィルターを容易にする。  

---

## 2. ディレクトリ構成 / Directory Tree  

repo-root/
  2025/
    06/
      openai.com/
        2025-06-04_what-is-ace-tools.md
      nytimes.com/
        2025-06-01_llm-policy-debate.md

> **Note**: まとめたいフォルダ名ポリシーが別にある場合は、ここを置換してください。  

---

## 3. 出力フォーマット / File Specs  

### 3.1 metadata.yaml (必須)  

| フィールド        | 型 / 例                                 | 説明 |
|------------------|-----------------------------------------|------|
| `title`          | `"ChatGPT, an AI model"`                | `<title>` タグ、もしくは `<h1>` |
| `source`         | `"https://openai.com/blog/chatgpt"`     | 元 URL |
| `author`         | `"openai.com"`                          | `<meta name="author">`。無い場合はドメイン |
| `published`      | `"2025-05-30T14:00:00Z"`                | 公開日時 (取れなければ空文字) |
| `created`        | `"2025-06-04T03:30:45Z"`                | 取得日時 (処理開始時点、UTC) |
| `description`    | `"Official ChatGPT launch announcement"`| `<meta name="description">` |
| `tags`           | `["codex", "ai", "nlp"]`                | `codex` を含むタグ配列 |
| `image`          | `"https://cdn.openai.com/og/chatgpt.png"`| OGP 画像 URL (無ければ空文字) |

> YAML を推奨しますが、JSON でも可。日付は必ず **ISO-8601**。  

---

### 3.2 summary.md (必須)  

```md
## 概要 / Summary  
- 箇条書き 3-6 行で要点を日本語で  
- 重要キーワードは **bold**  
- 原文引用は 120 文字以内  

ポイント: 要約は「読む前に全体像をつかむ」ためのコンパクトさを最重視。

⸻

3.3 raw.html (必須)
	•	requests.get(url).text を UTF-8 そのまま保存。
	•	処理は不要 (JavaScript 実行後の HTML が必要なら playwright 等で実装し直す)。

⸻

4. 処理フロー / Workflow
	1.	Input: エージェントに URL が渡される。
	2.	Fetch: HTTP GET → raw.html 保存。
	3.	Parse: BeautifulSoup 等で以下を抽出
	•	<title>
	•	<meta>*, OGP, <time> など
	4.	Build metadata.yaml
	•	未取得項目は空文字。必ず tags に "codex" を入れる。
	5.	Generate summary.md
	•	500 字以内、日本語、箇条書き。
	6.	Commit: git add → git commit -m "Add clip: <title or domain>".
	7.	Repeat for each URL.

⸻

5. 命名・タグ規約 / Naming & Tag Rules
	•	フォルダ名: YYYY-MM-DD_HHMMSS (UTC)
	•	ブランチ: 必要に応じ clips/<date>
	•	必須タグ: codex
	•	推奨タグ: コンテンツ種別 (article, tutorial, spec など)

⸻

6. 注意事項 / Caveats
	•	PDF や image only ページは未対応。別途ダウンロードして raw.bin とする。
	•	robots.txt を尊重。スクレイピング禁止サイトは除外。
	•	JavaScript レンダリングが必須のサイトは Headless browser を使用。
	•	ライセンス等の法的配慮を忘れずに。

⸻

Happy clipping! 🚀

