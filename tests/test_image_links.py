import pathlib
import re

# 対応画像拡張子を必要に応じて追加してください
IMG_EXT = r"png|jpe?g|gif|webp|svg"

INLINE_IMG_RE = re.compile(
    rf'!\[[^\]]*]\((https://[^)]+\.({IMG_EXT})(?:\?[^)]*)?)\)',
    flags=re.IGNORECASE,
)

PAREN_IMG_RE = re.compile(
    rf'\(([^)]+\.({IMG_EXT})(?:\?[^)]*)?)\)',
    flags=re.IGNORECASE,
)


def test_image_links():
    """
    画像リンクが https:// かつ行内 ![](URL) であることを検証。
    alt テキストはあってもなくても OK。
    """
    md_files = pathlib.Path("2025").rglob("*.md")
    errors: list[str] = []

    for md in md_files:
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            good_urls = {m.group(1) for m in INLINE_IMG_RE.finditer(line)}

            for m in PAREN_IMG_RE.finditer(line):
                url = m.group(1)

                if not url.startswith("https://"):
                    errors.append(f"{md}:{lineno}:非 https URL → {url}")

                if url not in good_urls:
                    errors.append(f"{md}:{lineno}:![](url) 形式で書かれていない → {url}")

    assert not errors, "Image link errors:\n" + "\n".join(errors)