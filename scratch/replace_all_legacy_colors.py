with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Precise replacements
replacements = [
    # Loader
    ('filter: drop-shadow(0 0 16px rgba(0, 240, 118, 0.4));', 'filter: drop-shadow(0 0 16px rgba(122, 16, 40, 0.25));'),
    ('border: 3px solid rgba(0, 240, 118, 0.15);', 'border: 3px solid rgba(122, 16, 40, 0.15);'),
    ('box-shadow: 0 0 15px rgba(0, 240, 118, 0.25);', 'box-shadow: 0 0 15px rgba(122, 16, 40, 0.15);'),
    ('border: 1px dashed rgba(0, 240, 118, 0.35);', 'border: 1px dashed rgba(217, 119, 6, 0.35);'),

    # Button shadows
    ('box-shadow: 0 6px 28px rgba(94, 234, 212, 0.6);', 'box-shadow: 0 6px 28px rgba(122, 16, 40, 0.35);'),
    ('box-shadow: 0 6px 22px rgba(167, 139, 250, 0.35);', 'box-shadow: 0 6px 22px rgba(158, 42, 68, 0.25);'),
    ('background: rgba(94, 234, 212, 0.08);', 'background: rgba(122, 16, 40, 0.08);'),
    ('box-shadow: 0 0 18px rgba(94, 234, 212, 0.25);', 'box-shadow: 0 0 18px rgba(122, 16, 40, 0.15);'),
    ('box-shadow: 0 6px 24px rgba(167, 139, 250, 0.55);', 'box-shadow: 0 6px 24px rgba(158, 42, 68, 0.3);'),

    # Navbar
    ('border-color: rgba(94, 234, 212, 0.3);', 'border-color: rgba(122, 16, 40, 0.25);'),
    ('filter: drop-shadow(0 0 10px rgba(94, 234, 212, 0.3));', 'filter: drop-shadow(0 0 10px rgba(122, 16, 40, 0.15));'),
    ('background: rgba(94, 234, 212, 0.1);', 'background: rgba(122, 16, 40, 0.08);'),
    ('box-shadow: inset 0 0 0 1px rgba(94, 234, 212, 0.3);', 'box-shadow: inset 0 0 0 1px rgba(122, 16, 40, 0.25);'),
    ('background: rgba(94, 234, 212, 0.14);', 'background: rgba(122, 16, 40, 0.12);'),
    ('background: rgba(94, 234, 212, 0.12);', 'background: rgba(122, 16, 40, 0.09);'),

    # Page hero
    ('background: radial-gradient(circle at 50% 0%, rgba(0, 240, 118, 0.1) 0%, transparent 65%);',
     'background: radial-gradient(circle at 50% 0%, rgba(122, 16, 40, 0.06) 0%, transparent 65%);'),

    # Form focus
    ('box-shadow: 0 0 0 3px rgba(0, 240, 118, 0.2);', 'box-shadow: 0 0 0 3px rgba(122, 16, 40, 0.2);'),

    # Auth
    ('filter: drop-shadow(0 0 12px rgba(94, 234, 212, 0.45));', 'filter: drop-shadow(0 0 12px rgba(122, 16, 40, 0.25));'),
    ('background: radial-gradient(circle at 30% 30%, rgba(0, 240, 118, 0.12) 0%, transparent 60%);',
     'background: radial-gradient(circle at 30% 30%, rgba(217, 119, 6, 0.12) 0%, transparent 60%);'),

    # 404 page
    ('radial-gradient(ellipse 80% 60% at 50% 50%, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.06) 50%, transparent 80%);',
     'radial-gradient(ellipse 80% 60% at 50% 50%, rgba(122, 16, 40, 0.12) 0%, rgba(217, 119, 6, 0.06) 50%, transparent 80%);'),
    ('radial-gradient(circle at 20px 20px, rgba(94, 234, 212, 0.22) 1.5px, transparent 2px),',
     'radial-gradient(circle at 20px 20px, rgba(122, 16, 40, 0.22) 1.5px, transparent 2px),'),
    ('radial-gradient(circle at 60px 60px, rgba(167, 139, 250, 0.22) 1.5px, transparent 2px);',
     'radial-gradient(circle at 60px 60px, rgba(217, 119, 6, 0.22) 1.5px, transparent 2px);'),
    ('filter: drop-shadow(0 0 45px rgba(167, 139, 250, 0.25));', 'filter: drop-shadow(0 0 45px rgba(122, 16, 40, 0.25));'),
    ('text-shadow: 0 0 40px rgba(255, 255, 255, 0.5), 0 0 70px rgba(167, 139, 250, 0.4);',
     'text-shadow: 0 0 40px rgba(255, 255, 255, 0.8), 0 0 70px rgba(217, 119, 6, 0.35);'),
    ('text-shadow: 0 4px 20px rgba(0, 0, 0, 0.95), 0 0 30px rgba(94, 234, 212, 0.65);',
     'text-shadow: 0 4px 20px rgba(58, 1, 14, 0.65), 0 0 30px rgba(217, 119, 6, 0.45);'),
    ('background: linear-gradient(90deg, #ff3366, #fbbf24, #9333ea, #00f076);',
     'background: linear-gradient(90deg, #7A1028, #D97706, #9E2A44, #F5A623);'),
    ('filter: drop-shadow(0 0 14px rgba(0, 240, 118, 0.35));', 'filter: drop-shadow(0 0 14px rgba(122, 16, 40, 0.25));'),

    # Pricing table highlight
    ('background: rgba(94, 234, 212, 0.04);', 'background: rgba(122, 16, 40, 0.04);'),
    ('border-left: 1px solid rgba(94, 234, 212, 0.25);', 'border-left: 1px solid rgba(122, 16, 40, 0.25);'),
    ('border-right: 1px solid rgba(94, 234, 212, 0.25);', 'border-right: 1px solid rgba(122, 16, 40, 0.25);'),
    ('background: rgba(94, 234, 212, 0.09);', 'background: rgba(122, 16, 40, 0.08);'),
]

count = 0
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        count += 1
    else:
        print(f"Not found: {old}")

print(f"Successfully performed {count} color upgrades.")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

