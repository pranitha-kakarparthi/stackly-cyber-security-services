with open('pages/contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
print(sections[4].encode('ascii', errors='replace').decode('ascii'))

