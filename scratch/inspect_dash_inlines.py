import re

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check inline widths or flex styles
inline_styles = re.findall(r'style="([^"]*(?:width|grid|flex|nowrap|overflow|position)[^"]*)"', text)
print(f"Total inline styles with layout properties: {len(inline_styles)}")

unique_inlines = set(inline_styles)
for s in sorted(unique_inlines)[:20]:
    clean = s.encode('ascii', 'replace').decode('ascii')
    print("  Style:", clean[:90])

