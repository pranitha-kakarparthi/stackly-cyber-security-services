import re

# Standard dropdown HTML for index.html (with pages/ prefix)
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

# Standard dropdown HTML for pages/*.html (sibling links)
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

# Standard Defense Services footer list for index.html
INDEX_FOOTER_SERVICES = '''<div class="footer-links-col">
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

# Standard Defense Services footer list for pages/*.html
PAGES_FOOTER_SERVICES = '''<div class="footer-links-col">
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

print("Templates ready.")

