with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[2350:2550], start=2351):
    if '@media' in l or 'padding' in l or 'gap' in l or 'grid-template' in l:
        print(f"{i:4}: {l.strip()}")

