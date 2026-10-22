import glob
import re

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    wraps = re.findall(r'<div class="person-image-wrap">(.*?)</div>', text, re.DOTALL)
    for w in wraps:
        other_tags = re.findall(r'<([^/][^>]*)>', w)
        non_img = [t for t in other_tags if not t.startswith('img')]
        if non_img:
            print(f"{path}: Found elements inside person-image-wrap: {non_img}")
print("Done inspecting person-image-wrap.")

