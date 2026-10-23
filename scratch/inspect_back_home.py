with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('auth-form-side')
print("=== sign-in.html around auth-form-side ===")
print(text[idx-50:idx+600].encode('ascii', errors='replace').decode('ascii'))

with open('pages/sign-up.html', 'r', encoding='utf-8') as f:
    text_up = f.read()

idx_up = text_up.find('auth-form-side')
print("\n=== sign-up.html around auth-form-side ===")
print(text_up[idx_up-50:idx_up+600].encode('ascii', errors='replace').decode('ascii'))

