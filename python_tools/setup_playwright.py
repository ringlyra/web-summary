#!/usr/bin/env python3
"""Install Playwright browsers for offline use.

Run this after installing requirements to avoid re-downloading browsers every time.
"""
import os
import subprocess
from pathlib import Path

def main():
    browsers_dir = Path('.playwright-browsers').resolve()
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(browsers_dir)
    browsers_dir.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(['playwright', 'install'], check=True)
    except FileNotFoundError:
        raise SystemExit('Playwright not found. Run `pip install -r requirements.txt` first.')
    print(f"Browsers installed under {browsers_dir}")

if __name__ == '__main__':
    main()
