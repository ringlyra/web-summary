import sys
import requests
from bs4 import BeautifulSoup
from readability import Document
from markdownify import markdownify as md
from urllib.parse import urlparse
from datetime import datetime, timezone
import os

url = sys.argv[1]
resp = requests.get(url, timeout=10)
resp.raise_for_status()
html = resp.text
soup = BeautifulSoup(html, 'html.parser')

def get_meta(prop):
    tag = soup.find('meta', attrs={'property': prop}) or soup.find('meta', attrs={'name': prop})
    if tag and tag.get('content'):
        return tag['content']
    return ''

title = get_meta('og:title') or soup.title.string.strip()
author = soup.find('meta', attrs={'name':'author'})
if author:
    author = author['content']
else:
    author = urlparse(url).hostname
published = get_meta('article:published_time')
image = get_meta('og:image')
fetched = datetime.now(timezone.utc).isoformat()
source = url

parsed = urlparse(url)
domain = parsed.hostname
path_segments = parsed.path.strip('/').split('/')
content_md = ""
if domain == "github.com" and len(path_segments) == 2:
    user, repo = path_segments
    for branch in ["master", "main"]:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/README.md"
        r = requests.get(raw_url)
        if r.status_code == 200:
            content_md = r.text
            break

if not content_md:
    article_tag = soup.find('article')
    if article_tag:
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
published_date = published[:10] if published else datetime.now(timezone.utc).strftime('%Y-%m-%d')
year,month,_ = published_date.split('-')
path = os.path.join(year, month, domain)
os.makedirs(path, exist_ok=True)
filename = f"{published_date}_{file_title}.md"
filepath = os.path.join(path, filename)

with open(filepath,'w') as f:
    f.write("<!-- metadata -->\n")
    f.write(f"- **title**: {title}\n")
    f.write(f"- **source**: {source}\n")
    f.write(f"- **author**: {author}\n")
    f.write(f"- **published**: {published}\n")
    f.write(f"- **fetched**: {fetched}\n")
    f.write(f"- **tags**: codex\n")
    f.write(f"- **image**: {image}\n\n")
    f.write("## 要約\n\n")
    f.write("TODO: summary\n\n")
    f.write("## 本文\n\n")
    f.write(content_md)

print(filepath)
