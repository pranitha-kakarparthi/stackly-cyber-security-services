with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('--- NAV BRAND LOGO (lines 515-535) ---')
print(''.join(lines[514:535]))

print('--- FORM CONTROL FOCUS (lines 1645-1670) ---')
print(''.join(lines[1645:1670]))

print('--- FOOTER (lines 2315-2420) ---')
print(''.join(lines[2315:2420]))

