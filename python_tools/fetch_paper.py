#!/usr/bin/env python3
"""
usage: python fetch_paper.py <doi> <output_dir>

例:
    python fetch_paper.py 10.48550/arXiv.2207.03928 ./papers
"""

import sys
import os
from pathlib import Path
from typing import Optional
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

import re
import requests
from PyPDF2 import PdfReader
import json

SUMMARY_PLACEHOLDER = "<日本語の要約を書く>"

# 環境変数 SUMMARY があればそちらを採用する
SUMMARY_TEXT = os.environ.get("SUMMARY", SUMMARY_PLACEHOLDER)


def clean_text(raw_text: str) -> str:
    """Remove spurious line breaks and hyphenation."""
    lines = raw_text.splitlines()
    filtered: list[str] = []
    for line in lines:
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            filtered.append("")
            continue
        if line.startswith("arXiv:"):
            continue
        if len(line) <= 3 and line.isdigit():
            continue
        filtered.append(line)

    joined: list[str] = []
    for line in filtered:
        if joined and joined[-1].endswith("-") and line:
            # Keep hyphen when next line also contains a hyphen near the start
            if "-" in line[:5]:
                joined[-1] = joined[-1] + line.lstrip()
            elif line[0].islower():
                joined[-1] = joined[-1][:-1] + line.lstrip()
            else:
                joined[-1] = joined[-1][:-1] + line.lstrip()
            continue
        joined.append(line.rstrip())

    result: list[str] = []
    for line in joined:
        s = line.strip()
        if not s:
            if result and result[-1]:
                result.append("")
            continue
        if result and result[-1]:
            last = result[-1]
            if not last.endswith((".", "!", "?", ":")):
                if last and last[-1].isalnum() and s[0].islower():
                    result[-1] += s
                else:
                    result[-1] += " " + s
            else:
                result.append(s)
        else:
            result.append(s)
    return "\n".join(result)


def extract_text(pdf_path: Path) -> str:
    """Extract and clean text from PDF."""
    reader = PdfReader(str(pdf_path))
    raw = "\n".join(page.extract_text() or "" for page in reader.pages)
    return clean_text(raw)


def safe_filename(doi: str) -> str:
    """DOI をファイル名に安全変換"""
    return doi.replace("/", "_").replace(":", "_")


def fetch_arxiv_meta(paper_id: str) -> dict:
    """Fetch metadata from arXiv API.

    The HTTPS endpoint occasionally fails in the container environment,
    so fall back to HTTP if necessary.
    """
    api_https = f"https://export.arxiv.org/api/query?search_query=id:{paper_id}"
    try:
        r = requests.get(api_https, timeout=120)
        r.raise_for_status()
    except Exception:
        api_http = api_https.replace("https://", "http://")
        r = requests.get(api_http, timeout=120)
        r.raise_for_status()

    root = ET.fromstring(r.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)
    if entry is None:
        return {}
    title = entry.findtext("atom:title", default="", namespaces=ns).strip()
    published = entry.findtext("atom:published", default="", namespaces=ns)
    summary = entry.findtext("atom:summary", default="", namespaces=ns).strip()
    authors = [
        a.findtext("atom:name", default="", namespaces=ns)
        for a in entry.findall("atom:author", ns)
    ]
    return {
        "title": title,
        "published": published,
        "summary": summary,
        "author": [a for a in authors if a],
    }


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

    paper_id: str | None = None

    # --- 1. PDF を取得 ----------------------------------------------
    try:
        if doi.startswith("10.48550/arXiv."):
            paper_id = doi.split("arXiv.")[-1]
            pdf_url = f"https://arxiv.org/pdf/{paper_id}"
        elif doi.lower().startswith("http"):
            pdf_url = doi
            if "arxiv.org/pdf/" in pdf_url:
                paper_id = pdf_url.rsplit("/", 1)[-1].replace(".pdf", "")
        else:
            pdf_url = f"https://doi.org/{doi}"
        r = requests.get(pdf_url, timeout=120)
        r.raise_for_status()
        pdf_path.write_bytes(r.content)
    except Exception as e:
        print(f"[Error] PDF 取得失敗: {e}")
        return None

    # --- 2. PDF → TXT ---------------------------------------------
    try:
        txt_path.write_text(extract_text(pdf_path), encoding="utf-8")
    except Exception as e:
        print(f"[Warning] テキスト抽出失敗 (続行): {e}")

    # --- 3. Markdown 生成 -------------------------------------------
    md_path = base.with_suffix(".md")
    meta = {}
    if paper_id:
        try:
            meta = fetch_arxiv_meta(paper_id)
        except Exception as e:
            print(f"[Warning] メタデータ取得失敗: {e}")
    if meta:
        try:
            json_path.write_text(
                json.dumps(meta, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except Exception as e:
            print(f"[Warning] JSON 保存失敗: {e}")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: {meta.get('title', '')!r}\n")
        f.write(f"source: {pdf_url}\n")
        f.write("author:\n")
        for a in meta.get("author", ["arxiv.org"]):
            f.write(f"  - {a}\n")
        f.write(f"published: '{meta.get('published', '')}'\n")
        f.write(f"fetched: '{datetime.now(timezone.utc).isoformat()}'\n")
        f.write("tags:\n  - codex\n  - arxiv\n")
        f.write("image: \n")
        f.write("---\n\n")
        f.write("## 要約\n\n")
        summary_md = SUMMARY_TEXT
        f.write(summary_md + "\n\n")
        f.write("## 本文\n\n")
        f.write(txt_path.read_text(encoding="utf-8"))

    # rename Markdown file to normalized name
    title_slug = (
        re.sub(r"[^a-zA-Z0-9_-]+", "-", meta.get("title", "paper").lower()).strip("-")
        or "paper"
    )
    if meta.get("published"):
        pub_date = meta["published"][:10].replace("/", "-")
    else:
        pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_md = md_path.with_name(f"{pub_date}_{title_slug}.md")
    md_path.rename(new_md)
    md_path = new_md

    print(f"PDF  : {pdf_path}")
    print(f"TXT  : {txt_path}")
    print(f"MD   : {md_path}")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: fetch_paper.py <doi> <output_dir>")

    doi_arg, out_dir_arg = sys.argv[1], Path(sys.argv[2])
    fetch_paper(doi_arg, out_dir_arg)
