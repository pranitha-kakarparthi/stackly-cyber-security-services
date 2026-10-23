with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<div class="mobile-nav-overlay"[\s\S]*?</div>\s*</div>)', text)
if m:
    print("=== index.html mobile-nav-overlay ===")
    print(m.group(1).encode('ascii', errors='replace').decode('ascii'))

