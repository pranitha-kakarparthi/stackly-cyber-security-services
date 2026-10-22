import re

for filename in ['assets/css/style.css', 'assets/css/dashboard.css']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # find all hex colors
    hexes = set(re.findall(r'#[0-9a-fA-F]{3,8}', text))
    print(f"\n=== HEX COLORS IN {filename} ===")
    for h in sorted(hexes):
        # count occurrences
        cnt = text.count(h)
        print(f"  {h:10}: {cnt} times")

