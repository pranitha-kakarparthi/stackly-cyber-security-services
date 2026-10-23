with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('/* Mobile Large (<= 425px) */')
idx_end = css.find('/* Mobile Small (320px - 375px) */', idx)
print("=== Current @media (max-width: 425px) block ===")
print(css[idx:idx_end])

