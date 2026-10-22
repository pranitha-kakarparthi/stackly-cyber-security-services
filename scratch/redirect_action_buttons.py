import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="pages/services.html" class="btn btn-pill-glass btn-lg"', 'href="404.html" class="btn btn-pill-glass btn-lg"')
html = html.replace('href="pages/contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')
html = html.replace('href="pages/service-soc.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="pages/service-pentest.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="pages/service-cloud-security.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="pages/service-incident-response.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="pages/contact.html" class="btn btn-primary btn-block"', 'href="404.html" class="btn btn-primary btn-block"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in index.html")

# 2. Update pages/about.html
with open('pages/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')
html = html.replace('href="pricing.html" class="btn btn-outline btn-lg"', 'href="404.html" class="btn btn-outline btn-lg"')
html = html.replace('href="contact.html" class="btn btn-outline btn-sm"', 'href="404.html" class="btn btn-outline btn-sm"')

with open('pages/about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/about.html")

# 3. Update pages/pricing.html
with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')
html = html.replace('href="contact.html" class="btn btn-outline btn-lg"', 'href="404.html" class="btn btn-outline btn-lg"')

with open('pages/pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/pricing.html")

# 4. Update pages/service-cloud-security.html
with open('pages/service-cloud-security.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')

with open('pages/service-cloud-security.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/service-cloud-security.html")

# 5. Update pages/service-incident-response.html
with open('pages/service-incident-response.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')

with open('pages/service-incident-response.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/service-incident-response.html")

# 6. Update pages/service-pentest.html
with open('pages/service-pentest.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')

with open('pages/service-pentest.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/service-pentest.html")

# 7. Update pages/service-soc.html
with open('pages/service-soc.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="contact.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')

with open('pages/service-soc.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/service-soc.html")

# 8. Update pages/services.html
with open('pages/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="service-soc.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="service-pentest.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="service-cloud-security.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="service-incident-response.html" class="btn btn-outline btn-block btn-sm"', 'href="404.html" class="btn btn-outline btn-block btn-sm"')
html = html.replace('href="pricing.html" class="btn btn-primary btn-lg"', 'href="404.html" class="btn btn-primary btn-lg"')
html = html.replace('href="contact.html" class="btn btn-outline btn-lg"', 'href="404.html" class="btn btn-outline btn-lg"')

with open('pages/services.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated action CTAs in pages/services.html")

