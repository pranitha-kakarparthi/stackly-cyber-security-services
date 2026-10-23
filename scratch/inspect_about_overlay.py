with open('pages/about.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('mobile-nav-overlay')
print(idx)
print(text[idx-100:idx+800].encode('ascii', errors='replace').decode('ascii'))

