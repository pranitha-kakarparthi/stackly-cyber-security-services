import glob
import re

html_files = sorted(glob.glob('**/*.html', recursive=True))
total_removed = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match any hero-floating-pill div
    pattern = r'\s*<div\s+class="[^"]*hero-floating-pill[^"]*"[^>]*>[\s\S]*?</div>'
    
    new_content, count = re.subn(pattern, '', content)
    if count > 0:
        total_removed += count
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"{filepath}: removed {count} floating pill(s)")

print(f"\nTotal floating pills removed across site: {total_removed}")

