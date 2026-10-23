with open('pages/service-soc.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*aria-label=["\']([^"\']+)["\']', text)
print(f"Total sections in service-soc.html: {len(sections)}")
for i, s in enumerate(sections):
    print(f"{i+1}. {s}")

