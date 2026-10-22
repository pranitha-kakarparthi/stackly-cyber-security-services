import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for filename in ['assets/css/style.css', 'assets/css/dashboard.css']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    old_patterns = [
        '#030508', '#070b13', '#0c1220', '#111a2e', '#080d19', '#060a14', '#041210', '#0a0f1a', '#080c16',
        '#5eead4', '#2dd4bf', '#99f6e4', '#a78bfa', '#c084fc', '#ddd6fe', '#38bdf8', '#0ea5e9',
        '0, 240, 118', '94, 234, 212', '167, 139, 250', '56, 189, 248'
    ]
    
    counts = {}
    for p in old_patterns:
        c = text.count(p)
        if c > 0:
            counts[p] = c
    print(f"=== {filename} ===")
    for p, c in counts.items():
        print(f"  {p:20}: {c} occurrences")

