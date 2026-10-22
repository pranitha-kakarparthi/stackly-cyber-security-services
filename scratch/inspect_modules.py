with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
modules = re.findall(r'<div class="dash-module-section[^"]*" id="([^"]+)">', text)
print("Modules found:", modules)
for m in modules:
    start = text.find(f'id="{m}"')
    print(f"Module {m} starts at char {start}")

