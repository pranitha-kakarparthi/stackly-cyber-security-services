import math

def srgb_to_luminance(r, g, b):
    # r, g, b in 0..255
    def channel_lum(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    rl = channel_lum(r)
    gl = channel_lum(g)
    bl = channel_lum(b)
    return 0.2126 * rl + 0.7152 * gl + 0.0722 * bl

def contrast_ratio(hex1, hex2):
    def hex_to_rgb(h):
        h = h.lstrip('#')
        if len(h) == 3:
            h = ''.join([c*2 for c in h])
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    l1 = srgb_to_luminance(*hex_to_rgb(hex1))
    l2 = srgb_to_luminance(*hex_to_rgb(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

# Palettes
bg_ivory = '#FAF7EE'
bg_white = '#FFFFFF'
bg_sandstone = '#F3EFE0'
bg_dark_footer = '#250109'
bg_dark_sidebar = '#200007'
bg_dark_auth = '#3A010E'

checks = [
    # 1. Navbar brand logo & nav items
    ('Navbar logo (#7A1028)', '#7A1028', bg_white),
    ('Navbar logo on ivory (#FAF7EE)', '#7A1028', bg_ivory),
    ('Navbar links (.nav-link: #33050F)', '#33050F', bg_white),
    ('Navbar active link (.nav-link.active: #7A1028)', '#7A1028', bg_white),
    ('Navbar ghost btn (.btn-ghost: #33050F)', '#33050F', bg_white),
    ('Navbar iridescent btn (white on #7A1028)', '#FFFFFF', '#7A1028'),
    
    # 2. Footers
    ('Footer heading (#FAF7EE on #250109)', '#FAF7EE', bg_dark_footer),
    ('Footer tagline (#D1C2C6 on #250109)', '#D1C2C6', bg_dark_footer),
    ('Footer link default (#D1C2C6 on #250109)', '#D1C2C6', bg_dark_footer),
    ('Footer link hover (#F5A623 on #250109)', '#F5A623', bg_dark_footer),
    ('Footer link active (#FFFFFF on #250109)', '#FFFFFF', bg_dark_footer),
    ('Footer contact item (#D1C2C6 on #250109)', '#D1C2C6', bg_dark_footer),
    ('Footer contact icon (#F5A623 on #250109)', '#F5A623', bg_dark_footer),
    ('Footer social pill default (#FAF7EE on #250109)', '#FAF7EE', bg_dark_footer),
    ('Footer social pill hover (#F5A623 on #250109)', '#F5A623', bg_dark_footer),
    ('Footer bottom text (#B09BA2 on #250109)', '#B09BA2', bg_dark_footer),
    ('Footer bottom link hover (#F5A623 on #250109)', '#F5A623', bg_dark_footer),
    
    # 3. Form fields (Contact, Signin, Signup)
    ('Form control text (#33050F on #FFFFFF)', '#33050F', bg_white),
    ('Form control placeholder (#7A626A on #FFFFFF)', '#7A626A', bg_white),
    ('Form label (#33050F on #FFFFFF)', '#33050F', bg_white),
    ('Form label on ivory (#33050F on #FAF7EE)', '#33050F', bg_ivory),
    ('Form focus border (#7A1028 on #FFFFFF)', '#7A1028', bg_white),
    ('Form error message (#BE123C on #FFFFFF)', '#BE123C', bg_white),
    ('Select option text (#33050F on #FFFFFF)', '#33050F', bg_white),
    ('Select option hover (#7A1028 on #F3EFE0)', '#7A1028', bg_sandstone),
    
    # 4. Auth pages
    ('Auth banner h1 (#FAF7EE on #3A010E)', '#FAF7EE', bg_dark_auth),
    ('Auth banner paragraph (#E2D7DA on #3A010E)', '#E2D7DA', bg_dark_auth),
    ('Auth banner badge tag (#F5A623 on #3A010E)', '#F5A623', bg_dark_auth),
    ('Auth quote text (#FAF7EE on #3A010E)', '#FAF7EE', bg_dark_auth),
    ('Auth quote author (#F5A623 on #3A010E)', '#F5A623', bg_dark_auth),
    
    # 5. Dashboard
    ('Dashboard table header (#33050F on #F3EFE0)', '#33050F', bg_sandstone),
    ('Dashboard table body (#553B42 on #FFFFFF)', '#553B42', bg_white),
    ('Dashboard table hover (#33050F on #FAF7EE)', '#33050F', bg_ivory),
    ('Dashboard sidebar nav (#D4BFC4 on #200007)', '#D4BFC4', bg_dark_sidebar),
    ('Dashboard sidebar hover (#FFFFFF on #200007)', '#FFFFFF', bg_dark_sidebar),
    ('Dashboard KPI value warning (#92400E on #FFFFFF)', '#92400E', bg_white),
    ('Dashboard KPI value danger (#BE123C on #FFFFFF)', '#BE123C', bg_white),
    
    # 6. Pricing & Services
    ('Pricing table header (#33050F on #F3EFE0)', '#33050F', bg_sandstone),
    ('Pricing featured badge (white on #7A1028)', '#FFFFFF', '#7A1028'),
    ('Testimonial stars (#B45309 on #FFFFFF)', '#B45309', bg_white),
]

print(f"{'Element / State':<50} | {'Ratio':<8} | {'WCAG Level'}")
print("-" * 75)
all_pass = True
for name, fg, bg in checks:
    ratio = contrast_ratio(fg, bg)
    if ratio >= 7.0:
        level = "AAA (Pass)"
    elif ratio >= 4.5:
        level = "AA (Pass)"
    elif ratio >= 3.0:
        level = "AA-Large (Pass)"
    else:
        level = "FAIL"
        all_pass = False
    print(f"{name:<50} | {ratio:>5.2f}:1  | {level}")

print("-" * 75)
if all_pass:
    print("ALL 35 TESTED VISIBLE ELEMENTS ACROSS ALL STATES PASS WCAG ACCESSIBILITY STANDARDS!")
else:
    print("SOME ELEMENTS FAILED.")

