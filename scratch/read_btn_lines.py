with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[365:410], start=366):
    print(f"{i:4}: {l}", end='')

