import glob
import re

INDEX_MOBILE_OVERLAY = '''    <!-- Fullscreen Mobile Navigation Overlay Drawer -->
    <div
      class="mobile-nav-overlay"
      role="dialog"
      aria-modal="true"
      aria-label="Mobile Navigation"
    >
      <div class="mobile-nav-brand">
        <a href="index.html" class="mobile-brand-link" aria-label="Stackly Home">
          <img src="assets/images/logoStackly.webp" alt="Stackly Logo" width="145" height="38">
        </a>
      </div>

      <ul class="mobile-menu-list">
        <li><a href="index.html" class="mobile-nav-link active">Home</a></li>
        <li><a href="pages/about.html" class="mobile-nav-link">About Us</a></li>
        <li class="mobile-nav-item has-dropdown">
          <div class="mobile-dropdown-header">
            <a href="pages/services.html" class="mobile-nav-link">Services</a>
            <button type="button" class="mobile-dropdown-btn open" aria-expanded="true" aria-label="Toggle Services Submenu">
              <svg class="mobile-chevron" viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
          <ul class="mobile-submenu open">
            <li>
              <a href="pages/service-soc.html" class="mobile-service-card">
                <span class="mobile-service-icon">🛡️</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">24/7 Managed SOC</span>
                  <span class="mobile-service-desc">Continuous threat detection & SIEM monitoring</span>
                </div>
              </a>
            </li>
            <li>
              <a href="pages/service-pentest.html" class="mobile-service-card">
                <span class="mobile-service-icon">🎯</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Penetration Testing</span>
                  <span class="mobile-service-desc">Red Teaming, Web, API & Cloud assessments</span>
                </div>
              </a>
            </li>
            <li>
              <a href="pages/service-cloud-security.html" class="mobile-service-card">
                <span class="mobile-service-icon">☁️</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Cloud & Zero Trust</span>
                  <span class="mobile-service-desc">Multi-cloud architecture & posture management</span>
                </div>
              </a>
            </li>
            <li>
              <a href="pages/service-incident-response.html" class="mobile-service-card">
                <span class="mobile-service-icon">🚨</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Incident Response</span>
                  <span class="mobile-service-desc">1-hour rapid retainer & digital forensics</span>
                </div>
              </a>
            </li>
            <li>
              <a href="pages/service-vulnerability-management.html" class="mobile-service-card">
                <span class="mobile-service-icon">🔍</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Vulnerability Management</span>
                  <span class="mobile-service-desc">Continuous CVE radar & risk prioritization</span>
                </div>
              </a>
            </li>
            <li>
              <a href="pages/service-compliance.html" class="mobile-service-card">
                <span class="mobile-service-icon">📜</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">ISO 27001 Compliance</span>
                  <span class="mobile-service-desc">Audit readiness & automated evidence vault</span>
                </div>
              </a>
            </li>
            <li class="mobile-service-overview-item">
              <a href="pages/services.html" class="mobile-overview-link">View All Services Overview &rarr;</a>
            </li>
          </ul>
        </li>
        <li><a href="pages/pricing.html" class="mobile-nav-link">Pricing</a></li>
        <li><a href="pages/contact.html" class="mobile-nav-link">Contact</a></li>
      </ul>

      <div class="mobile-actions">
        <a href="pages/sign-in.html" class="btn btn-secondary btn-block">Sign In</a>
        <a href="pages/sign-up.html" class="btn btn-primary btn-block">Get Started</a>
      </div>
    </div>'''

