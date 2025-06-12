import pathlib
import re

# 対応拡張子（画像）必要に応じて追加
IMG_EXT = r"(?:png|jpe?g|gif|webp|svg)"

INLINE_IMG_RE = re.compile(
    rf"!\[[^\]]*]\((https://[^)]+\.{IMG_EXT}(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)

PAREN_IMG_RE = re.compile(
    rf"\(([^)]+\.{IMG_EXT}(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)

SUMMARY_DIR = pathlib.Path("Summary")  # ここだけ指定すれば OK


def test_image_links():
    """
    Summary/ 配下の .md ファイルについて
    - https:// で始まる
    - 同じ行に ![任意](URL) 形式で書かれている
    という 2 条件を画像リンクに対してチェックする
    """
    errors: list[str] = []

    for md in SUMMARY_DIR.rglob("*.md"):
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            good_urls = {m.group(1) for m in INLINE_IMG_RE.finditer(line)}

            for m in PAREN_IMG_RE.finditer(line):
                url = m.group(1)

                if not url.startswith("https://"):
                    errors.append(f"{md}:{lineno}: https ではない → {url}")
                if url not in good_urls:
                    errors.append(f"{md}:{lineno}: ![...](url) 形式ではない → {url}")

    assert not errors, "画像リンクのフォーマットエラー:\n" + "\n".join(errors)
