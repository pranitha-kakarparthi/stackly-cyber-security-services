with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[2200:2350], start=2201):
    print(f"{i:4}: {l}", end='')

