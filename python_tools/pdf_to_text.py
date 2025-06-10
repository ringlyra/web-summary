import sys
from pathlib import Path
import requests
from PyPDF2 import PdfReader


def pdf_to_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    text_parts = []
    for page in reader.pages:
        text_parts.append(page.extract_text())
    return "\n".join(text_parts)


def main(url: str, out_file: Path):
    # download pdf
    r = requests.get(url)
    r.raise_for_status()
    tmp_path = out_file.with_suffix('.pdf')
    tmp_path.write_bytes(r.content)

    text = pdf_to_text(tmp_path)
    out_file.write_text(text)

    print(out_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pdf_to_text.py <pdf_url> <output_txt>")
        sys.exit(1)
    url = sys.argv[1]
    out_file = Path(sys.argv[2])
    main(url, out_file)
