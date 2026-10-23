with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.auth-banner-side\b', css)]
for pos in matches:
    print(pos, css[pos-100:pos+300])
    print("=" * 40)

