import glob, re

print("=== 1. GOOGLE FONTS IN HTML HEADERS ===")
for fpath in glob.glob('**/*.html', recursive=True):
    if 'scratch' in fpath: continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    fonts_links = re.findall(r'<link[^>]*fonts\.googleapis\.com[^>]*>', content)
    for fl in fonts_links:
        print(f"{fpath}: {fl}")

print("\n=== 2. FONT-FAMILY IN CSS FILES ===")
for fpath in glob.glob('assets/css/*.css'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if 'font-family' in line.lower():
            print(f"{fpath}:{i+1}: {line.strip()}")

print("\n=== 3. INLINE FONT-FAMILY IN HTML ===")
for fpath in glob.glob('**/*.html', recursive=True):
    if 'scratch' in fpath: continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if 'font-family' in line.lower():
            print(f"{fpath}:{i+1}: {line.strip()}")

