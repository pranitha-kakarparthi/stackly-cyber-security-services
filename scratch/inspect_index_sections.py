with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check all sections in index.html
sections = re.findall(r'<section\b[^>]*>(.*?)</section>', text, re.DOTALL)
print(f"Total sections in index.html: {len(sections)}")

# Check any inline style with color or background in index.html
for i, s in enumerate(sections, start=1):
    classes = re.findall(r'class=["\']([^"\']+)["\']', s)
    headers = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', s)
    print(f"\nSection {i}: {classes[0] if classes else 'no-class'} | Header: {headers[0] if headers else 'no-header'}")
    inlines = re.findall(r'style=["\']([^"\']*)["\']', s)
    if inlines:
        for il in inlines:
            if any(k in il for k in ['color', 'background', '#']):
                print(f"   inline: {il}")

