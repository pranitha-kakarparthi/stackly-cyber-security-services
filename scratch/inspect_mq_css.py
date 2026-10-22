with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

mq_start = css.find('/* ==========================================================================\n   DASHBOARD RESPONSIVENESS')
print(css[mq_start:])

