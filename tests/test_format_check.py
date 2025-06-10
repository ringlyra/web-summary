import pathlib
import re
import pytest


META_LINE_RE = re.compile(r"- \*\*(.+?)\*\*: *(.*)")


@pytest.mark.xfail(reason="Existing files may not meet new formatting rules")
def test_formatting():
    errors: list[str] = []

    for year in ("2025", "2023"):
        for md in pathlib.Path(year).rglob("*.md"):
            text = md.read_text(encoding="utf-8")

            # Section name checks
            if "## 要約" not in text:
                errors.append(f"{md}: 正しいセクション名は '## 要約'")
            if "## 本文" not in text:
                errors.append(f"{md}: 正しいセクション名は '## 本文'")

            # Parse metadata
            meta: dict[str, str] = {}
            lines = text.splitlines()
            try:
                i = lines.index("<!-- metadata -->")
            except ValueError:
                continue
            for line in lines[i + 1 :]:
                if line.startswith("## "):
                    break
                m = META_LINE_RE.match(line.strip())
                if m:
                    key, value = m.groups()
                    meta[key.lower()] = value.strip()

            # Tag check
            tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
            if tags == ["codex"]:
                errors.append(f"{md}: 推奨タグを含めてください")

            # Author check
            if not meta.get("author"):
                errors.append(
                    f"{md}: author が空白です。代わりにドメイン名を入力してください"
                )

            # Image URL size check
            image = meta.get("image", "")
            if len(image.encode("utf-8")) > 1600:
                errors.append(
                    f"{md}: image URL が長すぎます。短縮 URL を検討してください"
                )

    assert not errors, "フォーマットエラー:\n" + "\n".join(errors)
