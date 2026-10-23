with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.page-hero\b[\s\S]*?\{[\s\S]*?\})', text)
for m in matches[:5]:
    print(m)
    print("-" * 40)

matches_stage = re.findall(r'(\.hero-stage\b[\s\S]*?\{[\s\S]*?\})', text)
for m in matches_stage[:5]:
    print(m)
    print("-" * 40)

