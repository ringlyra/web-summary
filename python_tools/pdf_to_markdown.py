#!/usr/bin/env python3
"""
Usage:
    python pdf_to_markdown.py <pdf_url> <output_md>
Requirements:
    pip install "markitdown[pdf]" requests
"""
import sys
from pathlib import Path
import requests
from markitdown import MarkItDown


def download_pdf(url: str, tmp_path: Path) -> None:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/113.0 Safari/537.36"
        ),
        "Referer": url,
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    tmp_path.write_bytes(r.content)


def pdf_to_markdown(pdf_path: Path) -> str:
    md = MarkItDown()                # core オブジェクトを生成
    result = md.convert(str(pdf_path))  # ファイルパスを渡して変換
    return result.text_content          # Markdown 文字列を取得


def main(url: str, out_file: Path) -> None:
    pdf_path = out_file.with_suffix(".pdf")

    # 1. PDF をダウンロード
    download_pdf(url, pdf_path)

    # 2. Markdown へ変換
    markdown_text = pdf_to_markdown(pdf_path)

    # 3. 保存（UTF-8）
    out_file.write_text(markdown_text, encoding="utf-8")

    print(f"✔  Saved Markdown to: {out_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pdf_to_markdown.py <pdf_url> <output_md>")
        sys.exit(1)

    url_arg = sys.argv[1]
    out_path = Path(sys.argv[2])
    main(url_arg, out_path)
