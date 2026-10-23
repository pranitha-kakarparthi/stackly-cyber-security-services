with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.back-to-top' in l:
        print(''.join(lines[i:i+35]))
        break

