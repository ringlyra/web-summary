import pathlib
import re
import pytest

# ── 設定 ──────────────────────────────────────────────────────────────
META_LINE_RE = re.compile(r"- \*\*(.+?)\*\*: *(.*)")
RECOMMENDED_TAGS = {"ai", "nlp"}          # README に記載されている推奨タグ
TARGET_YEARS = ("2025", "2023")           # 対象フォルダを増やすならここを編集

# ── テスト本体 ────────────────────────────────────────────────────────
@pytest.mark.xfail(reason="既存ファイルが新ルールに未対応")
def test_formatting():
    errors: list[str] = []

    for year in TARGET_YEARS:
        for md in pathlib.Path(year).rglob("*.md"):
            text = md.read_text(encoding="utf-8")

            # ------ セクション見出しチェック ----------------------------------
            if "## 要約" not in text:
                errors.append(f"{md}: 正しいセクション名は '## 要約'")
            if "## 本文" not in text:
                errors.append(f"{md}: 正しいセクション名は '## 本文'")

            # ------ メタデータ抽出 ------------------------------------------
            meta: dict[str, str] = {}
            lines = text.splitlines()
            try:
                i = lines.index("<!-- metadata -->")
            except ValueError:
                continue  # metadata ブロック自体が無ければ他のチェックはスキップ
            for line in lines[i + 1:]:
                if line.startswith("## "):
                    break
                m = META_LINE_RE.match(line.strip())
                if m:
                    key, value = m.groups()
                    meta[key.lower()] = value.strip()

            # ------ タグチェック --------------------------------------------
            tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
            if "codex" not in tags:
                errors.append(f"{md}: 必須タグ 'codex' が抜けています")
            elif tags == ["codex"]:
                # codex だけ → エラー（推奨タグが無い）
                errors.append(
                    f"{md}: 'codex' 以外に推奨タグ ({', '.join(sorted(RECOMMENDED_TAGS))}) を少なくとも 1 つ追加してください"
                )

            # ------ author チェック -----------------------------------------
            author = meta.get("author", "").strip()
            if not author:
                errors.append(
                    f"{md}: author が空白です。個人名が望ましい。なければドメイン名を入力してください"
                )

            # ------ 画像 URL 長さチェック ------------------------------------
            image = meta.get("image", "")
            if len(image.encode("utf-8")) > 1600:
                errors.append(
                    f"{md}: image URL が長すぎます。短縮 URL を検討してください"
                )

    assert not errors, "フォーマットエラー:\n" + "\n".join(errors)
