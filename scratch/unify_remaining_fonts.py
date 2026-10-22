with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('.metric-number {\n  font-size: 1.85rem;\n  font-weight: 800;\n  color: var(--primary);\n  line-height: 1.1;\n  font-family: var(--font-mono);',
              '.metric-number {\n  font-size: 1.85rem;\n  font-weight: 800;\n  color: var(--primary);\n  line-height: 1.1;\n  font-family: var(--font-sans);')
c = c.replace('.pricing-cost {\n  display: flex;\n  align-items: baseline;\n  gap: 0.35rem;\n  margin-bottom: 2rem;\n  font-family: var(--font-mono);',
              '.pricing-cost {\n  display: flex;\n  align-items: baseline;\n  gap: 0.35rem;\n  margin-bottom: 2rem;\n  font-family: var(--font-sans);')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(c)

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dc = f.read()

dc = dc.replace('.dash-stat-val {\n  font-size: 1.5rem;\n  font-weight: 800;\n  font-family: var(--font-mono);',
                '.dash-stat-val {\n  font-size: 1.5rem;\n  font-weight: 800;\n  font-family: var(--font-sans);')

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(dc)

print('Updated .metric-number, .pricing-cost, and .dash-stat-val to var(--font-sans).')

