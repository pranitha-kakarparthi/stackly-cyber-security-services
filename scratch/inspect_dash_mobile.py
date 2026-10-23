with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    d_css = f.read()

import re
matches = re.findall(r'(@media[^{]*\{[\s\S]*?\})', d_css)
print(f"dashboard.css has {len(matches)} media queries:")
for m in matches:
    print(m[:300])
    print("-" * 30)

