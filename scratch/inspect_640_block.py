with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('@media (max-width: 640px)')
idx_end = css.find('/* ==========================================================================\n   404 ERROR PAGE STYLES', idx)
print("=== Current @media (max-width: 640px) block ===")
print(css[idx:idx_end])

