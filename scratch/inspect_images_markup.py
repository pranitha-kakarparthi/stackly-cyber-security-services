import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<img[^>]+>', text):
    tag = m.group(0)
    if any(k in tag for k in ['elena', 'alex', 'marcus', 'david', 'rachel', 'sarah', 'michael', 'amira', 'robert', 'auditor', 'engineer']):
        start = max(0, m.start() - 250)
        end = min(len(text), m.end() + 250)
        print("MATCH:", tag)
        print("CONTEXT:")
        print(text[start:end])
        print("="*60)

