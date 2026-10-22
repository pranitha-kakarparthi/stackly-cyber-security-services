with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

def show_rule(selector):
    pattern = r'(' + re.escape(selector) + r'\s*\{[^}]+\})'
    m = re.search(pattern, text)
    if m:
        print(f"=== {selector} ===")
        print(m.group(0))
    else:
        print(f"Not found: {selector}")

show_rule('.btn-primary,')
show_rule('.btn-secondary,')
show_rule('.btn-outline')
show_rule('.btn-ghost')
show_rule('.form-control')
show_rule('.cyber-sim-box')
show_rule('.pricing-card.featured')
show_rule('.hero-subtext')
show_rule('.ambient-ribbons-container')

