import glob
import re

files_with_overlay = []
files_without_overlay = []

for f in ['index.html'] + sorted(glob.glob('pages/*.html')):
    if f in ['404.html', 'pages/404.html', 'pages/dashboard.html', 'pages/sign-in.html', 'pages/sign-up.html']:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'mobile-nav-overlay' in c:
        files_with_overlay.append(f)
    else:
        files_without_overlay.append(f)

print("Files with overlay:", files_with_overlay)
print("Files without overlay:", files_without_overlay)

