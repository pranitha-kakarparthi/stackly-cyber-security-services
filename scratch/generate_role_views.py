# -*- coding: utf-8 -*-
"""
Generates the fully expanded, multi-section, responsive dashboard with:
- Topbar adjustments with comfortable spacing
- Drawer backdrop for seamless mobile interaction
- 3 independent role dashboards in module-overview, EACH with 8-9 rich domain-specific sections
- Modules 2 through 8 (Threats, Vulnerabilities, Firewall, Incidents, Compliance, Reports, Users),
  EACH with 8 distinct, non-repeated, deeply relevant cyber security sections.
"""

# Let's write the module generators
ciso_html = """
          <!-- ==================================================================
               ROLE 1: CHIEF INFORMATION SECURITY OFFICER (CISO) DASHBOARD
               Contains 8 distinct, comprehensive, non-repeating strategic sections
               ================================================================== -->
          <div id="view-role-ciso" class="role-dashboard-container">
            <!-- SECTION 1: CISO COMMAND BANNER & HIGH-PRIORITY GOVERNANCE -->
            <section class="dash-section" aria-label="Executive Enclave Command">
              <div style="background: linear-gradient(135deg, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2.5vw, 2rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
                <div>
                  <span class="badge-tag" style="margin-bottom: 0.5rem;">
                    <span class="badge-dot"></span> Executive CISO Enclave • Top-Secret Clearance Active
                  </span>
                  <h2 style="font-size: clamp(1.35rem, 2vw, 1.75rem); margin-bottom: 0.35rem; font-weight: 800; color: var(--text-primary);">
                    Enterprise Cyber Risk & Governance Command
                  </h2>
                  <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px; line-height: 1.5;">
                    Real-time strategic oversight of global enterprise cyber resilience, board threat indicators, Lloyd's loss prevention warranty attestation, and continuous regulatory compliance.
                  </p>
                </div>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                  <button type="button" class="btn btn-primary btn-sm dash-action-btn">
                    <span>📑</span> Generate Board Briefing (PDF)
                  </button>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">
                    <span>🛡️</span> Authorize Security Policy
                  </button>
                </div>
              </div>
            </section>

            <!-- SECTION 2: BOARD-LEVEL STRATEGIC KPI MATRIX -->
            <section class="dash-section" aria-label="Strategic Cyber Defense KPIs">
              <div class="dash-section-header">
                <div>
                  <h3 class="dash-section-title"><span>📊</span> Strategic Board Resilience Metrics</h3>
                  <div class="dash-section-subtitle">Real-time quantifications aligned with FAIR risk governance models</div>
                </div>
                <span class="badge-tag">Audited Today</span>
              </div>
              <div class="dash-kpi-grid">
                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Enterprise Resilience Score</span>
                    <span class="kpi-icon">🛡️</span>
                  </div>
                  <div class="kpi-value" style="color: var(--primary);">94 / 100</div>
                  <div class="kpi-trend up">
                    <span>↑ +4 pts</span> Tier 1 Sovereign Zero-Trust Posture
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Annual Cyber Defense ROI</span>
                    <span class="kpi-icon">📈</span>
                  </div>
                  <div class="kpi-value" style="color: var(--accent);">+340%</div>
                  <div class="kpi-trend up">
                    <span>✓ $14.2M</span> Estimated breach loss averted
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Regulatory Audit Assurance</span>
                    <span class="kpi-icon">📜</span>
                  </div>
                  <div class="kpi-value" style="color: var(--text-primary);">100% Pass</div>
                  <div class="kpi-trend up">
                    <span>✓ ISO 27001</span> SOC 2 Type II, HIPAA, GDPR
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Cyber Liability Warranty</span>
                    <span class="kpi-icon">🔒</span>
                  </div>
                  <div class="kpi-value" style="color: var(--text-primary);">$10,000,000</div>
                  <div class="kpi-trend up">
                    <span>✓ Underwritten</span> Active with Lloyd's syndicate
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 3: ENTERPRISE CYBER RISK HEATMAP & ASSET EXPOSURE -->
            <section class="dash-section" aria-label="Enterprise Cyber Risk Heatmap">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>📊</span> Enterprise Cyber Risk Heatmap & Financial Exposure (Q4 2026)
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Assessed across crown-jewel business data stores and mission-critical hybrid endpoints
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export Risk Matrix</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="CISO Risk Heatmap Table">
                    <thead>
                      <tr>
                        <th>Asset & Core Business Domain</th>
                        <th>Exposure Level</th>
                        <th>Potential Financial Impact</th>
                        <th>Mean Dwell Time</th>
                        <th>Compensating Controls</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Customer PII Storage & Core DB</strong></td>
                        <td><span class="severity-pill severity-low">Minimal Risk</span></td>
                        <td>$8,400,000 (Averted)</td>
                        <td>0.00 Mins</td>
                        <td>FIPS 140-3 Hardware Token & AES-256-GCM</td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Review</button></td>
                      </tr>
                      <tr>
                        <td><strong>Active Directory Root Forest</strong></td>
                        <td><span class="severity-pill severity-low">Hardened</span></td>
                        <td>$4,200,000 (Protected)</td>
                        <td>&lt; 3.0 Mins</td>
                        <td>Continuous Kerberos Sentinel & Tier-0 Separation</td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Review</button></td>
                      </tr>
                      <tr>
                        <td><strong>SWIFT Financial Settlement Rail</strong></td>
                        <td><span class="severity-pill severity-low">Isolated</span></td>
                        <td>$12,000,000 (Air-Gapped)</td>
                        <td>0.00 Mins</td>
                        <td>BGP Microsegmentation & Dual-Key Approval</td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Review</button></td>
                      </tr>
                      <tr>
                        <td><strong>Kubernetes Microservice Ingress</strong></td>
                        <td><span class="severity-pill severity-medium">Medium Risk</span></td>
                        <td>$1,200,000 (Mitigated)</td>
                        <td>&lt; 15.0 Mins</td>
                        <td>Falco eBPF Syscall Monitor & Istio mTLS Mesh</td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Review</button></td>
                      </tr>
                      <tr>
                        <td><strong>AWS Production VPC (us-east-1)</strong></td>
                        <td><span class="severity-pill severity-low">Compliant</span></td>
                        <td>$3,500,000 (Covered)</td>
                        <td>&lt; 4.0 Mins</td>
                        <td>GuardDuty + Stackly Sensor Continuous Telemetry</td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Review</button></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 4: CISO STRATEGIC GOVERNANCE & EXECUTIVE APPROVALS -->
            <section class="dash-section" aria-label="Executive Approvals Queue">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>✍️</span> CISO Executive Approvals & Policy Exceptions Queue
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Requires CISO cryptographic sign-off under Zero-Trust Governance Mandate
                    </div>
                  </div>
                  <span class="badge-tag">3 Pending Actions</span>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table">
                    <thead>
                      <tr>
                        <th>Policy Change Request</th>
                        <th>Requesting Lead</th>
                        <th>Business Justification</th>
                        <th>Risk Assessment</th>
                        <th>Action Required</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Zero-Trust mTLS Rollout Exemption</strong></td>
                        <td>Priya Sharma (Data Eng)</td>
                        <td>Legacy Mainframe ETL ingest pipeline migration</td>
                        <td><span class="severity-pill severity-medium">Compensating IPSEC in Place</span></td>
                        <td>
                          <div style="display: flex; gap: 0.5rem;">
                            <button type="button" class="btn btn-primary btn-sm dash-action-btn">Approve</button>
                            <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Deny</button>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td><strong>Cloudflare WAF Custom Rule Bypass</strong></td>
                        <td>David Chen (SRE Lead)</td>
                        <td>Payment gateway webhooks high-throughput load test</td>
                        <td><span class="severity-pill severity-low">Temporary 2-Hour Window</span></td>
                        <td>
                          <div style="display: flex; gap: 0.5rem;">
                            <button type="button" class="btn btn-primary btn-sm dash-action-btn">Approve</button>
                            <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Deny</button>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td><strong>CrowdStrike Sensor Expansion (+250 Nodes)</strong></td>
                        <td>Alex Vance (SOC Commander)</td>
                        <td>Acquisition infrastructure integration (Salem Command)</td>
                        <td><span class="severity-pill severity-low">Zero Security Impact</span></td>
                        <td>
                          <div style="display: flex; gap: 0.5rem;">
                            <button type="button" class="btn btn-primary btn-sm dash-action-btn">Approve</button>
                            <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Deny</button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 5: MULTI-STANDARD REGULATORY COMPLIANCE SCORECARD -->
            <section class="dash-section" aria-label="Regulatory Compliance Scorecard">
              <div class="dash-section-header">
                <div>
                  <h3 class="dash-section-title"><span>📜</span> Multi-Standard Continuous Regulatory Compliance</h3>
                  <div class="dash-section-subtitle">Real-time control synchronization mapped against international statutory frameworks</div>
                </div>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Audit Evidence Vault</button>
              </div>
              <div class="dash-grid-4">
                <div class="dash-stat-card">
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: var(--primary);">ISO/IEC 27001</span>
                    <span class="severity-pill severity-low">93/93 Controls</span>
                  </div>
                  <div class="dash-stat-val">100% Certified</div>
                  <div class="dash-stat-lbl">External certification body: BSI Group • Unconditional pass</div>
                </div>

                <div class="dash-stat-card">
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: var(--secondary);">SOC 2 Type II</span>
                    <span class="severity-pill severity-low">Clean Opinion</span>
                  </div>
                  <div class="dash-stat-val">0 Deficiencies</div>
                  <div class="dash-stat-lbl">Audited by Ernst & Young • Security, Availability, Confidentiality</div>
                </div>

                <div class="dash-stat-card">
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: var(--accent);">HIPAA Security</span>
                    <span class="severity-pill severity-low">100% Aligned</span>
                  </div>
                  <div class="dash-stat-val">ePHI Encrypted</div>
                  <div class="dash-stat-lbl">Continuous audit of patient record tokenization & access vaults</div>
                </div>

                <div class="dash-stat-card">
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: var(--warning);">EU GDPR Art 32</span>
                    <span class="severity-pill severity-low">98 / 100</span>
                  </div>
                  <div class="dash-stat-val">Compliant</div>
                  <div class="dash-stat-lbl">Data Protection Impact Assessment active across all multi-tenant nodes</div>
                </div>
              </div>
            </section>

            <!-- SECTION 6: THIRD-PARTY VENDOR & SUPPLY CHAIN RISK RATINGS -->
            <section class="dash-section" aria-label="Supply Chain Risk Ratings">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>🏢</span> Critical Third-Party Cloud & Supply Chain Security Ratings
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Real-time assessment of external digital vendors holding enterprise data touchpoints
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Request Vendor Audit</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table">
                    <thead>
                      <tr>
                        <th>Vendor & Service Tier</th>
                        <th>Classification</th>
                        <th>Security Rating</th>
                        <th>CVE Vulnerabilities</th>
                        <th>DPA / SOC 2 Status</th>
                        <th>Risk Decision</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Amazon Web Services (GovCloud & Commercial)</strong></td>
                        <td>Tier-1 Cloud Fabric</td>
                        <td><strong style="color: var(--accent);">98 / 100 (A+)</strong></td>
                        <td>0 Active Critical</td>
                        <td>SOC 2 Type II Current</td>
                        <td><span class="severity-pill severity-low">Approved</span></td>
                      </tr>
                      <tr>
                        <td><strong>Datadog Enterprise Observability</strong></td>
                        <td>Tier-1 APM & Logging</td>
                        <td><strong style="color: var(--primary);">95 / 100 (A)</strong></td>
                        <td>0 Active Critical</td>
                        <td>ISO 27001 Certified</td>
                        <td><span class="severity-pill severity-low">Approved</span></td>
                      </tr>
                      <tr>
                        <td><strong>Snowflake Enterprise Data Warehouse</strong></td>
                        <td>Tier-1 Analytical Store</td>
                        <td><strong style="color: var(--primary);">96 / 100 (A)</strong></td>
                        <td>0 Active Critical</td>
                        <td>FedRAMP Moderate</td>
                        <td><span class="severity-pill severity-low">Approved</span></td>
                      </tr>
                      <tr>
                        <td><strong>Salesforce CRM Platform</strong></td>
                        <td>Tier-2 Enterprise SaaS</td>
                        <td><strong style="color: var(--warning);">89 / 100 (B+)</strong></td>
                        <td>1 Low Disclosed</td>
                        <td>SOC 2 Type II Verified</td>
                        <td><span class="severity-pill severity-low">Monitored</span></td>
                      </tr>
                      <tr>
                        <td><strong>Okta Workforce Identity Cloud</strong></td>
                        <td>Tier-1 Identity Gateway</td>
                        <td><strong style="color: var(--accent);">99 / 100 (A+)</strong></td>
                        <td>0 Active Critical</td>
                        <td>FIPS 140-3 Hardware Compliant</td>
                        <td><span class="severity-pill severity-low">Approved</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 7: SOVEREIGN CYBER INSURANCE & LOSS WARRANTY ATTESTATION -->
            <section class="dash-section" aria-label="Cyber Insurance & Warranty">
              <div class="dash-grid-2">
                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>🔒</span> Lloyd's Syndicate Underwritten Warranty</h3>
                    <span class="severity-pill severity-low">Active Policy</span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
                    Full warranty certificate issued by Lloyd's of London syndicates backing Stackly autonomous defensive measures against breach financial impact.
                  </p>
                  <ul class="card-meta-list" style="margin-bottom: 1.25rem;">
                    <li class="card-meta-item"><span class="card-meta-icon">✓</span> <strong>$10,000,000</strong> Total Loss Recovery Indemnity</li>
                    <li class="card-meta-item"><span class="card-meta-icon">✓</span> <strong>Zero Ransomware Payout:</strong> 100% Forensic Recovery Guarantee</li>
                    <li class="card-meta-item"><span class="card-meta-icon">✓</span> <strong>Forensic Deductible:</strong> $0 on all contracted cloud workloads</li>
                  </ul>
                  <button type="button" class="btn btn-primary btn-sm dash-action-btn">Download Warranty Certificate</button>
                </div>

                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>📑</span> FAIR Quantitative Risk Exposure</h3>
                    <span class="badge-tag">Updated Oct 2026</span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
                    Factor Analysis of Information Risk (FAIR) loss event probability calculations for board governance committees.
                  </p>
                  <div class="dash-grid-2" style="margin-bottom: 1rem;">
                    <div class="dash-stat-card">
                      <div class="dash-stat-val" style="color: var(--accent);">$420k</div>
                      <div class="dash-stat-lbl">Probable Max Loss (PML)</div>
                    </div>
                    <div class="dash-stat-card">
                      <div class="dash-stat-val" style="color: var(--primary);">0.04%</div>
                      <div class="dash-stat-lbl">Annual Breach Probability</div>
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">View Full Loss Exceedance Curve</button>
                </div>
              </div>
            </section>

            <!-- SECTION 8: EMERGENCY CYBER CRISIS & BOARD ESCALATION PROTOCOL -->
            <section class="dash-section" aria-label="Crisis Escalation Protocol">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title"><span>🚨</span> Emergency Cyber Crisis & Board Escalation Protocol</h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Rapid command chain authorized to convene emergency board meetings within 60 minutes
                    </div>
                  </div>
                  <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Test War Room Bridge</button>
                </div>
                <div class="dash-grid-3">
                  <div class="dash-stat-card">
                    <strong style="color: var(--primary);">Incident Commander</strong>
                    <div style="font-size: 0.95rem; font-weight: 700; margin: 0.25rem 0;">Elena Rostova, CISO</div>
                    <div class="dash-stat-lbl">Direct Encrypted Satellite Phone • Priority 1 Clearance</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--secondary);">External Legal Counsel</strong>
                    <div style="font-size: 0.95rem; font-weight: 700; margin: 0.25rem 0;">Morrison & Foerster LLP</div>
                    <div class="dash-stat-lbl">Global Cyber Breach Practice • Attorney-Client Privilege Bridge</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--warning);">Board Notification SLA</strong>
                    <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">&lt; 2.0 Hours</div>
                    <div class="dash-stat-lbl">Mandatory SEC 4-day disclosure evaluation ready</div>
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 9: CISO EXECUTIVE SHORTCUT ENCLAVE -->
            <section class="dash-section" aria-label="Executive Shortcuts">
              <div class="dash-quick-actions">
                <strong style="color: var(--primary);">🛡️ CISO Executive Shortcuts:</strong>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>📑</span> Download Board Briefing</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>📜</span> Export ISO 27001 Evidence</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🏢</span> Vendor Risk Ratings</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🔒</span> Underwriter Warranty Attestation</button>
                <button type="button" class="btn btn-secondary btn-sm dash-action-btn"><span>🚨</span> Convene Emergency Security Committee</button>
              </div>
            </section>
          </div>
"""

