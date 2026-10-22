import re

# ==============================================================================
# 1. EXPAND pages/about.html (currently 6 -> target 8 sections)
# ==============================================================================
with open('pages/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

about_sections_7_8 = '''    <!-- SECTION 7: GLOBAL ACCREDITATIONS & CLEARANCES -->
    <section class="section section-alt" aria-label="Security Clearances and Accreditations">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Institutional Clearances</div>
          <h2 class="section-title">Recognized Industry Accreditations & Standards</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Our security personnel maintain the industry's highest military and enterprise defense certifications, validated annually by external certification bodies.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2.25rem; margin-bottom: 0.75rem;">🛡️</div>
            <h3 class="card-title" style="font-size: 1.1rem;">ISO/IEC 27001:2022</h3>
            <p class="card-desc" style="font-size: 0.85rem;">
              Certified Information Security Management System covering all multi-tenant operations.
            </p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">View Certificate</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2.25rem; margin-bottom: 0.75rem;">📜</div>
            <h3 class="card-title" style="font-size: 1.1rem;">AICPA SOC 2 Type II</h3>
            <p class="card-desc" style="font-size: 0.85rem;">
              Unqualified clean opinion spanning Security, Confidentiality, and 99.99% Availability.
            </p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">Audit Report</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2.25rem; margin-bottom: 0.75rem;">🎯</div>
            <h3 class="card-title" style="font-size: 1.1rem;">CREST Accredited</h3>
            <p class="card-desc" style="font-size: 0.85rem;">
              CREST Certified Penetration Testing providers adhering to rigorous ethical testing charters.
            </p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">Member Badge</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2.25rem; margin-bottom: 0.75rem;">🔒</div>
            <h3 class="card-title" style="font-size: 1.1rem;">FIPS 140-3 Cryptography</h3>
            <p class="card-desc" style="font-size: 0.85rem;">
              Hardware Security Modules (HSM) validated for government-grade cryptographic token security.
            </p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">Validation Spec</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: GLOBAL FOLLOW-THE-SUN SOC MESH -->
    <section class="section" aria-label="Global Operations Mesh">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">24/7 Resilience</div>
            <h2 class="section-title">Follow-the-Sun Distributed Command Centers</h2>
            <p style="margin-bottom: 1.25rem;">
              Cyber adversaries do not respect time zones. Stackly operates interconnected Security Operations Command hubs strategically distributed across India, Southeast Asia, Europe, and the Americas.
            </p>
            <p style="color: var(--text-secondary); margin-bottom: 1.75rem;">
              Whenever an alert triggers in your cloud infrastructure, it is ingested by awake, highly focused Tier-3 analysts executing verified threat playbooks without fatigue or shift handover delays.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>🌐</span> Tour Virtual SOC Grid
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>📑</span> SLA Performance Metrics
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.2rem; color: var(--text-primary); margin-bottom: 1.25rem;">
                <span>📡</span> Active SOC Node Status
              </h3>
              <div style="display: flex; flex-direction: column; gap: 0.85rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem; background: rgba(0,0,0,0.3); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div>
                    <strong style="color: var(--text-primary); font-size: 0.9rem;">Salem Command Hub (India)</strong>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Primary Sovereign Operations Enclave</div>
                  </div>
                  <span class="severity-pill severity-low">Online (Alpha Shift)</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem; background: rgba(0,0,0,0.3); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div>
                    <strong style="color: var(--text-primary); font-size: 0.9rem;">London Cyber Center (UK)</strong>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">EMEA Threat Telemetry Ingestion</div>
                  </div>
                  <span class="severity-pill severity-low">Online (Beta Shift)</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem; background: rgba(0,0,0,0.3); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div>
                    <strong style="color: var(--text-primary); font-size: 0.9rem;">Singapore Node (APAC)</strong>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">High-Frequency Cloud Sensor Radar</div>
                  </div>
                  <span class="severity-pill severity-low">Online (Gamma Shift)</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

about_main_end = about_html.find('</main>')
if about_main_end != -1 and 'SECTION 7: GLOBAL ACCREDITATIONS' not in about_html:
    about_html = about_html[:about_main_end] + about_sections_7_8 + about_html[about_main_end:]
    with open('pages/about.html', 'w', encoding='utf-8') as f:
        f.write(about_html)
    print("Added Sections 7 & 8 to pages/about.html")


# ==============================================================================
# 2. EXPAND pages/services.html (currently 5 -> target 8 sections)
# ==============================================================================
with open('pages/services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

services_sections_6_7_8 = '''    <!-- SECTION 6: UNIFIED DEFENSE TECHNOLOGY STACK -->
    <section class="section section-alt" aria-label="Defense Technology Ecosystem">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Integration Ecosystem</div>
          <h2 class="section-title">Enterprise Technology Stack & Ingestion Connectors</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            We interface natively with your existing enterprise infrastructure with zero vendor lock-in and zero friction.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">☁️</div>
            <h4 class="card-title">Cloud Platforms</h4>
            <p class="card-desc" style="font-size: 0.85rem;">AWS CloudTrail, Azure Sentinel, GCP Cloud Logging, Cloudflare WAF.</p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block" style="margin-top: 0.75rem;">View Connectors</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💻</div>
            <h4 class="card-title">Endpoint & EDR</h4>
            <p class="card-desc" style="font-size: 0.85rem;">CrowdStrike Falcon, Microsoft Defender, SentinelOne, Carbon Black.</p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block" style="margin-top: 0.75rem;">View Connectors</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📦</div>
            <h4 class="card-title">K8s & Containers</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Falco eBPF runtime security, Aqua Security, Prisma Cloud, Cilium.</p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block" style="margin-top: 0.75rem;">View Connectors</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔑</div>
            <h4 class="card-title">Identity & Access</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Okta, Azure Active Directory, HashiCorp Vault, CyberArk PAM.</p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block" style="margin-top: 0.75rem;">View Connectors</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: PROPRIETARY THREAT INTELLIGENCE SYNDICATION -->
    <section class="section" aria-label="Threat Intelligence Syndication">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">Predictive Intelligence</div>
            <h2 class="section-title">Dark Web Reconnaissance & Adversary Tracking</h2>
            <p style="margin-bottom: 1.25rem;">
              Stackly operates an autonomous fleet of covert dark web crawler honeypots infiltrating underground forums, illicit ransomware negotiation channels, and Russian Telegram bot networks.
            </p>
            <p style="color: var(--text-secondary); margin-bottom: 1.75rem;">
              When threat actors trade credentials or stage attack tooling targeting your industry vertical, our analysts ingest indicators of compromise (IOCs) before the first packet strikes your perimeter.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>🔍</span> Sample Threat Intelligence Bulletin
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>📑</span> Honeypot Methodology
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem;">
                <span>⚡</span> Ingested Threat Feed Feats
              </h3>
              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                    <span style="font-size: 0.8rem; color: var(--text-muted);">CISA KEV Catalog</span>
                    <span style="font-size: 0.8rem; color: var(--accent);">Synchronized (5m ago)</span>
                  </div>
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">1,180 Actively Exploited CVE Signatures</strong>
                </div>

                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                    <span style="font-size: 0.8rem; color: var(--text-muted);">MITRE ATT&CK Matrix v15</span>
                    <span style="font-size: 0.8rem; color: var(--primary);">100% Mapped</span>
                  </div>
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">620 Adversary TTP Detection Playbooks</strong>
                </div>

                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Dark Web Botnet Trackers</span>
                    <span style="font-size: 0.8rem; color: var(--accent);">Active Defense</span>
                  </div>
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">4.8M Malicious IP & C2 Indicators Blocked</strong>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: 14-DAY RAPID ONBOARDING ROADMAP -->
    <section class="section section-alt" aria-label="Client Onboarding Roadmap">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Frictionless Transition</div>
          <h2 class="section-title">Your 14-Day Sovereign SOC Onboarding Journey</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Our dedicated security engineers ensure an airtight transition with zero business interruption and rapid time-to-value.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card">
            <span class="step-num">01</span>
            <h4 class="card-title">Days 1 - 3: Scoping</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Architecture review, compliance boundary mapping, and mutual NDA execution with zero-trust key setup.
            </p>
          </div>

          <div class="tilt-card">
            <span class="step-num">02</span>
            <h4 class="card-title">Days 4 - 7: Connectors</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              API log forwarding configured across cloud VPCs, identity providers, and server fleet without downtime.
            </p>
          </div>

          <div class="tilt-card">
            <span class="step-num">03</span>
            <h4 class="card-title">Days 8 - 11: Tuning</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              AI behavioral baseline learning, custom threshold calibration, and false-positive suppression rules.
            </p>
          </div>

          <div class="tilt-card">
            <span class="step-num">04</span>
            <h4 class="card-title">Days 12 - 14: Go-Live</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Simulated red team drill execution, automated containment activation, and 24/7 handover ceremony.
            </p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;" data-animate="fade-up">
          <a href="404.html" class="btn btn-primary btn-lg">
            <span>🛡️</span> Schedule Scoping Consultation
          </a>
        </div>
      </div>
    </section>
'''

services_main_end = services_html.find('</main>')
if services_main_end != -1 and 'SECTION 6: UNIFIED DEFENSE' not in services_html:
    services_html = services_html[:services_main_end] + services_sections_6_7_8 + services_html[services_main_end:]
    with open('pages/services.html', 'w', encoding='utf-8') as f:
        f.write(services_html)
    print("Added Sections 6, 7 & 8 to pages/services.html")


# ==============================================================================
# 3. EXPAND pages/service-soc.html (currently 7 -> target 8 sections)
# ==============================================================================
with open('pages/service-soc.html', 'r', encoding='utf-8') as f:
    soc_html = f.read()

soc_section_8 = '''    <!-- SECTION 8: MULTI-CLOUD INGESTION COMPATIBILITY -->
    <section class="section section-alt" aria-label="Multi-Cloud Ingestion Compatibility">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Universal Sensor Ingestion</div>
          <h2 class="section-title">Supported Sensor Ingestion Fabrics</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Our Managed SOC ingests native telemetry seamlessly across all major hyperscalers and on-premises infrastructure.
          </p>
        </div>

        <div class="cards-grid-3" data-animate="fade-up">
          <div class="tilt-card">
            <div class="card-icon">☁️</div>
            <h4 class="card-title">Amazon Web Services (AWS)</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Native integration with AWS CloudTrail, GuardDuty, VPC Flow Logs, Security Hub, and AWS WAF with cross-account IAM role assumption.
            </p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">View AWS Reference Architecture</a>
          </div>

          <div class="tilt-card">
            <div class="card-icon">🔷</div>
            <h4 class="card-title">Microsoft Azure & Entra ID</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Real-time ingestion of Azure Activity Logs, Microsoft Defender for Cloud, Sentinel SIEM feeds, and Entra ID conditional access telemetries.
            </p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">View Azure Integration Spec</a>
          </div>

          <div class="tilt-card">
            <div class="card-icon">🌐</div>
            <h4 class="card-title">Google Cloud & Kubernetes</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Full support for Google Cloud Audit Logs, Security Command Center, GKE container audit pipelines, and Falco eBPF security daemonsets.
            </p>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">View GCP Integration Spec</a>
          </div>
        </div>
      </div>
    </section>
'''

soc_main_end = soc_html.find('</main>')
if soc_main_end != -1 and 'SECTION 8: MULTI-CLOUD INGESTION' not in soc_html:
    soc_html = soc_html[:soc_main_end] + soc_section_8 + soc_html[soc_main_end:]
    with open('pages/service-soc.html', 'w', encoding='utf-8') as f:
        f.write(soc_html)
    print("Added Section 8 to pages/service-soc.html")


# ==============================================================================
# 4. EXPAND pages/service-pentest.html (currently 6 -> target 8 sections)
# ==============================================================================
with open('pages/service-pentest.html', 'r', encoding='utf-8') as f:
    pentest_html = f.read()

pentest_sections_7_8 = '''    <!-- SECTION 7: TESTING METHODOLOGIES & BENCHMARKS -->
    <section class="section section-alt" aria-label="Testing Methodologies and Frameworks">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Rigorous Standards</div>
          <h2 class="section-title">International Penetration Testing Methodologies</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Our offensive assessments strictly follow global institutional cyber security testing frameworks to guarantee repeatability and depth.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📘</div>
            <h4 class="card-title">OWASP Top 10 & ASVS</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Application Security Verification Standard levels 1 through 3 for modern web and mobile APIs.</p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">View Standard</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚔️</div>
            <h4 class="card-title">PTES Standard</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Penetration Testing Execution Standard covering all 7 phases from intelligence gathering to post-exploitation.</p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">View Standard</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📜</div>
            <h4 class="card-title">NIST SP 800-115</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Technical Guide to Information Security Testing and Assessment for regulated federal and financial entities.</p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">View Standard</a>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔬</div>
            <h4 class="card-title">OSSTMM 3.0</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Open Source Security Testing Methodology Manual providing empirical security metrics and operational ratings.</p>
            <a href="404.html" class="badge-tag" style="margin-top: 0.5rem; text-decoration: none;">View Standard</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: REMEDIATION VERIFICATION & RETESTING SLA -->
    <section class="section" aria-label="Remediation Support and Retesting Guarantee">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">Zero Guesswork</div>
            <h2 class="section-title">90-Day Free Retesting & Verified Attestation</h2>
            <p style="margin-bottom: 1.25rem;">
              A penetration test is only valuable if vulnerabilities are successfully patched. We partner with your engineering teams to review source code fixes and re-execute exploits free of charge within 90 days.
            </p>
            <p style="color: var(--text-secondary); margin-bottom: 1.75rem;">
              Once remediations are validated, our CREST-certified lead testers issue an authoritative Letter of Clean Attestation accepted by enterprise vendor risk departments, auditors, and cyber insurance underwriters.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>📄</span> Sample Executive Attestation Letter
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>🔒</span> Red Team Playbook Guide
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem;">
                <span>🛡️</span> Deliverables Guarantee
              </h3>
              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Executive Summary (C-Suite & Board)</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">High-level business risk impact without dense jargon.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Technical Finding Sheets (Developers)</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Step-by-step reproduction scripts & drop-in patch snippets.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Live Engineering Debrief Session</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">60-minute video conference with the testing team.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

pentest_main_end = pentest_html.find('</main>')
if pentest_main_end != -1 and 'SECTION 7: TESTING METHODOLOGIES' not in pentest_html:
    pentest_html = pentest_html[:pentest_main_end] + pentest_sections_7_8 + pentest_html[pentest_main_end:]
    with open('pages/service-pentest.html', 'w', encoding='utf-8') as f:
        f.write(pentest_html)
    print("Added Sections 7 & 8 to pages/service-pentest.html")


# ==============================================================================
# 5. EXPAND pages/service-cloud-security.html (currently 6 -> target 8 sections)
# ==============================================================================
with open('pages/service-cloud-security.html', 'r', encoding='utf-8') as f:
    cloud_html = f.read()

cloud_sections_7_8 = '''    <!-- SECTION 7: ZERO TRUST ARCHITECTURE PRINCIPLES -->
    <section class="section section-alt" aria-label="Zero Trust Architectural Pillars">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Core Pillars</div>
          <h2 class="section-title">Zero-Trust Architectural Implementation Pillars</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            "Never trust, always verify." Our architecture dismantles perimeter-only defense models in favor of continuous cryptographic authorization.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔐</div>
            <h4 class="card-title">Identity as Perimeter</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Every user, service account, and workload authenticates dynamically using ephemeral mTLS certificates and biometric hardware tokens.
            </p>
          </div>

          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🧱</div>
            <h4 class="card-title">Microsegmentation</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Workload isolation policies isolating databases from web tiers so breached credentials cannot pivot laterally across subnets.
            </p>
          </div>

          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <h4 class="card-title">Least-Privilege IAM</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              Automated pruning of over-permissioned cloud roles with Just-In-Time (JIT) access grants expiring automatically within 60 minutes.
            </p>
          </div>

          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
            <h4 class="card-title">Continuous Telemetry</h4>
            <p class="card-desc" style="font-size: 0.85rem;">
              eBPF system call monitoring inspecting process executions inside Kubernetes containers before kernel execution.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: INFRASTRUCTURE AS CODE (IAC) DRIFT SCANNING -->
    <section class="section" aria-label="IaC Security and CI/CD Guardrails">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">Shift Left Security</div>
            <h2 class="section-title">Automated Terraform & CloudFormation Guardrails</h2>
            <p style="margin-bottom: 1.25rem;">
              Security begins before code is ever merged. Our cloud architects embed automated policy-as-code guardrails into your GitHub Actions, GitLab CI, and AWS CodePipeline workflows.
            </p>
            <p style="color: var(--text-secondary); margin-bottom: 1.75rem;">
              Prevent exposed S3 buckets, permissive security groups, and unencrypted EBS volumes from deploying into production with instant developer feedback in pull requests.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>🛡️</span> Request Cloud Architecture Review
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>📑</span> CIS Benchmark Scoring Guide
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem;">
                <span>⚙️</span> Automated CI/CD Safeguards
              </h3>
              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Terraform Drift Detection (Hourly)</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Auto-reverts manual console changes that violate security baselines.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Secrets & Token Leak Prevention</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Pre-commit hooks intercepting hardcoded AWS keys or JWT secrets.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Container Image Vulnerability Gate</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Blocks deployment of Docker images containing Critical CVEs.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

cloud_main_end = cloud_html.find('</main>')
if cloud_main_end != -1 and 'SECTION 7: ZERO TRUST ARCHITECTURE' not in cloud_html:
    cloud_html = cloud_html[:cloud_main_end] + cloud_sections_7_8 + cloud_html[cloud_main_end:]
    with open('pages/service-cloud-security.html', 'w', encoding='utf-8') as f:
        f.write(cloud_html)
    print("Added Sections 7 & 8 to pages/service-cloud-security.html")


# ==============================================================================
# 6. EXPAND pages/service-incident-response.html (currently 6 -> target 8 sections)
# ==============================================================================
with open('pages/service-incident-response.html', 'r', encoding='utf-8') as f:
    ir_html = f.read()

ir_sections_7_8 = '''    <!-- SECTION 7: FORENSIC CHAIN OF CUSTODY EVIDENCE VAULT -->
    <section class="section section-alt" aria-label="Digital Forensics and Chain of Custody">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Court-Admissible Evidence</div>
          <h2 class="section-title">Cryptographic Chain-of-Custody & Forensic Vault</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Our digital forensics team preserves critical evidence according to NIST SP 800-86 and ISO/IEC 27037 standards to support law enforcement and litigation.
          </p>
        </div>

        <div class="cards-grid-4" data-animate="fade-up">
          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💾</div>
            <h4 class="card-title">Volatile RAM Dumps</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Live memory captures extracting unencrypted C2 decryption keys and injected DLLs.</p>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💿</div>
            <h4 class="card-title">Bit-Stream Disk Images</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Cryptographically verified bit-for-bit physical disk clones using hardware write-blockers.</p>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔐</div>
            <h4 class="card-title">SHA-256 Hashing</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Immutable cryptographic hash verification ensuring zero evidence tampering or contamination.</p>
          </div>

          <div class="tilt-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📜</div>
            <h4 class="card-title">Expert Testimony</h4>
            <p class="card-desc" style="font-size: 0.85rem;">Court-ready sworn affidavits and expert witness forensic testimony for cyber litigation.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: POST-BREACH HARDENING & EXECUTIVE REPORTING -->
    <section class="section" aria-label="Post-Incident Hardening and Surveillance">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">Long-Term Defense</div>
            <h2 class="section-title">Post-Breach Remediation & 60-Day Surveillance</h2>
            <p style="margin-bottom: 1.25rem;">
              Containing the active breach is only half the battle. Adversaries frequently leave dormant persistence mechanisms, secondary backdoors, or scheduled tasks designed to detonate months later.
            </p>
            <p style="color: var(--text-secondary); margin-bottom: 1.75rem;">
              Stackly implements comprehensive root cause analysis, adversary attribution, and maintains high-vigilance threat hunter surveillance over your network for 60 consecutive days post-containment.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>🚨</span> Dispatch Rapid Incident Commander
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>📑</span> Post-Incident Hardening Roadmap
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem;">
                <span>🛡️</span> Retainer SLA Guarantees
              </h3>
              <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Emergency Hotline Response: &lt; 15 Minutes</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Direct bridge to named Senior Incident Commander.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">On-Site Dispatch (Global): &lt; 4 Hours</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Forensic personnel deployable with flyaway forensic kits.</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                  <strong style="color: var(--text-primary); font-size: 0.85rem;">Full Regulatory Disclosure Dossier: &lt; 72 Hours</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.25rem;">Mandatory GDPR Article 33 and SEC Form 8-K breach briefs.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

ir_main_end = ir_html.find('</main>')
if ir_main_end != -1 and 'SECTION 7: FORENSIC CHAIN OF CUSTODY' not in ir_html:
    ir_html = ir_html[:ir_main_end] + ir_sections_7_8 + ir_html[ir_main_end:]
    with open('pages/service-incident-response.html', 'w', encoding='utf-8') as f:
        f.write(ir_html)
    print("Added Sections 7 & 8 to pages/service-incident-response.html")

print("All sections expanded across all subpages!")

