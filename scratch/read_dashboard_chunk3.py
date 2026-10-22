with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[350:520], start=351):
    print(f"{i:3}: {l}", end='')

