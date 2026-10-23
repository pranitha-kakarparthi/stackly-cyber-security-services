with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '''function initMobileNav() {
  const toggleBtn = document.querySelector('.nav-toggle');
  const overlay = document.querySelector('.mobile-nav-overlay');
  if (!toggleBtn || !overlay) return;

  const toggleMenu = () => {
    const isOpen = toggleBtn.classList.toggle('open');
    overlay.classList.toggle('open', isOpen);
    document.body.classList.toggle('drawer-open', isOpen);
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  };

  toggleBtn.addEventListener('click', toggleMenu);

  // Close overlay when clicking any navigation link
  const links = overlay.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', () => {
      toggleBtn.classList.remove('open');
      overlay.classList.remove('open');
      document.body.classList.remove('drawer-open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    });
  });
}'''

new_code = '''function initMobileNav() {
  const toggleBtn = document.querySelector('.nav-toggle');
  const overlay = document.querySelector('.mobile-nav-overlay');
  if (!toggleBtn || !overlay) return;

  const toggleMenu = (forceState) => {
    const isOpen = typeof forceState === 'boolean' 
      ? forceState 
      : toggleBtn.classList.toggle('open');
    
    if (typeof forceState === 'boolean') {
      toggleBtn.classList.toggle('open', isOpen);
    }
    overlay.classList.toggle('open', isOpen);
    document.body.classList.toggle('drawer-open', isOpen);
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  };

  toggleBtn.addEventListener('click', () => toggleMenu());

  // Interactive Services Dropdown Submenu Accordion Toggle
  const dropdownToggleBtns = overlay.querySelectorAll('.mobile-dropdown-btn');
  dropdownToggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const parentItem = btn.closest('.has-dropdown');
      if (parentItem) {
        const submenu = parentItem.querySelector('.mobile-submenu');
        const isCurrentlyOpen = submenu && submenu.classList.contains('open');
        const willOpen = !isCurrentlyOpen;
        
        btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
        btn.classList.toggle('open', willOpen);
        if (submenu) {
          submenu.classList.toggle('open', willOpen);
        }
      }
    });
  });

  // Close overlay when clicking any destination link (excluding dropdown toggles)
  const links = overlay.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      toggleMenu(false);
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay.classList.contains('open')) {
      toggleMenu(false);
    }
  });
}'''

if target in js:
    js = js.replace(target, new_code)
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Successfully updated initMobileNav in assets/js/main.js")
else:
    print("Could not match target in main.js")

