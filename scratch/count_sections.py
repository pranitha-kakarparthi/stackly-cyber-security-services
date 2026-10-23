import glob
import re

files = ['index.html', '404.html'] + sorted(glob.glob('pages/*.html'))
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    sections = re.findall(r'<section\b[^>]*>', content)
    print(f"{path}: {len(sections)} sections")
