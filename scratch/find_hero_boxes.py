import glob
import re

for f in sorted(glob.glob('**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    pills = re.findall(r'<div class="[^"]*hero-floating-pill[^"]*"[^>]*>[\s\S]*?</div>', c)
    if pills:
        print(f"{f}: {len(pills)} pills found")
        for p in pills:
            clean = re.sub(r'\s+', ' ', p.strip())
            print(f"  -> {clean[:100]}")

