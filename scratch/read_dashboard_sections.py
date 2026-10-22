with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
comments = re.findall(r'/\* ==+.*?\*/', text, re.DOTALL)
for c in comments:
    first_line = c.strip().split('\n')[1] if len(c.strip().split('\n')) > 1 else c
    print(first_line.strip())

