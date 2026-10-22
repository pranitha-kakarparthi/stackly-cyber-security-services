import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
print(f"Total HTML files: {len(html_files)}")
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    links = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', text)
    hrefs = []
    for l in links:
        m = re.search(r'href=["\']([^"\']+)["\']', l)
        if m:
            hrefs.append(m.group(1))
    print(f"{path:35} -> {hrefs}")

