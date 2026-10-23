with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('/* Laptop / Desktop (<= 1024px) */')
print(css[idx:idx+1500])

