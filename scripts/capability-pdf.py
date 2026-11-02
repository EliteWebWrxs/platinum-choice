"""
Generates static/files/pcc-capability-statement.pdf from the capability statement page.

Run from the project root after changing the statement copy or credentials:
    python3 scripts/capability-pdf.py

Needs pypdf (pip install pypdf), Google Chrome and node_modules. Starts its own dev server.
"""

import os
import subprocess
import tempfile
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'static/files/pcc-capability-statement.pdf'
CHROME = os.environ.get('CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

PORT = 5198
URL = f'http://localhost:{PORT}/capability-statement'
TABS = ['', '#workforce-development']


def wait_for_server():
    for _ in range(60):
        try:
            urlopen(URL)
            return
        except URLError:
            time.sleep(0.5)
    raise SystemExit('Dev server did not start')


def render(url, path, profile):
    subprocess.run(
        [
            CHROME,
            '--headless=new',
            '--disable-gpu',
            f'--user-data-dir={profile}',
            '--virtual-time-budget=8000',
            '--no-pdf-header-footer',
            f'--print-to-pdf={path}',
            url,
        ],
        check=True,
        capture_output=True,
    )


def main():
    server = subprocess.Popen(
        ['pnpm', 'exec', 'vite', 'dev', '--port', str(PORT), '--strictPort'],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for_server()
        with tempfile.TemporaryDirectory() as tmp:
            writer = PdfWriter()
            for i, tab in enumerate(TABS):
                path = Path(tmp) / f'{i}.pdf'
                render(URL + tab, path, Path(tmp) / 'chrome')
                writer.append(path)
            writer.add_metadata({'/Title': 'Platinum Choice Consulting Capability Statement'})
            writer.write(OUT)
    finally:
        server.terminate()
        server.wait()
    print(f'{OUT.relative_to(ROOT)}: {len(writer.pages)} pages')


if __name__ == '__main__':
    main()
