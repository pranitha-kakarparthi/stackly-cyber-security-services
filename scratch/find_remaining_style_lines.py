import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if any(k in l for k in ['00f076', '0, 240, 118', '94, 234, 212', '167, 139, 250']):
        print(f"{i:4}: {l.strip()}")

