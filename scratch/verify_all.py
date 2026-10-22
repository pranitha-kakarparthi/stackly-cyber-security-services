import os
import re
import glob

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

print(f"Scanning {len(html_files)} HTML files...")

errors = []
total_links = 0
total_images = 0

for file_path in html_files:
    dir_name = os.path.dirname(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check 404 rules
    if '404.html' in file_path:
        if '<header' in content or '<nav' in content:
            errors.append(f"{file_path}: 404 page contains <header> or <nav> tag!")
        if '<footer' in content:
            errors.append(f"{file_path}: 404 page contains <footer> tag!")
        if 'vortex-page-wrap' not in content and 'error-page-wrap' not in content:
            errors.append(f"{file_path}: 404 page missing centered vortex page wrap!")

    # Check Logo behavior (where img is directly inside the a tag)
    logo_matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>\s*<img[^>]*logoStackly[^>]*>', content)
    for target in logo_matches:
        if dir_name == '':
            if target != 'index.html':
                errors.append(f"{file_path}: Root logo does not link to index.html (links to {target})")
        else:
            if target != '../index.html' and target != 'index.html':
                errors.append(f"{file_path}: Subpage logo does not link to ../index.html (links to {target})")

    # Check href attributes
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        if href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('http'):
            continue
        total_links += 1
        clean_href = href.split('?')[0].split('#')[0]
        if not clean_href:
            continue
        target_path = os.path.normpath(os.path.join(dir_name, clean_href))
        if not os.path.exists(target_path):
            errors.append(f"{file_path}: Broken href target -> {clean_href} (resolved to {target_path})")

    # Check img src attributes
    srcs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content)
    for src in srcs:
        if src.startswith('data:') or src.startswith('http'):
            continue
        total_images += 1
        clean_src = src.split('?')[0].split('#')[0]
        target_path = os.path.normpath(os.path.join(dir_name, clean_src))
        if not os.path.exists(target_path):
            errors.append(f"{file_path}: Broken image src -> {clean_src} (resolved to {target_path})")

    # Check script src attributes
    scripts = re.findall(r'<script\s+[^>]*src=["\']([^"\']+)["\']', content)
    for script in scripts:
        if script.startswith('http'):
            continue
        clean_script = script.split('?')[0]
        target_path = os.path.normpath(os.path.join(dir_name, clean_script))
        if not os.path.exists(target_path):
            errors.append(f"{file_path}: Broken script src -> {clean_script} (resolved to {target_path})")

    # Check link href attributes (stylesheets)
    css_links = re.findall(r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\']', content)
    for css in css_links:
        clean_css = css.split('?')[0]
        target_path = os.path.normpath(os.path.join(dir_name, clean_css))
        if not os.path.exists(target_path):
            errors.append(f"{file_path}: Broken CSS link -> {clean_css} (resolved to {target_path})")

print(f"\nVerification Results:")
print(f"Total HTML files verified: {len(html_files)}")
print(f"Total links verified: {total_links}")
print(f"Total images verified: {total_images}")

if errors:
    print(f"\nFAILED with {len(errors)} issues:")
    for err in errors:
        print(f"  - {err}")
    exit(1)
else:
    print("\nALL CHECKS PASSED PERFECTLY! 100% Valid Links, Images, Stylesheets, Logo Redirections, and 404 Layouts.")
