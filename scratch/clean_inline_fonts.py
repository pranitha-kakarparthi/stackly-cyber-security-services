# Clean contact.html
with open('pages/contact.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('style="font-size: 1.25rem; font-weight: 700; font-family: var(--font-mono); color: var(--primary);"', 
              'style="font-size: 1.25rem; font-weight: 700; color: var(--primary);"')
with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Clean pricing.html
with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('style="color: var(--danger); font-family: var(--font-mono);"', 'style="color: var(--danger);"')
c = c.replace('style="color: var(--primary); font-family: var(--font-mono);"', 'style="color: var(--primary);"')
c = c.replace('style="color: var(--accent); font-family: var(--font-mono); font-size: 1.25rem;"', 'style="color: var(--accent); font-size: 1.25rem;"')
with open('pages/pricing.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Cleaned inline font-family overrides.')

