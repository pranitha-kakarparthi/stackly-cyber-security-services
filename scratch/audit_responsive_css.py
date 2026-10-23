with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'@media\s*\([^)]+\)\s*\{', css)
print("Unique media query breakpoints:")
for m in set(matches):
    print(" ", m)

# Search for negative margins in media queries
neg_margins = re.findall(r'(@media[^{]*\{[\s\S]*?margin[^{}]*-[0-9][\s\S]*?\})', css)
print(f"\nFound {len(neg_margins)} media queries with negative margins:")
for nm in neg_margins:
    print(nm[:400])
    print("-" * 30)

