import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    has_loader = 'id="page-loader"' in text
    scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
    print(f"{fpath:35}: has_loader={has_loader}, scripts={scripts}")

