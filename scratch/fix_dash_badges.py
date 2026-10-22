with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('background: rgba(56, 189, 248, 0.2); border-color: rgba(56, 189, 248, 0.4);',
                    'background: rgba(122, 16, 40, 0.08); border-color: rgba(122, 16, 40, 0.25); color: var(--primary);')
text = text.replace('style="background: #38bdf8;"', 'style="background: var(--accent);"')

text = text.replace('background: rgba(167, 139, 250, 0.2); border-color: rgba(167, 139, 250, 0.4);',
                    'background: rgba(122, 16, 40, 0.08); border-color: rgba(122, 16, 40, 0.25); color: var(--primary);')
text = text.replace('style="background: #a78bfa;"', 'style="background: var(--accent);"')

text = text.replace('background: rgba(167, 139, 250, 0.15); border-color: rgba(167, 139, 250, 0.35); color: #a78bfa; margin-bottom: 0.35rem;',
                    'background: rgba(122, 16, 40, 0.08); border-color: rgba(122, 16, 40, 0.25); color: var(--primary); margin-bottom: 0.35rem;')

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated dashboard badge tags to high-contrast velvet wine and amber.")

