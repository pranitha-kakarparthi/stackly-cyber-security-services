import re

# Read current dashboard.html
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Let's inspect head and topbar so we preserve them 100%
topbar_end = orig.find('<main class="dash-content" role="main">')
header_part = orig[:topbar_end + len('<main class="dash-content" role="main">\n')]

footer_start = orig.find('</main>\n    </div>\n  </div>')
if footer_start == -1:
    footer_start = orig.find('</main>')

footer_part = orig[footer_start:]

print(f"Header part length: {len(header_part)}")
print(f"Footer part length: {len(footer_part)}")

