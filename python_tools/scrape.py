import sys
import os
import json
from urllib.parse import urlparse
from datetime import datetime, timezone

import requests
import re

from bs4 import BeautifulSoup
from readability import Document
from markdownify import markdownify as md

url = sys.argv[1]
parsed_url = urlparse(url)

html = None
def parse_rjina_text(text):
    lines = text.splitlines()
    t = lines[0].split(":", 1)[1].strip() if lines and lines[0].startswith("Title:") else ""
    published = ""
    for line in lines:
        if line.startswith("Published Time:"):
            published = line.split(":", 1)[1].strip()
            break
    try:
        idx = lines.index("Markdown Content:")
        content = "\n".join(lines[idx + 1:])
    except ValueError:
        content = text
    return t, published, content

if parsed_url.hostname == "help.openai.com":
    proxy_url = f"https://r.jina.ai/{url}"
    r = requests.get(proxy_url, timeout=120)
    r.raise_for_status()
    title, published, content_md = parse_rjina_text(r.text)
    author = parsed_url.hostname
    image = ""
    html = None
else:
    r = requests.get(url, timeout=120)
    use_proxy = r.status_code >= 400 or "Your request has been blocked" in r.text or "Access Denied" in r.text
    if use_proxy:
        proxy_url = f"https://r.jina.ai/{url}"
        r = requests.get(proxy_url, timeout=120)
    r.raise_for_status()
    if use_proxy:
        title, published, content_md = parse_rjina_text(r.text)
        author = parsed_url.hostname
        image = ""
        html = None
    else:
        html = r.text

if html is not None:
    soup = BeautifulSoup(html, 'html.parser')

    def get_meta(prop):
        tag = soup.find('meta', attrs={'property': prop}) or soup.find('meta', attrs={'name': prop})
        if tag and tag.get('content'):
            return tag['content']
        return ''

    title = (
        get_meta('og:title')
        or get_meta('citation_title')
        or (soup.title.string.strip() if soup.title else '')
    )
    authors = soup.find_all('meta', attrs={'name': 'citation_author'})
    if authors:
        author = ", ".join([a['content'] for a in authors])
    else:
        author_tag = soup.find('meta', attrs={'name':'author'})
        if author_tag:
            author = author_tag['content']
        else:
            author = urlparse(url).hostname
    published = (
        get_meta("article:published_time")
        or get_meta("citation_date")
        or get_meta("citation_publication_date")
    )

    if not published:
        for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
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
                        dt = datetime.strptime(
                            f"{day} {month_name} {year}", "%d %B %Y"
                        )
                else:
                    dt = datetime.strptime(
                        f"{day} {month_name} {year}", "%d %B %Y"
                    )
                published = dt.replace(tzinfo=timezone.utc).isoformat()
    image = get_meta('og:image')
fetched = datetime.now(timezone.utc).isoformat()
source = url

parsed = urlparse(url)
domain = parsed.hostname
path_segments = parsed.path.strip('/').split('/')
if 'content_md' not in locals():
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
    article_tag = soup.find('article', attrs={'class': re.compile('post|article', re.I)})
    if article_tag and len(article_tag.get_text(strip=True)) > 200:
        content_html = article_tag.decode_contents()
    else:
        article = Document(html)
        content_html = article.summary()
    content_md = md(content_html)

# filename from url slug instead of title
import re
slug = os.path.basename(parsed.path.strip('/')) or 'index'
file_title = re.sub(r'[^a-zA-Z0-9_-]+', '-', slug).strip('-')
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
            dt = datetime.strptime(published.split()[0] if fmt.startswith("%Y") else published, fmt)
            break
        except Exception:
            continue
    if dt is None:
        published_date = published[:10].replace('/', '-')
    else:
        dt = dt.replace(tzinfo=timezone.utc)
        published_date = dt.strftime('%Y-%m-%d')
        published = dt.isoformat()
else:
    dt = datetime.now(timezone.utc)
    published_date = dt.strftime('%Y-%m-%d')
year,month,_ = published_date.split('-')
path = os.path.join("Summary", year, month, domain)
os.makedirs(path, exist_ok=True)
filename = f"{published_date}_{file_title}.md"
filepath = os.path.join(path, filename)

with open(filepath, "w") as f:
    f.write("---\n")
    f.write(f"title: {title!r}\n")
    f.write(f"source: {source}\n")
    f.write(f"author: {author}\n")
    f.write(f"published: {published!r}\n")
    f.write(f"fetched: {fetched!r}\n")
    f.write("tags:\n")
    f.write("  - codex\n")
    f.write(f"image: {image}\n")
    f.write("---\n\n")
    f.write("## 要約\n\n")
    f.write("TODO: summary\n\n")
    f.write("## 本文\n\n")
    f.write(content_md)

print(filepath)
