import re

HERO_UPGRADES = {
    'pages/about.html': {
        'pattern': r'<section class="page-hero" aria-label="About Stackly Security Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="About Stackly Security Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">About Us</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Engineering Sovereign Cyber Resilience
            </div>
            <h1 class="page-hero-title">Defenders of the Modern Digital Enterprise</h1>
            <p class="page-hero-desc">
              Founded by elite military intelligence veterans and certified white-hat exploit analysts, Stackly protects over $8B in digital infrastructure assets across North America, Europe, and the Indo-Pacific.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Speak With Leadership</a>
              <a href="services.html" class="btn btn-outline btn-lg">Explore Defense Portfolio</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Defense Operations: Active 24/7
              </div>
              <img src="../assets/images/cyber-security-defense-operations.webp" alt="Stackly Cyber Defense Operations Center" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Enterprise Assets: $8B+ Protected
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/services.html': {
        'pattern': r'<section class="page-hero" aria-label="Services Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Services Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Services Overview</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Full-Spectrum Defense Operations
            </div>
            <h1 class="page-hero-title">End-to-End Enterprise Cyber Solutions</h1>
            <p class="page-hero-desc">
              Defend against persistent threat groups with integrated detection, offensive security verification, multi-cloud hardening, and instant containment.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Request Security Consultation</a>
              <a href="pricing.html" class="btn btn-outline btn-lg">View Investment Tiers</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Enterprise Threat Mesh: Armed
              </div>
              <img src="../assets/images/cyber-defense-matrix-lock.webp" alt="Cyber Defense Matrix Cryptographic Lock" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> 99.98% Interception Rate
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/pricing.html': {
        'pattern': r'<section class="page-hero" aria-label="Pricing Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Pricing Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Pricing & Plans</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Predictable Enterprise Investments
            </div>
            <h1 class="page-hero-title">Transparent Defense Investment Plans</h1>
            <p class="page-hero-desc">
              No hidden log ingestion charges. No surprise incident escalation penalties. Transparent monthly tiers backed by binding Service Level Agreements.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Get Custom Enterprise Quote</a>
              <a href="404.html" class="btn btn-outline btn-lg">Download SLA Factsheet</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Enterprise SLA: 99.99% Guaranteed
              </div>
              <img src="../assets/images/cyber-security-sentinel-breakthrough.webp" alt="Stackly Cyber Sentinel Defense Breakthrough" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Zero Hidden Ingestion Fees
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/contact.html': {
        'pattern': r'<section class="page-hero" aria-label="Contact Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Contact Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Contact Us</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Direct Security Operations Link
            </div>
            <h1 class="page-hero-title">Connect with Our Cyber Defense Specialists</h1>
            <p class="page-hero-desc">
              Have questions regarding our 24/7 Managed SOC, require immediate penetration test scoping, or need emergency incident triage? Our engineers respond promptly.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="#contact-form-section" class="btn btn-primary btn-lg">Dispatch An Inquiry</a>
              <a href="404.html" class="btn btn-outline btn-lg">Emergency Hotline</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Global SOC Dispatch: Standing By
              </div>
              <img src="../assets/images/cyber-defense-command-center.webp" alt="Global Cyber Defense Command Operations" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> SLA Triage: &lt; 15 Minutes
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/service-soc.html': {
        'pattern': r'<section class="page-hero" aria-label="Managed SOC Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Managed SOC Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">24/7 Managed SOC</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Sub-15 Minute Threat Containment SLA
            </div>
            <h1 class="page-hero-title">24/7/365 Managed Security Operations Center</h1>
            <p class="page-hero-desc">
              Continuous threat detection, high-fidelity SIEM event correlation, and proactive incident response powered by certified Tier 1-3 security analysts.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Request SOC Onboarding Audit</a>
              <a href="404.html" class="btn btn-outline btn-lg">View SOC SLA Specs</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Telemetry Ingestion: 4.8M EPS
              </div>
              <img src="../assets/images/soc-team-monitoring-center.webp" alt="24/7 SOC Monitoring Operations Center" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> MTTD: Under 3 Minutes
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/service-pentest.html': {
        'pattern': r'<section class="page-hero" aria-label="Penetration Testing Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Penetration Testing Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Penetration Testing</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Offensive Security & Red Teaming
            </div>
            <h1 class="page-hero-title">Adversary Emulation & Offensive Penetration Testing</h1>
            <p class="page-hero-desc">
              Identify vulnerabilities before adversaries exploit them. We perform deep manual exploit validation across web apps, APIs, cloud fabrics, and corporate internal networks.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Scope An Offensive Pentest</a>
              <a href="404.html" class="btn btn-outline btn-lg">Sample Pentest Deliverable</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Red Team Ops: Armed
              </div>
              <img src="../assets/images/cyber-security-sentinel-hooded.webp" alt="Offensive Penetration Testing Sentinel Specialist" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Zero-Day Simulation: 100% Non-Destructive
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/service-cloud-security.html': {
        'pattern': r'<section class="page-hero" aria-label="Cloud Security Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Cloud Security Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Cloud Security & Zero Trust</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Multi-Cloud Infrastructure Hardening
            </div>
            <h1 class="page-hero-title">Zero Trust Architecture & Multi-Cloud Defense</h1>
            <p class="page-hero-desc">
              Replace vulnerable network boundaries with explicit verification. We design and enforce unified Zero Trust controls across AWS, Azure, Google Cloud, and Kubernetes clusters.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Request Cloud Architecture Review</a>
              <a href="404.html" class="btn btn-outline btn-lg">Zero Trust Checklist</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Micro-Segmentation: Enforced
              </div>
              <img src="../assets/images/cloud-zero-trust-defense-architecture.webp" alt="Cloud Zero Trust Defense Architecture Matrix" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Multi-Cloud Posture: Real-Time
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    },
    'pages/service-incident-response.html': {
        'pattern': r'<section class="page-hero" aria-label="Incident Response Hero">[\s\S]*?</section>',
        'new': '''<section class="page-hero" aria-label="Incident Response Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Incident Response</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem; border-color: rgba(190, 18, 60, 0.4); color: var(--danger);">
              <span class="badge-dot" style="background: #ef4444; box-shadow: 0 0 10px #ef4444;"></span>
              1-Hour Guaranteed Emergency SLA
            </div>
            <h1 class="page-hero-title">Incident Response Retainer & Forensic Containment</h1>
            <p class="page-hero-desc">
              When an active cyber crisis unfolds, hesitation is fatal. Our Incident Response Commanders deploy within 60 minutes to neutralize ransomware, acquire forensic images, and restore operational continuity.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Activate Emergency Retainer</a>
              <a href="404.html" class="btn btn-outline btn-lg">Incident Playbook Specs</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></span> Rapid SLA: 60-Minute Retainer
              </div>
              <img src="../assets/images/incident-response-containment-matrix.webp" alt="Incident Response Forensics and Containment Matrix" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Breach Isolation: Active
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    }
}

for path, data in HERO_UPGRADES.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = re.subn(data['pattern'], data['new'], content, count=1)
    if count == 0:
        print(f"[FAIL] Could not match hero pattern in {path}")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[SUCCESS] Upgraded hero in {path}")

