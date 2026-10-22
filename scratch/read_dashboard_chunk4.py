with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[520:675], start=521):
    print(f"{i:3}: {l}", end='')

