with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('.page-hero')
print("Position:", idx)
print(text[idx-200:idx+800])
