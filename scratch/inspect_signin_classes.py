with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="auth-[^"]*"', text)
print("Auth classes in sign-in.html:", matches)

