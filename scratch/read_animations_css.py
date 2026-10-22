with open('assets/css/animations.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of animations.css:", len(text))
import re
for m in re.finditer(r'(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\))', text):
    print(m.group(0))

