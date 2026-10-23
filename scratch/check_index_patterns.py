import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

dd = re.search(r'<ul class="dropdown-menu">[\s\S]*?</ul>', text)
print("Index dropdown found:", bool(dd))

ft = re.search(r'<div class="footer-links-col">\s*<h4 class="footer-heading">Defense Services</h4>[\s\S]*?</ul>\s*</div>', text)
print("Index footer found:", bool(ft))

