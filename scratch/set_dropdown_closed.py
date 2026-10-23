import glob
import re

files_to_update = ['index.html'] + glob.glob('pages/*.html')
count_updated = 0

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace button class="mobile-dropdown-btn open" aria-expanded="true"
    new_content = re.sub(
        r'<button\s+type="button"\s+class="mobile-dropdown-btn\s+open"\s+aria-expanded="true"',
        r'<button type="button" class="mobile-dropdown-btn" aria-expanded="false"',
        new_content
    )
    # Replace ul class="mobile-submenu open"
    new_content = re.sub(
        r'<ul\s+class="mobile-submenu\s+open">',
        r'<ul class="mobile-submenu">',
        new_content
    )

    if new_content != content:
        count_updated += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} -> Services dropdown closed by default")

print(f"Total files updated: {count_updated}")

