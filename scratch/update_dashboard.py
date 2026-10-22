import re

# ==============================================================================
# 1. UPDATE pages/dashboard.html
# ==============================================================================
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()

# Replace sidebar role selector with exactly the 3 designated roles
old_sidebar_rolebox = '''      <!-- Role Switcher in Sidebar (Enables live testing of all 4 roles) -->
      <div class="dash-sidebar-rolebox">
        <div class="role-switcher-label">Active Security View</div>
        <select id="dash-role-selector" class="role-select-box" aria-label="Switch Role Dashboard">
          <option value="Security Administrator">🛡️ Security Admin / CISO</option>
          <option value="SOC Analyst / Manager">⚡ SOC Analyst / Commander</option>
          <option value="Enterprise Client">🏢 Enterprise Client / CTO</option>
          <option value="Compliance Auditor">📜 Compliance Auditor</option>
        </select>
      </div>'''

new_sidebar_rolebox = '''      <!-- Role Switcher in Sidebar (Enables seamless testing of all 3 official roles) -->
      <div class="dash-sidebar-rolebox">
        <div class="role-switcher-label">Active Security View</div>
        <select id="dash-role-selector" class="role-select-box" aria-label="Switch Role Dashboard">
          <option value="Chief Information Security Officer (CISO)">🛡️ CISO Executive View</option>
          <option value="Lead SOC Operations Commander">⚡ SOC Commander View</option>
          <option value="Enterprise Client IT Director">🏢 Enterprise Client View</option>
        </select>
      </div>'''

dash_norm = dash_html.replace('\r\n', '\n')
old_sb_norm = old_sidebar_rolebox.replace('\r\n', '\n')
if old_sb_norm in dash_norm:
    dash_html = dash_norm.replace(old_sb_norm, new_sidebar_rolebox)
    print("Updated sidebar role selector in dashboard.html")
else:
    print("Warning: could not find old_sidebar_rolebox in dashboard.html")

# Replace Module 1 Overview with the 3 comprehensive role-specific dashboards
overview_start = dash_html.find('<!-- MODULE 1: OPERATIONS OVERVIEW (Default Active) -->')
overview_end = dash_html.find('<!-- MODULE 2: THREAT FEEDS & SIEM -->')

