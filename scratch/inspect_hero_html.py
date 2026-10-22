with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
hero_match = re.search(r'<section\b[^>]*class=["\'][^"\']*hero[^"\']*["\'][^>]*>.*?</section>', text, re.DOTALL)
if hero_match:
    print(hero_match.group(0)[:2500])
else:
    print("Hero section not found by regex")

