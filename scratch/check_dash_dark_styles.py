with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'style=["\'][^"\']*(?:background|color)[^"\']*["\']', text)
print(f"Total inline styles with background/color in dashboard.html: {len(matches)}")
dark_bgs = [m for m in matches if any(k in m for k in ['rgba(0', 'rgba(1', '#0', '#1', '#2', 'gradient'])]
print(f"Potential dark backgrounds: {len(dark_bgs)}")
for d in dark_bgs[:20]:
    print("  ", d)

