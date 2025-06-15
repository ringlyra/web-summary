import pathlib
import yaml
import pytest

# ── 設定 ──────────────────────────────────────────────────────────────
SUMMARY_DIR = pathlib.Path("Summary")  # ここだけ指定すれば OK
MAX_IMAGE_BYTES = 1600  # image URL 長さの上限

# ── テスト本体 ────────────────────────────────────────────────────────
def test_formatting():
    errors: list[str] = []

    # Summary 配下をすべて対象にする
    for md in SUMMARY_DIR.rglob("*.md"):
        text  = md.read_text(encoding="utf-8")
        lines = text.splitlines()

        # ------ セクション見出しチェック ------------------------------
        body_lines = [l.strip() for l in lines if l.strip().startswith("## 本文")]
        if not body_lines:
            errors.append(f"{md}: 正しいセクション名は '## 本文'")
        else:
            for l in body_lines:
                if l != "## 本文":
                    errors.append(f"{md}: '## 本文' の行に余計な文字があります: '{l}'")

        summary_lines = [l.strip() for l in lines if l.strip().startswith("## 要約")]
        if not summary_lines:
            errors.append(f"{md}: 正しいセクション名は '## 要約'")
        else:
            for l in summary_lines:
                if l != "## 要約":
                    errors.append(f"{md}: '## 要約' の行に余計な文字があります: '{l}'")

        # ------ メタデータ抽出 --------------------------------------
        meta: dict[str, str] = {}
        try:
            start = lines.index("---")
            end = lines.index("---", start + 1)
        except ValueError:
            errors.append(f"{md}: YAML メタデータブロックがありません")
            continue
        yaml_text = "\n".join(lines[start + 1 : end])
        try:
            meta = yaml.load(yaml_text, Loader=yaml.BaseLoader) or {}
        except Exception as e:
            errors.append(f"{md}: YAML パースエラー: {e}")
            continue

        # ------ タグチェック ----------------------------------------
        tags_field = meta.get("tags", [])
        if isinstance(tags_field, str):
            tags = [t.strip() for t in tags_field.split(",") if t.strip()]
        elif isinstance(tags_field, list):
            tags = [str(t).strip() for t in tags_field if str(t).strip()]
        else:
            tags = []
        if "codex" not in tags:
            errors.append(f"{md}: 必須タグ 'codex' が抜けています")
        elif tags == ["codex"]:
            errors.append(f"{md}: 'codex' 以外に関連タグを少なくとも 1 つ追加してください。どんなタグが適切か考えてみてください")

        # ------ image URL 長さチェック ------------------------------
        image = meta.get("image", "")
        if image and len(image.encode("utf-8")) > MAX_IMAGE_BYTES:
            errors.append(f"{md}: image URL が {MAX_IMAGE_BYTES} バイトを超えています。`image:` フィールドを空にしてください")

    # 1 件でもあれば失敗
    assert not errors, "フォーマットエラー:\n" + "\n".join(errors)
