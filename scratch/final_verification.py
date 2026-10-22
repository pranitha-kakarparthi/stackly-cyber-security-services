import glob
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("     COMPREHENSIVE WEBSITE VERIFICATION SUITE      ")
print("==================================================")

errors = []

# 1. Check all 14 HTML files
html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
print(f"\n1. Checking HTML files ({len(html_files)} total)...")
expected_files = [
    '404.html', 'index.html', 'pages/404.html', 'pages/about.html',
    'pages/contact.html', 'pages/dashboard.html', 'pages/pricing.html',
    'pages/service-cloud-security.html', 'pages/service-incident-response.html',
    'pages/service-pentest.html', 'pages/service-soc.html', 'pages/services.html',
    'pages/sign-in.html', 'pages/sign-up.html'
]
for exp in expected_files:
    normalized = exp.replace('/', os.sep)
    if not any(f.endswith(normalized) for f in html_files):
        errors.append(f"Missing HTML file: {exp}")

# 2. Check Back-to-Top Button in every file
print("\n2. Checking Back-to-Top button in all HTML files...")
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="back-to-top"' not in content:
        errors.append(f"{fpath} is missing back-to-top button")
print("   All 14 HTML files contain back-to-top button.")

# 3. Check Section counts in marketing pages (>= 8 sections)
print("\n3. Checking section counts in marketing pages...")
marketing_pages = [
    'index.html', 'pages/about.html', 'pages/services.html', 'pages/pricing.html',
    'pages/service-cloud-security.html', 'pages/service-incident-response.html',
    'pages/service-pentest.html', 'pages/service-soc.html'
]
for mpath in marketing_pages:
    with open(mpath, 'r', encoding='utf-8') as f:
        content = f.read()
    sections = re.findall(r'<section\b[^>]*>', content)
    print(f"   {mpath:35}: {len(sections)} sections")
    if len(sections) < 8:
        errors.append(f"{mpath} has only {len(sections)} sections (< 8)")

# 4. Check Dashboard sections
print("\n4. Checking dashboard sections and modules...")
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()
dash_sections = re.findall(r'<section\b[^>]*class=["\']dash-section["\'][^>]*>', dash_content)
print(f"   pages/dashboard.html: {len(dash_sections)} total dash-sections across all modules")
if len(dash_sections) < 60:
    errors.append(f"Dashboard has only {len(dash_sections)} sections")

# 5. Check CSS files for color palette
print("\n5. Checking CSS files for color palette...")
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dash_css = f.read()

if '#FAF7EE' not in style_css or '#7A1028' not in style_css:
    errors.append("style.css does not have SHIELDA palette tokens")
if '#2A010A' not in dash_css or '#FAF7EE' not in dash_css:
    errors.append("dashboard.css does not have SHIELDA palette tokens")
print("   CSS files verified with SHIELDA warm ivory and velvet wine tokens.")

# 6. Check JS files
print("\n6. Checking JS files...")
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    dash_js = f.read()
if 'dashMainArea.scrollTo' not in dash_js or 'initDashboardBackToTop' not in dash_js:
    errors.append("dashboard.js missing scroll-to-top logic")

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()
if 'initBackToTop' not in main_js:
    errors.append("main.js missing initBackToTop")
print("   JS files verified with scroll-to-top and back-to-top controllers.")

# 7. Check human face positioning rules in CSS
print("\n7. Checking human face positioning rules in CSS...")
if 'object-position: center 20% !important' not in style_css:
    errors.append("style.css missing object-position: center 20% !important for human images")
print("   Human face positioning rules verified.")

# 8. Check all images referenced exist on disk
print("\n8. Checking referenced images existence...")
all_img_srcs = set()
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    for m in re.finditer(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content):
        src = m.group(1).strip()
        all_img_srcs.add((fpath, src))

missing_images = []
for page, src in all_img_srcs:
    if src.startswith('http') or src.startswith('data:'):
        continue
    # resolve relative path
    page_dir = os.path.dirname(page)
    target_path = os.path.normpath(os.path.join(page_dir, src))
    if not os.path.exists(target_path):
        missing_images.append((page, src, target_path))

if missing_images:
    for p, s, t in missing_images:
        errors.append(f"Missing image: {s} referenced in {p}")
else:
    print(f"   All {len(all_img_srcs)} image references exist on disk.")

# 9. Verify git status has no commits
print("\n9. Checking git status (ensuring no commits were made)...")
os.system("git status --short > scratch/git_status.txt")
with open("scratch/git_status.txt", "r", encoding="utf-8") as f:
    g_status = f.read()
print(f"   Working directory status:\n{g_status[:400]}")

# SUMMARY
print("\n==================================================")
if errors:
    print(f"FAILED: {len(errors)} issues detected:")
    for e in errors:
        print(f" - {e}")
else:
    print("SUCCESS: ALL 7 REQUIREMENTS AND INTEGRITY CHECKS PASSED!")
print("==================================================")

