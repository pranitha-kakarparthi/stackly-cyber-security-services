with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<div class="container hero-stage-container">')
print(text[idx:idx+2000])

