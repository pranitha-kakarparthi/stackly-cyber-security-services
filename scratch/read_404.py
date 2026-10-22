import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('404.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of 404.html:", len(text))
print("Content of 404.html:")
print(text)

