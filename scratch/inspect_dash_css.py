import re

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect breakpoints and potential overflow issues
media_queries = re.findall(r'@media[^{]+\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', css)
print(f"Total media query blocks: {len(media_queries)}")

# Let's look for fixed widths, nowrap, or overflow hidden without min-width: 0
nowraps = re.findall(r'([^{}]*\{[^}]*white-space:\s*nowrap[^}]*\})', css)
print(f"Nowrap rules count: {len(nowraps)}")
for n in nowraps[:10]:
    selector = n.split('{')[0].strip()
    print("  Nowrap:", selector)

fixed_widths = re.findall(r'([^{}]*\{[^}]*width:\s*\d+px[^}]*\})', css)
print(f"\nFixed width rules count: {len(fixed_widths)}")
for fw in fixed_widths[:10]:
    selector = fw.split('{')[0].strip()
    print("  Fixed width:", selector)

