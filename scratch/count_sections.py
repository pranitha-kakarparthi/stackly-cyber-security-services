import glob
import re

files = glob.glob('*.html') + glob.glob('pages/*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    sections = re.findall(r'<section[^>]*>', content)
    print(f"{f:35} : {len(sections)} sections")

