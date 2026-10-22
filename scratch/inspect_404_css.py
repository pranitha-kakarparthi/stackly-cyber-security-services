with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'vortex' in l.lower():
        print(f'{i+1}: {l.strip()[:100]}')