new_module_overview = '''<!-- MODULE 1: OPERATIONS OVERVIEW (Role Adaptive Hub) -->
        <div class="dash-module-section active" id="module-overview">

          <!-- ==================================================================
               ROLE 1: CHIEF INFORMATION SECURITY OFFICER (CISO) DASHBOARD
               Focus: Executive governance, risk heatmap, budget ROI, compliance vault
               ================================================================== -->
          <div id="view-role-ciso" class="role-dashboard-container">
            <!-- 1. CISO Executive Banner -->
            <div style="background: linear-gradient(135deg, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: 1.5rem 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.5rem;">
                  <span class="badge-dot"></span> Executive CISO Enclave • Top-Secret Clearance
                </span>
                <h2 style="font-size: 1.6rem; margin-bottom: 0.35rem; font-weight: 800;">Enterprise Cyber Risk & Governance Oversight</h2>
                <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px;">
                  Real-time strategic oversight of global enterprise resilience, board-level threat indicators, cyber liability warranty, and continuous regulatory audit attestation.
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

            <!-- 2. CISO 4-Column Executive KPI Cards -->
            <div class="dash-kpi-grid" style="margin-top: 1.75rem;">
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
                <div class="kpi-value">100% Pass</div>
                <div class="kpi-trend up">
                  <span>✓ ISO 27001</span> SOC 2 Type II, HIPAA, GDPR
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Cyber Liability Warranty</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value">$10,000,000</div>
                <div class="kpi-trend up">
                  <span>✓ Underwritten</span> Active with Lloyd's syndicate
                </div>
              </div>
            </div>

            <!-- 3. CISO Split Data: Enterprise Risk Heatmap & Policy Approvals -->
            <div class="dash-split-grid" style="margin-top: 1.75rem;">
              <!-- Left: Strategic Risk Heatmap -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>📊</span> Enterprise Cyber Risk Heatmap (Q4 2026)
                  </h3>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export Risk Matrix</button>
                </div>
                <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
                  Aggregated vulnerability attack surface score calculated across 48 Multi-Cloud VPCs and SaaS dependencies.
                </p>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="CISO Risk Heatmap Table">
                    <thead>
                      <tr>
                        <th>Threat Category</th>
                        <th>Risk Exposure</th>
                        <th>Active Mitigation</th>
                        <th>Trend</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Cloud Misconfiguration</strong></td>
                        <td><span class="severity-pill severity-low">Low (12/100)</span></td>
                        <td>Automated Terraform drift detection active</td>
                        <td><span style="color: var(--accent);">↓ -18%</span></td>
                      </tr>
                      <tr>
                        <td><strong>Ransomware & Lateral Movement</strong></td>
                        <td><span class="severity-pill severity-low">Minimal (8/100)</span></td>
                        <td>Zero-Trust microsegmentation enforced</td>
                        <td><span style="color: var(--accent);">↓ -24%</span></td>
                      </tr>
                      <tr>
                        <td><strong>Phishing & Social Engineering</strong></td>
                        <td><span class="severity-pill severity-medium">Controlled (28/100)</span></td>
                        <td>FIDO2 hardware MFA required for all staff</td>
                        <td><span style="color: var(--accent);">↓ -12%</span></td>
                      </tr>
                      <tr>
                        <td><strong>Third-Party Supply Chain</strong></td>
                        <td><span class="severity-pill severity-medium">Moderate (36/100)</span></td>
                        <td>42 SaaS vendors audited under ISO 27001</td>
                        <td><span style="color: #fbbf24;">→ Stable</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Right: Executive Authorization & Approvals -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>✍️</span> CISO Executive Approvals Queue
                  </h3>
                  <span class="badge-tag" style="margin: 0; font-size: 0.725rem; padding: 0.2rem 0.6rem;">3 Pending</span>
                </div>
                <div class="timeline-feed">
                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></span>
                    <span class="timeline-time">Urgent</span>
                    <div class="timeline-title">Emergency Quarantine Ratification</div>
                    <div class="timeline-desc">Automated isolation of Host K8s-Prod-Worker-09 flagged for memory tampering.</div>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem; font-size: 0.75rem; padding: 0.25rem 0.6rem;">
                      Cryptographic Sign & Approve
                    </button>
                  </div>

                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: var(--primary); box-shadow: 0 0 8px var(--primary);"></span>
                    <span class="timeline-time">Today</span>
                    <div class="timeline-title">Zero-Trust IAM Policy Exception</div>
                    <div class="timeline-desc">Vendor CloudScale-API requesting temporary mTLS ingress for database migration.</div>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem; font-size: 0.75rem; padding: 0.25rem 0.6rem;">
                      Review Scope & Authorize
                    </button>
                  </div>

                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: var(--accent); box-shadow: 0 0 8px var(--accent);"></span>
                    <span class="timeline-time">Pending</span>
                    <div class="timeline-title">Q4 SOC Sensor Telemetry Expansion</div>
                    <div class="timeline-desc">Proposal to ingest 25,000 additional EPS from newly acquired European entity.</div>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem; font-size: 0.75rem; padding: 0.25rem 0.6rem;">
                      Approve Budget Allocation
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 4. CISO Quick Shortcuts -->
            <div class="dash-quick-actions" style="margin-top: 2rem;">
              <strong style="color: var(--text-primary); font-size: 0.95rem; margin-right: 0.5rem;">
                🛡️ CISO Executive Shortcuts:
              </strong>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>📑</span> Download Board Briefing
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>📜</span> Export ISO 27001 Evidence
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🏢</span> Vendor Risk Ratings
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🔒</span> Underwriter Warranty Attestation
              </button>
              <button type="button" class="btn btn-primary btn-sm dash-action-btn" style="margin-left: auto;">
                <span>🚨</span> Convene Emergency Security Committee
              </button>
            </div>
          </div>


          <!-- ==================================================================
               ROLE 2: LEAD SOC OPERATIONS COMMANDER DASHBOARD
               Focus: 52k EPS telemetry, MITRE ATT&CK queue, live quarantine sandbox
               ================================================================== -->
          <div id="view-role-soc" class="role-dashboard-container" style="display: none;">
            <!-- 1. SOC Tactical Banner -->
            <div style="background: linear-gradient(135deg, rgba(244, 63, 94, 0.12) 0%, rgba(56, 189, 248, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: 1.5rem 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.5rem;">
                  <span class="badge-dot"></span> Live SOC Command Center • Shift Alpha
                </span>
                <h2 style="font-size: 1.6rem; margin-bottom: 0.35rem; font-weight: 800;">Real-Time SIEM Telemetry & Threat Containment</h2>
                <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px;">
                  Correlating 52,480 EPS across multi-cloud sensor fabrics with autonomous SOAR containment playbooks executing in under 4.2 minutes.
                </p>
              </div>
              <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">
                  <span>⚡</span> Trigger Sensor Sweep
                </button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">
                  <span>🛑</span> Deploy Network Quarantine
                </button>
              </div>
            </div>

            <!-- 2. SOC 4-Column Tactical KPI Cards -->
            <div class="dash-kpi-grid" style="margin-top: 1.75rem;">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Live SIEM Ingestion Throughput</span>
                  <span class="kpi-icon">⚡</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">52,480 EPS</div>
                <div class="kpi-trend up">
                  <span>✓ 110ms</span> Cluster ingest latency
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Active Alarm Queue</span>
                  <span class="kpi-icon">🛑</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">0 In Queue</div>
                <div class="kpi-trend down" style="color: var(--accent);">
                  <span>✓ 100% SLA</span> 18 threats contained past 4h
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Mean Detection / Containment</span>
                  <span class="kpi-icon">⏱️</span>
                </div>
                <div class="kpi-value">38s / 4.2m</div>
                <div class="kpi-trend up">
                  <span>↑ 40%</span> Faster than contractual SLA
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">SOAR Playbook Precision</span>
                  <span class="kpi-icon">🤖</span>
                </div>
                <div class="kpi-value">99.4%</div>
                <div class="kpi-trend up">
                  <span>✓ Zero</span> False positive escalations
                </div>
              </div>
            </div>

            <!-- 3. SOC Split Data: MITRE ATT&CK Queue & Quarantine Sandbox -->
            <div class="dash-split-grid" style="margin-top: 1.75rem;">
              <!-- Left: Live Threat Ingestion & Containment -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>🚨</span> MITRE ATT&CK Real-Time Alert Stream
                  </h3>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Filter Feed</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="SOC Threat Ingestion Table">
                    <thead>
                      <tr>
                        <th>Severity</th>
                        <th>Technique / Vector</th>
                        <th>Target System</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><span class="severity-pill severity-critical">Critical</span></td>
                        <td>T1059.001 - In-Memory PowerShell Injection</td>
                        <td>DC-WIN-04 (10.0.4.12)</td>
                        <td>
                          <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">
                            Isolate Host
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td><span class="severity-pill severity-high">High</span></td>
                        <td>T1078.004 - Cloud IAM Role Hijacking Probe</td>
                        <td>AWS IAM Lambda AssumeRole</td>
                        <td>
                          <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">
                            Revoke Token
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td><span class="severity-pill severity-medium">Medium</span></td>
                        <td>T1190 - Exploit Public-Facing Application</td>
                        <td>Edge NGINX Gateway</td>
                        <td>
                          <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">
                            Drop IP Block
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td><span class="severity-pill severity-low">Low</span></td>
                        <td>T1566.002 - Spearphishing Attachment Detonated</td>
                        <td>finance@stackly.security</td>
                        <td>
                          <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">
                            Purge Mailbox
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Right: Interactive Quarantine Sandbox -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>🔬</span> Isolated Quarantine Sandbox
                  </h3>
                  <span class="severity-pill severity-low">Sandbox Active</span>
                </div>
                <div style="background: #060a14; padding: 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin-bottom: 1rem;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Sample Hash (SHA-256):</span>
                    <span style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--primary);">7f9b...a10e</span>
                  </div>
                  <div style="font-size: 0.85rem; color: var(--text-primary); font-weight: 600;">Trojan.Dropper.AgentV4 (Detonated)</div>
                  <div style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 0.35rem;">
                    Attempted outbound C2 beacon to 194.26.29.112:8443. Traffic blocked by firewall zero-trust egress filter.
                  </div>
                </div>
                <div class="timeline-feed">
                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: var(--accent);"></span>
                    <span class="timeline-time">11:15 AM</span>
                    <div class="timeline-title">Memory Forensics Dump Generated</div>
                    <div class="timeline-desc">Complete volatile memory capture stored for forensic chain of custody.</div>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.35rem; font-size: 0.75rem; padding: 0.2rem 0.5rem;">
                      Export PCAP & Artifacts
                    </button>
                  </div>
                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: var(--primary);"></span>
                    <span class="timeline-time">10:48 AM</span>
                    <div class="timeline-title">Shift Alpha Handover Log Updated</div>
                    <div class="timeline-desc">All MITRE ATT&CK queues resolved with zero outstanding triage tickets.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 4. SOC Quick Shortcuts -->
            <div class="dash-quick-actions" style="margin-top: 2rem;">
              <strong style="color: var(--text-primary); font-size: 0.95rem; margin-right: 0.5rem;">
                ⚡ SOC Command Shortcuts:
              </strong>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🔍</span> Deep Packet Inspection
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🚫</span> Global IP Blacklist
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🔒</span> Enforce Honeypot Decoys
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🤖</span> Edit SOAR Playbooks
              </button>
              <button type="button" class="btn btn-primary btn-sm dash-action-btn" style="margin-left: auto;">
                <span>🚨</span> Emergency Threat Lockdown
              </button>
            </div>
          </div>


          <!-- ==================================================================
               ROLE 3: ENTERPRISE CLIENT IT DIRECTOR DASHBOARD
               Focus: Monitored infrastructure assets, patch queue, SLA uptime, analyst hotline
               ================================================================== -->
          <div id="view-role-client" class="role-dashboard-container" style="display: none;">
            <!-- 1. Enterprise Client Banner -->
            <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.12) 0%, rgba(16, 185, 129, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: 1.5rem 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.25rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.5rem;">
                  <span class="badge-dot"></span> Enterprise Client IT Enclave • Protected Status
                </span>
                <h2 style="font-size: 1.6rem; margin-bottom: 0.35rem; font-weight: 800;">Enterprise Protected Assets & SLA Command Hub</h2>
                <p style="font-size: 0.925rem; color: var(--text-secondary); margin: 0; max-width: 720px;">
                  Comprehensive health overview of your enrolled cloud infrastructure, real-time vulnerability patch status, and 24/7 dedicated engineering pod hotline.
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

            <!-- 2. Client 4-Column Infrastructure & SLA KPI Cards -->
            <div class="dash-kpi-grid" style="margin-top: 1.75rem;">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Monitored Enterprise Assets</span>
                  <span class="kpi-icon">☁️</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">1,968</div>
                <div class="kpi-trend up">
                  <span>✓ 100%</span> 48 VPCs, 1,240 Pods, 680 Endpoints
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Contractual SLA Uptime</span>
                  <span class="kpi-icon">⚡</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">99.998%</div>
                <div class="kpi-trend up">
                  <span>✓ 365 Days</span> Zero unscheduled downtime
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Critical Vulnerability SLA</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value">100% Patched</div>
                <div class="kpi-trend up">
                  <span>✓ &lt;4 Hours</span> Turnaround (0 overdue CVEs)
                </div>
              </div>

              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Active Defense Subscription</span>
                  <span class="kpi-icon">🏢</span>
                </div>
                <div class="kpi-value" style="font-size: 1.4rem;">Sovereign SOC</div>
                <div class="kpi-trend up">
                  <span>✓ Tier 1</span> Dedicated SOC Pod Assigned
                </div>
              </div>
            </div>

            <!-- 3. Client Split Data: Monitored Cloud Assets & Patching Queue -->
            <div class="dash-split-grid" style="margin-top: 1.75rem;">
              <!-- Left: Enrolled Infrastructure Health -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>🖥️</span> Monitored Cloud Workload Health
                  </h3>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn">Enroll New Node</button>
                </div>
                <div class="data-table-wrap">
                  <table class="dash-table" aria-label="Client Asset Health Table">
                    <thead>
                      <tr>
                        <th>Cloud Environment</th>
                        <th>Workload Cluster</th>
                        <th>SOC Sensor Status</th>
                        <th>Health Posture</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>AWS Production (us-east-1)</strong></td>
                        <td>48 VPCs • 184 RDS Instances</td>
                        <td><span class="severity-pill severity-low">Active (CrowdStrike)</span></td>
                        <td><span style="color: var(--accent);">✓ 100% Healthy</span></td>
                      </tr>
                      <tr>
                        <td><strong>Kubernetes Microservices</strong></td>
                        <td>1,240 Pods • EKS Cluster</td>
                        <td><span class="severity-pill severity-low">Active (Falco Runtime)</span></td>
                        <td><span style="color: var(--accent);">✓ 100% Healthy</span></td>
                      </tr>
                      <tr>
                        <td><strong>Corporate Endpoints</strong></td>
                        <td>680 Workstations & Laptops</td>
                        <td><span class="severity-pill severity-low">Active (EDR Agent)</span></td>
                        <td><span style="color: var(--accent);">✓ 99.8% Patched</span></td>
                      </tr>
                      <tr>
                        <td><strong>Edge API Gateways</strong></td>
                        <td>Cloudflare Enterprise WAF</td>
                        <td><span class="severity-pill severity-low">Active (DDoS Shield)</span></td>
                        <td><span style="color: var(--accent);">✓ 0 Ingress Drops</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Right: Dedicated Security Engineering Support Hotline -->
              <div class="dash-panel">
                <div class="dash-panel-header">
                  <h3 class="dash-panel-title">
                    <span>📞</span> Dedicated Security Engineer Hotline
                  </h3>
                  <span class="badge-tag" style="margin: 0; font-size: 0.725rem; padding: 0.2rem 0.6rem;">Online Now</span>
                </div>
                <div style="background: #060a14; padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin-bottom: 1.25rem;">
                  <div style="display: flex; align-items: center; gap: 0.85rem; margin-bottom: 0.75rem;">
                    <div style="width: 44px; height: 44px; border-radius: var(--radius-full); background: linear-gradient(135deg, var(--primary), var(--accent)); display: flex; align-items: center; justify-content: center; font-weight: 800; color: #030508;">
                      AM
                    </div>
                    <div>
                      <div style="font-weight: 700; color: var(--text-primary); font-size: 0.95rem;">Alex Morgan (Lead Architect)</div>
                      <div style="font-size: 0.8rem; color: var(--text-secondary);">Dedicated Enterprise Defense Pod Lead</div>
                    </div>
                  </div>
                  <p style="font-size: 0.825rem; color: var(--text-secondary); margin-bottom: 1rem;">
                    Direct encrypted bridge available 24/7/365. Contractual emergency response turnaround within 15 minutes.
                  </p>
                  <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <button type="button" class="btn btn-primary btn-sm dash-action-btn">
                      <span>📹</span> Launch Encrypted Bridge
                    </button>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn">
                      <span>🎟️</span> Submit Support Ticket
                    </button>
                  </div>
                </div>

                <div class="timeline-feed">
                  <div class="timeline-event">
                    <span class="timeline-dot" style="background: var(--accent);"></span>
                    <span class="timeline-time">Yesterday</span>
                    <div class="timeline-title">Q3 Penetration Test Attestation Available</div>
                    <div class="timeline-desc">Clean bill of health issued with zero high-severity findings open.</div>
                    <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.35rem; font-size: 0.75rem; padding: 0.2rem 0.5rem;">
                      Download Attestation Letter (PDF)
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 4. Client Quick Shortcuts -->
            <div class="dash-quick-actions" style="margin-top: 2rem;">
              <strong style="color: var(--text-primary); font-size: 0.95rem; margin-right: 0.5rem;">
                🏢 Client Service Shortcuts:
              </strong>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>📊</span> Monthly SLA Review
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>🛡️</span> Request Ad-Hoc PenTest
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>☁️</span> Manage Cloud VPC Sensors
              </button>
              <button type="button" class="btn btn-secondary btn-sm dash-action-btn">
                <span>📑</span> Vendor Security Questionnaire
              </button>
              <button type="button" class="btn btn-primary btn-sm dash-action-btn" style="margin-left: auto;">
                <span>🚨</span> Direct Incident Hotline (24/7)
              </button>
            </div>
          </div>

        </div>

        '''

