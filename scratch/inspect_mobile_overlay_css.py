with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.mobile-nav-overlay[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches:
    print(m)
    print("=" * 40)

