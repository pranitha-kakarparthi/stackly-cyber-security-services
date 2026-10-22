with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'style=["\'][^"\']*(?:94,\s*234,\s*212|167,\s*139,\s*250|56,\s*189,\s*248)[^"\']*["\']', text)
for m in matches:
    print(m.group(0))

