import re

for filename in ['assets/css/style.css', 'assets/css/dashboard.css']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # check for cyan/mint/neon green
    suspicious = re.findall(r'(#[0-9a-fA-F]{6}|rgba?\([^)]+\))', text)
    found = []
    for s in suspicious:
        s_lower = s.lower()
        if any(c in s_lower for c in ['00f076', '5eead4', '38bdf8', '0, 240, 118', '94, 234, 212', '167, 139, 250']):
            found.append(s)
    print(f"{filename}: found {len(found)} remaining legacy color references:")
    for item in set(found):
        print("  ", item)