soc_html = """
          <!-- ==================================================================
               ROLE 2: LEAD SOC OPERATIONS COMMANDER DASHBOARD
               Contains 8 distinct, comprehensive, non-repeating tactical sections
               ================================================================== -->
          <div id="view-role-soc" class="role-dashboard-container" style="display: none;">
            <!-- SECTION 1: SOC BATTLE STATION HEADER & DEFCON POSTURE -->
            <section class="dash-section" aria-label="SOC Tactical Command Station">
              <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.12) 0%, rgba(94, 234, 212, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2.5vw, 2rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
                <div>
                  <span class="badge-tag" style="margin-bottom: 0.5rem; background: rgba(56, 189, 248, 0.2); border-color: rgba(56, 189, 248, 0.4);">
                    <span class="badge-dot" style="background: #38bdf8;"></span> DEFCON 2 • 52,400 EPS Telemetry Stream Active
                  </span>
                  <h2 style="font-size: clamp(1.35rem, 2vw, 1.75rem); margin-bottom: 0.35rem; font-weight: 800; color: var(--text-primary);">
                    Tactical Cyber Operations & Incident Response Battle Station
                  </h2>
                  <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px; line-height: 1.5;">
                    Live telemetry ingestion across multi-cloud fabrics, automated SOAR playbooks, deep memory sandbox isolation, and continuous threat hunting.
                  </p>
                </div>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                  <button type="button" class="btn btn-primary btn-sm dash-action-btn">
                    <span>⚡</span> Trigger Sensor Sweep
                  </button>
                  <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                    <span>🛑</span> Deploy Network Quarantine
                  </button>
                </div>
              </div>
            </section>

            <!-- SECTION 2: TACTICAL OPERATIONS KPI METRICS -->
            <section class="dash-section" aria-label="Tactical Operations KPIs">
              <div class="dash-section-header">
                <div>
                  <h3 class="dash-section-title"><span>⚡</span> Real-Time Tactical Stream Telemetry</h3>
                  <div class="dash-section-subtitle">Real-time throughput metrics across global sensor clusters</div>
                </div>
                <span class="badge-tag">Zero Packet Loss</span>
              </div>
              <div class="dash-kpi-grid">
                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">SIEM Ingest Latency</span>
                    <span class="kpi-icon">⚡</span>
                  </div>
                  <div class="kpi-value" style="color: var(--primary);">110ms</div>
                  <div class="kpi-trend up">
                    <span>✓ 110ms</span> Cluster ingest latency
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Critical Incidents Contained</span>
                    <span class="kpi-icon">🛑</span>
                  </div>
                  <div class="kpi-value" style="color: var(--accent);">18 Contained</div>
                  <div class="kpi-trend up">
                    <span>✓ 100% SLA</span> 18 threats contained past 4h
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Mean Detection Time (MTTD)</span>
                    <span class="kpi-icon">⏱️</span>
                  </div>
                  <div class="kpi-value">2.1 Min</div>
                  <div class="kpi-trend up">
                    <span>✓ &lt;4.2 Min</span> Outpacing global benchmark
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">AI Threat False-Positive Ratio</span>
                    <span class="kpi-icon">🤖</span>
                  </div>
                  <div class="kpi-value">0.02%</div>
                  <div class="kpi-trend up">
                    <span>✓ Zero</span> False positive escalations
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 3: MITRE ATT&CK REAL-TIME ALERT INGESTION STREAM -->
            <section class="dash-section" aria-label="Live Alert Ingestion Stream">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>🚨</span> MITRE ATT&CK Real-Time Alert Ingestion Stream
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Automated threat correlation against MITRE ATT&CK Enterprise v14 matrix
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Stream Filters</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="SOC Threat Ingestion Table">
                    <thead>
                      <tr>
                        <th>TTP & Threat Identifier</th>
                        <th>Severity</th>
                        <th>Source Node</th>
                        <th>Target Workload</th>
                        <th>Autonomous Action Taken</th>
                        <th>Command Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>T1021.002 SMB/WMI Pivot</strong></td>
                        <td><span class="severity-pill severity-critical">Critical</span></td>
                        <td>10.0.14.88 (Unmanaged IoT)</td>
                        <td>Srv-Finance-DC01</td>
                        <td>Automated Subnet Isolation</td>
                        <td><button type="button" class="btn btn-primary btn-sm dash-action-btn">Inspect</button></td>
                      </tr>
                      <tr>
                        <td><strong>T1558.003 Kerberoasting SPN</strong></td>
                        <td><span class="severity-pill severity-high">High</span></td>
                        <td>10.0.2.140 (Compromised User)</td>
                        <td>Active Directory Service</td>
                        <td>Session & Kerberos Token Revoked</td>
                        <td><button type="button" class="btn btn-primary btn-sm dash-action-btn">Inspect</button></td>
                      </tr>
                      <tr>
                        <td><strong>T1078.004 Cloud API Key Abuse</strong></td>
                        <td><span class="severity-pill severity-high">High</span></td>
                        <td>194.26.29.112 (Tor Exit Node)</td>
                        <td>AWS S3 Production Enclave</td>
                        <td>IAM Role Auto-Detached</td>
                        <td><button type="button" class="btn btn-primary btn-sm dash-action-btn">Inspect</button></td>
                      </tr>
                      <tr>
                        <td><strong>T1059.001 PowerShell Encoded Run</strong></td>
                        <td><span class="severity-pill severity-medium">Medium</span></td>
                        <td>Host-Marketing-04</td>
                        <td>Local Process Registry</td>
                        <td>Process Killed & Memory Dumped</td>
                        <td><button type="button" class="btn btn-primary btn-sm dash-action-btn">Inspect</button></td>
                      </tr>
                      <tr>
                        <td><strong>T1110.003 Password Spraying</strong></td>
                        <td><span class="severity-pill severity-low">Low</span></td>
                        <td>Botnet Cluster (14 IPs)</td>
                        <td>SSO Gateway Portal</td>
                        <td>IP Subnet Drop on Cloudflare</td>
                        <td><button type="button" class="btn btn-primary btn-sm dash-action-btn">Inspect</button></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 4: ISOLATED QUARANTINE SANDBOX & DETONATION CHAMBER -->
            <section class="dash-section" aria-label="Quarantine Sandbox">
              <div class="dash-grid-2">
                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>🔬</span> Isolated Quarantine Sandbox & Detonation</h3>
                    <span class="severity-pill severity-critical">Live Inspection</span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
                    Suspicious payloads detonated inside isolated QEMU/KVM hypervisors with kernel-level memory hooking and unencrypted payload extraction.
                  </p>
                  <div class="dash-stat-card" style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between;">
                      <strong>Payload: Trojan.Win64.CobaltStrike.Stager</strong>
                      <span class="severity-pill severity-critical">Detonated</span>
                    </div>
                    <div style="font-family: var(--font-mono); font-size: 0.775rem; color: var(--text-muted); margin-top: 0.25rem;">
                      SHA-256: 8f2bc4a812e34d9a10c0e819b4221193aa47bf317498c142b918731adbf42319
                    </div>
                    <div style="font-size: 0.8rem; color: var(--accent); margin-top: 0.5rem;">
                      C2 Extraction: 185.220.101.5:443 (DNS Tunneling Payload Neutralized)
                    </div>
                  </div>
                  <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Purge Sandbox & Export YARA Signature</button>
                </div>

                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>🤖</span> SOAR Automated Playbook Execution Log</h3>
                    <span class="badge-tag">100% Autonomous</span>
                  </div>
                  <div class="timeline-feed">
                    <div class="timeline-event">
                      <div class="timeline-dot"></div>
                      <div class="timeline-time">10:14:02 UTC • Host-102</div>
                      <div class="timeline-title">Playbook #PB-01: Autonomous Ransomware Kill-Switch</div>
                      <div class="timeline-desc">Detected canary file modification. Isolated network adapter in 1.2s.</div>
                    </div>
                    <div class="timeline-event">
                      <div class="timeline-dot"></div>
                      <div class="timeline-time">10:11:45 UTC • Srv-SQL-01</div>
                      <div class="timeline-title">Playbook #PB-04: Credential Invalidation</div>
                      <div class="timeline-desc">Revoked active Kerberos TGT and forced hardware token re-auth.</div>
                    </div>
                    <div class="timeline-event">
                      <div class="timeline-dot"></div>
                      <div class="timeline-time">09:58:10 UTC • Edge Firewall</div>
                      <div class="timeline-title">Playbook #PB-09: Perimeter BGP Null-Route</div>
                      <div class="timeline-desc">Blacklisted malicious scanner CIDR across all 12 edge points of presence.</div>
                    </div>
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 5: PROACTIVE THREAT HUNTING & BEHAVIORAL PIPELINE -->
            <section class="dash-section" aria-label="Proactive Threat Hunting">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title"><span>🔎</span> Proactive Threat Hunting & Anomaly Investigations</h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Hypothesis-driven sweeps querying eBPF system calls, memory anomalies, and beaconing
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Launch Ad-Hoc Hunt</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table">
                    <thead>
                      <tr>
                        <th>Hunt ID & Hypothesis</th>
                        <th>Target Matrix</th>
                        <th>Ingested Records</th>
                        <th>Anomalies Verified</th>
                        <th>Lead Hunter</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>#HUNT-104: DNS Tunneling Detection</strong></td>
                        <td>Core DNS & Ingress Proxies</td>
                        <td>48,200,000 queries</td>
                        <td>1 Verified Host (Contained)</td>
                        <td>David Chen, GREM</td>
                        <td><span class="severity-pill severity-low">Resolved</span></td>
                      </tr>
                      <tr>
                        <td><strong>#HUNT-105: LSASS Unhooked Memory Reads</strong></td>
                        <td>All Windows Tier-0 Servers</td>
                        <td>1,240,000 events</td>
                        <td>0 Anomalies (Clean)</td>
                        <td>Marcus Vance, GCIA</td>
                        <td><span class="severity-pill severity-low">Completed</span></td>
                      </tr>
                      <tr>
                        <td><strong>#HUNT-106: Kubernetes Lateral Syscall Escapes</strong></td>
                        <td>GKE / EKS Container Pods</td>
                        <td>8,900,000 syscalls</td>
                        <td>0 Anomalies (100% Policy Pass)</td>
                        <td>Priya Sharma, GCFE</td>
                        <td><span class="severity-pill severity-low">In Progress</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 6: GLOBAL DISTRIBUTED SENSOR & HONEYPOT MESH -->
            <section class="dash-section" aria-label="Global Sensor Mesh">
              <div class="dash-section-header">
                <div>
                  <h3 class="dash-section-title"><span>🌐</span> Global Distributed Sensor Network & Decoy Honeypots</h3>
                  <div class="dash-section-subtitle">Real-time status of Stackly physical and virtual sensors deployed worldwide</div>
                </div>
                <span class="badge-tag">All Nodes Operational</span>
              </div>
              <div class="dash-grid-4">
                <div class="dash-stat-card">
                  <strong style="color: var(--primary);">🇩🇪 Frankfurt Core Node</strong>
                  <div class="dash-stat-val">18,400 EPS</div>
                  <div class="dash-stat-lbl">Cluster Latency: 18ms • 24 Decoy Probes Blocked</div>
                </div>

                <div class="dash-stat-card">
                  <strong style="color: var(--secondary);">🇸🇬 Singapore Edge Node</strong>
                  <div class="dash-stat-val">14,200 EPS</div>
                  <div class="dash-stat-lbl">Cluster Latency: 24ms • 12 Decoy Probes Blocked</div>
                </div>

                <div class="dash-stat-card">
                  <strong style="color: var(--accent);">🇮🇳 Salem Command Node</strong>
                  <div class="dash-stat-val">19,800 EPS</div>
                  <div class="dash-stat-lbl">Cluster Latency: 12ms • 8 Decoy Probes Blocked</div>
                </div>

                <div class="dash-stat-card">
                  <strong style="color: var(--warning);">🇺🇸 US-East Cloud Sensor</strong>
                  <div class="dash-stat-val">22,100 EPS</div>
                  <div class="dash-stat-lbl">Cluster Latency: 14ms • 31 Decoy Probes Blocked</div>
                </div>
              </div>
            </section>

            <!-- SECTION 7: SOC SHIFT HANDOVER & WATCH OFFICER ROSTER -->
            <section class="dash-section" aria-label="SOC Watch Officer Roster">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title"><span>👥</span> Tactical SOC Shift Handover & Watch Officer Roster</h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Certified GIAC/CREST security analysts maintaining active 24/7 eyes-on-glass monitoring
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Complete Shift Log</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table">
                    <thead>
                      <tr>
                        <th>Watch Officer & Role</th>
                        <th>Credentials</th>
                        <th>Active Workstation</th>
                        <th>Clearance Tier</th>
                        <th>Assigned Queues</th>
                        <th>Shift Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Marcus Vance (Watch Commander)</strong></td>
                        <td>CISSP, GCIA, GCIH</td>
                        <td>Command Battle Station 1</td>
                        <td>Top-Secret (SOC-L3)</td>
                        <td>P1 Critical Containment, SOAR Trigger</td>
                        <td><span class="severity-pill severity-low">On Duty (Deck)</span></td>
                      </tr>
                      <tr>
                        <td><strong>Priya Sharma (Forensic Lead)</strong></td>
                        <td>GCFE, EnCE</td>
                        <td>Forensics Station 4</td>
                        <td>Secret (SOC-L2)</td>
                        <td>Sandbox Detonation, Memory Dump Analysis</td>
                        <td><span class="severity-pill severity-low">On Duty (Deck)</span></td>
                      </tr>
                      <tr>
                        <td><strong>David Chen (Threat Hunter)</strong></td>
                        <td>GREM, OSCP</td>
                        <td>Intelligence Station 2</td>
                        <td>Secret (SOC-L2)</td>
                        <td>MITRE ATT&CK Matrix TTP Validation</td>
                        <td><span class="severity-pill severity-low">On Duty (Deck)</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 8: SOC COMMAND ACTION CONTROLS -->
            <section class="dash-section" aria-label="SOC Command Shortcuts">
              <div class="dash-quick-actions">
                <strong style="color: var(--primary);">⚡ SOC Command Shortcuts:</strong>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🔍</span> Deep Packet Inspection</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🚫</span> Global IP Blacklist</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🍯</span> Enforce Honeypot Decoys</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🤖</span> Edit SOAR Playbooks</button>
                <button type="button" class="btn btn-secondary btn-sm dash-action-btn"><span>🚨</span> Emergency Threat Lockdown</button>
              </div>
            </section>
          </div>
"""

