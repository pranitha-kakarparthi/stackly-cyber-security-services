import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = re.findall(r'style=["\'][^"\']*rgba\(\s*0\s*,\s*0\s*,\s*0[^"\']*["\']', text)
    if matches:
        print(f"\n{fpath}: {len(matches)} dark rgba inline styles")
        for m in matches[:5]:
            print("  ", m)

