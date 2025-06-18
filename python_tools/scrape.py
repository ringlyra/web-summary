import sys
import os
import json
from urllib.parse import urlparse
from datetime import datetime, timezone

import requests
import re

from bs4 import BeautifulSoup, Tag
from readability import Document
from markdownify import markdownify as md

url = sys.argv[1]
parsed_url = urlparse(url)

SUMMARY_PLACEHOLDER = "<日本語の要約を書く>"

# 環境変数 SUMMARY があればそちらを採用する
SUMMARY_TEXT = os.environ.get("SUMMARY", SUMMARY_PLACEHOLDER)

# Initialize variables for type checkers
html: str | None = None
title: str = ""
published: str = ""
content_md: str = ""
authors: list[str] = []
image: str = ""
soup: BeautifulSoup | None = None


def parse_rjina_text(text):
    lines = text.splitlines()
    t = (
        lines[0].split(":", 1)[1].strip()
        if lines and lines[0].startswith("Title:")
        else ""
    )
    published = ""
    for line in lines:
        if line.startswith("Published Time:"):
            published = line.split(":", 1)[1].strip()
            break
    try:
        idx = lines.index("Markdown Content:")
        content = "\n".join(lines[idx + 1 :])
    except ValueError:
        content = text
    return t, published, content


if parsed_url.hostname == "help.openai.com":
    proxy_url = f"https://r.jina.ai/{url}"
    r = requests.get(proxy_url, timeout=120)
    r.raise_for_status()
    title, published, content_md = parse_rjina_text(r.text)
    authors = [parsed_url.hostname]
    image = ""
    html = None
else:
    r = requests.get(url, timeout=120)
    use_proxy = (
        r.status_code >= 400
        or "Your request has been blocked" in r.text
        or "Access Denied" in r.text
    )
    if use_proxy:
        proxy_url = f"https://r.jina.ai/{url}"
        r = requests.get(proxy_url, timeout=120)
    r.raise_for_status()
    if use_proxy:
        title, published, content_md = parse_rjina_text(r.text)
        authors = [parsed_url.hostname or ""]
        image = ""
        html = None
    else:
        html = r.text

if html is not None:
    soup = BeautifulSoup(html, "html.parser")
    assert soup is not None

    def get_meta(s: BeautifulSoup, prop: str) -> str:
        tag = s.find("meta", attrs={"property": prop}) or s.find(
            "meta", attrs={"name": prop}
        )
        if isinstance(tag, Tag) and tag.get("content"):
            return str(tag["content"])
        return ""

    title = (
        get_meta(soup, "og:title")
        or get_meta(soup, "citation_title")
        or (soup.title.string.strip() if soup.title and soup.title.string else "")
    )
    author_tags = soup.find_all("meta", attrs={"name": "citation_author"})
    if author_tags:
        authors = [str(a["content"]) for a in author_tags if isinstance(a, Tag)]
    else:
        author_tag = soup.find("meta", attrs={"name": "author"})
        if isinstance(author_tag, Tag):
            authors = [str(author_tag["content"])]
        else:
            authors = [urlparse(url).hostname or ""]
    published = (
        get_meta(soup, "article:published_time")
        or get_meta(soup, "citation_date")
        or get_meta(soup, "citation_publication_date")
    )

    if not published:
        for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                if not isinstance(script, Tag) or not script.string:
                    continue
                data = json.loads(script.string)
            except Exception:
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if isinstance(item, dict) and item.get("datePublished"):
                    published = item["datePublished"]
                    break
            if published:
                break

    if not published:
        entry_footer = soup.find("div", class_="entryFooter")
        if entry_footer:
            text = entry_footer.get_text(" ")
            m = re.search(r"(\d{1,2})(?:st|nd|rd|th) (\w+) (\d{4})", text)
            t = re.search(r"(\d+:\d+) ?(am|pm)", text, re.I)
            if m:
                day, month_name, year = m.groups()
                if t:
                    time_str = f"{t.group(1)} {t.group(2)}"
                    try:
                        dt = datetime.strptime(
                            f"{day} {month_name} {year} {time_str}", "%d %B %Y %I:%M %p"
                        )
                    except Exception:
                        dt = datetime.strptime(f"{day} {month_name} {year}", "%d %B %Y")
                else:
                    dt = datetime.strptime(f"{day} {month_name} {year}", "%d %B %Y")
                published = dt.replace(tzinfo=timezone.utc).isoformat()
    if not published:
        date_div = soup.find("div", class_="ltx_dates")
        if isinstance(date_div, Tag):
            text = date_div.get_text(strip=True).strip("()")
            try:
                dt = datetime.strptime(text, "%b %d, %Y")
                published = dt.replace(tzinfo=timezone.utc).isoformat()
            except Exception:
                pass
    image = get_meta(soup, "og:image")
