with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[640:720], start=641):
    print(f"{i:3}: {l}", end='')

