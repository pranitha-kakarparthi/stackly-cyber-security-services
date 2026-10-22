import glob, re

def check_html_files():
    for fpath in glob.glob('**/*.html', recursive=True):
        if 'scratch' in fpath:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for inline styles with color or background
        inline_styles = re.findall(r'style=["\']([^"\']+)["\']', content)
        for s in inline_styles:
            if any(k in s for k in ['color', 'background']):
                # check if dark hex or rgb is used
                print(f'{fpath}: inline style -> {s}')

check_html_files()

