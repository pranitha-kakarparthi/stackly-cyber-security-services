with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('scratch/overview_structure.txt', 'w', encoding='utf-8') as out:
    for i in range(165, len(lines)):
        l = lines[i]
        if 'id=' in l or ('class=' in l and any(k in l for k in ['role-', 'dash-module-section', 'dash-kpi', 'panel', 'table', 'section'])):
            out.write(f"L{i+1:4d}: {l.strip()[:100]}\n")

print("Written overview_structure.txt")