fetched = datetime.now(timezone.utc).isoformat()
source = url

parsed = urlparse(url)


def extract_domain(parsed_url):
    """Return host including subdomain but without port."""
    host = parsed_url.netloc.split("@")[-1]
    host = host.split(":")[0]
    return host.lower()


domain = extract_domain(parsed)
path_segments = parsed.path.strip("/").split("/")
if "content_md" not in locals():
    content_md = ""
if domain == "github.com" and len(path_segments) == 2:
    user, repo = path_segments
    for branch in ["master", "main"]:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/README.md"
        r = requests.get(raw_url)
        if r.status_code == 200:
            content_md = r.text
            break

if html is not None and not content_md:
    assert soup is not None
    article_tag = soup.find(
        "article", attrs={"class": re.compile("post|article", re.I)}
    )
    if isinstance(article_tag, Tag) and len(article_tag.get_text(strip=True)) > 200:
        content_html = article_tag.decode_contents()
    else:
        article = Document(html)
        content_html = article.summary()

    content_soup = BeautifulSoup(content_html, "html.parser")

    # convert relative URLs to absolute for images, links and video sources
    for tag in content_soup.find_all(["img", "a", "source"]):
        if not isinstance(tag, Tag):
            continue
        attr = "href" if tag.name == "a" else "src"
        url_val = tag.get(attr)
        if isinstance(url_val, str) and url_val.startswith("/"):
            tag[attr] = f"https://{parsed.netloc}{url_val}"

    # arXiv uses spans for bullet symbols and bold text, which break markdownify
    if parsed.netloc.endswith("arxiv.org"):
        for span in content_soup.select("span.ltx_tag_item"):
            if span.string and "\u2022" in span.string:
                span.decompose()
        for bold in content_soup.select("span.ltx_font_bold"):
            bold.name = "strong"
            bold.attrs = {}

    content_html = str(content_soup)

    content_md = md(content_html)

# filename from url slug instead of title
slug = os.path.basename(parsed.path.strip("/")) or "index"
file_title = re.sub(r"[^a-zA-Z0-9_-]+", "-", slug).strip("-")
# ensure path
if published:
    dt = None
    for fmt in (
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%b %d, %Y",
        "%B %d, %Y",
        "%d %b %Y",
        "%d %B %Y",
    ):
        try:
            dt = datetime.strptime(
                published.split()[0] if fmt.startswith("%Y") else published, fmt
            )
            break
        except Exception:
            continue
    if dt is None:
        published_date = published[:10].replace("/", "-")
    else:
        dt = dt.replace(tzinfo=timezone.utc)
        published_date = dt.strftime("%Y-%m-%d")
        published = dt.isoformat()
else:
    dt = datetime.now(timezone.utc)
    published_date = dt.strftime("%Y-%m-%d")
year, month, _ = published_date.split("-")
path = os.path.join("Summary", year, month, domain)
os.makedirs(path, exist_ok=True)
filename = f"{published_date}_{file_title}.md"
filepath = os.path.join(path, filename)

with open(filepath, "w") as f:
    f.write("---\n")
    f.write(f"title: {title!r}\n")
    f.write(f"source: {source}\n")
    f.write("author:\n")
    for a in authors:
        f.write(f"  - {a}\n")
    f.write(f"published: {published!r}\n")
    f.write(f"fetched: {fetched!r}\n")
    f.write("tags:\n")
    f.write("  - codex\n")
    domain_tag = domain.split(".")[-2] if "." in domain else domain
    if domain_tag != "codex":
        f.write(f"  - {domain_tag}\n")
    f.write(f"image: {image}\n")
    f.write("---\n\n")
    f.write("## 要約\n\n")
    summary_md = SUMMARY_TEXT
    f.write(summary_md + "\n\n")
    f.write("## 本文\n\n")
    f.write(content_md)

print(filepath)
