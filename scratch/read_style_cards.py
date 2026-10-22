with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1000:1150], start=1001):
    print(f"{i:4}: {l}", end='')

