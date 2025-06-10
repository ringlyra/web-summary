import pathlib
import re

MEDIA_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
IMG_EXT = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
VIDEO_EXT = ('.mp4',)


def test_media_syntax():
    md_files = list(pathlib.Path('2025').rglob('*.md'))
    errors = []
    for md_file in md_files:
        for idx, line in enumerate(md_file.read_text(encoding='utf-8').splitlines(), 1):
            for match in MEDIA_RE.finditer(line):
                url = match.group(1)
                if not url.startswith('https://'):
                    errors.append(f'{md_file}:{idx}:{url}')
                    continue
                ext = url.split('?')[0].lower()
                if ext.endswith(VIDEO_EXT):
                    continue
                if not ext.endswith(IMG_EXT):
                    errors.append(f'{md_file}:{idx}:{url}')
    assert not errors, 'Media syntax errors:\n' + '\n'.join(errors)
