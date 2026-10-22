with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, start=1):
    if any(k in l for k in ['#38bdf8', '#a78bfa', '167, 139, 250', '56, 189, 248']):
        print(f"{i:4}: {l.strip()}")

