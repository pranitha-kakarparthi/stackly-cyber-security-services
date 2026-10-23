import glob
import re

files = sorted(glob.glob('pages/*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'(<section class="page-hero"[\s\S]*?>[\s\S]*?</section>)', c)
    if m:
        first_few = m.group(1).split('\n')[:8]
        print(f"=== {f} ===")
        print("\n".join(first_few))

