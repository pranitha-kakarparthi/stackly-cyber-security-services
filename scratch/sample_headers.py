import re
import sys

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

headers = re.findall(r'<div class="dash-panel-header">([\s\S]*?)</div>\s*<(?:div|table|ul)', text)
print(f"Total dash-panel-header instances: {len(headers)}")
for i, h in enumerate(headers[:6]):
    clean = re.sub(r'\s+', ' ', h.strip()).encode('ascii', 'replace').decode('ascii')
    print(f"Header {i+1}: {clean[:120]}")

