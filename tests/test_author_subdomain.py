import pathlib
from urllib.parse import urlparse
import yaml

SUMMARY_DIR = pathlib.Path("Summary")


def test_author_field():
    errors: list[str] = []

    for md in SUMMARY_DIR.rglob("*.md"):
        lines = md.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("---")
            end = lines.index("---", start + 1)
        except ValueError:
            continue

        meta = yaml.load("\n".join(lines[start + 1 : end]), Loader=yaml.BaseLoader) or {}
        author = str(meta.get("author", "")).strip()
        source = str(meta.get("source", "")).strip()

        if not author:
            errors.append(f"{md}: author が空白です。個人名が望ましい。なければドメイン名を入力してください")
            continue

        if not source:
            continue
        host = urlparse(source).hostname or ""
        if host:
            host_parts = host.split(".")
            if len(host_parts) > 2:
                apex = ".".join(host_parts[-2:])
                if author == apex:
                    errors.append(
                        f"{md}: サブドメインがあるのに省略されています。URLをもう一度確認して正しいドメイン名を入力してください"
                    )

    assert not errors, "author フィールドのエラー:\n" + "\n".join(errors)
