import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
img_tags = []

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'<img[^>]+>', text)
    for m in matches:
        if any(h in m.lower() for h in ['elena', 'alex', 'marcus', 'david', 'rachel', 'sarah', 'michael', 'amira', 'robert', 'auditor', 'engineer', 'officer', 'analyst', 'tester', 'architect', 'commander', 'client', 'avatar', 'team', 'person', 'portrait', 'user']):
            img_tags.append((path, m))

print(f"Found {len(img_tags)} human image tags:")
for p, tag in img_tags:
    print(f"{p:30}: {tag[:100]}")

