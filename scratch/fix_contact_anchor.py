with open('pages/contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<section class="section section-alt" aria-label="Direct Message Form">'
replacement = '<section id="contact-form-section" class="section section-alt" aria-label="Direct Message Form">'

if target in c:
    c = c.replace(target, replacement)
    with open('pages/contact.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed contact-form-section id in pages/contact.html")
else:
    print("Target not found!")

