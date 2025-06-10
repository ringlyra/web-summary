import pathlib
import re

# 対応拡張子（動画）
VIDEO_EXT = r"(?:mp4|mov|m3u8)"

# ![任意の alt](https://… .mp4|mov|m3u8)
INLINE_VIDEO_RE = re.compile(
    rf"!\[[^\]]*]\((https://[^)]+\.{VIDEO_EXT}(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)

# (https://… .mp4|mov|m3u8) ― alt 有無は問わない
PAREN_VIDEO_RE = re.compile(
    rf"\(([^)]+\.{VIDEO_EXT}(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)


def test_video_links():
    """
    - https:// で始まる
    - 同じ行に ![任意](URL) 形式で書かれている
    という 2 条件を動画リンクに対してチェックする
    """
    errors: list[str] = []

    for md in pathlib.Path("2025").rglob("*.md"):
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            good_urls = {m.group(1) for m in INLINE_VIDEO_RE.finditer(line)}

            for m in PAREN_VIDEO_RE.finditer(line):
                url = m.group(1)

                if not url.startswith("https://"):
                    errors.append(
                        f"{md}:{lineno}: https ではない → {url}"
                    )
                if url not in good_urls:
                    errors.append(
                        f"{md}:{lineno}: ![...](url) 形式ではない → {url}"
                    )

    assert not errors, "動画リンクのフォーマットエラー:\n" + "\n".join(errors)