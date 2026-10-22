import glob
import re

files = ['index.html'] + glob.glob('pages/*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    prefix = "../" if (f.startswith('pages/') or f.startswith('pages\\')) and '404.html' not in f else ""
    target_404 = f"{prefix}404.html"

    # 1. In footers: update "Defense Services" column links to 404
    # Pattern: within <div class="footer-links-col"> with <h4>Defense Services</h4>
    def replace_defense_services(match):
        block = match.group(0)
        # replace any href="..." with target_404 inside this block
        block = re.sub(r'href=["\'][^"\']+["\']', f'href="{target_404}"', block)
        return block

    content = re.sub(
        r'<div class="footer-links-col">\s*<h4 class="footer-heading">Defense Services</h4>.*?</ul>\s*</div>',
        replace_defense_services,
        content,
        flags=re.DOTALL
    )

    # 2. In footers: update bottom links to 404
    def replace_footer_bottom(match):
        block = match.group(0)
        block = re.sub(r'href=["\'][^"\']+["\']', f'href="{target_404}"', block)
        return block

    content = re.sub(
        r'<div class="footer-bottom-links">.*?</div>',
        replace_footer_bottom,
        content,
        flags=re.DOTALL
    )

    # 3. In contact information cards/footer: phone and email links to 404
    content = re.sub(
        r'<a href="[^"]*"\s+class="footer-link">(\+91[^<]*|hello@[^<]*)</a>',
        rf'<a href="{target_404}" class="footer-link">\1</a>',
        content
    )

    # 4. Any remaining in-body action buttons or card CTAs in marketing pages that might link to non-404
    # e.g., href="contact.html" with class btn, or href="service-*.html" with class btn
    if 'sign' not in f and 'dashboard' not in f and '404' not in f:
        # Match <a href="..." class="btn ..."> where href is not #... and not in quick links
        # If it's a CTA button, redirect to 404
        content = re.sub(
            r'<a\s+href=["\'](?!#|mailto|tel|404|\.\./404)[^"\']+["\']\s+class=["\']btn\s+([^"\']*)["\']',
            rf'<a href="{target_404}" class="btn \1"',
            content
        )
        content = re.sub(
            r'<a\s+class=["\']btn\s+([^"\']*)["\']\s+href=["\'](?!#|mailto|tel|404|\.\./404)[^"\']+["\']',
            rf'<a class="btn \1" href="{target_404}"',
            content
        )

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(f"Updated links in {f}")

print("All footers and action buttons redirected to 404 except quick links!")