def get_page_mobile_overlay(active_page):
    return f'''    <!-- Fullscreen Mobile Navigation Overlay Drawer -->
    <div
      class="mobile-nav-overlay"
      role="dialog"
      aria-modal="true"
      aria-label="Mobile Navigation"
    >
      <div class="mobile-nav-brand">
        <a href="../index.html" class="mobile-brand-link" aria-label="Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Logo" width="145" height="38">
        </a>
      </div>

      <ul class="mobile-menu-list">
        <li><a href="../index.html" class="mobile-nav-link">Home</a></li>
        <li><a href="about.html" class="mobile-nav-link{' active' if active_page == 'about' else ''}">About Us</a></li>
        <li class="mobile-nav-item has-dropdown">
          <div class="mobile-dropdown-header">
            <a href="services.html" class="mobile-nav-link{' active' if 'service' in active_page else ''}">Services</a>
            <button type="button" class="mobile-dropdown-btn open" aria-expanded="true" aria-label="Toggle Services Submenu">
              <svg class="mobile-chevron" viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
          <ul class="mobile-submenu open">
            <li>
              <a href="service-soc.html" class="mobile-service-card{' active-service' if active_page == 'service-soc' else ''}">
                <span class="mobile-service-icon">🛡️</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">24/7 Managed SOC</span>
                  <span class="mobile-service-desc">Continuous threat detection & SIEM monitoring</span>
                </div>
              </a>
            </li>
            <li>
              <a href="service-pentest.html" class="mobile-service-card{' active-service' if active_page == 'service-pentest' else ''}">
                <span class="mobile-service-icon">🎯</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Penetration Testing</span>
                  <span class="mobile-service-desc">Red Teaming, Web, API & Cloud assessments</span>
                </div>
              </a>
            </li>
            <li>
              <a href="service-cloud-security.html" class="mobile-service-card{' active-service' if active_page == 'service-cloud-security' else ''}">
                <span class="mobile-service-icon">☁️</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Cloud & Zero Trust</span>
                  <span class="mobile-service-desc">Multi-cloud architecture & posture management</span>
                </div>
              </a>
            </li>
            <li>
              <a href="service-incident-response.html" class="mobile-service-card{' active-service' if active_page == 'service-incident-response' else ''}">
                <span class="mobile-service-icon">🚨</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Incident Response</span>
                  <span class="mobile-service-desc">1-hour rapid retainer & digital forensics</span>
                </div>
              </a>
            </li>
            <li>
              <a href="service-vulnerability-management.html" class="mobile-service-card{' active-service' if active_page == 'service-vulnerability-management' else ''}">
                <span class="mobile-service-icon">🔍</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">Vulnerability Management</span>
                  <span class="mobile-service-desc">Continuous CVE radar & risk prioritization</span>
                </div>
              </a>
            </li>
            <li>
              <a href="service-compliance.html" class="mobile-service-card{' active-service' if active_page == 'service-compliance' else ''}">
                <span class="mobile-service-icon">📜</span>
                <div class="mobile-service-info">
                  <span class="mobile-service-title">ISO 27001 Compliance</span>
                  <span class="mobile-service-desc">Audit readiness & automated evidence vault</span>
                </div>
              </a>
            </li>
            <li class="mobile-service-overview-item">
              <a href="services.html" class="mobile-overview-link">View All Services Overview &rarr;</a>
            </li>
          </ul>
        </li>
        <li><a href="pricing.html" class="mobile-nav-link{' active' if active_page == 'pricing' else ''}">Pricing</a></li>
        <li><a href="contact.html" class="mobile-nav-link{' active' if active_page == 'contact' else ''}">Contact</a></li>
      </ul>

      <div class="mobile-actions">
        <a href="sign-in.html" class="btn btn-secondary btn-block">Sign In</a>
        <a href="sign-up.html" class="btn btn-primary btn-block">Get Started</a>
      </div>
    </div>'''

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_new, count = re.subn(r'<!--\s*(?:Fullscreen\s*)?Mobile(?:\s*Navigation)?\s*Overlay(?:\s*Drawer)?\s*-->\s*<div\s+class="mobile-nav-overlay"[\s\S]*?</div>\s*</div>', INDEX_MOBILE_OVERLAY, idx_content, count=1)
if count:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_new)
    print("[OK] Replaced mobile-nav-overlay in index.html")
else:
    # Try direct pattern
    idx_new, count = re.subn(r'<div\s+class="mobile-nav-overlay"[\s\S]*?</div>\s*</div>', INDEX_MOBILE_OVERLAY, idx_content, count=1)
    if count:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(idx_new)
        print("[OK] Replaced mobile-nav-overlay in index.html (fallback)")
    else:
        print("[WARN] Could not find mobile-nav-overlay in index.html")

# 2. Update subpages
SUBPAGES = {
    'pages/about.html': 'about',
    'pages/services.html': 'services',
    'pages/pricing.html': 'pricing',
    'pages/contact.html': 'contact',
    'pages/service-soc.html': 'service-soc',
    'pages/service-pentest.html': 'service-pentest',
    'pages/service-cloud-security.html': 'service-cloud-security',
    'pages/service-incident-response.html': 'service-incident-response',
    'pages/service-vulnerability-management.html': 'service-vulnerability-management',
    'pages/service-compliance.html': 'service-compliance'
}

for path, page_key in SUBPAGES.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacement = get_page_mobile_overlay(page_key)
    
    if 'class="mobile-nav-overlay"' in content:
        new_content, count = re.subn(r'(?:<!--\s*(?:Fullscreen\s*)?Mobile(?:\s*Navigation)?\s*Overlay(?:\s*Drawer)?\s*-->\s*)?<div\s+class="mobile-nav-overlay"[\s\S]*?</div>\s*</div>', replacement, content, count=1)
        if count:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Replaced mobile-nav-overlay in {path}")
        else:
            print(f"[WARN] Failed regex in {path}")
    else:
        # Insert right after </header>
        header_end = '</header>'
        if header_end in content:
            new_content = content.replace(header_end, f'{header_end}\n\n{replacement}', 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Inserted mobile-nav-overlay into {path}")
        else:
            print(f"[WARN] </header> not found in {path}")

