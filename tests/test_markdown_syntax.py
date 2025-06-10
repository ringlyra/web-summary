import pathlib
import re

MEDIA_RE = re.compile(r'\(([^)]+\.(?:mp4|mov|m3u8)(?:\?[^)]*)?)\)')


def test_video_links():
    md_files = list(pathlib.Path('2025').rglob('*.md'))
    errors = []
    for md_file in md_files:
        for idx, line in enumerate(md_file.read_text(encoding='utf-8').splitlines(), 1):
            for match in MEDIA_RE.finditer(line):
                url = match.group(1)
                if not url.startswith('https://'):
                    errors.append(f'{md_file}:{idx}:{url}')
    assert not errors, 'Video link errors:\n' + '\n'.join(errors)


