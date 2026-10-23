with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('auth-form-side')
print(repr(text[idx-10:idx+80]))

