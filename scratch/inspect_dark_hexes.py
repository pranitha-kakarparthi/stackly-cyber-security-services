with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

dark_hexes = ['#010608', '#030508', '#040e12', '#080d19', '#080d1a', '#090e1b', '#090e1c', '#0d1427', '#0d1527', '#101930', '#101c38', '#cbd5e1', '#80f2ff']

for i, l in enumerate(lines, start=1):
    for h in dark_hexes:
        if h in l.lower():
            print(f"{i:4}: [{h}] {l.strip()}")

