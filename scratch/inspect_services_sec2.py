with open('pages/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<section class="section" aria-label="Flagship Defense Services">[\s\S]*?</section>)', text)
if m:
    print(m.group(1).encode('ascii', errors='replace').decode('ascii'))

