with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.hero-stage {')
print(text[idx:idx+1200])

