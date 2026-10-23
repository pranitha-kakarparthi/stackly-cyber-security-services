import re

with open('pages/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
print(f"Total sections: {len(sections)}")
for i, s in enumerate(sections):
    m = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', s)
    h = m.group(1) if m else "No Heading"
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    print(f"Section {i+1}: {clean_h}")

