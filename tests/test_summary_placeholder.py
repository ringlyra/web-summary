import pathlib

SUMMARY_DIR = pathlib.Path("Summary")
PLACEHOLDER = "<日本語の要約を書く>"
MESSAGE = "<日本語の要約を書く>のプレースホルダーが残っています。作成した要約に置き換えてください。"


def test_summary_placeholder():
    errors: list[str] = []

    for md in SUMMARY_DIR.rglob("*.md"):
        lines = md.read_text(encoding="utf-8").splitlines()
        try:
            start = lines.index("## 要約")
        except ValueError:
            continue

        summary_lines: list[str] = []
        for line in lines[start + 1 :]:
            if line.strip().startswith("## "):
                break
            summary_lines.append(line)

        if PLACEHOLDER in "\n".join(summary_lines):
            errors.append(str(md))

    assert not errors, MESSAGE + "\n" + "\n".join(errors)
