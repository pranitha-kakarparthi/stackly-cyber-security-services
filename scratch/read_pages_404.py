with open('pages/404.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("pages/404.html length:", len(text))
for l in text.splitlines()[:30]:
    print(l)

