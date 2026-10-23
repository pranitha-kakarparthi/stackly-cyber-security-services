import glob, re

for fpath in sorted(glob.glob('**/*.html', recursive=True)):
    if 'scratch' in fpath: continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    non_logo = [img for img in imgs if 'logo' not in img]
    print(f'{fpath} has {len(non_logo)} non-logo images:')
    for img in non_logo:
        print(f'   {img}')

