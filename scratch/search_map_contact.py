with open('pages/contact.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'map' in l.lower() or 'location' in l.lower():
        print(f'{i+1}: {l.strip()[:100]}')

