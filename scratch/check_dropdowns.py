import glob
import re

files = ['index.html', '404.html'] + glob.glob('pages/*.html')
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'<ul class="dropdown-menu">([\s\S]*?)</ul>', content)
    if matches:
        links = re.findall(r'href="([^"]+)"', matches[0])
        print(f"{path}: ({len(links)} links)")
        for l in links:
            print(f"   {l}")
    else:
        print(f"{path}: NO DROPDOWN")

