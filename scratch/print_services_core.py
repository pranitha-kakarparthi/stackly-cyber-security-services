import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[250:375]))

