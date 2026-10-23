import os
import glob
import re

files_updated = []

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace in navbar
idx_content_new = re.sub(
    r'(<a[^>]*class="nav-brand"[^>]*>[\s\S]*?<img[^>]*src=")assets/images/logoStackly\.webp(")',
    r'\1assets/images/logoStackly-wine.webp\2',
    idx_content
)
# Replace in mobile overlay
idx_content_new = re.sub(
    r'(<a[^>]*class="mobile-brand-link"[^>]*>[\s\S]*?<img[^>]*src=")assets/images/logoStackly\.webp(")',
    r'\1assets/images/logoStackly-wine.webp\2',
    idx_content_new
)
if idx_content_new != idx_content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_content_new)
    files_updated.append('index.html')

# 2. Update pages/*.html
for p in sorted(glob.glob('pages/*.html')):
    if '404' in p or 'dashboard' in p or 'sign-in' in p or 'sign-up' in p:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace in navbar
    new_content = re.sub(
        r'(<a[^>]*class="nav-brand"[^>]*>[\s\S]*?<img[^>]*src=")[\./]*assets/images/logoStackly\.webp(")',
        r'\1../assets/images/logoStackly-wine.webp\2',
        content
    )
    # Replace in mobile overlay
    new_content = re.sub(
        r'(<a[^>]*class="mobile-brand-link"[^>]*>[\s\S]*?<img[^>]*src=")[\./]*assets/images/logoStackly\.webp(")',
        r'\1../assets/images/logoStackly-wine.webp\2',
        new_content
    )
    if new_content != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_updated.append(p)

print(f"Updated {len(files_updated)} files:")
for f in files_updated:
    print(" -", f)

