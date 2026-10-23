import re

def update_file(path, old_pattern, new_text, is_regex=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if is_regex:
        new_content, count = re.subn(old_pattern, new_text, content, count=1)
    else:
        count = content.count(old_pattern)
        new_content = content.replace(old_pattern, new_text, 1)
        
    if count == 0:
        print(f"[WARN] No replacement made in {path}!")
        return False
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] Updated {path} ({count} match)")
        return True

# 1. Update index.html dropdown and footer
INDEX_DROPDOWN = '''<ul class="dropdown-menu">
                <li class="dropdown-item">
                  <a href="pages/service-soc.html" class="dropdown-link">
                    <span class="dropdown-icon">🛡️</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">24/7 Managed SOC</span>
                      <span class="dropdown-desc">Continuous threat detection & SIEM monitoring</span>
                    </div>
                  </a>
                </li>
                <li class="dropdown-item">
                  <a href="pages/service-pentest.html" class="dropdown-link">
                    <span class="dropdown-icon">🎯</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">Penetration Testing</span>
                      <span class="dropdown-desc">Red Teaming, Web, API & Cloud assessments</span>
                    </div>
                  </a>
                </li>
                <li class="dropdown-item">
                  <a href="pages/service-cloud-security.html" class="dropdown-link">
                    <span class="dropdown-icon">☁️</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">Cloud & Zero Trust</span>
                      <span class="dropdown-desc">Multi-cloud architecture & posture management</span>
                    </div>
                  </a>
                </li>
                <li class="dropdown-item">
                  <a href="pages/service-incident-response.html" class="dropdown-link">
                    <span class="dropdown-icon">🚨</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">Incident Response</span>
                      <span class="dropdown-desc">1-hour rapid retainer & digital forensics</span>
                    </div>
                  </a>
                </li>
                <li class="dropdown-item">
                  <a href="pages/service-vulnerability-management.html" class="dropdown-link">
                    <span class="dropdown-icon">🔍</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">Vulnerability Management</span>
                      <span class="dropdown-desc">Continuous CVE radar & risk prioritization</span>
                    </div>
                  </a>
                </li>
                <li class="dropdown-item">
                  <a href="pages/service-compliance.html" class="dropdown-link">
                    <span class="dropdown-icon">📜</span>
                    <div class="dropdown-info">
                      <span class="dropdown-title">ISO 27001 Compliance</span>
                      <span class="dropdown-desc">Audit readiness & automated evidence vault</span>
                    </div>
                  </a>
                </li>
              </ul>'''

INDEX_FOOTER = '''<div class="footer-links-col">
          <h4 class="footer-heading">Defense Services</h4>
          <ul class="footer-links-list">
            <li><a href="pages/service-soc.html" class="footer-link">Managed SOC 24/7</a></li>
            <li><a href="pages/service-pentest.html" class="footer-link">Penetration Testing</a></li>
            <li><a href="pages/service-cloud-security.html" class="footer-link">Cloud Security & Zero Trust</a></li>
            <li><a href="pages/service-incident-response.html" class="footer-link">Incident Response Retainer</a></li>
            <li><a href="pages/service-vulnerability-management.html" class="footer-link">Vulnerability Management</a></li>
            <li><a href="pages/service-compliance.html" class="footer-link">ISO 27001 Compliance</a></li>
          </ul>
        </div>'''

update_file('index.html', r'<ul class="dropdown-menu">[\s\S]*?</ul>', INDEX_DROPDOWN, is_regex=True)
update_file('index.html', r'<div class="footer-links-col">\s*<h4 class="footer-heading">Defense Services</h4>[\s\S]*?</ul>\s*</div>', INDEX_FOOTER, is_regex=True)

# Also fix the greeting suffix in index.html and update the 6 service card links
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Fix greeting suffix
idx_content = re.sub(r'data-greeting-suffix="[^"]*"', 'data-greeting-suffix=" • Autonomous Defense Active"', idx_content)

# In index.html section 6, link the 6 cards directly to pages/service-*.html
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-primary btn-sm"\n                >Explore SOC Details</a\n              >',
    '<a href="pages/service-soc.html" class="btn btn-primary btn-sm">Explore SOC Details</a>'
)
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-primary btn-sm"\n                >Explore Pentest Details</a\n              >',
    '<a href="pages/service-pentest.html" class="btn btn-primary btn-sm">Explore Pentest Details</a>'
)
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-primary btn-sm"\n                >Explore Cloud Security</a\n              >',
    '<a href="pages/service-cloud-security.html" class="btn btn-primary btn-sm">Explore Cloud Security</a>'
)
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-primary btn-sm"\n                >Explore Incident Response</a\n              >',
    '<a href="pages/service-incident-response.html" class="btn btn-primary btn-sm">Explore Incident Response</a>'
)
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-secondary btn-sm"\n                >Learn About Threat Hunting</a\n              >',
    '<a href="pages/service-vulnerability-management.html" class="btn btn-secondary btn-sm">Explore Vulnerability Radar</a>'
)
idx_content = idx_content.replace(
    '<a href="404.html" class="btn btn-secondary btn-sm"\n                >Learn About Compliance</a\n              >',
    '<a href="pages/service-compliance.html" class="btn btn-secondary btn-sm">Explore ISO Compliance</a>'
)

