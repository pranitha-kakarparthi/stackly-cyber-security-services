with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.auth-nav-top[\s\S]*?\{[\s\S]*?\})', css)
for m in matches:
    print(m)
    print("-" * 30)

media_nav = re.findall(r'(@media[^{]*\{[\s\S]*?\.auth-nav-top[\s\S]*?\})', css)
print("Media queries with auth-nav-top:")
for m in media_nav:
    print(m)
    print("=" * 30)

