with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('/* Laptop / Desktop (<= 1024px) */')
idx_end = css.find('/* Tablet (<= 768px) */', idx)
print("=== Current @media (max-width: 1024px) block ===")
print(css[idx:idx_end])

