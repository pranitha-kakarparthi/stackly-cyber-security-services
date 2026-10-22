import glob

font_links = '''  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono (Unified Design System) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">'''

for fpath in glob.glob('**/*.html', recursive=True):
    if 'scratch' in fpath: continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if font_links already present
    if 'Plus+Jakarta+Sans' not in content:
        # insert before </head> or before the first <link rel="stylesheet"
        if '<link rel="stylesheet"' in content:
            content = content.replace('<link rel="stylesheet"', font_links + '\n  <link rel="stylesheet"', 1)
        else:
            content = content.replace('</head>', font_links + '\n</head>', 1)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Google Fonts to {fpath}")
    else:
        print(f"Already present in {fpath}")

print("Completed Google Fonts injection across all HTML files.")

