import glob
import re

files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))

with open('scratch/images_list.txt', 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        
        matches = re.findall(r'(<img[^>]+>)', c)
        if matches:
            out.write(f"\n==================== {f} ({len(matches)} images) ====================\n")
            for m in matches:
                out.write(f"  {m}\n")

print("Written to scratch/images_list.txt")

