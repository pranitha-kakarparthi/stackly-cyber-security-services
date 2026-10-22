import glob
import re

html_files = sorted(glob.glob('pages/*.html'))
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for m in re.finditer(r'style=["\'][^"\']*rgba\(\s*0\s*,\s*0\s*,\s*0[^"\']*["\']', text):
        start = max(0, m.start() - 60)
        end = min(len(text), m.end() + 100)
        print(f"\n{fpath}:")
        print(text[start:end])

