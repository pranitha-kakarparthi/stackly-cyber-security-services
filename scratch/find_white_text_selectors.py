with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all occurrences of color, background, border
properties = re.findall(r'(?:color|background|background-color|border|border-color|fill|stroke)\s*:\s*([^;]+);', text)
unique_props = set(p.strip() for p in properties)
print(f"Total unique color properties in style.css: {len(unique_props)}")

# Check for #fff or rgba(255, 255, 255...
white_texts = [p for p in unique_props if any(w in p.lower() for w in ['#fff', '255, 255, 255', 'white'])]
print(f"White or light properties count: {len(white_texts)}")

# Find which selectors use these white texts
for match in re.finditer(r'([^{]+)\{([^}]+)\}', text):
    sel = match.group(1).strip()
    body = match.group(2)
    # Check if sel has color: #fff or color: white or rgba(255,255,255)
    color_m = re.findall(r'(?<!background-)color\s*:\s*([^;]+);', body)
    for c in color_m:
        c_clean = c.strip().lower()
        if '#fff' in c_clean or 'white' in c_clean or '255, 255, 255' in c_clean or 'var(--text-inverse)' in c_clean:
            # check background
            bg_m = re.findall(r'background(?:-color)?\s*:\s*([^;]+);', body)
            print(f"SELECTOR: {sel[:50]:50} | COLOR: {c_clean[:30]:30} | BG: {str(bg_m)[:40]}")

