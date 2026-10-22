import re

with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Detailed Comparison Section with realigned, balanced, responsive layout
old_comparison_start = html.find('<section class="section section-alt" aria-label="Feature Comparison Matrix">')
old_comparison_end = html.find('<!-- SECTION 4: ROI & BREACH COST CALCULATOR -->')

realigned_comparison = '''<section class="section section-alt" aria-label="Feature Comparison Matrix" id="detailed-comparison">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="badge-tag" style="margin-bottom: 0.75rem;">
            <span class="badge-dot"></span> Architectural Specifications
          </div>
          <h2 class="section-title">Direct Feature Comparison Across Tiers</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Evaluate operational specifications, response SLAs, and dedicated engineering allocations side-by-side to choose the right clearance for your enterprise.
          </p>
        </div>

        <!-- Realigned & Centered Comparison Stage -->
        <div class="pricing-comparison-wrap" data-animate="fade-up">
          <table class="pricing-comparison-table" aria-label="Comprehensive Cyber Defense Specification Matrix">
            <thead>
              <tr>
                <th scope="col">Capability / Specification</th>
                <th scope="col">
                  <div>Essential Shield</div>
                  <div style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); margin-top: 0.25rem;">Core SMB Protection</div>
                </th>
                <th scope="col" class="col-highlight">
                  <span class="col-badge-popular">MOST POPULAR</span>
                  <div style="color: var(--primary);">Advanced SOC 24/7</div>
                  <div style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); margin-top: 0.25rem;">Mid-Enterprise Defense</div>
                </th>
                <th scope="col">
                  <div>Enterprise Zero-Trust</div>
                  <div style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); margin-top: 0.25rem;">Global Infrastructure</div>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>SOC Monitoring Hours</strong></td>
                <td>8x5 Regional Business Hours</td>
                <td class="col-highlight"><span style="color: var(--primary); font-weight: 700;">24/7/365 Continuous</span></td>
                <td><span style="color: var(--accent); font-weight: 700;">24/7/365 Continuous</span></td>
              </tr>
              <tr>
                <td><strong>P1 Critical Incident Triage SLA</strong></td>
                <td>2 Hours</td>
                <td class="col-highlight"><strong style="color: var(--primary);">15 Minutes</strong></td>
                <td><strong style="color: var(--accent);">&lt; 10 Minutes</strong></td>
              </tr>
              <tr>
                <td><strong>Included Endpoint EDR Sensors</strong></td>
                <td>Up to 50 Endpoints</td>
                <td class="col-highlight">250 Endpoints</td>
                <td>Unlimited Scale</td>
              </tr>
              <tr>
                <td><strong>Multi-Cloud VPC Ingestion</strong></td>
                <td>1 Production VPC</td>
                <td class="col-highlight">Up to 8 Multi-Cloud VPCs</td>
                <td>Unlimited Hybrid Fabrics</td>
              </tr>
              <tr>
                <td><strong>Offensive Red Team Penetration Testing</strong></td>
                <td>Annual Automated Baseline</td>
                <td class="col-highlight">Bi-Weekly Scans + 1 Manual Test</td>
                <td>Continuous Red Teaming</td>
              </tr>
              <tr>
                <td><strong>Emergency IR Retainer SLA</strong></td>
                <td>Best Effort (4-8 Hours)</td>
                <td class="col-highlight">4 Hours Guaranteed On-Call</td>
                <td>1 Hour Dedicated Pod</td>
              </tr>
              <tr>
                <td><strong>Compliance Assurance Vault (ISO/SOC2)</strong></td>
                <td>Quarterly Snapshots</td>
                <td class="col-highlight">Continuous Automated Evidence</td>
                <td>Full Auditor-Ready Portal</td>
              </tr>
              <tr>
                <td><strong>Dedicated Senior Cyber Architect</strong></td>
                <td>Shared Ticket Pool</td>
                <td class="col-highlight">Dedicated Named Lead Pod</td>
                <td>Direct 24/7 Executive Hotline</td>
              </tr>
              <tr>
                <td style="border-bottom: none;"><strong>Deployment Action</strong></td>
                <td class="pricing-table-cta">
                  <a href="404.html" class="btn btn-outline btn-sm btn-block">Deploy Essential</a>
                </td>
                <td class="pricing-table-cta col-highlight">
                  <a href="404.html" class="btn btn-primary btn-sm btn-block">Deploy Advanced SOC</a>
                </td>
                <td class="pricing-table-cta">
                  <a href="404.html" class="btn btn-outline btn-sm btn-block">Deploy Zero-Trust</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    '''

if old_comparison_start != -1 and old_comparison_end != -1:
    html = html[:old_comparison_start] + realigned_comparison + html[old_comparison_end:]
    print("Replaced Detailed Comparison section successfully in pricing.html")
else:
    print("Warning: could not find comparison section boundaries in pricing.html")

# 2. Add Section 7 and Section 8 before </main>
sec_end = html.find('</main>')

