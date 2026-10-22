import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'color:[^;]+|background:[^;]+|background-color:[^;]+|border:[^;]+|border-bottom:[^;]+', text)
print("Total color properties in dashboard.css:", len(matches))

# Check for hardcoded hex or rgba
for m in set(matches):
    if any(k in m for k in ['#', 'rgb']):
        print("  ", m.strip())

