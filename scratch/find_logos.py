import glob
import re

for filepath in sorted(glob.glob('**/*.html', recursive=True)):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        if 'logoStackly' in line:
            # check 3 lines before and after for context
            context_snippet = "".join(lines[max(0, idx-3):min(len(lines), idx+2)]).strip()
            # extract class if any
            m = re.search(r'class="([^"]+)"', context_snippet)
            cls = m.group(1) if m else "none"
            print(f"{filepath}:{idx} [{cls}] -> {line.strip()[:70]}")

