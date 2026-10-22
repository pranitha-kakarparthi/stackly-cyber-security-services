import glob
import re
import sys

files = ['index.html'] + glob.glob('pages/*.html')

with open('scratch/audit_report.txt', 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        hrefs = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\']', content)
        target_404 = [h for h in hrefs if '404' in h]
        non_404 = [h for h in hrefs if '404' not in h]
        out.write(f"\n==================== {f} (total={len(hrefs)}, 404={len(target_404)}, non_404={len(non_404)}) ====================\n")
        
        for m in re.finditer(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL):
            href = m.group(1)
            tag_text = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
            tag_text = ' '.join(tag_text.split())
            if '404' not in href:
                out.write(f"  {href:40} | {tag_text[:50]}\n")

print("Audit written to scratch/audit_report.txt")

