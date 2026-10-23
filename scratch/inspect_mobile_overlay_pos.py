with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('mobile-nav-overlay')
print(idx)
print(text[idx-50:idx+1500].encode('ascii', errors='replace').decode('ascii'))

