import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of sign-in.html:", len(text))
for m in text.split('\n')[:50]:
    print(m)

