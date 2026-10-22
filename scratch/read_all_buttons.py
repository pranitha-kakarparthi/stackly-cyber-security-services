with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[380:460], start=381):
    print(f"{i:4}: {l}", end='')

