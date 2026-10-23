import re

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect sections and panels
sections = re.findall(r'<section\b[^>]*class="([^"]*)"[^>]*>', text)
print(f"Total section tags: {len(sections)}")

# Let's find all grids
grids = re.findall(r'class="([^"]*(?:grid|flex|row|panel)[^"]*)"', text)
unique_grids = set(grids)
print(f"Grid and layout classes found ({len(unique_grids)}):")
for g in sorted(unique_grids)[:25]:
    print(f"  - {g}")

