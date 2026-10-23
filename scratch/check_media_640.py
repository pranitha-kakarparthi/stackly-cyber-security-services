with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('@media (max-width: 640px)')
print(css[idx:idx+1200])

