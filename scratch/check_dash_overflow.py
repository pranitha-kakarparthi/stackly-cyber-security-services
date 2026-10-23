import re

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

styles = re.findall(r'style="([^"]+)"', text)
potential_issues = []
for s in styles:
    if any(k in s for k in ['height:', 'width:', 'min-width:', 'position: absolute', 'nowrap']):
        potential_issues.append(s)

print(f"Total potential inline style issues: {len(potential_issues)}")
for pi in potential_issues[:25]:
    clean = pi.encode('ascii', 'replace').decode('ascii')
    print("  ->", clean[:90])

