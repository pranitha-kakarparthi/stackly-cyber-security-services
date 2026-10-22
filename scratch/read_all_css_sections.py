with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'/\* ==+\s*([^\n*]+)\s*==+\s*\*/', text)
sections = []
for m in matches:
    sections.append((m.start(), m.group(1).strip()))

sections.append((len(text), 'EOF'))

for i in range(len(sections)-1):
    start = sections[i][0]
    end = sections[i+1][0]
    name = sections[i][1]
    sec_text = text[start:end]
    print(f"\n--- SECTION: {name} (length {len(sec_text)}) ---")
    # Print sample
    for line in sec_text.splitlines()[:15]:
        print("  ", line)

