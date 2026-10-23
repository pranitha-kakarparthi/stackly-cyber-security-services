with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Need a Custom Scoped Proposal')
print(repr(text[idx+400:idx+800]))

