import pathlib
from urllib.parse import urlparse
import yaml

SUMMARY_DIR = pathlib.Path("Summary")


def test_folder_matches_host():
    errors = []
    for md in SUMMARY_DIR.rglob("*.md"):
        lines = md.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("---")
            end = lines.index("---", start + 1)
        except ValueError:
            continue
        meta = (
            yaml.load("\n".join(lines[start + 1 : end]), Loader=yaml.BaseLoader) or {}
        )
        source = str(meta.get("source", "")).strip()
        if not source:
            continue
        host = urlparse(source).hostname or ""
        if not host:
            continue
        folder = md.parent.name
        if host != folder:
            errors.append(
                f"{md}: フォルダ名 '{folder}' が URL ホスト '{host}' と一致していません"
            )
    assert not errors, "フォルダ名とホストの不一致:\n" + "\n".join(errors)
