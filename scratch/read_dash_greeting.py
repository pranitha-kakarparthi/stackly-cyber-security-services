with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[120:135], start=121):
    print(f"{i:3}: {l}", end='')

