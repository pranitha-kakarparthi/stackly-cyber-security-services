with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1848:1930], start=1849):
    print(f"{i:4}: {l}", end='')

