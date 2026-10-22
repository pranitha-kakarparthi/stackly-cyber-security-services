with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[200:230], start=201):
    print(f"{i:3}: {l}", end='')

