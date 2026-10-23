with open('index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

import re
m_logo = re.search(r'<a href="[^"]*" class="nav-brand"[\s\S]*?</a>', idx_text)
if m_logo:
    print("=== index.html nav-brand ===")
    print(m_logo.group(0))

with open('pages/about.html', 'r', encoding='utf-8') as f:
    about_text = f.read()

m_logo_about = re.search(r'<a href="[^"]*" class="nav-brand"[\s\S]*?</a>', about_text)
if m_logo_about:
    print("\n=== pages/about.html nav-brand ===")
    print(m_logo_about.group(0))

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

matches = re.findall(r'(\.nav-brand[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
for m in matches:
    print("\n=== style.css nav-brand ===")
    print(m[:400])

