with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[20:180], start=21):
    print(f"{i:3}: {l}", end='')

