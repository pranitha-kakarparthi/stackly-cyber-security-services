with open('assets/css/animations.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace green & cyan animation colors with velvet wine and golden amber
text = text.replace('rgba(0, 240, 118, 0.2)', 'rgba(122, 16, 40, 0.2)')
text = text.replace('rgba(0, 240, 118, 0.1)', 'rgba(122, 16, 40, 0.1)')
text = text.replace('rgba(0, 240, 118, 0.48)', 'rgba(122, 16, 40, 0.35)')
text = text.replace('rgba(0, 240, 118, 0.22)', 'rgba(122, 16, 40, 0.18)')
text = text.replace('rgba(0, 240, 118, 0.4)', 'rgba(122, 16, 40, 0.25)')
text = text.replace('rgba(0, 240, 118, 0.85)', 'rgba(217, 119, 6, 0.85)')
text = text.replace('rgba(94, 234, 212, 0)', 'rgba(122, 16, 40, 0)')
text = text.replace('rgba(94, 234, 212, 0.9)', 'rgba(217, 119, 6, 0.9)')
text = text.replace('rgba(94, 234, 212, 0.55)', 'rgba(122, 16, 40, 0.55)')
text = text.replace('rgba(167, 139, 250, 0.4)', 'rgba(217, 119, 6, 0.4)')

with open('assets/css/animations.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated assets/css/animations.css successfully.")

