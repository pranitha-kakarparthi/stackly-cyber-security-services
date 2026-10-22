with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1150:1300], start=1151):
    print(f"{i:4}: {l}", end='')

