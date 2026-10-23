from generate_service_templates import get_service_header, get_service_footer

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ISO 27001, SOC 2 & Enterprise Security Compliance | Stackly Cyber Security Services</title>
  <meta name="description" content="Automate audit readiness, continuous evidence collection, and achieve ISO 27001:2022 and SOC 2 Type II certification in 14 days with Stackly's compliance engineers.">
  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono (Unified Design System) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/animations.css">
</head>
<body data-page="service-compliance">
  <!-- Accessibility Skip Link -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Modern Viewport Loader -->
  <div id="page-loader" aria-live="polite" role="status">
    <div class="loader-content">
      <div class="loader-brand">
        <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Security Services" width="160" height="42">
      </div>
      <div class="loader-spinner-wrap">
        <div class="loader-spinner"></div>
        <div class="loader-pulse-ring"></div>
      </div>
      <div class="loader-text">
        <span class="loader-status-dot"></span>
        <span>Validating Compliance Evidence Vault...</span>
      </div>
    </div>
  </div>

{get_service_header('service-compliance', 'ISO 27001 Compliance')}

  <main id="main-content">
    <!-- SECTION 1: ENHANCED HERO STAGE WITH CYBER IMAGE & ANIMATIONS -->
    <section class="page-hero" aria-label="ISO 27001 Compliance Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">ISO 27001 Compliance</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Audit-Ready in 14 Days
            </div>
            <h1 class="page-hero-title">Continuous Enterprise Security & ISO 27001 Compliance</h1>
            <p class="page-hero-desc">
              Transform burdensome annual audits into automated, continuous operational assurance. Stackly designs, implements, and defends your ISO/IEC 27001:2022, SOC 2 Type II, HIPAA, and GDPR posture with binding audit guarantees.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Begin Fast-Track Certification</a>
              <a href="404.html" class="btn btn-outline btn-lg">Download Readiness Checklist</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> ISO 27001 & SOC 2 Type II
              </div>
              <img src="../assets/images/iso-compliance-security-vault.webp" alt="ISO Compliance Security Vault Graphic" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> Audit Readiness: 100%
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: SOVEREIGN COMPLIANCE FRAMEWORKS -->
    <section class="section" aria-label="Supported Compliance Frameworks">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Multi-Standard Assurance</div>
          <h2 class="section-title">Complete Regulatory & Governance Coverage</h2>
          <p>
            One centralized evidence vault satisfies multiple international and regional security standards simultaneously without duplicate documentation.
          </p>
        </div>

        <div class="cards-grid-3">
          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">📜</div>
            <h3 class="card-title">ISO/IEC 27001:2022 ISMS</h3>
            <p class="card-desc">
              Complete Information Security Management System design, Annex A control implementation, internal audit facilitation, and Stage 1 & 2 audit accompaniment.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">🔐</div>
            <h3 class="card-title">SOC 2 Type I & Type II</h3>
            <p class="card-desc">
              Trust Services Criteria implementation covering Security, Availability, Processing Integrity, Confidentiality, and Privacy with continuous telemetry evidence.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">🏥</div>
            <h3 class="card-title">HIPAA Security & HITECH</h3>
            <p class="card-desc">
              Safeguarding Protected Health Information (ePHI) across cloud architectures with strict administrative, physical, and technical safeguard validation.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">⚖️</div>
            <h3 class="card-title">GDPR & Digital Data Privacy</h3>
            <p class="card-desc">
              Article 32 security processing benchmarks, Records of Processing Activities (RoPA), Data Protection Impact Assessments (DPIA), and breach notification workflows.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">💳</div>
            <h3 class="card-title">PCI-DSS 4.0 Compliance</h3>
            <p class="card-desc">
              Cardholder Data Environment (CDE) scoping, quarterly ASV vulnerability scans, multi-factor enforcement, and customized RoC / SAQ completion.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">🏛️</div>
            <h3 class="card-title">NIST Cybersecurity Framework 2.0</h3>
            <p class="card-desc">
              Comprehensive maturity alignment across Govern, Identify, Protect, Detect, Respond, and Recover pillars for federal and enterprise suppliers.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: CONTINUOUS EVIDENCE VAULT ARCHITECTURE -->
    <section class="section section-alt" aria-label="Evidence Automation Architecture">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Automated Proof</div>
          <h2 class="section-title">Zero Screenshots: Real-Time Evidence Gathering</h2>
          <p>
            Say goodbye to frantic spreadsheet chasing before audits. Our automated connectors continuously prove technical compliance across your infrastructure.
          </p>
        </div>

        <div class="cards-grid-3">
          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">🔄</div>
            <h3 class="card-title">Continuous Control Monitoring</h3>
            <p class="card-desc">
              Automated API webhooks track MFA enforcement, disk encryption states, PR review requirements, and IAM role rotators in real time.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">🗄️</div>
            <h3 class="card-title">Immutable Evidence Ledger</h3>
            <p class="card-desc">
              Timestamped cryptographic proof stored with WORM (Write Once, Read Many) integrity, readily accessible to external certified audit assessors.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">🚨</div>
            <h3 class="card-title">Instant Drift Alerting</h3>
            <p class="card-desc">
              If an engineer opens an S3 bucket or disables required firewall logging, our pipeline triggers a Slack/Teams alert within 60 seconds.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: 14-DAY FAST-TRACK ROADMAP -->
    <section class="section" aria-label="14-Day Fast-Track Roadmap">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Accelerated Path</div>
          <h2 class="section-title">From Zero to Audit-Ready in 14 Days</h2>
          <p>
            Our proven, four-phase sprint methodology eliminates bureaucratic delay and gets your organization certified on an aggressive timeline.
          </p>
        </div>

        <div class="cards-grid-4">
          <div class="tilt-card" data-animate="fade-up">
            <div style="font-size: 1.75rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">Days 1-3</div>
            <h4 class="card-title">Scoping & Gap Audit</h4>
            <p class="card-desc">Full boundary definition, asset inventory collation, and identification of missing technical controls.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div style="font-size: 1.75rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">Days 4-7</div>
            <h4 class="card-title">Policy Customization</h4>
            <p class="card-desc">Tailoring 24 mandatory security policies and employee handbooks aligned with your actual tech stack.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div style="font-size: 1.75rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">Days 8-11</div>
            <h4 class="card-title">Technical Remediation</h4>
            <p class="card-desc">Enforcing SSO, MDM configuration, branch protection, vulnerability scanning, and access reviews.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="300">
            <div style="font-size: 1.75rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">Days 12-14</div>
            <h4 class="card-title">Mock Internal Audit</h4>
            <p class="card-desc">Dry-run audit simulation with accredited assessors ensuring 100% first-time external certification pass.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: CERTIFIED COMPLIANCE AUDITORS -->
    <section class="section section-alt" aria-label="Compliance Leadership Team">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Accredited Experts</div>
          <h2 class="section-title">Certified Lead Auditors Defending Your Posture</h2>
          <p>
            Direct access to seasoned IRCA-certified ISO 27001 Lead Auditors and former Big-4 security assurance partners.
          </p>
        </div>

        <div class="cards-grid-2" style="max-width: 860px; margin: 0 auto;">
          <div class="person-card" data-animate="fade-up">
            <div class="person-image-wrap">
              <img src="../assets/images/security-compliance-auditor.webp" alt="Lead Compliance Auditor" width="400" height="260" loading="lazy">
            </div>
            <div class="person-info">
              <h3 class="person-name">Priya Sundaram</h3>
              <div class="person-role">Head of Governance, Risk & Compliance (GRC)</div>
              <p class="person-bio">
                Over 14 years conducting enterprise compliance audits across SaaS, banking, and defense supply chains. Successfully guided over 120 companies to accredited certification.
              </p>
              <div class="person-badges">
                <span class="person-badge">ISO 27001 LA</span>
                <span class="person-badge">CISA</span>
                <span class="person-badge">CRISC</span>
              </div>
            </div>
          </div>

          <div class="person-card" data-animate="fade-up" data-delay="100">
            <div class="person-image-wrap">
              <img src="../assets/images/chief-information-security-officer-elena-rostova.webp" alt="Elena Rostova CISO" width="400" height="260" loading="lazy">
            </div>
            <div class="person-info">
              <h3 class="person-name">Elena Rostova</h3>
              <div class="person-role">Chief Information Security Officer</div>
              <p class="person-bio">
                Former defense security director with extensive experience establishing sovereign compliance postures, cryptographic governance, and third-party risk management frameworks.
              </p>
              <div class="person-badges">
                <span class="person-badge">CISO</span>
                <span class="person-badge">CISM</span>
                <span class="person-badge">CCSP</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: COMPLIANCE ASSURANCE SLA & GUARANTEES -->
    <section class="section" aria-label="Compliance Assurance Guarantees">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Guaranteed Results</div>
          <h2 class="section-title">Our Binding Audit Defense Commitment</h2>
          <p>
            We don't leave you with a binder of policies and walk away. We sit alongside your team during external auditor interviews until your certification is officially awarded.
          </p>
        </div>

        <div class="cards-grid-3">
          <div class="tilt-card" data-animate="fade-up">
            <div class="sim-stat-val" style="color: var(--primary);">100%</div>
            <h3 class="card-title">First-Time Pass Guarantee</h3>
            <p class="card-desc">
              If an external auditor raises a major non-conformity within the agreed scope, our team remediates it immediately at zero additional fee.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="sim-stat-val" style="color: var(--primary);">&lt; 24 Hrs</div>
            <h3 class="card-title">Auditor Inquiry Turnaround</h3>
            <p class="card-desc">
              Direct technical evidence delivery to external audit assessors within 24 hours of request throughout your audit surveillance window.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="sim-stat-val" style="color: var(--primary);">365 Days</div>
            <h3 class="card-title">Continuous Maintenance</h3>
            <p class="card-desc">
              Year-round evidence refresh, annual policy updates, quarterly vendor risk reviews, and periodic employee phishing training records.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: AUTOMATED EVIDENCE CONNECTOR ECOSYSTEM -->
    <section class="section section-alt" aria-label="Evidence Ingestion Connectors">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Integration Power</div>
          <h2 class="section-title">Direct Connectors Across Your Infrastructure</h2>
          <p>
            Native API integrations pull telemetry directly from the platforms your engineers and operations teams use daily.
          </p>
        </div>

        <div class="cards-grid-4">
          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">☁️</div>
            <h4 class="card-title">Cloud Platforms</h4>
            <p class="card-desc">AWS, Microsoft Azure, Google Cloud Platform, and Cloudflare.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">🔑</div>
            <h4 class="card-title">Identity & Access</h4>
            <p class="card-desc">Okta, Azure Active Directory, Google Workspace, and Ping Identity.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">💻</div>
            <h4 class="card-title">Code & DevOps</h4>
            <p class="card-desc">GitHub, GitLab, Bitbucket, Terraform, and Docker Hub.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="300">
            <div class="card-icon-wrap">📱</div>
            <h4 class="card-title">Device & MDM</h4>
            <p class="card-desc">Jamf Pro, Microsoft Intune, Kandji, and CrowdStrike Falcon.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: COMPLIANCE SCOPING & CONSULTATION CTA -->
    <section class="section" aria-label="Compliance Scoping Consultation">
      <div class="container-narrow">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Fast-Track Readiness</div>
          <h2 class="section-title">Unlock Enterprise Deals With Accredited Certification</h2>
          <p>
            Stop losing enterprise prospects due to lengthy vendor security questionnaires. Request a confidential compliance gap assessment today.
          </p>
        </div>

        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn-primary btn-lg">Engage Compliance Auditors</a>
          <a href="pricing.html" class="btn btn-outline btn-lg">View Compliance Packages</a>
        </div>
      </div>
    </section>
  </main>

{get_service_footer()}
'''

with open('pages/service-compliance.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created pages/service-compliance.html with 8 sections!")

