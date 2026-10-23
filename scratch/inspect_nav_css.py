with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.nav-menu-wrapper[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches:
    print(m[:600])
    print("=" * 40)

matches_toggle = re.findall(r'(\.nav-toggle[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches_toggle:
    print(m[:600])
    print("=" * 40)

