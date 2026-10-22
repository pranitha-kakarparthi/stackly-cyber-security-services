import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dash_css = f.read()

print("=== CHECKING FORM CONTROLS IN STYLE.CSS ===")
form_match = re.search(r'/\* ==+.*FORMS.*?\*/.*?(?=/\* ==+|$)', style_css, re.DOTALL)
if form_match:
    print(form_match.group(0)[:1500])

print("\n=== CHECKING BUTTONS IN STYLE.CSS ===")
btn_match = re.search(r'/\* ==+.*BUTTON.*?\*/.*?(?=/\* ==+|$)', style_css, re.DOTALL)
if btn_match:
    print(btn_match.group(0)[:1500])

