#!/usr/bin/env python3
"""
usage: python fetch_paper.py <doi> <output_dir>

例:
    python fetch_paper.py 10.48550/arXiv.2207.03928 ./papers
"""

import sys
from pathlib import Path
from typing import Optional

from paperscraper.pdf import save_pdf           # paperscraper 標準 API
from PyPDF2 import PdfReader                     # テキスト抽出用


def extract_text(pdf_path: Path) -> str:
    """PDF → 文字列（PyPDF2 で各ページ抽出）"""
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def safe_filename(doi: str) -> str:
    """DOI をファイル名に安全変換"""
    return doi.replace("/", "_").replace(":", "_")


def fetch_paper(doi: str, out_dir: Path) -> Optional[Path]:
    """
    DOI から PDF とメタデータ(JSON) を取得し、
    PDF→TXT も生成してパスを返す。
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    base = out_dir / safe_filename(doi)
    pdf_path = base.with_suffix(".pdf")
    json_path = base.with_suffix(".json")
    txt_path = base.with_suffix(".txt")

    # --- 1. PDF & メタデータを取得 ----------------------------------
    try:
        # save_metadata=True なら <ファイル名>.json が自動保存される
        save_pdf({"doi": doi}, filepath=str(pdf_path), save_metadata=True)
    except Exception as e:
        print(f"[Error] PDF 取得失敗: {e}")
        return None

    # --- 2. PDF → TXT ---------------------------------------------
    try:
        txt_path.write_text(extract_text(pdf_path), encoding="utf-8")
    except Exception as e:
        print(f"[Warning] テキスト抽出失敗 (続行): {e}")

    print(f"PDF  : {pdf_path.relative_to(Path.cwd())}")
    print(f"JSON : {json_path.relative_to(Path.cwd())}")
    print(f"TXT  : {txt_path.relative_to(Path.cwd())}")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: fetch_paper.py <doi> <output_dir>")

    doi_arg, out_dir_arg = sys.argv[1], Path(sys.argv[2])
    fetch_paper(doi_arg, out_dir_arg)
