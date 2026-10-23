import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find the two floating pills inside hero-sentinel-frame
pattern = r'\s*<div class="hero-floating-pill pill-top-left"[^>]*>[\s\S]*?</div>\s*<div class="hero-floating-pill pill-bottom-right"[^>]*>[\s\S]*?</div>'

new_text, count = re.subn(pattern, '', text)
print(f"Substitutions made: {count}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

