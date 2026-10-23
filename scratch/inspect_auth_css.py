with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.auth-wrapper[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches[:5]:
    print(m)
    print("=" * 40)

media_auth = re.findall(r'(@media[^{]*\{[\s\S]*?\.auth-[\s\S]*?\n\})', css)
for m in media_auth:
    print("--- MEDIA ---")
    print(m)

