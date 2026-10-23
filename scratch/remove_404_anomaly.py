import re

for filepath in ['404.html', 'pages/404.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Pattern to match the Report Security Anomaly anchor
    pattern = r'\s*<a\s+href="[^"]*contact\.html"\s+class="btn\s+btn-outline\s+btn-lg"[^>]*>[\s\S]*?Report\s+Security\s+Anomaly[\s\S]*?</a>'
    
    new_c, count = re.subn(pattern, '', c)
    print(f"{filepath}: removed {count} instance(s)")
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_c)

