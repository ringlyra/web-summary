import pathlib
import re

GIF_RE = re.compile(
    r"!\[[^\]]*]\((https://[^)]+\.gif(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)
PAREN_GIF_RE = re.compile(
    r"\(([^)]+\.gif(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)

SUMMARY_DIR = pathlib.Path("Summary")


def test_gif_links():
    """
    Summary/ 配下の .md ファイルについて
    - https:// で始まる
    - 同じ行に ![任意](URL) 形式で書かれている
    という 2 条件をgifリンクに対してチェックする
    """
    errors: list[str] = []

    for md in SUMMARY_DIR.rglob("*.md"):
        lines = md.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            good_urls = {m.group(1) for m in GIF_RE.finditer(line)}
            for m in PAREN_GIF_RE.finditer(line):
                url = m.group(1)
                if not url.startswith("https://"):
                    errors.append(f"{md}:{lineno}: https ではない → {url}")
                if url not in good_urls:
                    errors.append(f"{md}:{lineno}: ![...](url) 形式ではない → {url}")

    assert not errors, "GIFリンクのフォーマットエラー:\n" + "\n".join(errors)
