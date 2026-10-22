import glob

html_files = sorted(glob.glob('*.html') + glob.glob('pages/*.html'))
button_markup = """  <!-- Back to Top Floating Button -->
  <button type="button" class="back-to-top" id="back-to-top" aria-label="Back to top" title="Back to top">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 15l-6-6-6 6"/>
    </svg>
  </button>
</body>"""

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="back-to-top"' in content:
        print(f"Skipping {path}: already has back-to-top")
        continue
    
    if '</body>' in content:
        new_content = content.replace('</body>', button_markup, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected back-to-top button into {path}")
    else:
        print(f"WARNING: No </body> found in {path}")

