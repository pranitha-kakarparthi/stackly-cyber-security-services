import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# find comments that divide sections
comments = re.findall(r'/\* ==+.*?\*/', text, re.DOTALL)
print(f"Total section dividers: {len(comments)}")
for c in comments:
    first_line = c.strip().split('\n')[1] if len(c.strip().split('\n')) > 1 else c
    print(first_line.strip())

