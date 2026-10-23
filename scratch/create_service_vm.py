import sys
from generate_service_templates import get_service_header, get_service_footer

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Continuous Vulnerability Management & Risk Prioritization | Stackly Cyber Security Services</title>
  <meta name="description" content="Proactive, continuous vulnerability management, asset discovery, and EPSS exploit-based risk prioritization to eliminate attack surface vulnerabilities before exploitation.">
  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono (Unified Design System) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/animations.css">
</head>
<body data-page="service-vulnerability-management">
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
        <span>Initializing Vulnerability Harvester...</span>
      </div>
    </div>
  </div>

{get_service_header('service-vulnerability-management', 'Vulnerability Management')}

  <main id="main-content">
    <!-- SECTION 1: ENHANCED HERO STAGE WITH CYBER IMAGE & ANIMATIONS -->
    <section class="page-hero" aria-label="Vulnerability Management Hero">
      <div class="container">
        <div class="page-hero-grid">
          <div class="page-hero-content" data-animate="fade-up">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../index.html">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="services.html">Services</a>
              <span class="breadcrumb-separator">/</span>
              <span aria-current="page">Vulnerability Management</span>
            </nav>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Continuous Attack Surface Radar
            </div>
            <h1 class="page-hero-title">Continuous Vulnerability Management & Threat Prioritization</h1>
            <p class="page-hero-desc">
              Eliminate critical exposures before threat actors weaponize them. Stackly provides 24/7 automated CVE scanning, agentless cloud discovery, and AI-driven EPSS risk contextualization backed by certified remediation engineers.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="contact.html" class="btn btn-primary btn-lg">Request Attack Surface Audit</a>
              <a href="404.html" class="btn btn-outline btn-lg">View Sample CVE Report</a>
            </div>
          </div>

          <div class="page-hero-visual" data-animate="zoom-in">
            <div class="hero-visual-radar" aria-hidden="true"></div>
            <div class="hero-visual-frame">
              <div class="hero-floating-pill pill-top-left">
                <span class="hero-pill-dot"></span> Continuous CVE Radar: Active
              </div>
              <img src="../assets/images/vulnerability-management-scanner.webp" alt="Vulnerability Management Scanner Matrix" width="480" height="280" loading="eager">
              <div class="hero-floating-pill pill-bottom-right">
                <span class="hero-pill-dot dot-amber"></span> EPSS Exploit Priority: 99.4%
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: CORE ARCHITECTURE & CAPABILITIES GRID -->
    <section class="section" aria-label="Vulnerability Management Core Architecture">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Adaptive Intelligence</div>
          <h2 class="section-title">Beyond Periodic Scans: Real-Time Surface Hardening</h2>
          <p>
            Traditional quarterly scans leave 89 days of blind spots. Our continuous pipeline monitors internal subnets, public domains, cloud instances, and third-party dependencies every minute.
          </p>
        </div>

        <div class="cards-grid-3">
          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">🌐</div>
            <h3 class="card-title">External Attack Surface Management</h3>
            <p class="card-desc">
              Continuous reconnaissance of exposed IP ranges, shadow IT micro-services, abandoned DNS records, and unauthenticated cloud buckets.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">⚙️</div>
            <h3 class="card-title">Credentialed Host & Container Scans</h3>
            <p class="card-desc">
              Deep inspection of operating system patches, misconfigured SSH/RDP daemons, privilege escalation paths, and container image registries.
            </p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">📊</div>
            <h3 class="card-title">EPSS & Threat Contextualization</h3>
            <p class="card-desc">
              We replace arbitrary CVSS numbers with Exploit Prediction Scoring (EPSS), active CISA KEV exploitation catalogs, and threat actor telemetry.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: 4-PHASE VULNERABILITY LIFECYCLE METHODOLOGY -->
    <section class="section section-alt" aria-label="Continuous Vulnerability Lifecycle">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Operational Rigor</div>
          <h2 class="section-title">The Four-Stage Continuous Hardening Pipeline</h2>
          <p>
            A standardized, closed-loop lifecycle that bridges the gap between security discovery and engineering patch execution.
          </p>
        </div>

        <div class="cards-grid-4">
          <div class="tilt-card" data-animate="fade-up">
            <div style="font-size: 2rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">01</div>
            <h4 class="card-title">Continuous Discovery</h4>
            <p class="card-desc">Real-time asset fingerprinting across multi-cloud VPCs, on-prem networks, remote endpoints, and code repositories.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div style="font-size: 2rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">02</div>
            <h4 class="card-title">Contextual Risk Ranking</h4>
            <p class="card-desc">Machine-learning triage maps reachable attack paths, data sensitivity, and active dark-web weaponization proofs.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div style="font-size: 2rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">03</div>
            <h4 class="card-title">Remediation Orchestration</h4>
            <p class="card-desc">Prescriptive patch instructions, Ansible/Terraform remediation playbooks, and automated Jira ticket routing to DevOps.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="300">
            <div style="font-size: 2rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">04</div>
            <h4 class="card-title">Verification Rescan</h4>
            <p class="card-desc">Automated non-intrusive re-testing ensures the patch successfully closed the flaw without service side-effects.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: REMEDIATION SLAS & SEVERITY BENCHMARKS -->
    <section class="section" aria-label="Remediation SLA Guarantees">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Binding Timeframes</div>
          <h2 class="section-title">Strict Remediation Service Level Agreements</h2>
          <p>
            Quantifiable turnaround timeframes ensuring high-risk exposures are quarantined immediately before threat actors exploit them.
          </p>
        </div>

        <div class="cards-grid-3">
          <div class="tilt-card" style="border-top: 3px solid var(--danger);" data-animate="fade-up">
            <div class="sim-stat-val" style="color: var(--danger);">&lt; 24 Hours</div>
            <h3 class="card-title">P1 - Critical Exposure SLA</h3>
            <p class="card-desc">
              Weaponized remote code execution (RCE) flaws, zero-auth admin bypasses, and active CISA Known Exploited Vulnerabilities.
            </p>
            <ul class="card-meta-list" style="margin-top: 1rem;">
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> 15-minute emergency alert delivery</li>
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> WAF temporary virtual patch applied</li>
            </ul>
          </div>

          <div class="tilt-card" style="border-top: 3px solid var(--warning);" data-animate="fade-up" data-delay="100">
            <div class="sim-stat-val" style="color: var(--warning);">&lt; 72 Hours</div>
            <h3 class="card-title">P2 - High Risk Exposure SLA</h3>
            <p class="card-desc">
              Privilege escalation, authenticated SQL injection, exposed internal dashboards, and missing key firmware updates.
            </p>
            <ul class="card-meta-list" style="margin-top: 1rem;">
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> Engineering remediation plan issued</li>
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> Dedicated patch verification testing</li>
            </ul>
          </div>

          <div class="tilt-card" style="border-top: 3px solid var(--primary);" data-animate="fade-up" data-delay="200">
            <div class="sim-stat-val" style="color: var(--primary);">&lt; 14 Days</div>
            <h3 class="card-title">P3/P4 - Medium & Low SLA</h3>
            <p class="card-desc">
              Information disclosure, cipher suite deprecation, TLS posture enhancements, and internal hardening recommendations.
            </p>
            <ul class="card-meta-list" style="margin-top: 1rem;">
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> Bi-weekly executive status synthesis</li>
              <li class="card-meta-item"><span class="card-meta-icon">✓</span> Compliance audit evidence export</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: SPECIALIZED VULNERABILITY ASSESSMENT ENGINEERS -->
    <section class="section section-alt" aria-label="Vulnerability Engineering Leadership">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Certified Personnel</div>
          <h2 class="section-title">Led By Industry-Recognized Exploit Researchers</h2>
          <p>
            Automated tools find symptoms; our certified exploit analysts understand real-world adversary behavior and root causes.
          </p>
        </div>

        <div class="cards-grid-2" style="max-width: 860px; margin: 0 auto;">
          <div class="person-card" data-animate="fade-up">
            <div class="person-image-wrap">
              <img src="../assets/images/vulnerability-assessment-engineer.webp" alt="Lead Vulnerability Assessment Engineer" width="400" height="260" loading="lazy">
            </div>
            <div class="person-info">
              <h3 class="person-name">Vikram Anand</h3>
              <div class="person-role">Director of Vulnerability Research & Threat Intel</div>
              <p class="person-bio">
                Ex-defense security researcher specializing in automated firmware disassembly, kernel vulnerability classification, and CVE coordination.
              </p>
              <div class="person-badges">
                <span class="person-badge">OSWE</span>
                <span class="person-badge">CISSP</span>
                <span class="person-badge">GWAPT</span>
              </div>
            </div>
          </div>

          <div class="person-card" data-animate="fade-up" data-delay="100">
            <div class="person-image-wrap">
              <img src="../assets/images/penetration-tester-marcus-vance.webp" alt="Marcus Vance Lead Pentester" width="400" height="260" loading="lazy">
            </div>
            <div class="person-info">
              <h3 class="person-name">Marcus Vance</h3>
              <div class="person-role">Principal Offensive Security Engineer</div>
              <p class="person-bio">
                Over a decade evaluating large-scale cloud footprints and complex web applications. Lead researcher behind 14 published enterprise CVE disclosures.
              </p>
              <div class="person-badges">
                <span class="person-badge">OSCP</span>
                <span class="person-badge">OSCE</span>
                <span class="person-badge">CRTO</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: ENTERPRISE SCANNER INTEGRATIONS & ECOSYSTEM -->
    <section class="section" aria-label="Scanner Ecosystem Integrations">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Unified Telemetry</div>
          <h2 class="section-title">Seamlessly Integrated With Your Security Stack</h2>
          <p>
            We ingest, deduplicate, and correlate findings across industry-standard scanning engines into a single consolidated pane of glass.
          </p>
        </div>

        <div class="cards-grid-4">
          <div class="tilt-card" data-animate="fade-up">
            <div class="card-icon-wrap">🛡️</div>
            <h4 class="card-title">Network & Host</h4>
            <p class="card-desc">Tenable.io, Qualys VMDR, Rapid7 InsightVM, and OpenVAS integrations.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="100">
            <div class="card-icon-wrap">☁️</div>
            <h4 class="card-title">Cloud Infrastructure</h4>
            <p class="card-desc">AWS Inspector, Microsoft Defender for Cloud, and Google Security Command Center.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="200">
            <div class="card-icon-wrap">📦</div>
            <h4 class="card-title">Container & K8s</h4>
            <p class="card-desc">Trivy, Aqua Security, Sysdig Secure, and Docker Scout continuous image scanning.</p>
          </div>

          <div class="tilt-card" data-animate="fade-up" data-delay="300">
            <div class="card-icon-wrap">💻</div>
            <h4 class="card-title">AppSec & DevSecOps</h4>
            <p class="card-desc">Snyk, SonarQube, GitHub Dependabot, and GitLab Security pipeline webhooks.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: ENTERPRISE CASE STUDY & IMPACT PROOF -->
    <section class="section section-alt" aria-label="Vulnerability Mitigation Case Study">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Real-World Resilience</div>
          <h2 class="section-title">Eliminating 1,400+ Critical Flaws in a Global FinTech Grid</h2>
          <p>
            How Stackly's continuous vulnerability program safeguarded a banking platform processing $4.2B in annual transaction volume.
          </p>
        </div>

        <div class="form-card" style="max-width: 920px; margin: 0 auto; background: var(--surface-card);" data-animate="zoom-in">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1.5rem; margin-bottom: 1.5rem;">
            <div>
              <div style="font-size: 2.25rem; font-weight: 800; color: var(--primary);">94.8%</div>
              <div style="font-size: 0.85rem; color: var(--text-muted);">Critical Vulnerability Reduction</div>
            </div>
            <div>
              <div style="font-size: 2.25rem; font-weight: 800; color: var(--primary);">18 Hrs</div>
              <div style="font-size: 0.85rem; color: var(--text-muted);">Mean Time to Remediate P1 Flaws</div>
            </div>
            <div>
              <div style="font-size: 2.25rem; font-weight: 800; color: var(--primary);">0</div>
              <div style="font-size: 0.85rem; color: var(--text-muted);">Production Breaches or Unscheduled Outages</div>
            </div>
          </div>
          <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.95rem; margin: 0;">
            "Before Stackly, our engineering team was overwhelmed by 400-page PDF vulnerability scanner reports that nobody had time to parse. Stackly contextualized our actual exploit risk, delivered precise patch code snippets, and reduced our exposure window from 45 days down to under 24 hours."
          </p>
          <div style="margin-top: 1rem; font-weight: 700; color: var(--text-primary); font-size: 0.9rem;">
            — VP of Engineering, Tier-1 Payments Processing Infrastructure
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: FAQ & SCOPING CONSULTATION CTA -->
    <section class="section" aria-label="Vulnerability Management Consultation">
      <div class="container-narrow">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Take Action</div>
          <h2 class="section-title">Schedule An Attack Surface Reconnaissance Audit</h2>
          <p>
            Discover what threat actors see when targeting your public IP ranges and cloud assets. Receive a comprehensive, confidential vulnerability assessment within 48 hours.
          </p>
        </div>

        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn-primary btn-lg">Engage Vulnerability Engineers</a>
          <a href="pricing.html" class="btn btn-outline btn-lg">Review Subscription Pricing</a>
        </div>
      </div>
    </section>
  </main>

{get_service_footer()}
'''

with open('pages/service-vulnerability-management.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created pages/service-vulnerability-management.html with 8 sections!")