client_html = """
          <!-- ==================================================================
               ROLE 3: ENTERPRISE CLIENT IT DIRECTOR DASHBOARD
               Contains 8 distinct, comprehensive, non-repeating client sections
               ================================================================== -->
          <div id="view-role-client" class="role-dashboard-container" style="display: none;">
            <!-- SECTION 1: CLIENT DEFENSE OPERATIONS HEADER -->
            <section class="dash-section" aria-label="Client Operations Command">
              <div style="background: linear-gradient(135deg, rgba(167, 139, 250, 0.12) 0%, rgba(94, 234, 212, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2.5vw, 2rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
                <div>
                  <span class="badge-tag" style="margin-bottom: 0.5rem; background: rgba(167, 139, 250, 0.2); border-color: rgba(167, 139, 250, 0.4);">
                    <span class="badge-dot" style="background: #a78bfa;"></span> Protected Organization: Apex Global Enterprises • Tier-1 Dedicated Pod
                  </span>
                  <h2 style="font-size: clamp(1.35rem, 2vw, 1.75rem); margin-bottom: 0.35rem; font-weight: 800; color: var(--text-primary);">
                    Enterprise Client Infrastructure Defense Operations
                  </h2>
                  <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px; line-height: 1.5;">
                    Live health telemetry of your protected cloud VPCs, hybrid clusters, vulnerability patch turnaround SLA, and direct access to your dedicated security team.
                  </p>
                </div>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                  <button type="button" class="btn btn-primary btn-sm dash-action-btn">
                    <span>📊</span> Download Monthly SLA Report
                  </button>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">
                    <span>💬</span> Contact Dedicated Analyst
                  </button>
                </div>
              </div>
            </section>

            <!-- SECTION 2: CLIENT INFRASTRUCTURE SLA & HEALTH KPIS -->
            <section class="dash-section" aria-label="Client Infrastructure Health KPIs">
              <div class="dash-section-header">
                <div>
                  <h3 class="dash-section-title"><span>🏢</span> Client Service Level Assurance (SLA) Scorecard</h3>
                  <div class="dash-section-subtitle">Real-time contractually guaranteed protection metrics</div>
                </div>
                <span class="badge-tag">SLA 100% Met</span>
              </div>
              <div class="dash-kpi-grid">
                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Protected Workloads</span>
                    <span class="kpi-icon">☁️</span>
                  </div>
                  <div class="kpi-value" style="color: var(--primary);">48 VPCs</div>
                  <div class="kpi-trend up">
                    <span>✓ 100%</span> 48 VPCs, 1,240 Pods, 680 Endpoints
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Continuous SLA Uptime</span>
                    <span class="kpi-icon">⚡</span>
                  </div>
                  <div class="kpi-value" style="color: var(--accent);">100.0%</div>
                  <div class="kpi-trend up">
                    <span>✓ 365 Days</span> Zero unscheduled downtime
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Vulnerability Patch Turnaround</span>
                    <span class="kpi-icon">🛡️</span>
                  </div>
                  <div class="kpi-value">&lt;4 Hours</div>
                  <div class="kpi-trend up">
                    <span>✓ &lt;4 Hours</span> Turnaround (0 overdue CVEs)
                  </div>
                </div>

                <div class="kpi-card js-tilt">
                  <div class="kpi-top">
                    <span class="kpi-label">Dedicated SOC Lead Assigned</span>
                    <span class="kpi-icon">🏢</span>
                  </div>
                  <div class="kpi-value">Tier 1 Pod</div>
                  <div class="kpi-trend up">
                    <span>✓ Tier 1</span> Dedicated SOC Pod Assigned
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 3: MONITORED MULTI-CLOUD WORKLOAD HEALTH INVENTORY -->
            <section class="dash-section" aria-label="Cloud Workload Health">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>🖥️</span> Monitored Cloud Workload Health & Asset Telemetry
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Real-time status of agentless cloud connectors and endpoint sensors across your enterprise
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Deploy Sensor</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="Client Asset Health Table">
                    <thead>
                      <tr>
                        <th>Workload Enclave / Cloud Provider</th>
                        <th>Protected Assets</th>
                        <th>Security Health</th>
                        <th>Last Security Sweep</th>
                        <th>Incident Status</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>AWS Production VPC (us-east-1)</strong></td>
                        <td>140 Microservices, 48 RDS DBs</td>
                        <td><span style="color: var(--accent);">✓ 100% Healthy</span></td>
                        <td>4 Mins Ago</td>
                        <td><span class="severity-pill severity-low">0 Active Threats</span></td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Manage</button></td>
                      </tr>
                      <tr>
                        <td><strong>Azure Active Directory / Entra ID</strong></td>
                        <td>1,240 Enterprise Identities</td>
                        <td><span style="color: var(--accent);">✓ 100% Healthy</span></td>
                        <td>Continuous Real-time</td>
                        <td><span class="severity-pill severity-low">Zero Compromises</span></td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Manage</button></td>
                      </tr>
                      <tr>
                        <td><strong>Frankfurt Hybrid Infrastructure</strong></td>
                        <td>16 Bare-Metal DB Hosts</td>
                        <td><span style="color: var(--accent);">✓ 99.8% Patched</span></td>
                        <td>12 Mins Ago</td>
                        <td><span class="severity-pill severity-low">0 Active Threats</span></td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Manage</button></td>
                      </tr>
                      <tr>
                        <td><strong>Google Cloud BigQuery Analytics</strong></td>
                        <td>42 Compute Clusters</td>
                        <td><span style="color: var(--accent);">✓ 100% Healthy</span></td>
                        <td>18 Mins Ago</td>
                        <td><span class="severity-pill severity-low">Zero Exfiltration</span></td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Manage</button></td>
                      </tr>
                      <tr>
                        <td><strong>Salem Corporate Branch Gateway</strong></td>
                        <td>240 Secured Workstations</td>
                        <td><span style="color: var(--accent);">✓ 0 Ingress Drops</span></td>
                        <td>2 Mins Ago</td>
                        <td><span class="severity-pill severity-low">ZTNA Active</span></td>
                        <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Manage</button></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 4: PRIORITY VULNERABILITY REMEDIATION TRACKER -->
            <section class="dash-section" aria-label="Vulnerability Remediation Tracker">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title">
                      <span>🛡️</span> Priority Vulnerability Remediation & Maintenance Schedule
                    </h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Pre-tested patches scheduled to avoid business disruptions during production hours
                    </div>
                  </div>
                  <span class="badge-tag">0 Overdue CVEs</span>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table">
                    <thead>
                      <tr>
                        <th>CVE Identifier & Description</th>
                        <th>CVSS Score</th>
                        <th>Impacted Environment</th>
                        <th>Scheduled Maintenance Window</th>
                        <th>Rollback Safeguards</th>
                        <th>Remediation Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>CVE-2026-4421 (Linux Kernel Mem Fix)</strong></td>
                        <td><span class="severity-pill severity-high">8.8 High</span></td>
                        <td>8 Kubernetes Worker Nodes</td>
                        <td>Sunday 02:00 UTC (Next Window)</td>
                        <td>Canary 10% Traffic Check</td>
                        <td><span class="severity-pill severity-low">Staged & Tested</span></td>
                      </tr>
                      <tr>
                        <td><strong>CVE-2026-1930 (OpenSSL Handshake Patch)</strong></td>
                        <td><span class="severity-pill severity-high">7.5 High</span></td>
                        <td>4 Edge NGINX Proxies</td>
                        <td>Wednesday 01:00 UTC</td>
                        <td>Zero-Downtime Hot Reload</td>
                        <td><span class="severity-pill severity-low">Approved</span></td>
                      </tr>
                      <tr>
                        <td><strong>CVE-2026-0814 (Spring Boot Framework)</strong></td>
                        <td><span class="severity-pill severity-medium">6.8 Medium</span></td>
                        <td>2 Internal Billing Microservices</td>
                        <td>Next Routine Sprint Rollout</td>
                        <td>Automated Container Re-spin</td>
                        <td><span class="severity-pill severity-low">In Validation</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <!-- SECTION 5: DEDICATED SECURITY ENGINEER HOTLINE & BRIDGE -->
            <section class="dash-section" aria-label="Dedicated Engineer Hotline">
              <div class="dash-grid-2">
                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>📞</span> Dedicated Security Engineer Hotline</h3>
                    <span class="severity-pill severity-low">Online Now</span>
                  </div>
                  <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1rem;">
                    Direct dedicated liaison assigned to Apex Global Enterprises with sub-15 minute response guarantee for all technical inquiries.
                  </p>
                  <div class="dash-stat-card" style="margin-bottom: 1rem;">
                    <div style="font-weight: 700; color: var(--primary);">Principal Defense Architect: David Chen, CISSP</div>
                    <div style="font-size: 0.825rem; color: var(--text-secondary); margin-top: 0.25rem;">
                      Direct Hotline: <strong>+91 9876543210</strong> (Ext 401) • PGP Fingerprint: 4E91 B572 C801
                    </div>
                  </div>
                  <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                    <button type="button" class="btn btn-primary btn-sm dash-action-btn"><span>📹</span> Launch Encrypted Bridge</button>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🎟️</span> Submit Support Ticket</button>
                  </div>
                </div>

                <div class="dash-panel">
                  <div class="dash-panel-header">
                    <h3 class="dash-panel-title"><span>📊</span> Monthly SLA Delivery Historical Trends</h3>
                    <span class="badge-tag">Past 6 Months</span>
                  </div>
                  <div class="dash-grid-2" style="margin-bottom: 1rem;">
                    <div class="dash-stat-card">
                      <div class="dash-stat-val" style="color: var(--accent);">3.1 Mins</div>
                      <div class="dash-stat-lbl">Average Detection (SLA: 15m)</div>
                    </div>
                    <div class="dash-stat-card">
                      <div class="dash-stat-val" style="color: var(--primary);">11.8 Mins</div>
                      <div class="dash-stat-lbl">Average Containment (SLA: 60m)</div>
                    </div>
                  </div>
                  <div style="font-size: 0.825rem; color: var(--text-secondary);">
                    Contractual SLA Compliance: <strong>100.0%</strong>. Zero penalty credits triggered.
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 6: CLOUD SECURITY POSTURE MANAGEMENT (CSPM) -->
            <section class="dash-section" aria-label="Cloud Security Posture">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title"><span>☁️</span> Cloud Security Posture (CSPM) & IAM Guardrails</h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Continuous configuration drift audit against AWS, Azure, and Google Cloud security baselines
                    </div>
                  </div>
                  <span class="badge-tag">Zero Configuration Drift</span>
                </div>
                <div class="dash-grid-3">
                  <div class="dash-stat-card">
                    <strong style="color: var(--primary);">S3 / Blob Storage Security</strong>
                    <div class="dash-stat-val" style="color: var(--accent); font-size: 1.25rem;">100% Blocked</div>
                    <div class="dash-stat-lbl">Zero publicly accessible storage buckets or objects</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--secondary);">IAM Access Key Age</strong>
                    <div class="dash-stat-val" style="color: var(--primary); font-size: 1.25rem;">&lt; 90 Days</div>
                    <div class="dash-stat-lbl">All API credentials auto-rotated within 90 days</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--warning);">Root Account MFA</strong>
                    <div class="dash-stat-val" style="color: var(--accent); font-size: 1.25rem;">Hardware Token</div>
                    <div class="dash-stat-lbl">FIPS 140-3 physical key enforced on all cloud root accounts</div>
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 7: EMPLOYEE SECURITY AWARENESS & PHISHING METRICS -->
            <section class="dash-section" aria-label="Security Awareness Metrics">
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <div>
                    <h3 class="dash-panel-title"><span>👥</span> Employee Security Awareness & Phishing Simulation Health</h3>
                    <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                      Human defense resilience metrics across your organization's 1,240 employees
                    </div>
                  </div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Schedule Simulation</button>
                </div>
                <div class="dash-grid-4">
                  <div class="dash-stat-card">
                    <strong style="color: var(--primary);">Phishing Click Rate</strong>
                    <div class="dash-stat-val" style="color: var(--accent);">1.2%</div>
                    <div class="dash-stat-lbl">Industry benchmark is 7.8% (Apex 85% more resilient)</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--secondary);">Report Rate</strong>
                    <div class="dash-stat-val" style="color: var(--primary);">84.2%</div>
                    <div class="dash-stat-lbl">Simulated attacks reported to SOC within 10 minutes</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--accent);">Training Completion</strong>
                    <div class="dash-stat-val">98.6%</div>
                    <div class="dash-stat-lbl">1,223 / 1,240 active corporate personnel certified</div>
                  </div>
                  <div class="dash-stat-card">
                    <strong style="color: var(--warning);">Remediation Coaching</strong>
                    <div class="dash-stat-val">14 Staff</div>
                    <div class="dash-stat-lbl">Completed targeted 1-on-1 awareness modules</div>
                  </div>
                </div>
              </div>
            </section>

            <!-- SECTION 8: CLIENT SERVICE OPERATIONS SHORTCUTS -->
            <section class="dash-section" aria-label="Client Operations Shortcuts">
              <div class="dash-quick-actions">
                <strong style="color: var(--primary);">🏢 Client Service Shortcuts:</strong>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>📊</span> Monthly SLA Review</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>🎯</span> Request Ad-Hoc PenTest</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>☁️</span> Manage Cloud VPC Sensors</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn"><span>📑</span> Vendor Security Questionnaire</button>
                <button type="button" class="btn btn-secondary btn-sm dash-action-btn"><span>🚨</span> Direct Incident Hotline (24/7)</button>
              </div>
            </section>
          </div>
"""

print("CISO, SOC, and Client HTML blocks defined successfully.")

