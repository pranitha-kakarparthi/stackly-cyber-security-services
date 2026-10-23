import glob
import re

files = ['index.html'] + sorted(glob.glob('pages/*.html'))
total_removed = 0

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find footer
    footer_m = re.search(r'(<footer\b[\s\S]*?</footer>)', content)
    if not footer_m:
        continue
    
    footer_str = footer_m.group(1)
    orig_footer = footer_str

    # Pattern to remove Sign In <li> in footer
    footer_str = re.sub(
        r'\s*<li>\s*<a\s+href="[^"]*sign-in\.html"[^>]*>[\s\S]*?Sign\s+In\s*</a>\s*</li>',
        '',
        footer_str,
        flags=re.IGNORECASE
    )

    # Pattern to remove Sign Up <li> in footer
    footer_str = re.sub(
        r'\s*<li>\s*<a\s+href="[^"]*sign-up\.html"[^>]*>[\s\S]*?Sign\s+Up\s*</a>\s*</li>',
        '',
        footer_str,
        flags=re.IGNORECASE
    )

    if footer_str != orig_footer:
        content = content.replace(orig_footer, footer_str)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        total_removed += 1
        print(f"Removed Sign In & Sign Up from footer in: {fpath}")

print(f"\nTotal files updated: {total_removed}")

