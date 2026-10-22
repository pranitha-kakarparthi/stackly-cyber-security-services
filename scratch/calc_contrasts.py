def get_luminance(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    
    def adjust(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4

    rl = adjust(r)
    gl = adjust(g)
    bl = adjust(b)
    return 0.2126 * rl + 0.7152 * gl + 0.0722 * bl

def contrast_ratio(hex1, hex2):
    lum1 = get_luminance(hex1)
    lum2 = get_luminance(hex2)
    bright = max(lum1, lum2)
    dark = min(lum1, lum2)
    return (bright + 0.05) / (dark + 0.05)

bg_primary = '#FAF7EE'
bg_white = '#FFFFFF'
bg_secondary = '#F3EFE0'
bg_dark = '#3A010E'
btn_primary = '#7A1028'

text_colors = {
    '--text-primary (#33050F)': '#33050F',
    '--text-secondary (#553B42)': '#553B42',
    '--text-muted (#7E646B)': '#7E646B',
    '--primary (#7A1028)': '#7A1028',
    '--secondary (#9E2A44)': '#9E2A44',
    '--accent (#D97706)': '#D97706',
    'white on btn_primary': ('#FFFFFF', btn_primary),
    'white on bg_dark': ('#FAF7EE', bg_dark),
}

print(f"=== CONTRAST RATIOS AGAINST --bg-primary ({bg_primary}) ===")
for name, col in text_colors.items():
    if isinstance(col, tuple):
        cr = contrast_ratio(col[0], col[1])
        print(f"  {name:30}: {cr:.2f}:1  -> {'PASS (AAA)' if cr >= 7 else 'PASS (AA)' if cr >= 4.5 else 'FAIL'}")
    else:
        cr = contrast_ratio(col, bg_primary)
        print(f"  {name:30}: {cr:.2f}:1  -> {'PASS (AAA)' if cr >= 7 else 'PASS (AA)' if cr >= 4.5 else 'FAIL'}")

print(f"\n=== CONTRAST RATIOS AGAINST #FFFFFF (Cards) ===")
for name, col in text_colors.items():
    if not isinstance(col, tuple):
        cr = contrast_ratio(col, bg_white)
        print(f"  {name:30}: {cr:.2f}:1  -> {'PASS (AAA)' if cr >= 7 else 'PASS (AA)' if cr >= 4.5 else 'FAIL'}")

