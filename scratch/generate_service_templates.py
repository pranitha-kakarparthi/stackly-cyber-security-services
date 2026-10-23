import os

# Helper to generate common header and footer for service pages
def get_service_header(active_page, page_title):
    return f'''  <!-- Sticky Full-Width Header & Navigation -->
  <header class="site-header" role="banner">
    <div class="container navbar">
      <a href="../index.html" class="nav-brand" aria-label="Stackly Cyber Security Services Home">
        <img src="../assets/images/logoStackly.webp" alt="Stackly Logo" class="nav-brand-logo" width="145" height="38">
      </a>

      <nav class="nav-menu-wrapper" role="navigation" aria-label="Main Navigation">
        <ul class="nav-menu">
          <li class="nav-item">
            <a href="../index.html" class="nav-link">Home</a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link">About Us</a>
          </li>
          <li class="nav-item">
            <a href="services.html" class="nav-link dropdown-trigger active" aria-haspopup="true">
              Services
              <svg class="dropdown-chevron" viewBox="0 0 20 20" fill="currentColor" width="14" height="14">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </a>
            <ul class="dropdown-menu">
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
            </ul>
          </li>
          <li class="nav-item">
            <a href="pricing.html" class="nav-link">Pricing</a>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">Contact</a>
          </li>
        </ul>
      </nav>

      <div class="nav-actions">
        <a href="sign-in.html" class="btn btn-ghost btn-sm">Log In</a>
        <a href="sign-up.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>
      </div>

      <button class="nav-toggle" aria-label="Toggle Navigation Menu" aria-expanded="false">
        <span class="nav-toggle-bar"></span>
        <span class="nav-toggle-bar"></span>
        <span class="nav-toggle-bar"></span>
      </button>
    </div>
  </header>'''

def get_service_footer():
    return '''  <!-- Modern Full-Width Global Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand-info">
          <a href="../index.html">
            <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Security Services" class="footer-logo" width="150" height="39">
          </a>
          <p class="footer-tagline">
            Stackly Cyber Security Services provides mission-critical 24/7 SOC operations, Red Team offensive testing, and Zero-Trust architecture to safeguard global enterprises against cyber threats.
          </p>
          <div class="footer-socials">
            <a href="404.html" class="social-badge-link" aria-label="Stackly on LinkedIn" title="LinkedIn">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
              <span>LinkedIn</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="Stackly on X / Twitter" title="X (Twitter)">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
              <span>X (Twitter)</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="Stackly on GitHub" title="GitHub">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
              <span>GitHub</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="Stackly on YouTube" title="YouTube">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              <span>YouTube</span>
            </a>
          </div>
        </div>

        <div class="footer-links-col">
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links-list">
            <li><a href="../index.html" class="footer-link">Home</a></li>
            <li><a href="about.html" class="footer-link">About Us</a></li>
            <li><a href="services.html" class="footer-link">Services Overview</a></li>
            <li><a href="pricing.html" class="footer-link">Pricing & Plans</a></li>
            <li><a href="contact.html" class="footer-link">Contact Us</a></li>
            <li><a href="sign-in.html" class="footer-link">Sign In</a></li>
            <li><a href="sign-up.html" class="footer-link">Sign Up</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4 class="footer-heading">Defense Services</h4>
          <ul class="footer-links-list">
            <li><a href="service-soc.html" class="footer-link">Managed SOC 24/7</a></li>
            <li><a href="service-pentest.html" class="footer-link">Penetration Testing</a></li>
            <li><a href="service-cloud-security.html" class="footer-link">Cloud Security & Zero Trust</a></li>
            <li><a href="service-incident-response.html" class="footer-link">Incident Response Retainer</a></li>
            <li><a href="service-vulnerability-management.html" class="footer-link">Vulnerability Management</a></li>
            <li><a href="service-compliance.html" class="footer-link">ISO 27001 Compliance</a></li>
          </ul>
        </div>

        <div class="footer-contact-info">
          <h4 class="footer-heading">Global Headquarters</h4>
          <div class="footer-contact-item">
            <span class="footer-contact-icon">📍</span>
            <span>MMR Complex, Chinna Thirupathi, Salem, Tamil Nadu 636008</span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon">📞</span>
            <a href="404.html" class="footer-link">+91 9876543210</a>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-icon">✉️</span>
            <a href="404.html" class="footer-link">hello@thestackly.com</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Stackly Cyber Security Services. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="404.html">Privacy Policy</a>
          <a href="404.html">Terms of Service</a>
          <a href="404.html">Security Disclosure</a>
          <a href="404.html">SLA Commitment</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Back to Top Floating Button with Cyber Radar Pulse Ring Animation -->
  <button type="button" class="back-to-top" id="back-to-top" aria-label="Back to top" title="Back to top">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 15l-6-6-6 6"/>
    </svg>
  </button>

  <script src="../assets/js/main.js"></script>
</body>
</html>'''

