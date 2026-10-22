import re

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- AUDITING DASHBOARD SECTIONS ---")

# Check role dashboards
roles = ['view-role-ciso', 'view-role-soc', 'view-role-client']
for r in roles:
    start = html.find(f'id="{r}"')
    next_start = -1
    for r2 in roles:
        if r2 != r:
            pos = html.find(f'id="{r2}"', start + 1)
            if pos != -1 and (next_start == -1 or pos < next_start):
                next_start = pos
    if next_start == -1:
        next_start = html.find('</div>\n\n        <!-- MODULE 2', start)
    
    role_block = html[start:next_start]
    sections = re.findall(r'<section class="dash-section"', role_block)
    print(f"Role [{r}]: {len(sections)} sections")

# Check modules
modules = [
    'module-overview',
    'module-threats',
    'module-vulnerabilities',
    'module-firewall',
    'module-incidents',
    'module-compliance',
    'module-reports',
    'module-users'
]

for m in modules:
    start = html.find(f'id="{m}"')
    next_start = -1
    for m2 in modules:
        if m2 != m:
            pos = html.find(f'id="{m2}"', start + 1)
            if pos != -1 and (next_start == -1 or pos < next_start):
                next_start = pos
    if next_start == -1:
        next_start = html.find('</main>', start)
        
    mod_block = html[start:next_start]
    sections = re.findall(r'<section class="dash-section"', mod_block)
    panels = re.findall(r'class="dash-panel"', mod_block)
    print(f"Module [{m}]: {len(sections)} sections ({len(panels)} panels)")

