with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
s6 = sections[5]
cards = re.findall(r'<div class="tilt-card"[\s\S]*?</div>\s*</div>', s6)
print(f"Cards count in index section 6: {len(cards)}")
for c in cards:
    title = re.search(r'<h3[^>]*>(.*?)</h3>', c)
    href = re.search(r'href="([^"]*)"', c)
    print(f"Card: {title.group(1) if title else 'No title'} -> {href.group(1) if href else 'No href'}")

