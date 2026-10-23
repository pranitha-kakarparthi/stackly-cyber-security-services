with open('pages/services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'card-title' in l or 'service' in l.lower() and '<h' in l.lower():
        print(f'{i+1}: {l.strip()[:100]}')

