import re
import glob

# Check inline styles in HTML files
print("=== INLINE STYLES IN HTML FILES ===")
html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # find style="..." containing color or background
    inline_styles = re.findall(r'style=["\']([^"\']*(?:color|background)[^"\']*)["\']', text)
    if inline_styles:
        print(f"\n--- {fpath} ({len(inline_styles)} inline styles) ---")
        for s in inline_styles:
            if any(k in s for k in ['color', 'background']):
                print(f"   style='{s.strip()}'")

