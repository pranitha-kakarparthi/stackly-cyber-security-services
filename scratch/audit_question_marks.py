import glob
import re

files = ['index.html', '404.html'] + glob.glob('pages/*.html')
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Check for unicode replacement character \ufffd
    repl_chars = content.count('\ufffd')
    # Check for <span>?</span> or >?</span>
    lone_q = re.findall(r'>\s*\?\s*<', content)
    double_q = re.findall(r'>\s*\?\?\s*<', content)
    if repl_chars > 0 or lone_q or double_q:
        print(f"{path}: \ufffd count={repl_chars}, lone '?' count={len(lone_q)}, '??' count={len(double_q)}")

