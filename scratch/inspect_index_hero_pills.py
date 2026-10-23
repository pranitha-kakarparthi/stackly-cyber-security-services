with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('hero-sentinel-frame')
print(text[idx-50:idx+800])

