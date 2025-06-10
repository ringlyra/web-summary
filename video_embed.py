import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


def get_meta(url, prop_names):
    try:
        html = requests.get(url, timeout=10).text
    except Exception:
        return ""
    soup = BeautifulSoup(html, 'html.parser')
    for prop in prop_names:
        tag = soup.find('meta', attrs={'property': prop}) or soup.find('meta', attrs={'name': prop})
        if tag and tag.get('content'):
            return tag['content']
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python video_embed.py <video_url>")
        sys.exit(1)
    url = sys.argv[1]
    image = get_meta(url, ['og:image', 'twitter:image'])
    title = get_meta(url, ['og:title', 'twitter:title'])

    if not image:
        parsed = urlparse(url)
        if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
            vid = parse_qs(parsed.query).get('v')
            if not vid and parsed.path:
                vid = [parsed.path.strip('/')]
            if vid:
                image = f'https://img.youtube.com/vi/{vid[0]}/hqdefault.jpg'
    alt = f"{title} – 再生する" if title else "Play video"
    if not image:
        print('Could not determine thumbnail image.', file=sys.stderr)
        sys.exit(1)
    print(f"[![{alt}]({image})]({url})")


if __name__ == '__main__':
    main()
