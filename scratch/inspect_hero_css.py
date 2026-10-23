with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.page-hero-grid')
if idx != -1:
    print(text[idx:idx+2500])
else:
    print("page-hero-grid not found")
