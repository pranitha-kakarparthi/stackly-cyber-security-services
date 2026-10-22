with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add scroll to top in nav item click
old_click_pattern = """      const targetSectionId = item.getAttribute('data-target-module');
      if (targetSectionId) {
        document.querySelectorAll('.dash-module-section').forEach(sec => {
          sec.classList.remove('active');
        });
        const targetSec = document.getElementById(targetSectionId);
        if (targetSec) targetSec.classList.add('active');
      }

      // Close mobile drawer on item click"""

new_click_pattern = """      const targetSectionId = item.getAttribute('data-target-module');
      if (targetSectionId) {
        document.querySelectorAll('.dash-module-section').forEach(sec => {
          sec.classList.remove('active');
        });
        const targetSec = document.getElementById(targetSectionId);
        if (targetSec) targetSec.classList.add('active');
      }

      // Automatically scroll page to top upon clicking sidebar menu option
      const dashMainArea = document.getElementById('dash-main-area') || document.querySelector('.dash-main');
      if (dashMainArea) {
        dashMainArea.scrollTo({ top: 0, behavior: 'smooth' });
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Close mobile drawer on item click"""

if old_click_pattern in text:
    text = text.replace(old_click_pattern, new_click_pattern)
    print("Added smooth scroll-to-top on sidebar menu click in dashboard.js")
else:
    print("WARNING: old_click_pattern not found")

# 2. Add initDashboardBackToTop call in DOMContentLoaded
if 'initDashboardBackToTop();' not in text:
    text = text.replace('initDashboardActionButtons();', 'initDashboardActionButtons();\\n  initDashboardBackToTop();')

# 3. Append initDashboardBackToTop function
if 'function initDashboardBackToTop()' not in text:
    dash_btt_fn = """
/* ==========================================================================
   DASHBOARD BACK TO TOP CONTROLLER
   Scrolls .dash-main and window to top smoothly
   ========================================================================== */
function initDashboardBackToTop() {
  const btn = document.getElementById('back-to-top');
  const dashMain = document.getElementById('dash-main-area') || document.querySelector('.dash-main');
  if (!btn) return;

  const checkScroll = () => {
    const scrollPos = (dashMain ? dashMain.scrollTop : 0) || window.scrollY || 0;
    if (scrollPos > 250) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  };

  if (dashMain) {
    dashMain.addEventListener('scroll', checkScroll, { passive: true });
  }
  window.addEventListener('scroll', checkScroll, { passive: true });
  checkScroll();

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    if (dashMain) {
      dashMain.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
"""
    text += dash_btt_fn
    print("Appended initDashboardBackToTop function to dashboard.js")

with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated assets/js/dashboard.js successfully.")

