import pathlib
import re

# ── 拡張子定義 ──────────────────────────────────────────────
VIDEO_EXT = r"(?:mp4|mov)"  # 動画
POSTER_EXT = r"(?:png|jpe?g|gif|webp|svg)"  # サムネイル画像

# ── 正しい動画リンク構文： [![alt](poster)](https://...video.mp4|mov)
CORRECT_VIDEO_LINK_RE = re.compile(
    rf"""\[!\[[^\]]*]\(      # [![alt](
          [^)]+\.{POSTER_EXT} #   poster 画像 URL
          (?:\?[^)]*)?        #   ?query を許容
        \)\]                  # )]
        \(
          (https://[^)]+\.{VIDEO_EXT}(?:\?[^)]*)?)  # ←★キャプチャ: 動画 URL
        \)""",
    flags=re.IGNORECASE | re.VERBOSE,
)

# ── 動画 URL を含む丸かっこ ( https://... .mp4|mov )
PAREN_VIDEO_RE = re.compile(
    rf"\(([^)]+\.{VIDEO_EXT}(?:\?[^)]*)?)\)",
    flags=re.IGNORECASE,
)

SUMMARY_DIR = pathlib.Path("Summary")  # ここだけ指定すれば OK


def test_video_links():
    """
    Summary/ 配下の .md ファイルについて
    1. 動画 URL は https:// で始まる
    2. 行内に [![alt](poster)](動画) 形式で書かれている
    の両方を満たしているかを検証する (対象拡張子は mp4, mov)
    """
    errors: list[str] = []

    # Summary 以下を再帰的に検索
    for md in SUMMARY_DIR.rglob("*.md"):
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            # その行に存在する「正しい動画 URL」を収集
            correct_urls = {m.group(1) for m in CORRECT_VIDEO_LINK_RE.finditer(line)}

            # 丸かっこ内の動画 URL を列挙し、違反がないか確認
            for m in PAREN_VIDEO_RE.finditer(line):
                url = m.group(1)

                if not url.startswith("https://"):
                    errors.append(f"{md}:{lineno}: https ではない → {url}")
                elif url not in correct_urls:
                    errors.append(
                        f"{md}:{lineno}: [![alt](poster)](url) 形式ではない → {url}"
                    )

    assert not errors, "動画リンクのフォーマットエラー:\n" + "\n".join(errors)
