with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.pricing-comparison-[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches:
    print(m[:500])
    print("-" * 30)

