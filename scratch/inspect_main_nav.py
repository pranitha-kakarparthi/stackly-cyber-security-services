with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = [m.start() for m in re.finditer(r'nav', js, re.IGNORECASE)]
for pos in matches[:10]:
    print(pos, js[pos-50:pos+150])
    print("-" * 30)

