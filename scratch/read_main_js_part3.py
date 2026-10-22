import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[230:], start=231):
    print(f"{i:3}: {l}", end='')

