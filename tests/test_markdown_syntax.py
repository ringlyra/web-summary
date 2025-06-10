import pathlib
import re


def test_media_syntax():
    md_files = list(pathlib.Path(".").rglob("*.md"))
    newline_pattern = re.compile(r"\[!\[\s*\n")
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        # check for newline after [![
        assert not newline_pattern.search(text), f"multiline media syntax in {path}"
        for idx, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("[!["):
                parts = line.split(")](")
                assert len(parts) == 2 and parts[1].rstrip().endswith(")"), (
                    f"nonstandard embed format in {path}:{idx}"
                )
