with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.page-hero\b', text)]
for pos in matches:
    print("Match at pos:", pos)
    print(text[pos:pos+300])
    print("=" * 40)

