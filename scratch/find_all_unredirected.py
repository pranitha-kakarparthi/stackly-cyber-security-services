import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

for path in html_files:
    is_root = ('/' not in path and '\\' not in path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # find all a tags
    matches = re.finditer(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', text, re.DOTALL)
    unredirected = []
    for m in matches:
        href = m.group(1).strip()
        label = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        label_clean = ' '.join(label.split())
        
        # skip skip-link and hashes
        if href.startswith('#') or href.startswith('javascript:'):
            continue
        
        # What is allowed as primary quick links?
        allowed_root = ['index.html', 'pages/about.html', 'pages/services.html', 'pages/pricing.html', 'pages/contact.html', 'pages/sign-in.html', 'pages/sign-up.html', 'pages/dashboard.html', '404.html']
        allowed_pages = ['../index.html', 'about.html', 'services.html', 'pricing.html', 'contact.html', 'sign-in.html', 'sign-up.html', 'dashboard.html', '404.html', '../404.html', '../pages/404.html']
        
        target = href.split('?')[0].split('#')[0]
        if is_root:
            if target not in allowed_root:
                unredirected.append((href, label_clean))
        else:
            if target not in allowed_pages:
                unredirected.append((href, label_clean))
                
    if unredirected:
        print(f"=== {path} ({len(unredirected)} unredirected links) ===")
        for h, l in unredirected[:8]:
            print(f"   href='{h}'  label='{l}'")

