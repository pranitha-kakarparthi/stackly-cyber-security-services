with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'\.auth-banner-side\s*\{[^}]*display:\s*none', css)
print("auth-banner-side display:none matches:", len(matches))

matches_all = re.findall(r'(\.auth-banner-side\b[\s\S]*?\{[\s\S]*?\})', css)
print(f"Total .auth-banner-side rules: {len(matches_all)}")
for m in matches_all:
    print(m[:250])
    print("-" * 30)

