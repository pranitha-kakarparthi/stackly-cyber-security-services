with open('assets/js/auth.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of auth.js:", len(text))
print("Has loader references in auth.js:", 'page-loader' in text or 'loader' in text)

