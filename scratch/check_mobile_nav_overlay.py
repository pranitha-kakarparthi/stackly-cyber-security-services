import glob

files = ['index.html', '404.html'] + glob.glob('pages/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'mobile-nav-overlay' in c:
        print(f"Found in {f}")
    else:
        print(f"NOT in {f}")

