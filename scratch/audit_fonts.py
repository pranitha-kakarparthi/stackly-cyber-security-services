import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. CSS FONT VARIABLES ===")
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip().startswith('--font-'):
            print(f"style.css: {line.strip()}")

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip().startswith('--font-'):
            print(f"dashboard.css: {line.strip()}")

print("\n=== 2. ALL FONT-FAMILY DECLARATIONS IN CSS ===")
for css_file in ['assets/css/style.css', 'assets/css/dashboard.css', 'assets/css/animations.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            if 'font-family' in line:
                print(f"{css_file}:{idx+1}: {line.strip()}")

print("\n=== 3. ALL FONT-FAMILY DECLARATIONS IN HTML (INLINE) ===")
for fpath in glob.glob('**/*.html', recursive=True):
    if any(k in fpath for k in ['scratch', '.git']):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        for idx, line in enumerate(f):
            if 'font-family' in line:
                print(f"{fpath}:{idx+1}: {line.strip()}")

print("\n=== 4. UNAUTHORIZED FONT NAMES SCAN ===")
unauthorized = ['inter', 'outfit', 'space grotesk', 'fira', 'courier', 'arial', 'helvetica', 'roboto', 'segoe', 'menlo', 'monaco', 'consolas']
unauthorized_found = 0
for fpath in glob.glob('**/*.html', recursive=True) + glob.glob('assets/**/*.css', recursive=True) + glob.glob('assets/**/*.js', recursive=True):
    if any(k in fpath for k in ['scratch', '.git']):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        for idx, line in enumerate(f):
            lower = line.lower()
            if any(term in lower for term in ['font-family', 'font:', 'family=']):
                for un in unauthorized:
                    if re.search(r'\b' + re.escape(un) + r'\b', lower):
                        print(f"WARNING: {fpath}:{idx+1}: {line.strip()}")
                        unauthorized_found += 1

if unauthorized_found == 0:
    print("SUCCESS: Zero unauthorized font names found across the entire repository!")
