with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<section class="hero-stage"')
print(text[idx:idx+3500])