# Also add floating pills inside index hero-sentinel-frame
if 'hero-floating-pill' not in idx_content:
    idx_content = idx_content.replace(
        '<div class="sentinel-ambient-glow" aria-hidden="true"></div>',
        '''<div class="sentinel-ambient-glow" aria-hidden="true"></div>
              <div class="hero-floating-pill pill-top-left" style="top: 24px; left: 24px;">
                <span class="hero-pill-dot"></span> Threat Defense Engine: Active
              </div>
              <div class="hero-floating-pill pill-bottom-right" style="bottom: 24px; right: 24px;">
                <span class="hero-pill-dot dot-amber"></span> 99.98% Breach Defense SLA
              </div>'''
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("[OK] Enhanced index.html hero badges and service cards")

# 2. Standard Dropdown & Footer for pages/*.html
PAGES_DROPDOWN = '''<ul class="dropdown-menu">
              <li class="dropdown-item">
                <a href="service-soc.html" class="dropdown-link">
                  <span class="dropdown-icon">🛡️</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">24/7 Managed SOC</span>
                    <span class="dropdown-desc">Continuous threat detection & SIEM monitoring</span>
                  </div>
                </a>
              </li>
              <li class="dropdown-item">
                <a href="service-pentest.html" class="dropdown-link">
                  <span class="dropdown-icon">🎯</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">Penetration Testing</span>
                    <span class="dropdown-desc">Red Teaming, Web, API & Cloud assessments</span>
                  </div>
                </a>
              </li>
              <li class="dropdown-item">
                <a href="service-cloud-security.html" class="dropdown-link">
                  <span class="dropdown-icon">☁️</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">Cloud & Zero Trust</span>
                    <span class="dropdown-desc">Multi-cloud architecture & posture management</span>
                  </div>
                </a>
              </li>
              <li class="dropdown-item">
                <a href="service-incident-response.html" class="dropdown-link">
                  <span class="dropdown-icon">🚨</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">Incident Response</span>
                    <span class="dropdown-desc">1-hour rapid retainer & digital forensics</span>
                  </div>
                </a>
              </li>
              <li class="dropdown-item">
                <a href="service-vulnerability-management.html" class="dropdown-link">
                  <span class="dropdown-icon">🔍</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">Vulnerability Management</span>
                    <span class="dropdown-desc">Continuous CVE radar & risk prioritization</span>
                  </div>
                </a>
              </li>
              <li class="dropdown-item">
                <a href="service-compliance.html" class="dropdown-link">
                  <span class="dropdown-icon">📜</span>
                  <div class="dropdown-info">
                    <span class="dropdown-title">ISO 27001 Compliance</span>
                    <span class="dropdown-desc">Audit readiness & automated evidence vault</span>
                  </div>
                </a>
              </li>
            </ul>'''

PAGES_FOOTER = '''<div class="footer-links-col">
          <h4 class="footer-heading">Defense Services</h4>
          <ul class="footer-links-list">
            <li><a href="service-soc.html" class="footer-link">Managed SOC 24/7</a></li>
            <li><a href="service-pentest.html" class="footer-link">Penetration Testing</a></li>
            <li><a href="service-cloud-security.html" class="footer-link">Cloud Security & Zero Trust</a></li>
            <li><a href="service-incident-response.html" class="footer-link">Incident Response Retainer</a></li>
            <li><a href="service-vulnerability-management.html" class="footer-link">Vulnerability Management</a></li>
            <li><a href="service-compliance.html" class="footer-link">ISO 27001 Compliance</a></li>
          </ul>
        </div>'''

subpages = [
    'pages/about.html',
    'pages/services.html',
    'pages/pricing.html',
    'pages/contact.html',
    'pages/service-soc.html',
    'pages/service-pentest.html',
    'pages/service-cloud-security.html',
    'pages/service-incident-response.html',
    'pages/service-vulnerability-management.html',
    'pages/service-compliance.html'
]

for p in subpages:
    update_file(p, r'<ul class="dropdown-menu">[\s\S]*?</ul>', PAGES_DROPDOWN, is_regex=True)
    update_file(p, r'<div class="footer-links-col">\s*<h4 class="footer-heading">Defense Services</h4>[\s\S]*?</ul>\s*</div>', PAGES_FOOTER, is_regex=True)

print("Subpage dropdowns and footers updated.")

