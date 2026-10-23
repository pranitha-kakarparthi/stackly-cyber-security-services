# 1. Update dashboard.js
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    djs = f.read()

target_djs = """  if (collapseBtn && sidebar) {
    collapseBtn.onclick = () => {
      sidebar.classList.toggle('collapsed');
      if (layout) layout.classList.toggle('sidebar-collapsed');
      const isCollapsed = sidebar.classList.contains('collapsed');
      collapseBtn.setAttribute('aria-expanded', !isCollapsed);
    };
  }"""

replacement_djs = """  if (collapseBtn && sidebar) {
    collapseBtn.onclick = () => {
      if (window.innerWidth <= 1024) {
        sidebar.classList.remove('mobile-open');
        document.body.classList.remove('drawer-open');
      } else {
        sidebar.classList.toggle('collapsed');
        if (layout) layout.classList.toggle('sidebar-collapsed');
        const isCollapsed = sidebar.classList.contains('collapsed');
        collapseBtn.setAttribute('aria-expanded', !isCollapsed);
      }
    };
  }"""

if target_djs in djs:
    djs = djs.replace(target_djs, replacement_djs)
    with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
        f.write(djs)
    print("Updated dashboard.js sidebar collapse logic")

# 2. Update dashboard.css
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dcss = f.read()

css_addition = """
/* Prominent Mobile Sidebar Collapse / Close Button */
.sidebar-collapse-toggle.mobile-only-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: var(--radius-sm);
  color: #FAF7EE;
  font-size: 1.15rem;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.sidebar-collapse-toggle.mobile-only-btn:hover {
  background: rgba(217, 119, 6, 0.3);
  border-color: var(--accent-gold);
  color: var(--accent-gold);
  transform: scale(1.05);
}
"""

if '.sidebar-collapse-toggle.mobile-only-btn' not in dcss:
    dcss += css_addition
    with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
        f.write(dcss)
    print("Added mobile-only-btn styles to dashboard.css")

