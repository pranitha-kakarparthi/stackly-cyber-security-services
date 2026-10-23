import glob
import os
import re

print("=" * 60)
print("1. SECTION COUNT VERIFICATION")
print("=" * 60)
html_files = ['index.html', '404.html'] + sorted(glob.glob('pages/*.html'))
exempt_pages = ['404.html', 'pages/404.html', 'pages/contact.html', 'pages/sign-in.html', 'pages/sign-up.html']

all_sections_pass = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    count = len(re.findall(r'<section\b[^>]*>', c))
    f_norm = f.replace('\\', '/')
    is_exempt = f_norm in exempt_pages
    min_req = 0 if is_exempt else 8
    passed = count >= min_req
    if not passed:
        all_sections_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {f}: {count} sections (Req: {'>=8' if not is_exempt else 'Exempt'})")

print("\n" + "=" * 60)
print("2. IMAGE SIZES AND FORMATS (<100KB, .webp)")
print("=" * 60)
img_files = glob.glob('assets/images/*')
all_imgs_pass = True
for img in img_files:
    size = os.path.getsize(img)
    ext = os.path.splitext(img)[1].lower()
    is_webp = ext == '.webp'
    is_under_100k = size < 100 * 1024
    passed = is_webp and is_under_100k
    if not passed:
        all_imgs_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {os.path.basename(img)}: {size/1024:.1f} KB (Format: {ext})")

print("\n" + "=" * 60)
print("3. BACK TO TOP BUTTON AND RADAR ANIMATION")
print("=" * 60)
all_btt_pass = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_btt = 'class="back-to-top"' in c or 'class=\'back-to-top\'' in c
    if not has_btt:
        all_btt_pass = False
    print(f"[{'PASS' if has_btt else 'FAIL'}] {f} has back-to-top button")

with open('assets/css/style.css', 'r', encoding='utf-8') as fp:
    css = fp.read()

has_btt_anim = 'backToTopPulse' in css and 'backToTopFloat' in css and 'arrowBounce' in css
print(f"[{'PASS' if has_btt_anim else 'FAIL'}] CSS defines backToTopPulse, backToTopFloat, arrowBounce")

print("\n" + "=" * 60)
print("4. HERO ENHANCEMENTS AND CYBER VISUALS")
print("=" * 60)
hero_pages = [
    'index.html',
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
all_heroes_pass = True
for hp in hero_pages:
    with open(hp, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_hero_grid = 'page-hero-grid' in c or 'hero-sentinel-stage' in c
    has_pills = 'hero-floating-pill' in c
    has_radar = 'hero-visual-radar' in c or 'sentinel-ambient-glow' in c
    passed = has_hero_grid and has_pills and has_radar
    if not passed:
        all_heroes_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {hp}: Grid={has_hero_grid}, Pills={has_pills}, Radar/Glow={has_radar}")

print("\n" + "=" * 60)
print("5. CONTACT LOCATION REDIRECT TO 404")
print("=" * 60)
with open('pages/contact.html', 'r', encoding='utf-8') as fp:
    contact_c = fp.read()
loc_redirect = 'href="404.html"' in contact_c and 'View Location Map' in contact_c
print(f"[{'PASS' if loc_redirect else 'FAIL'}] pages/contact.html redirects Location card to 404.html")

print("\n" + "=" * 60)
print("SUMMARY OVERALL: " + ("ALL PASSED!" if (all_sections_pass and all_imgs_pass and all_btt_pass and has_btt_anim and all_heroes_pass and loc_redirect) else "SOME FAILED!"))
print("=" * 60)

