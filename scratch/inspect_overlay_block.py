with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Inspect current mobile-nav-overlay block
idx = css.find('.mobile-nav-overlay {')
idx_end = css.find('/* Ambient Holographic Floating Ribbons', idx)
print("=== Current mobile-nav-overlay block ===")
print(css[idx:idx_end])

