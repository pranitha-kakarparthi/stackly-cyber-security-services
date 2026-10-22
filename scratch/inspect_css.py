with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
selectors = re.findall(r'(\.[a-zA-Z0-9_-]+)\s*\{', text)
print("Unique selectors in dashboard.css:", len(set(selectors)))
print("Top-level selectors:", sorted(list(set(selectors)))[:30])

