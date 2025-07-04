# リポジトリ要約：URL Scraping Agent

## 概要

このリポジトリは **URLを受け取り、ウェブページから「メタデータ」「要約」「本文 (Markdown)」を抽出し、統一フォーマットでMarkdownファイルに保存する日本語対応ウェブスクレイピングエージェント** です。

## 主要機能

### 🔧 コア機能
- **ウェブページスクレイピング**: `python_tools/scrape.py`
  - HTML→Markdown変換
  - メタデータ自動抽出（OGP、タイトル、著者、公開日時）
  - プロキシによる自動フォールバック対応
  - readability-lxml を使用したクリーンなコンテンツ抽出

- **PDF論文処理**: `python_tools/fetch_paper.py`
  - arXivからのPDF自動取得
  - DOI対応
  - PDF→テキスト変換
  - arXiv APIからのメタデータ取得

### 📁 出力フォーマット
```
Summary/
└── YYYY/
    └── MM/
        └── domain.com/
            └── YYYY-MM-DD_title.md
```

各ファイルは以下の構造：
- **YAMLフロントマター**: title, source, author, published, fetched, tags, image
- **日本語要約**: 300-350文字
- **本文**: Markdown形式

### 🏗️ 技術構成

**依存関係** (`pyproject.toml`):
- beautifulsoup4 - HTMLパース
- markdownify - HTML→Markdown変換 
- PyPDF2 - PDF処理
- readability-lxml - コンテンツ抽出
- requests - HTTP通信
- PyYAML - メタデータ処理

**開発環境**:
- uv - パッケージ管理
- pre-commit - コード品質管理
- ruff, black, pyright - コードフォーマッティング

## アクティビティ状況

### 📊 処理済みサイト数（2025年6月時点）
60+の多様なドメインから継続的にコンテンツを収集：

**主要対象サイト**:
- **AI/ML**: openai.com, anthropic.com, huggingface.co, research.google
- **技術ブログ**: zenn.dev, qiita.com, dev.classmethod.jp
- **学術**: arxiv.org
- **企業**: github.com, microsoft.com, nvidia.com, apple.com
- **個人ブログ**: simonwillison.net など多数

### 🧪 テスト・品質管理
`tests/` ディレクトリに包括的なテストスイート：
- 効率性テスト
- フォーマット検証
- 画像リンク対応
- ドメイン別フォルダ管理

**パフォーマンス最適化**（`tests/EFFICIENCY_REPORT.md`）:
- HTTP リクエスト最適化で処理時間15-25%改善
- BeautifulSoup オブジェクト重複作成の修正
- 将来的な最適化で60%の性能向上見込み

## 設計思想

### 🎯 主要目標
1. **再現性 & 検索性**: 統一フォーマットでの機械的再利用
2. **最小限の加工**: 元HTML→Markdown変換と解釈の明確分離
3. **タグ駆動**: `codex`タグによるクエリー・フィルタ対応

### 🔄 処理フロー
1. URL受信
2. HTTP GET（必要に応じてプロキシ経由）
3. メタデータ・OGP・日付抽出
4. 本文HTML→Markdown変換
5. 統一フォーマットでファイル生成
6. 自動Git commit

### 📋 特徴的な機能
- **プロキシ自動フォールバック**: ブロック時にr.jina.ai経由
- **多様な日付形式対応**: ISO 8601, JSON-LD, カスタムパターン
- **相対URL自動変換**: 絶対URLに統一
- **arXiv特化処理**: PDF直接取得とAPIメタデータ連携
- **GitHub README対応**: master/main分岐自動検出

## 使用方法

```bash
# ウェブページ処理
python python_tools/scrape.py <URL>

# PDF論文処理  
python python_tools/fetch_paper.py <DOI> <output_dir>
```

## 今後の展望

効率化レポートに基づく改善計画：
- BeautifulSoup最適化（20-30%メモリ削減）
- 並行処理によるGitHub分岐確認
- キャッシュ機能追加（60-80%冗長リクエスト削減）

---

このエージェントは **日本語での技術情報収集・蓄積に特化した実用的なツール** として、継続的な改善とアクティブな利用が行われています。