with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:45], start=1):
    print(f"{i:2}: {repr(l)}")

