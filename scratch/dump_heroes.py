import re

pages = [
    'pages/about.html',
    'pages/services.html',
    'pages/pricing.html',
    'pages/contact.html',
    'pages/service-soc.html',
    'pages/service-pentest.html',
    'pages/service-cloud-security.html',
    'pages/service-incident-response.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>[\s\S]*?</section>)', text)
    if m:
        print(f"=== {p} ===")
        print(m.group(1).encode('ascii', errors='replace').decode('ascii'))
        print("--------------------------------------------------")

