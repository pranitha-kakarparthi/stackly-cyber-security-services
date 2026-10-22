with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('color: #ff6b6b; margin-bottom: 0.35rem;', 'color: var(--danger); font-weight: 700; margin-bottom: 0.35rem;')
c = c.replace('color: #fbbf24; margin-bottom: 0.35rem;', 'color: var(--warning); font-weight: 700; margin-bottom: 0.35rem;')

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated remaining badge colors in dashboard.html')

