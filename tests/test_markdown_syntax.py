import pathlib
import re

def test_media_syntax():
    md_files = list(pathlib.Path('.').rglob('*.md'))
    newline_pattern = re.compile(r'\[!\[\s*\n')
    for path in md_files:
        text = path.read_text(encoding='utf-8')
        # check for newline after [![
        assert not newline_pattern.search(text), f"multiline media syntax in {path}"
        for idx, line in enumerate(text.splitlines(), 1):
            if '[![' in line and line.strip().startswith('[!['):
                if ')](' not in line:
                    raise AssertionError(f"possible broken media syntax in {path}:{idx}")
