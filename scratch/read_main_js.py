with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of main.js:", len(text))
print("Sample of main.js:")
print(text[:1000])