if overview_start != -1 and overview_end != -1:
    dash_html = dash_html[:overview_start] + new_module_overview + dash_html[overview_end:]
    print("Module Overview replaced with 3 distinct role dashboards!")
else:
    print("Failed to find module boundaries:", overview_start, overview_end)

# In module-users (Authorized Operators table): update to only the 3 designated roles
old_operators_tbody = '''                  <tr>
                    <td><strong>Alex Morgan</strong></td>
                    <td>admin@stackly.security</td>
                    <td>Security Administrator</td>
                    <td><span class="severity-pill severity-low">Hardware FIDO2</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit</button></td>
                  </tr>
                  <tr>
                    <td><strong>Elena Rostova</strong></td>
                    <td>soc@stackly.security</td>
                    <td>SOC Analyst / Manager</td>
                    <td><span class="severity-pill severity-low">Hardware FIDO2</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit</button></td>
                  </tr>
                  <tr>
                    <td><strong>Marcus Vance</strong></td>
                    <td>client@enterprise.com</td>
                    <td>Enterprise Client</td>
                    <td><span class="severity-pill severity-low">TOTP Authenticator</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit</button></td>
                  </tr>
                  <tr>
                    <td><strong>Sarah Chen</strong></td>
                    <td>auditor@compliance.org</td>
                    <td>Compliance Auditor</td>
                    <td><span class="severity-pill severity-low">TOTP Authenticator</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit</button></td>
                  </tr>'''

