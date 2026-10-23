with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('/* Tablet (<= 768px) */')
print(css[idx:idx+2500])

