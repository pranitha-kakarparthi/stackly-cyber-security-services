import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
legacy_patterns = [
    '#0c1326', '#0a1122', '#060a14', '#030508', '#080d1a', '#080d19', '#090e1b', '#090e1c', '#0d1427', '#0d1527', '#101930', '#101c38',
    '#5eead4', '#38bdf8', '#a78bfa', '#f472b6', '#c084fc', '#00f076',
    '0, 240, 118', '94, 234, 212', '167, 139, 250', '56, 189, 248', 'rgba(0,0,0', 'rgba(0, 0, 0'
]

findings = {}
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    file_matches = []
    for p in legacy_patterns:
        count = text.count(p)
        if count > 0:
            file_matches.append((p, count))
    if file_matches:
        findings[fpath] = file_matches

print(f"Files with legacy colors or dark backgrounds: {len(findings)}")
for fpath, matches in findings.items():
    print(f"\n{fpath}:")
    for p, c in matches:
        print(f"   {p:20}: {c} times")

