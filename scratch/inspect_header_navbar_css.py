with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.site-header[\s\S]*?\{[\s\S]*?\})', css)
for m in matches:
    print(m)
    print("-" * 30)

matches_navbar = re.findall(r'(\.navbar\b[\s\S]*?\{[\s\S]*?\})', css)
for m in matches_navbar:
    print(m)
    print("-" * 30)

