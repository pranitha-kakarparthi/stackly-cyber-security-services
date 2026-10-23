import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """function initMobileNav() {
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
    if (isOpen) {
      overlay.scrollTop = 0;
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
  };

  toggleBtn.addEventListener('click', () => toggleMenu());"""

replacement = """function initMobileNav() {
  const toggleBtn = document.querySelector('.nav-toggle');
  const overlay = document.querySelector('.mobile-nav-overlay');
  if (!toggleBtn || !overlay) return;

  let lockedScrollPos = 0;

  // Helper: always keep Services dropdown closed by default on menu open
  const resetDropdowns = () => {
    overlay.querySelectorAll('.mobile-dropdown-btn').forEach(btn => {
      btn.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    });
    overlay.querySelectorAll('.mobile-submenu').forEach(sub => {
      sub.classList.remove('open');
    });
  };

  const toggleMenu = (forceState) => {
    const isCurrentlyOpen = overlay.classList.contains('open');
    const willOpen = typeof forceState === 'boolean' 
      ? forceState 
      : !isCurrentlyOpen;
    
    toggleBtn.classList.toggle('open', willOpen);
    overlay.classList.toggle('open', willOpen);
    toggleBtn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');

    if (willOpen) {
      // 1. Lock background content fixed at current scroll position
      lockedScrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
      document.documentElement.classList.add('drawer-open');
      document.body.classList.add('drawer-open');
      document.body.style.top = `-${lockedScrollPos}px`;
      
      // 2. Services dropdown must be in closed mode by default upon opening menu
      resetDropdowns();

      // 3. Ensure menu starts scrolled at the very top of its full container
      overlay.scrollTop = 0;
    } else {
      // Restore background position cleanly
      document.documentElement.classList.remove('drawer-open');
      document.body.classList.remove('drawer-open');
      const restorePos = Math.abs(parseInt(document.body.style.top || '0', 10)) || lockedScrollPos;
      document.body.style.top = '';
      window.scrollTo({ top: restorePos, behavior: 'instant' });

      // Reset dropdowns on close
      resetDropdowns();
    }
  };

  toggleBtn.addEventListener('click', () => toggleMenu());"""

if target in js:
    js = js.replace(target, replacement)
elif target.replace('\n', '\r\n') in js:
    js = js.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))
else:
    print("WARNING: Target block not found directly!")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated assets/js/main.js successfully")

