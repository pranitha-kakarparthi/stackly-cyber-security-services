import glob
import os
import re

print("============================================================")
print("COMPREHENSIVE WEBSITE AUDIT & VERIFICATION SUITE")
print("============================================================")

html_files = ['index.html', '404.html'] + sorted(glob.glob('pages/*.html'))
exempt_pages = ['404.html', 'pages/404.html', 'pages/contact.html', 'pages/sign-in.html', 'pages/sign-up.html']

# 1. Section Counts
print("\n--- 1. SECTION COUNT VERIFICATION (>=8 for marketing/services) ---")
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

# 2. Image Constraints (<100KB, .webp)
print("\n--- 2. IMAGE FORMAT & SIZE CHECK (<100KB, .webp) ---")
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

# 3. Logo in Menus (Must be wine logo for high contrast on light navbar/drawer)
print("\n--- 3. MENU BAR LOGO VISIBILITY (Must use logoStackly-wine.webp) ---")
nav_pages = [
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
all_logos_pass = True
for np in nav_pages:
    with open(np, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_nav_wine = 'logoStackly-wine.webp' in c
    has_header_logo = re.search(r'class="nav-brand"[^>]*>[\s\S]*?logoStackly-wine\.webp', c) is not None
    has_mobile_logo = re.search(r'class="mobile-brand-link"[^>]*>[\s\S]*?logoStackly-wine\.webp', c) is not None
    passed = has_header_logo and has_mobile_logo
    if not passed:
        all_logos_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {np}: Header={has_header_logo}, MobileDrawer={has_mobile_logo}")

# 4. Auth Pages Back to Home in Header
print("\n--- 4. AUTH PAGES MOBILE BACK-TO-HOME BUTTON ---")
auth_pages = ['pages/sign-in.html', 'pages/sign-up.html']
all_auth_pass = True
for ap in auth_pages:
    with open(ap, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_banner_back = 'auth-banner-back-btn' in c and 'Back to Home' in c
    has_form_back = 'Back to Home' in c and 'auth-nav-top' in c
    passed = has_banner_back and has_form_back
    if not passed:
        all_auth_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {ap}: BannerHeaderBack={has_banner_back}, FormTopBack={has_form_back}")

# 5. Index Hero Image Cleanup
print("\n--- 5. INDEX HERO IMAGE CLEANUP (No content boxes on hero image) ---")
with open('index.html', 'r', encoding='utf-8') as fp:
    idx_c = fp.read()
has_floating_pill = 'hero-floating-pill' in idx_c
passed_idx_pill = not has_floating_pill
print(f"[{'PASS' if passed_idx_pill else 'FAIL'}] index.html: Floating pills removed from hero sentinel image frame = {passed_idx_pill}")

# 6. Form Select Inputs Default to 'Select one'
print("\n--- 6. FORM SELECT FIRST OPTION (Must be 'Select one') ---")
all_selects_pass = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    selects = re.findall(r'<select\b[^>]*>([\s\S]*?)</select>', c)
    for s_idx, sel in enumerate(selects):
        first_opt = re.search(r'<option\b[^>]*>(.*?)</option>', sel)
        if first_opt:
            val = first_opt.group(1).strip()
            is_valid = 'Select one' in val or 'Select One' in val or 'Select one...' in val or 'select one' in val.lower()
            if not is_valid:
                all_selects_pass = False
                print(f"[FAIL] {f} select #{s_idx+1} first option is '{val}' (Expected 'Select one')")
if all_selects_pass:
    print("[PASS] All <select> elements across all pages default to 'Select one'!")

# 7. Mobile Drawer Accordion with 6 Services
print("\n--- 7. MOBILE DRAWER WITH 6 SERVICES ACCORDION ---")
all_drawers_pass = True
services = [
    'service-soc.html',
    'service-pentest.html',
    'service-cloud-security.html',
    'service-incident-response.html',
    'service-vulnerability-management.html',
    'service-compliance.html'
]
for np in nav_pages:
    with open(np, 'r', encoding='utf-8') as fp:
        c = fp.read()
    missing_svc = [s for s in services if s not in c]
    passed = len(missing_svc) == 0 and 'mobile-nav-overlay' in c and 'mobile-submenu' in c
    if not passed:
        all_drawers_pass = False
        print(f"[FAIL] {np} missing services: {missing_svc}")
    else:
        print(f"[PASS] {np} has full mobile drawer with all 6 services")

# 8. Back to Top Button in All Pages
print("\n--- 8. BACK TO TOP BUTTON IN ALL PAGES ---")
all_btt_pass = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_btt = 'back-to-top' in c
    if not has_btt:
        all_btt_pass = False
    print(f"[{'PASS' if has_btt else 'FAIL'}] {f}")

print("\n" + "=" * 60)
overall = all_sections_pass and all_imgs_pass and all_logos_pass and all_auth_pass and passed_idx_pill and all_selects_pass and all_drawers_pass and all_btt_pass
print("OVERALL SUITE RESULT: " + ("ALL TESTS PASSED!" if overall else "SOME TESTS FAILED - REVIEW ABOVE!"))
print("=" * 60)

