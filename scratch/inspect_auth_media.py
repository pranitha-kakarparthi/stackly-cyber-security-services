with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text_in = f.read()

with open('pages/sign-up.html', 'r', encoding='utf-8') as f:
    text_up = f.read()

import re
m_in = re.search(r'<div class="auth-banner-side">([\s\S]*?)</div>\s*<!-- Right Form Side', text_in)
if m_in:
    print("=== sign-in.html auth-banner-side ===")
    print(m_in.group(1).encode('ascii', errors='replace').decode('ascii'))

m_up = re.search(r'<div class="auth-banner-side">([\s\S]*?)</div>\s*<!-- Right Form Side', text_up)
if m_up:
    print("\n=== sign-up.html auth-banner-side ===")
    print(m_up.group(1).encode('ascii', errors='replace').decode('ascii'))

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

matches = re.findall(r'(@media[^{]*\{[\s\S]*?\.auth-banner-side[\s\S]*?\})', css)
print("\n=== Media queries affecting auth-banner-side ===")
for m in matches:
    print(m[:500])

