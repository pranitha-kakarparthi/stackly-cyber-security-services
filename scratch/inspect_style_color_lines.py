import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['0, 240, 118', '94, 234, 212', '167, 139, 250', '56, 189, 248', '#030508', '#5eead4', '#a78bfa', '#38bdf8']):
        print(f"{i+1:4}: {l.strip()}")

