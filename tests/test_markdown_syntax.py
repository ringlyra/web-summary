import pathlib
import re


def test_media_syntax():
    md_files = list(pathlib.Path(".").rglob("*.md"))
