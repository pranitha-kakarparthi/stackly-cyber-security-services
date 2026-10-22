with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div[^>]*class=["\'][^"\']*cta-card[^"\']*["\'][^>]*>.*?</div>\s*</div>', text, re.DOTALL)
if matches:
    print(matches[0][:1500])
else:
    print("cta-card not matched, searching by #0c1326:")
    pos = text.find('#0c1326')
    print(text[max(0, pos-200):min(len(text), pos+600)])

