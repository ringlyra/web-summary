import pathlib
import re

# ── ① 正しい inline 形式: ![](https://...mp4|mov|m3u8)
INLINE_VIDEO_RE = re.compile(
    r'!\[\]\((https://[^)]+\.(?:mp4|mov|m3u8)(?:\?[^)]*)?)\)',
    flags=re.IGNORECASE,
)

# ── ② かっこだけ検出: (https://...mp4|mov|m3u8)
PAREN_VIDEO_RE = re.compile(
    r'\(([^)]+\.(?:mp4|mov|m3u8)(?:\?[^)]*)?)\)',
    flags=re.IGNORECASE,
)


def test_video_links():
    """
    2025/ 以下の .md に含まれる動画リンクが
    1) https:// で始まり
    2) 行内で ![](URL) 形式になっているか
    を検証します。
    """
    md_files = pathlib.Path("2025").rglob("*.md")
    errors: list[str] = []

    for md in md_files:
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            good_urls = {m.group(1) for m in INLINE_VIDEO_RE.finditer(line)}

            for m in PAREN_VIDEO_RE.finditer(line):
                url = m.group(1)

                if not url.startswith("https://"):
                    errors.append(f"{md}:{lineno}:非 https URL → {url}")

                if url not in good_urls:
                    errors.append(f"{md}:{lineno}:![](url) 形式で書かれていない → {url}")

    assert not errors, "Video link errors:\n" + "\n".join(errors)