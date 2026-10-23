with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<li class="nav-item">[\s\S]*?<ul class="dropdown-menu">[\s\S]*?</ul>[\s\S]*?</li>', text)
if m:
    print(m.group(0).encode('ascii', errors='replace').decode('ascii'))

