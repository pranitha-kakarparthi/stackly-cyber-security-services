import glob
import re

files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

with open('scratch/icons_full_report.txt', 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()
        
        out.write(f"\n{'='*30} {f} {'='*30}\n")
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('<!--'):
                continue
            # Look for emojis or icon tags
            emojis = re.findall(r'[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff\u2b50-\u2b55]', line)
            has_svg = '<svg' in line
            has_icon_class = 'icon' in line.lower()
            
            if emojis or (has_icon_class and ('<span' in line or '<i' in line or '<div' in line)):
                out.write(f"Line {i:4d} | Emojis: {''.join(emojis):10s} | {stripped[:120]}\n")

print("Generated scratch/icons_full_report.txt")

