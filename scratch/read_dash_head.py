with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[30:50], start=31):
    print(f"{i:2}: {repr(l)}")

