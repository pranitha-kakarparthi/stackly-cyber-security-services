import glob
import re

for filepath in sorted(glob.glob('**/*.html', recursive=True)):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Check if there is spacer or bottom margin
    spacers = re.findall(r'<div[^>]*style="[^"]*height:\s*\d+px[^"]*"[^>]*>', c)
    if spacers:
        print(f"{filepath}: Found spacer divs: {spacers}")

