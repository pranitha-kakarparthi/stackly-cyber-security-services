with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<table[\s\S]*?</table>)', text)
if m:
    print("Found table in pricing.html, length:", len(m.group(1)))
    # check wrapper
    idx = text.find('<table')
    print("Wrapper context:")
    print(text[idx-250:idx+150])
else:
    print("No table in pricing.html")

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

m_css = re.search(r'(\.pricing-table[\s\S]*?)(?=\n/\*|\n\.\w|\n#|\n@media|\Z)', css)
if m_css:
    print("Pricing table CSS:")
    print(m_css.group(1)[:600])

