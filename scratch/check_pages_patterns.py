import glob
import re

files = [
    'pages/about.html',
    'pages/services.html',
    'pages/pricing.html',
    'pages/contact.html',
    'pages/service-soc.html',
    'pages/service-pentest.html',
    'pages/service-cloud-security.html',
    'pages/service-incident-response.html',
    'pages/service-vulnerability-management.html',
    'pages/service-compliance.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    dd = re.search(r'<ul class="dropdown-menu">[\s\S]*?</ul>', text)
    ft = re.search(r'<div class="footer-links-col">\s*<h4 class="footer-heading">Defense Services</h4>[\s\S]*?</ul>\s*</div>', text)
    print(f"{p}: Dropdown: {bool(dd)}, Footer: {bool(ft)}")

