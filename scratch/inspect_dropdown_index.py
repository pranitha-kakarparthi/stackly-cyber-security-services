import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<ul class="dropdown-menu">.*?</ul>', text, re.DOTALL)
if match:
    print(match.group(0))

