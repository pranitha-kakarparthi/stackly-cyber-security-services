with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
labels = re.findall(r'<label[^>]*>(.*?)</label>', text)
print("Labels in sign-in.html:", labels)
inputs = re.findall(r'<input[^>]*>', text)
print("Inputs in sign-in.html:", len(inputs))
for inp in inputs:
    print("  ", inp)

