import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_text = f.read()

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dash_text = f.read()

print("=== CHECKING OPACITIES AND RGBA IN STYLE.CSS ===")
for match in re.finditer(r'([^{]+)\{([^}]+)\}', style_text):
    sel = match.group(1).strip()
    body = match.group(2)
    # Check if there is opacity or rgba or border
    for line in body.splitlines():
        line = line.strip()
        if any(k in line for k in ['color:', 'border:', 'background:', 'background-color:']):
            # check if it uses rgba with 255,255,255 or 0,0,0
            if 'rgba(255, 255, 255' in line or 'rgba(0, 0, 0' in line or 'rgba(0,0,0' in line or '#fff' in line or '#000' in line:
                print(f"{sel[:40]:40} -> {line[:60]}")

