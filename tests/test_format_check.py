import pathlib
import re
import pytest

# ── 設定 ──────────────────────────────────────────────────────────────
META_LINE_RE = re.compile(r"- \*\*(.+?)\*\*: *(.*)")
TARGET_YEARS = ("2025", "2023")           # 対象フォルダ
MAX_IMAGE_BYTES = 1600                    # image URL 長さの上限

# ── テスト本体 ────────────────────────────────────────────────────────
def test_formatting():
    errors: list[str] = []

    for year in TARGET_YEARS:
        for md in pathlib.Path(year).rglob("*.md"):
            text = md.read_text(encoding="utf-8")
            lines = text.splitlines()

            # ------ セクション見出しチェック ------------------------------
            body_lines = [l.strip() for l in lines if l.strip().startswith("## 本文")]
            if not body_lines:
                errors.append(f"{md}: 正しいセクション名は '## 本文'")
            else:
                for l in body_lines:
                    if l != "## 本文":
                        errors.append(
                            f"{md}: '## 本文' の行に余計な文字があります: '{l}'"
                        )

            summary_lines = [l.strip() for l in lines if l.strip().startswith("## 要約")]
            if not summary_lines:
                errors.append(f"{md}: 正しいセクション名は '## 要約'")
            else:
                for l in summary_lines:
                    if l != "## 要約":
                        errors.append(
                            f"{md}: '## 要約' の行に余計な文字があります: '{l}'"
                        )

            # ------ メタデータ抽出 --------------------------------------
            meta: dict[str, str] = {}
            try:
                i = lines.index("<!-- metadata -->")
            except ValueError:
                errors.append(f"{md}: '<!-- metadata -->' ブロックがありません")
                continue
            for line in lines[i + 1:]:
                if line.startswith("## "):
                    break
                m = META_LINE_RE.match(line.strip())
                if m:
                    key, value = m.groups()
                    meta[key.lower()] = value.strip()

            # ------ タグチェック ----------------------------------------
            tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
            if "codex" not in tags:
                errors.append(f"{md}: 必須タグ 'codex' が抜けています")
            elif tags == ["codex"]:
                errors.append(
                    f"{md}: 'codex' 以外に関連タグを少なくとも 1 つ追加してください。どんなタグが適切か考えてみてください"
                )

            # ------ author チェック -------------------------------------
            author = meta.get("author", "").strip()
            if not author:
                errors.append(
                    f"{md}: author が空白です。個人名が望ましい。なければドメイン名を入力してください"
                )

            # ------ image URL 長さチェック ------------------------------
            image = meta.get("image", "")
            if image and len(image.encode("utf-8")) > MAX_IMAGE_BYTES:
                errors.append(
                    f"{md}: image URL が {MAX_IMAGE_BYTES} バイトを超えています。`image:` フィールドを空にしてください"
                )

    # 1 件でもあれば失敗
    assert not errors, "フォーマットエラー:\n" + "\n".join(errors)
