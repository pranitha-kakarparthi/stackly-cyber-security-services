import re

with open('pages/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
s2 = sections[1]
links = re.findall(r'<a[^>]*href="([^"]*)"[^>]*>([\s\S]*?)</a>', s2)
for href, label in links:
    clean_label = re.sub(r'<[^>]+>', '', label).strip()
    print(f"Href: {href} | Label: {clean_label}")

