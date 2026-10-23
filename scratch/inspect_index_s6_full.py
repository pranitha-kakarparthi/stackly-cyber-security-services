with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
s6 = sections[5]
print(s6.encode('ascii', errors='replace').decode('ascii'))

