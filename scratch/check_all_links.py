import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

# Allowed primary navigation links:
# From root (e.g. index.html):
#   index.html, pages/about.html, pages/services.html, pages/pricing.html, pages/contact.html, pages/sign-in.html, pages/sign-up.html, pages/dashboard.html, 404.html
# From pages/ (e.g. pages/about.html):
#   ../index.html, about.html, services.html, pricing.html, contact.html, sign-in.html, sign-up.html, dashboard.html, 404.html

for path in html_files:
    is_root = ('/' not in path and '\\' not in path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\']', text)
    non_nav = []
    for href in links:
        if href.startswith('#') or href.startswith('tel:') or href.startswith('mailto:'):
            continue
        # normalize
        clean = href.split('?')[0].split('#')[0]
        # check if it's main nav or 404
        valid_targets = ['index.html', 'about.html', 'services.html', 'pricing.html', 'contact.html', 'sign-in.html', 'sign-up.html', 'dashboard.html', '404.html', '../index.html', '../404.html']
        target_name = clean.split('/')[-1]
        if target_name not in valid_targets:
            non_nav.append(href)
    print(f"{path:35}: total links={len(links)}, non-standard={set(non_nav)}")

