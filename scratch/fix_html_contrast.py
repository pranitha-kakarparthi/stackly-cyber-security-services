import glob
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_text = f.read()

# Fix Section 11 dark CTA card
old_sec11 = 'style="text-align: center; max-width: 860px; margin: 0 auto; background: radial-gradient(circle at 50% 20%, rgba(0, 240, 118, 0.12) 0%, #0c1326 80%);"'
new_sec11 = 'style="text-align: center; max-width: 860px; margin: 0 auto; background: linear-gradient(145deg, #FFFFFF 0%, #F6F1E3 100%); border: 1.5px solid var(--border-cyber); box-shadow: 0 16px 45px rgba(58, 1, 14, 0.08);"'

if old_sec11 in index_text:
    index_text = index_text.replace(old_sec11, new_sec11)
    print("Fixed Section 11 card in index.html")

# Fix SVG ambient ribbons colors
index_text = index_text.replace('stop-color="#5eead4"', 'stop-color="#7A1028"')
index_text = index_text.replace('stop-color="#38bdf8"', 'stop-color="#D97706"')
index_text = index_text.replace('stop-color="#a78bfa"', 'stop-color="#9E2A44"')
index_text = index_text.replace('stop-color="#f472b6"', 'stop-color="#B45309"')

# Fix section 2 sim box
index_text = index_text.replace('background: rgba(0, 240, 118, 0.05);', 'background: rgba(122, 16, 40, 0.04);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_text)

# 2. Update pages/*.html to remove dark black rgba(0,0,0...) cards
html_pages = sorted(glob.glob('pages/*.html'))
for fpath in html_pages:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    modified = False
    if 'rgba(0,0,0,0.4)' in text:
        text = text.replace('background: rgba(0,0,0,0.4);', 'background: var(--bg-secondary);')
        modified = True
    if 'rgba(0,0,0,0.3)' in text:
        text = text.replace('background: rgba(0,0,0,0.3);', 'background: var(--bg-secondary);')
        modified = True
    if 'rgba(0, 0, 0, 0.4)' in text:
        text = text.replace('background: rgba(0, 0, 0, 0.4);', 'background: var(--bg-secondary);')
        modified = True
    
    # In dashboard.html: update header gradients
    if 'dashboard.html' in fpath:
        old_dash_grad = 'background: linear-gradient(135deg, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%);'
        new_dash_grad = 'background: linear-gradient(135deg, rgba(122, 16, 40, 0.05) 0%, rgba(217, 119, 6, 0.08) 100%);'
        if old_dash_grad in text:
            text = text.replace(old_dash_grad, new_dash_grad)
            modified = True
        
        # Other gradients in dashboard headers
        text = re.sub(
            r'background:\s*linear-gradient\(135deg,\s*rgba\((?:56,\s*189,\s*248|167,\s*139,\s*250|94,\s*234,\s*212|239,\s*68,\s*68|245,\s*158,\s*11)[^)]+\)\s*0%,\s*rgba\([^)]+\)\s*100%\);',
            'background: linear-gradient(135deg, rgba(122, 16, 40, 0.05) 0%, rgba(217, 119, 6, 0.08) 100%);',
            text
        )
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated contrast in {fpath}")

print("HTML contrast updates complete.")

