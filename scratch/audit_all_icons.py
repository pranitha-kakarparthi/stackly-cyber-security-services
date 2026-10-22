import glob
import re

files = glob.glob('*.html') + glob.glob('pages/*.html')

with open('scratch/icons_report.txt', 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        # Find all emoji chars
        # Emoji regex roughly: \u2000-\u3300, \U00010000-\U0010ffff
        emojis = re.findall(r'[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff\u2b50-\u2b55]', content)
        unique_emojis = sorted(list(set(emojis)))
        
        out.write(f"\n==================== {f} ({len(emojis)} icons total, {len(unique_emojis)} unique) ====================\n")
        out.write(f"Unique icons: {' '.join(unique_emojis)}\n\n")
        
        # Find specific context where icons are used
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            has_emoji = any(e in line for e in unique_emojis)
            if has_emoji:
                out.write(f"  L{i:4d}: {line.strip()[:100]}\n")

print("Icons audit written to scratch/icons_report.txt")

