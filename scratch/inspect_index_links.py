import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', text, re.DOTALL):
    href = m.group(1)
    label = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    label_clean = ' '.join(label.split())
    print(f"HREF: {href:40} | LABEL: {label_clean[:30]}")

