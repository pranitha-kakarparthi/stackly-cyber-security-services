import glob
import re

files = ['index.html', '404.html'] + sorted(glob.glob('pages/*.html'))
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', content)
    print(f"=== {path} ({len(imgs)} images) ===")
    for src, alt in imgs:
        if 'logo' not in src.lower():
            print(f"  {src} | {alt[:40]}")

