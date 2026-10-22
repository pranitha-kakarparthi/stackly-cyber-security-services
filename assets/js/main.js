/**
 * STACKLY CYBER SECURITY SERVICES - MAIN CLIENT CONTROLLER
 * Handles: Pure CSS Loader dismissal, Sticky Navbar, Full-screen Mobile Drawer,
 * Active Nav Highlighter, Dynamic Time-of-Day Greeting, 3D Tilt Engine,
 * Zoom-In / Zoom-Out Scroll Reveals, and Interactive Security Widgets.
 */

document.addEventListener('DOMContentLoaded', () => {
  initLoader();
  initStickyNavbar();
  initActiveNav();
  initMobileNav();
  initDynamicGreetings();
  initScrollAnimations();
  init3DTilt();
  initInteractivePerimeterScanner();
  initCharacterCounters();
  initBackToTop();
});

/* ==========================================================================
   1. LOADER DISMISSAL
   Dismisses loader as soon as DOMContentLoaded fires with fallback timeout
   ========================================================================== */
function initLoader() {
  const loader = document.getElementById('page-loader');
  if (!loader) return;

  const dismissLoader = () => {
    loader.classList.add('loaded');
    setTimeout(() => {
      try {
        loader.remove();
      } catch (e) {
        loader.style.display = 'none';
      }
    }, 400);
  };

  // Immediate dismiss if interactive, plus fallback
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(dismissLoader, 100);
  } else {
    window.addEventListener('DOMContentLoaded', dismissLoader, { once: true });
    window.addEventListener('load', dismissLoader, { once: true });
    setTimeout(dismissLoader, 800);
  }
}

// Immediately trigger if script evaluates after DOM ready
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initLoader();
}

/* ==========================================================================
   2. STICKY NAVBAR
   ========================================================================== */
function initStickyNavbar() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* ==========================================================================
   3. ACTIVE NAV ITEM HIGHLIGHTER
   Highlights current navigation link based on window pathname
   ========================================================================== */
function initActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-link, .mobile-nav-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    const targetPath = href.split('/').pop();
    if (targetPath === currentPath) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
      
      // If inside a dropdown, highlight parent dropdown trigger
      const parentDropdown = link.closest('.nav-item');
      if (parentDropdown) {
        const trigger = parentDropdown.querySelector('.dropdown-trigger');
        if (trigger) trigger.classList.add('active');
      }
    }
  });
}

/* ==========================================================================
   4. FULL-SCREEN MOBILE NAV OVERLAY & BODY SCROLL LOCK
   ========================================================================== */
function initMobileNav() {
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
}

/* ==========================================================================
   5. DYNAMIC TIME-OF-DAY GREETING
   Updates greeting based on visitor's current local hour and duration of the day
   ========================================================================== */
function initDynamicGreetings() {
  const greetingElements = document.querySelectorAll('[data-greeting]');
  if (!greetingElements.length) return;

  const hour = new Date().getHours();
  let greetingText = 'Good day';

  if (hour >= 5 && hour < 12) {
    greetingText = 'Good morning';
  } else if (hour >= 12 && hour < 17) {
    greetingText = 'Good afternoon';
  } else if (hour >= 17 && hour < 22) {
    greetingText = 'Good evening';
  } else {
    greetingText = 'Good night';
  }

  greetingElements.forEach(el => {
    const prefix = el.getAttribute('data-greeting-prefix') || '';
    const suffix = el.getAttribute('data-greeting-suffix') || '';
    el.textContent = `${prefix}${greetingText}${suffix}`;
  });
}

/* ==========================================================================
   6. SCROLL REVEAL ANIMATIONS (AOS STYLE: FADE, ZOOM-IN, ZOOM-OUT)
   ========================================================================== */
function initScrollAnimations() {
  // Respect prefers-reduced-motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('[data-animate]').forEach(el => el.classList.add('in-view'));
    return;
  }

  const animElements = document.querySelectorAll('[data-animate]');
  if (!animElements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  animElements.forEach(el => observer.observe(el));
}

/* ==========================================================================
   7. INTERACTIVE 3D PERSPECTIVE TILT ENGINE
   Smooth 3D card tilt with depth, highlight and mouse movement
   ========================================================================== */
function init3DTilt() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const tiltCards = document.querySelectorAll('.js-tilt, .tilt-card');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -9; // Max 9 deg
      const rotateY = ((x - centerX) / centerX) * 9;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    });
  });
}

/* ==========================================================================
   8. SIMULATED INTERACTIVE PERIMETER SCANNER
   Unique, interactive feature demonstrating real-time threat intelligence
   ========================================================================== */
function initInteractivePerimeterScanner() {
  const scanBtn = document.getElementById('run-sim-scan-btn');
  const targetInput = document.getElementById('sim-scan-target');
  const resultContainer = document.getElementById('sim-scan-results');
  if (!scanBtn || !targetInput || !resultContainer) return;

  scanBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const target = targetInput.value.trim() || 'demo.enterprise-client.org';
    scanBtn.disabled = true;
    scanBtn.textContent = 'Scanning Perimeter...';

    resultContainer.innerHTML = `
      <div style="padding: 1.5rem; background: rgba(0, 240, 118, 0.06); border: 1px dashed var(--primary); border-radius: var(--radius-md); text-align: center;">
        <span class="loader-status-dot" style="margin: 0 auto 0.75rem;"></span>
        <p style="color: var(--primary); font-family: var(--font-mono); font-size: 0.9rem;">
          Querying Global Threat Feeds for [${target}]... Testing TLS ciphers & firewall rules...
        </p>
      </div>
    `;

    setTimeout(() => {
      scanBtn.disabled = false;
      scanBtn.textContent = 'Run Security Scan';
      resultContainer.innerHTML = `
        <div style="padding: 1.5rem; background: rgba(16, 185, 129, 0.08); border: 1px solid var(--accent); border-radius: var(--radius-md);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; flex-wrap: wrap; gap: 0.5rem;">
            <strong style="color: var(--accent); display: flex; align-items: center; gap: 0.5rem;">
              <span>🛡️</span> Defense Analysis Complete for: ${target}
            </strong>
            <span class="severity-pill severity-low">Threat Posture: Protected</span>
          </div>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 0.85rem;">
            0 Critical Zero-Days detected. TLS 1.3 Active with Perfect Forward Secrecy. Stackly SOC 24/7 continuous sensor coverage recommended.
          </p>
          <a href="404.html" class="btn btn-primary btn-sm">Download Full Diagnostic Audit Report (PDF)</a>
        </div>
      `;
    }, 1200);
  });
}

/* ==========================================================================
   9. CHARACTER COUNTERS FOR FORMS
   ========================================================================== */
function initCharacterCounters() {
  const textareas = document.querySelectorAll('textarea[maxlength]');
  textareas.forEach(textarea => {
    const counterId = textarea.getAttribute('data-counter-id');
    if (!counterId) return;
    const counterEl = document.getElementById(counterId);
    if (!counterEl) return;

    const max = textarea.getAttribute('maxlength');
    const updateCount = () => {
      const current = textarea.value.length;
      counterEl.textContent = `${current} / ${max} characters`;
    };

    textarea.addEventListener('input', updateCount);
    updateCount();
  });
}


/* ==========================================================================
   10. BACK TO TOP CONTROLLER
   Smoothly scrolls page to the top when button is clicked; shows after scrolling
   ========================================================================== */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  const handleScroll = () => {
    if (window.scrollY > 280) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
