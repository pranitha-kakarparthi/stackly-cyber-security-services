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
    has_header_logo = re.search(r'class="nav-brand"[^>]*>[\s\S]*?logoStackly-wine\.webp', c) is not None
    has_mobile_logo = re.search(r'class="mobile-brand-link"[^>]*>[\s\S]*?logoStackly-wine\.webp', c) is not None
    passed = has_header_logo and has_mobile_logo
    if not passed:
        all_logos_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {np}: Header={has_header_logo}, MobileDrawer={has_mobile_logo}")

# 4. Collapse Option in Side Menu / Mobile Drawer
print("\n--- 4. COLLAPSE OPTION IN SIDE MENU / MOBILE DRAWER ---")
all_collapse_pass = True
for np in nav_pages:
    with open(np, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_close_btn = 'mobile-nav-close-btn' in c
    if not has_close_btn:
        all_collapse_pass = False
    print(f"[{'PASS' if has_close_btn else 'FAIL'}] {np}: Mobile Drawer has Close/Collapse Option = {has_close_btn}")

with open('pages/dashboard.html', 'r', encoding='utf-8') as fp:
    dash_c = fp.read()
dash_has_collapse = 'sidebar-collapse-btn' in dash_c and 'mobile-sidebar-close-btn' in dash_c
print(f"[{'PASS' if dash_has_collapse else 'FAIL'}] pages/dashboard.html has Sidebar Collapse Option = {dash_has_collapse}")

# 5. Hero Images Clean (No content boxes on images)
print("\n--- 5. HERO IMAGES CLEANUP (No white boxes on images) ---")
all_clean_heroes = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    pills = re.findall(r'<div class="[^"]*hero-floating-pill[^"]*"', c)
    if len(pills) > 0:
        all_clean_heroes = False
        print(f"[FAIL] {f} has {len(pills)} floating pills!")
if all_clean_heroes:
    print("[PASS] 100% of hero sections across all pages have zero content boxes on images!")

# 6. Footer Quick Links (NO Sign In or Sign Up)
print("\n--- 6. FOOTER QUICK LINKS (NO Sign In / Sign Up) ---")
all_footer_clean = True
for np in nav_pages:
    with open(np, 'r', encoding='utf-8') as fp:
        c = fp.read()
    footer_m = re.search(r'<footer\b[\s\S]*?</footer>', c)
    if footer_m:
        ft = footer_m.group(0)
        has_auth_link = 'sign-in.html' in ft or 'sign-up.html' in ft
        if has_auth_link:
            all_footer_clean = False
            print(f"[FAIL] {np} footer still has auth links!")
        else:
            print(f"[PASS] {np} footer has no Sign In/Sign Up in Quick Links")

# 7. Form Select First Option == 'Select one'
print("\n--- 7. FORM SELECT FIRST OPTION (Must be 'Select one') ---")
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

# 8. Services Dropdown Closed by Default
print("\n--- 8. SERVICES DROPDOWN CLOSED BY DEFAULT ---")
all_closed_pass = True
for np in nav_pages:
    with open(np, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_open_submenu = '<ul class="mobile-submenu open">' in c
    has_open_btn = 'mobile-dropdown-btn open' in c
    passed = not has_open_submenu and not has_open_btn
    if not passed:
        all_closed_pass = False
        print(f"[FAIL] {np} has open dropdown by default!")
    else:
        print(f"[PASS] {np} services dropdown is closed by default")

print("\n" + "=" * 60)
overall = all_sections_pass and all_imgs_pass and all_logos_pass and all_collapse_pass and all_clean_heroes and all_footer_clean and all_selects_pass and all_closed_pass
print("OVERALL SUITE RESULT: " + ("ALL TESTS PASSED!" if overall else "SOME TESTS FAILED - REVIEW ABOVE!"))
print("=" * 60)
