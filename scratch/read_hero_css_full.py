with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[750:980], start=751):
    print(f"{i:4}: {l}", end='')

