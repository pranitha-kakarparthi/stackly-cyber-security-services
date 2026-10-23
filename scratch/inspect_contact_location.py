with open('pages/contact.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l.lower() for k in ['location', 'address', 'headquarters', 'complex', 'salem', 'thirupathi', 'hq', 'map']):
        print(f'{i+1}: {l.strip()[:100]}')
        print(''.join(lines[max(0, i-2):min(len(lines), i+3)]))
        print('-'*40)

