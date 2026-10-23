with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'(navToggle[\s\S]*?)(?=\nfunction|\nconst|\nlet|\nvar|\Z)', js)
for m in matches:
    print(m[:1000])
    print("=" * 40)

