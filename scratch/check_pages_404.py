with open('pages/404.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('vortex-bg-image in pages/404.html:', 'vortex-bg-image' in text)
print('404 image path:', [l.strip() for l in text.splitlines() if 'vortex-404' in l])

