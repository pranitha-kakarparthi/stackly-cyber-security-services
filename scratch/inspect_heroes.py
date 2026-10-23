import glob
import re

for path in ['pages/service-vulnerability-management.html', 'pages/service-soc.html', 'pages/about.html', 'pages/services.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>[\s\S]*?</section>)', text)
    if m:
        print(f"=== {path} ===")
        print(m.group(1)[:400] + "\n...\n" + m.group(1)[-250:])

