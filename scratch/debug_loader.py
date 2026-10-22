import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css_text = f.read()

print("--- LOADER IN MAIN.JS ---")
for line in js_text.splitlines()[:50]:
    print(line)

print("\n--- LOADER IN STYLE.CSS ---")
matches = re.findall(r'#page-loader[^{]*\{[^}]+\}', css_text)
for m in matches:
    print(m)

loaded_matches = re.findall(r'\.loaded[^{]*\{[^}]+\}', css_text)
for m in loaded_matches:
    print(m)

