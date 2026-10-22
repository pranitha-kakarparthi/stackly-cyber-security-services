with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(172, 364):
    l = lines[i]
    if any(k in l for k in ['<h2', '<h3', '<h4', 'class="dash-panel"', 'class="dash-kpi-grid"', 'role-dashboard']):
        print(f"L{i+1:4d}: {l.strip()[:80]}")

