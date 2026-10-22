with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    l = line.strip()
    if any(k in l for k in ['data-role', 'data-target-module', 'id="module-', '<section', '<aside', 'dash-topbar', 'role-content', 'dash-main']):
        print(f"L{i:4d}: {l[:100]}")

