import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    for m in re.finditer(r'<img[^>]+>', text):
        tag = m.group(0)
        if any(k in tag for k in ['elena', 'alex', 'marcus', 'david', 'rachel', 'sarah', 'michael', 'amira', 'robert', 'auditor', 'engineer']):
            start = max(0, m.start() - 150)
            print(f"{path:25}: tag={tag[:60]}... context={text[start:m.start()].strip()[-50:]}")

