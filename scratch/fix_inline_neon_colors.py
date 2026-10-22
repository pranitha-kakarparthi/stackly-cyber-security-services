# Fix pricing.html
with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('style="color: #ff6b6b; font-family: var(--font-mono);"', 'style="color: var(--danger); font-family: var(--font-mono);"')
with open('pages/pricing.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Fix service-incident-response.html
with open('pages/service-incident-response.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('border-color: rgba(239, 68, 68, 0.4); color: #ff6b6b;', 'border-color: rgba(190, 18, 60, 0.4); color: var(--danger);')
c = c.replace('color: #ff6b6b; border-color: rgba(239, 68, 68, 0.4);', 'color: var(--danger); border-color: rgba(190, 18, 60, 0.4);')
with open('pages/service-incident-response.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Fix service-soc.html
with open('pages/service-soc.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('style="color: #ff6b6b;"', 'style="color: var(--danger);"')
c = c.replace('style="color: #fbbf24;"', 'style="color: var(--warning);"')
with open('pages/service-soc.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Fix dashboard.html
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('style="color: #fbbf24;"', 'style="color: var(--warning);"')
c = c.replace('style="background: #ff6b6b;"', 'style="background: var(--danger);"')
c = c.replace('style="background: #fbbf24;"', 'style="background: var(--warning);"')
with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated inline color styles in HTML files.')

