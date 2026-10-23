with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.mobile-nav-overlay')
print(css[idx:idx+2500])

