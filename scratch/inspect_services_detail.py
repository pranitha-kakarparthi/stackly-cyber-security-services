import re

with open('pages/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'(<section[^>]*>[\s\S]*?</section>)', text)
for i, s in enumerate(sections):
    print(f"=== Section {i+1} ===")
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    print("\n".join(lines[:6]))
    print("...")
    print("\n".join(lines[-3:]))