new_operators_tbody = '''                  <tr>
                    <td><strong>Elena Rostova</strong></td>
                    <td>ciso@stackly.security</td>
                    <td>Chief Information Security Officer (CISO)</td>
                    <td><span class="severity-pill severity-low">Hardware FIDO2</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit Clearance</button></td>
                  </tr>
                  <tr>
                    <td><strong>Alex Vance</strong></td>
                    <td>soc@stackly.security</td>
                    <td>Lead SOC Operations Commander</td>
                    <td><span class="severity-pill severity-low">Hardware FIDO2</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit Clearance</button></td>
                  </tr>
                  <tr>
                    <td><strong>Sarah Jenkins</strong></td>
                    <td>client@enterprise.com</td>
                    <td>Enterprise Client IT Director</td>
                    <td><span class="severity-pill severity-low">TOTP Authenticator</span></td>
                    <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit Clearance</button></td>
                  </tr>'''

dash_norm = dash_html.replace('\r\n', '\n')
old_op_norm = old_operators_tbody.replace('\r\n', '\n')
if old_op_norm in dash_norm:
    dash_html = dash_norm.replace(old_op_norm, new_operators_tbody)
    print("Updated authorized operators table to 3 roles!")
else:
    print("Warning: could not find old_operators_tbody in dashboard.html")

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_html)
print("pages/dashboard.html updated successfully!")