sections_7_and_8 = '''    <!-- SECTION 7: ENTERPRISE TACTICAL ADD-ONS -->
    <section class="section section-alt" aria-label="Enterprise Tactical Add-Ons">
      <div class="container">
        <div class="section-header" data-animate="fade-up">
          <div class="section-subtitle">Modular Defense Upgrades</div>
          <h2 class="section-title">Specialized Security Add-Ons & Retainers</h2>
          <p style="max-width: 680px; margin: 0 auto;">
            Expand your security umbrella on demand with dedicated forensic appliances, dark web intelligence syndication, and sovereign compliance accelerators.
          </p>
        </div>

        <div class="cards-grid-3" data-animate="fade-up">
          <div class="tilt-card">
            <div class="card-icon">⚡</div>
            <h3 class="card-title">15-Minute Critical IR Retainer</h3>
            <p class="card-desc">
              Pre-funded incident response hours with guaranteed sub-15-minute digital forensic engineer dispatch and live incident bridge activation.
            </p>
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary); margin: 1rem 0;">From $1,500<span style="font-size: 0.8rem; color: var(--text-muted);">/mo</span></div>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">Add to Agreement</a>
          </div>

          <div class="tilt-card">
            <div class="card-icon">🕵️</div>
            <h3 class="card-title">Dark Web Credential Surveillance</h3>
            <p class="card-desc">
              Automated surveillance of Russian and underground cybercrime forums for corporate domains, executive passwords, and leaked source code.
            </p>
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary); margin: 1rem 0;">From $850<span style="font-size: 0.8rem; color: var(--text-muted);">/mo</span></div>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">Add to Agreement</a>
          </div>

          <div class="tilt-card">
            <div class="card-icon">📜</div>
            <h3 class="card-title">Automated ISO 27001 Audit Vault</h3>
            <p class="card-desc">
              Automated evidence harvester mapping cloud telemetry directly to ISO 27001:2022 Annex A controls and SOC 2 Trust Principles.
            </p>
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary); margin: 1rem 0;">From $1,200<span style="font-size: 0.8rem; color: var(--text-muted);">/mo</span></div>
            <a href="404.html" class="btn btn-outline btn-sm btn-block">Add to Agreement</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: PROCUREMENT & COMPLIANCE ASSURANCE -->
    <section class="section" aria-label="Procurement and Legal Framework">
      <div class="container">
        <div class="hero-grid">
          <div data-animate="fade-up">
            <div class="section-subtitle">Enterprise Assurance</div>
            <h2 class="section-title">Institutional Procurement & Legal Guarantees</h2>
            <p style="margin-bottom: 1.25rem;">
              Stackly operates under standardized enterprise procurement legal frameworks, including enterprise Master Services Agreements (MSA), Business Associate Agreements (BAA) for healthcare, and Data Processing Agreements (DPA).
            </p>
            <div style="display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 2rem;">
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="color: var(--accent); font-weight: 800;">✓</span>
                <span style="color: var(--text-secondary); font-size: 0.95rem;">Mutual NDA signed electronically prior to technical scoping</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="color: var(--accent); font-weight: 800;">✓</span>
                <span style="color: var(--text-secondary); font-size: 0.95rem;">FIPS 140-3 hardware encryption keys strictly controlled by client</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="color: var(--accent); font-weight: 800;">✓</span>
                <span style="color: var(--text-secondary); font-size: 0.95rem;">Net 30 invoice procurement terms for approved enterprise accounts</span>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="404.html" class="btn btn-primary">
                <span>📄</span> Download Master Services Agreement (MSA)
              </a>
              <a href="404.html" class="btn btn-outline">
                <span>🔒</span> Security Whitepaper
              </a>
            </div>
          </div>

          <div data-animate="zoom-in" data-delay="150">
            <div class="hero-visual-card js-tilt" style="padding: 2rem;">
              <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: var(--text-primary);">
                <span>🛡️</span> Sovereign Security Warranties
              </h3>
              <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
                Every Stackly tier includes contractual financial compensation clauses in the event of documented SLA breach or detection latency failures.
              </p>
              <div style="background: rgba(0, 0, 0, 0.4); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                  <span style="color: var(--text-muted); font-size: 0.85rem;">SLA Penalty Credit:</span>
                  <span style="color: var(--accent); font-weight: 700;">Up to 50% Monthly Fee</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                  <span style="color: var(--text-muted); font-size: 0.85rem;">Underwritten Warranty:</span>
                  <span style="color: var(--primary); font-weight: 700;">$10,000,000 Policy</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--text-muted); font-size: 0.85rem;">Data Residency:</span>
                  <span style="color: var(--text-primary); font-weight: 700;">Zero Egress Guarantee</span>
                </div>
              </div>
              <a href="404.html" class="btn btn-outline btn-block btn-sm">
                View Underwriting Certificate
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

if sec_end != -1:
    html = html[:sec_end] + sections_7_and_8 + html[sec_end:]
    print("Added Sections 7 & 8 to pricing.html!")
else:
    print("Warning: could not find </main> in pricing.html")

# Ensure all action links in pricing.html redirect to 404
html = html.replace('href="contact.html" class="btn btn-secondary"', 'href="404.html" class="btn btn-secondary"')
html = html.replace('href="contact.html" class="btn btn-secondary btn-lg"', 'href="404.html" class="btn btn-secondary btn-lg"')

with open('pages/pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("pages/pricing.html updated successfully!")

