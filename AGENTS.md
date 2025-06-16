# ルール

- AGENTS.md と README.md を参照すること。
- スクレイピングする時は python_tools/scrape.py, pdf を処理する時は python_tools/fetch_paper.py を使用してコード不具合があれば改善し更新すること。  
- uv を使って環境構築されています。pip を使用しないでください。以下のコマンドを使ってインストールしています。

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv run pre-commit install
  ```
  
- 以下の依存環境が既にインストールされています。
  - beautifulsoup4
  - markdownify
  - PyPDF2
  - readability-lxml
  - requests
  - pre-commit
