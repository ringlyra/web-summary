# ルール
- あなたはウェブサイトをクリッピングして要約を作成するエージェントです。 AGENTS.md と README.md の指示に従ってタスクを実行してください。
- README.md を参照し、指示に従うこと。
- スクレイピングする時は python_tools/scrape.py, pdf を処理する時は python_tools/fetch_paper.py を使用し、コードの不具合があれば改善し更新すること。  


# セットアップ スクリプト
## uv インストール
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## toml から依存関係インストール
```
uv pip install --system -r pyproject.toml
```

## pre-commit と uv パッチインストール
```
uv tool install pre-commit --with pre-commit-uv
```

## コーディング用途に
```
uv tool install ruff
uv tool install black
uv tool install pyright
```

## エラー対策に rehash
```
pyenv rehash && hash -r
pre-commit install
```

> **Note**: セットアップ スクリプトは、リポジトリが複製された後に各タスクの開始時に自動的に実行されます。なので再度実行する必要はありません。
