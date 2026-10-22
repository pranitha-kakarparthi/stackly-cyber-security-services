with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1740:1850], start=1741):
    print(f"{i:4}: {l}", end='')

