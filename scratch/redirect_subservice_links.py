import glob

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

for path in html_files:
    is_root = ('/' not in path and '\\' not in path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if is_root:
        text = text.replace('href="pages/service-soc.html"', 'href="404.html"')
        text = text.replace('href="pages/service-pentest.html"', 'href="404.html"')
        text = text.replace('href="pages/service-cloud-security.html"', 'href="404.html"')
        text = text.replace('href="pages/service-incident-response.html"', 'href="404.html"')
    else:
        text = text.replace('href="service-soc.html"', 'href="404.html"')
        text = text.replace('href="service-pentest.html"', 'href="404.html"')
        text = text.replace('href="service-cloud-security.html"', 'href="404.html"')
        text = text.replace('href="service-incident-response.html"', 'href="404.html"')
        text = text.replace('href="../pages/service-soc.html"', 'href="404.html"')
        text = text.replace('href="../pages/service-pentest.html"', 'href="404.html"')
        text = text.replace('href="../pages/service-cloud-security.html"', 'href="404.html"')
        text = text.replace('href="../pages/service-incident-response.html"', 'href="404.html"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated subservice links to 404 in {path}")

