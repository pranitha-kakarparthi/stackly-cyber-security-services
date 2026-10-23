with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
for i, s in enumerate(sections):
    m = re.search(r'<(?:h1|h2|h3)[^>]*>(.*?)</(?:h1|h2|h3)>', s)
    h = re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else "No Heading"
    print(f"Pricing Sec {i+1}: {h}")

