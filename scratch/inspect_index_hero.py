with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<section class="hero')
end = text.find('</section>', start) + 10
print(text[start:end])