# ==============================================================================
# 2. UPDATE assets/js/dashboard.js
# ==============================================================================
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    dash_js = f.read()

# Role definitions mapping
dash_js_code = '''/**
 * STACKLY CYBER SECURITY SERVICES - DASHBOARD CONTROLLER
 * Session Authorization, 3 Dedicated Role Dashboards, Dynamic Time Greeting,
 * Sidebar Collapse & Mobile Full-Screen Drawer, and 404 Action Button Handlers.
 */

const ROLE_PROFILES = {
  'Chief Information Security Officer (CISO)': {
    name: 'Elena Rostova',
    title: 'Chief Information Security Officer (CISO)',
    avatar: 'E',
    viewId: 'view-role-ciso',
    status: 'Governance Enclave Active'
  },
  'Lead SOC Operations Commander': {
    name: 'Alex Vance',
    title: 'Lead SOC Operations Commander',
    avatar: 'A',
    viewId: 'view-role-soc',
    status: 'Live 52k EPS Feed Active'
  },
  'Enterprise Client IT Director': {
    name: 'Sarah Jenkins',
    title: 'Enterprise Client IT Director',
    avatar: 'S',
    viewId: 'view-role-client',
    status: 'Protected Infrastructure Online'
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // 1. Session Guard Check
  const currentUser = checkAuthSession();
  if (!currentUser) return;

  // Normalize role to one of the 3 supported roles
  normalizeUserRole(currentUser);

  // 2. Render User Details & Dynamic Greeting
  renderUserTopBar(currentUser);
  initSidebarControls();
  initRoleSwitcher(currentUser);
  initDashboardModules(currentUser.role);
  initDashboardActionButtons();
});

/* Normalize any legacy role into the 3 official roles */
function normalizeUserRole(user) {
  const currentRole = user.role || '';
  if (currentRole.includes('SOC') || currentRole.includes('Analyst') || currentRole.includes('Commander')) {
    user.role = 'Lead SOC Operations Commander';
  } else if (currentRole.includes('Client') || currentRole.includes('Enterprise') || currentRole.includes('Director')) {
    user.role = 'Enterprise Client IT Director';
  } else {
    user.role = 'Chief Information Security Officer (CISO)';
  }
}

/* Session Authentication Guard */
function checkAuthSession() {
  try {
    const sessionStr = localStorage.getItem('stackly_cyber_currentUser');
    if (!sessionStr) {
      // Default to CISO session if visited directly
      const defaultUser = {
        isLoggedIn: true,
        name: 'Elena Rostova',
        role: 'Chief Information Security Officer (CISO)',
        email: 'ciso@stackly.security'
      };
      localStorage.setItem('stackly_cyber_currentUser', JSON.stringify(defaultUser));
      localStorage.setItem('stackly_cyber_role', defaultUser.role);
      return defaultUser;
    }
    const user = JSON.parse(sessionStr);
    if (!user || !user.isLoggedIn) {
      window.location.href = 'sign-in.html';
      return null;
    }
    return user;
  } catch (e) {
    window.location.href = 'sign-in.html';
    return null;
  }
}

/* Render User Details & Time-Aware Greeting */
function renderUserTopBar(user) {
  const greetingEl = document.getElementById('dash-user-greeting');
  const nameEl = document.getElementById('dash-user-name');
  const roleEl = document.getElementById('dash-user-role');
  const avatarEl = document.getElementById('dash-user-avatar');
  const timestampEl = document.getElementById('dash-user-timestamp');

  const profile = ROLE_PROFILES[user.role] || ROLE_PROFILES['Chief Information Security Officer (CISO)'];

  // Dynamic greeting based on current local hour
  const hour = new Date().getHours();
  let timeGreeting = 'Good day';
  if (hour >= 5 && hour < 12) {
    timeGreeting = 'Good morning';
  } else if (hour >= 12 && hour < 17) {
    timeGreeting = 'Good afternoon';
  } else if (hour >= 17 && hour < 22) {
    timeGreeting = 'Good evening';
  } else {
    timeGreeting = 'Good night';
  }

  if (greetingEl) {
    greetingEl.innerHTML = `${timeGreeting}, <strong>${profile.name}</strong> <span class="dash-status-badge"><span class="badge-dot"></span> ${profile.status}</span>`;
  }
  if (nameEl) {
    nameEl.textContent = profile.name;
  }
  if (roleEl) {
    roleEl.textContent = profile.title;
  }
  if (avatarEl) {
    avatarEl.textContent = profile.avatar;
  }
  if (timestampEl) {
    const loginTime = user.lastLoginTime || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    timestampEl.textContent = `Zero-Trust Clearance Active • Last Authenticated: Today at ${loginTime}`;
  }

  // Sign out button
  const signoutBtn = document.getElementById('dash-signout-btn');
  if (signoutBtn) {
    signoutBtn.onclick = (e) => {
      e.preventDefault();
      localStorage.removeItem('stackly_cyber_currentUser');
      localStorage.removeItem('stackly_cyber_role');
      window.location.href = 'sign-in.html';
    };
  }
}

/* Sidebar Toggle & Mobile Full-Screen Drawer */
function initSidebarControls() {
  const sidebar = document.getElementById('dash-sidebar');
  const collapseBtn = document.getElementById('sidebar-collapse-btn');
  const mobileToggle = document.getElementById('mobile-dash-toggle');
  const mobileCloseBtn = document.getElementById('mobile-sidebar-close-btn');

  if (collapseBtn && sidebar) {
    collapseBtn.onclick = () => {
      sidebar.classList.toggle('collapsed');
      const isCollapsed = sidebar.classList.contains('collapsed');
      collapseBtn.setAttribute('aria-expanded', !isCollapsed);
    };
  }

  if (mobileToggle && sidebar) {
    mobileToggle.onclick = () => {
      const isOpen = sidebar.classList.toggle('mobile-open');
      document.body.classList.toggle('drawer-open', isOpen);
    };
  }

  if (mobileCloseBtn && sidebar) {
    mobileCloseBtn.onclick = () => {
      sidebar.classList.remove('mobile-open');
      document.body.classList.remove('drawer-open');
    };
  }
}

/* Role Selector to dynamically adapt dashboard view */
function initRoleSwitcher(currentUser) {
  const roleSelect = document.getElementById('dash-role-selector');
  if (!roleSelect) return;

  roleSelect.value = currentUser.role || 'Chief Information Security Officer (CISO)';

  roleSelect.onchange = () => {
    const newRole = roleSelect.value;
    currentUser.role = newRole;
    localStorage.setItem('stackly_cyber_currentUser', JSON.stringify(currentUser));
    localStorage.setItem('stackly_cyber_role', newRole);
    renderUserTopBar(currentUser);
    initDashboardModules(newRole);
  };
}

/* Show Role-Specific Dedicated Dashboard & Sidebar Tab Switching */
function initDashboardModules(role) {
  const currentRole = role || 'Chief Information Security Officer (CISO)';
  
  // 1. Show only the active role's dashboard container
  const cisoView = document.getElementById('view-role-ciso');
  const socView = document.getElementById('view-role-soc');
  const clientView = document.getElementById('view-role-client');

  if (cisoView) cisoView.style.display = 'none';
  if (socView) socView.style.display = 'none';
  if (clientView) clientView.style.display = 'none';

  if (currentRole.includes('SOC') || currentRole.includes('Commander')) {
    if (socView) socView.style.display = 'block';
  } else if (currentRole.includes('Client') || currentRole.includes('Director')) {
    if (clientView) clientView.style.display = 'block';
  } else {
    if (cisoView) cisoView.style.display = 'block';
  }

  // 2. Sidebar tab switching
  const navItems = document.querySelectorAll('.dash-nav-item');
  navItems.forEach(item => {
    item.onclick = () => {
      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');

      const targetSectionId = item.getAttribute('data-target-module');
      if (targetSectionId) {
        document.querySelectorAll('.dash-module-section').forEach(sec => {
          sec.classList.remove('active');
        });
        const targetSec = document.getElementById(targetSectionId);
        if (targetSec) targetSec.classList.add('active');
      }

      // Close mobile sidebar if open
      const sidebar = document.getElementById('dash-sidebar');
      if (sidebar && sidebar.classList.contains('mobile-open')) {
        sidebar.classList.remove('mobile-open');
        document.body.classList.remove('drawer-open');
      }
    };
  });
}

/* Ensure all action buttons inside dashboard redirect to 404 page */
function initDashboardActionButtons() {
  const actionButtons = document.querySelectorAll('.dash-action-btn, [data-action="404"]');
  actionButtons.forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      window.location.href = '404.html';
    };
  });
}
'''

with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
    f.write(dash_js_code)
print("assets/js/dashboard.js updated successfully!")

