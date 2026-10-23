import glob
import re

# 1. Update HTML files for mobile nav close button
files = ['index.html'] + sorted(glob.glob('pages/*.html'))
updated_count = 0

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Check if mobile-nav-brand exists without mobile-nav-close-btn
    if 'mobile-nav-brand' in c and 'mobile-nav-close-btn' not in c:
        pattern = r'(<div class="mobile-nav-brand">[\s\S]*?<a[^>]*class="mobile-brand-link"[^>]*>[\s\S]*?</a>)(\s*</div>)'
        replacement = r'''\1
        <button type="button" class="mobile-nav-close-btn" aria-label="Collapse Navigation Menu">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
          <span class="close-btn-text">Close</span>
        </button>\2'''
        new_c, n = re.subn(pattern, replacement, c)
        if n > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_c)
            updated_count += 1
            print(f"Added collapse option to: {fpath}")

print(f"Total HTML files updated with collapse button: {updated_count}")

# 2. Update assets/js/main.js to wire up mobile-nav-close-btn
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target_js = "toggleBtn.addEventListener('click', () => toggleMenu());"
replacement_js = """toggleBtn.addEventListener('click', () => toggleMenu());

  // Close / Collapse button inside the mobile drawer
  const closeBtns = overlay.querySelectorAll('.mobile-nav-close-btn');
  closeBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleMenu(false);
    });
  });"""

if target_js in js and 'mobile-nav-close-btn' not in js:
    js = js.replace(target_js, replacement_js)
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated assets/js/main.js with mobile-nav-close-btn listener")

# 3. Update assets/css/style.css with mobile-nav-close-btn styles
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

brand_old = """.mobile-nav-brand {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
}"""

brand_new = """.mobile-nav-brand {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.mobile-nav-close-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.95rem;
  border-radius: var(--radius-full);
  background: rgba(122, 16, 40, 0.08);
  border: 1px solid rgba(122, 16, 40, 0.2);
  color: var(--primary);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.mobile-nav-close-btn:hover,
.mobile-nav-close-btn:focus-visible {
  background: var(--primary);
  color: #FAF7EE;
  border-color: var(--primary);
  transform: scale(1.04);
}"""

if brand_old in css:
    css = css.replace(brand_old, brand_new)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated assets/css/style.css with mobile-nav-close-btn styles")

