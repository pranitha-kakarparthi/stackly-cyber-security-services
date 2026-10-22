with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[100:250], start=101):
    print(f"{i:3}: {l}", end='')

