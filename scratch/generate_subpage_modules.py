# -*- coding: utf-8 -*-
"""
Defines HTML for Modules 2 through 8, each containing 8 distinct, comprehensive, non-repeating sections.
"""

threats_html = """
        <!-- MODULE 2: THREAT FEEDS & SIEM (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-threats">
          <!-- SECTION 1: HEADER & DEFCON STATUS -->
          <section class="dash-section" aria-label="SIEM Status Header">
            <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(94, 234, 212, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.35); color: #ff6b6b; margin-bottom: 0.35rem;">
                  <span class="badge-dot" style="background: #ff6b6b;"></span> DEFCON 2 • Active Ingestion Stream (48,200 EPS)
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Real-Time Global Threat Intelligence & SIEM Streams
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Correlating telemetry from MITRE ATT&CK, CISA Known Exploited Vulnerabilities (KEV), and proprietary Stackly Dark Web honeypots.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Refresh Threat Feeds</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Filter Streams</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: SIEM TELEMETRY KPIS -->
          <section class="dash-section" aria-label="SIEM Telemetry Metrics">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Correlated Events / Day</span>
                  <span class="kpi-icon">⚡</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">2.1B+</div>
                <div class="kpi-trend up"><span>↑ +12%</span> Distributed Kafka ingest</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Active Threat Indicators (IoCs)</span>
                  <span class="kpi-icon">🎯</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">14,820</div>
                <div class="kpi-trend up"><span>✓ Sync</span> Synchronized globally</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Integrated Threat Feeds</span>
                  <span class="kpi-icon">📡</span>
                </div>
                <div class="kpi-value">18 Feeds</div>
                <div class="kpi-trend up"><span>✓ 100%</span> CISA, MISP, Talos, Falcon</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Ingest Packet Drops</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value">0 Drops</div>
                <div class="kpi-trend up"><span>✓ Zero Loss</span> Zero buffer exhaustion</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: LIVE GLOBAL INGEST STREAM TABLE -->
          <section class="dash-section" aria-label="Live Ingest Stream Table">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🚨</span> Real-Time Ingested Threat Events Stream</h3>
                <span class="badge-tag">Updating Live</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Threat Actor / Campaign</th>
                      <th>Observed CVE</th>
                      <th>Targeted Protocol</th>
                      <th>Source Geolocation</th>
                      <th>Mitigation Rule</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>APT29 (Cozy Bear)</strong></td>
                      <td>CVE-2024-21887</td>
                      <td>Ivanti Connect Secure VPN</td>
                      <td>Rotterdam, NL (Tor Relay)</td>
                      <td>Zero-Trust Gateway Isolation</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Inspect</button></td>
                    </tr>
                    <tr>
                      <td><strong>LockBit 3.0 Variant</strong></td>
                      <td>CVE-2023-38831</td>
                      <td>RAR Archive Execution</td>
                      <td>Saint Petersburg, RU</td>
                      <td>Endpoint Behavioral Kill</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Inspect</button></td>
                    </tr>
                    <tr>
                      <td><strong>FIN7 FinTech Harvesting</strong></td>
                      <td>CVE-2023-34362</td>
                      <td>MOVEit Transfer SQLi</td>
                      <td>Sofia, BG (Bulletproof Host)</td>
                      <td>WAF SQLi Signature Block</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Inspect</button></td>
                    </tr>
                    <tr>
                      <td><strong>Volt Typhoon Lateral</strong></td>
                      <td>T1059.003 Windows CLI</td>
                      <td>WMI Remote Execution</td>
                      <td>Hong Kong, HK</td>
                      <td>Process Tree Terminate</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Inspect</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: DARK WEB INTELLIGENCE & LEAKED CREDENTIALS -->
          <section class="dash-section" aria-label="Dark Web Intelligence">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>🕵️</span> Dark Web & Underground Cybercrime Surveillance</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Surveillance of Russian, Chinese, and Telegram threat actor markets for corporate domain assets
                  </div>
                </div>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Trigger Deep Scraping</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Surveillance Vector</th>
                      <th>Monitored Domain / Pattern</th>
                      <th>Last Scrape Cycle</th>
                      <th>Breached Credentials</th>
                      <th>Mitigation Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>BreachForums & Genesis V2 Scrape</strong></td>
                      <td>*@stackly.security & Corporate Domains</td>
                      <td>8 Mins Ago</td>
                      <td><span class="severity-pill severity-low">0 Leaked</span></td>
                      <td>Active Domain Watchdog Enforced</td>
                    </tr>
                    <tr>
                      <td><strong>Pastebin & GitHub Gist Secret Sweeper</strong></td>
                      <td>API Keys, RSA Private Keys, Tokens</td>
                      <td>3 Mins Ago</td>
                      <td><span class="severity-pill severity-low">0 Exposed</span></td>
                      <td>Entropy Regex Scanners Running</td>
                    </tr>
                    <tr>
                      <td><strong>Telegram Cybercrime Channel Parser</strong></td>
                      <td>Brand Names, C-Suite Executive Names</td>
                      <td>12 Mins Ago</td>
                      <td><span class="severity-pill severity-low">0 Mentions</span></td>
                      <td>Continuous VIP Threat Monitoring</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 5: ADVANCED PERSISTENT THREAT (APT) CAMPAIGN TRACKER -->
          <section class="dash-section" aria-label="APT Campaign Tracker">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>🌐</span> Active State-Sponsored Threat Actor Campaigns</h3>
              <span class="badge-tag">Threat Horizon Q4</span>
            </div>
            <div class="dash-grid-4">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">APT29 (Nobelium)</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Primary Target: Cloud Identity & Hybrid OAuth</div>
                <div class="dash-stat-lbl">Status: Defenses Hardened • FIDO2 Keys Enforced</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Lazarus Group</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Primary Target: SWIFT, FinTech & Crypto APIs</div>
                <div class="dash-stat-lbl">Status: Zero Air-Gap Breaches Recorded</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Volt Typhoon</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Primary Target: Critical Infrastructure & SOHO Routers</div>
                <div class="dash-stat-lbl">Status: Outbound BGP Strict Filters Active</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--warning);">LockBit 3.0 Syndicate</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Primary Target: Double-Extortion Ransomware</div>
                <div class="dash-stat-lbl">Status: Canary Behavioral Shields Online</div>
              </div>
            </div>
          </section>

          <!-- SECTION 6: LIVE C2 BEACONING DETECTIONS -->
          <section class="dash-section" aria-label="C2 Beaconing Detections">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📡</span> Command & Control (C2) Beaconing & Jitter Analysis</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export PCAP Evidence</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Beacon ID</th>
                      <th>Calculated Jitter Interval</th>
                      <th>Destination C2 Node</th>
                      <th>Local Host IP</th>
                      <th>Sensor Containment</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>#BC-991</strong></td>
                      <td>60.2s (+/- 3.2s Jitter)</td>
                      <td>198.51.100.44:443 (Known Cobalt Strike)</td>
                      <td>10.0.14.9 (Quarantined)</td>
                      <td><span class="severity-pill severity-low">Socket Killed in 0.8s</span></td>
                    </tr>
                    <tr>
                      <td><strong>#BC-992</strong></td>
                      <td>120.0s (DNS Tunneling Pattern)</td>
                      <td>ns1.malicious-dyn-dns.cc:53</td>
                      <td>10.0.8.44 (Cleaned)</td>
                      <td><span class="severity-pill severity-low">DNS Sinkholed</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 7: INTEGRATED THREAT FEED CONNECTORS -->
          <section class="dash-section" aria-label="Threat Feed Connectors">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>🔌</span> Integrated Threat Feed Connectors & Feed Health</h3>
              <span class="badge-tag">18 / 18 Active</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">CISA Automated Indicator Sharing (AIS)</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem;">1,400 IoCs/hr</div>
                <div class="dash-stat-lbl">Status: Operational • Latency: 42ms</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">MISP Threat Community Network</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem;">3,200 IoCs/hr</div>
                <div class="dash-stat-lbl">Status: Operational • Latency: 64ms</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">CrowdStrike Falcon X Intelligence</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem;">2,100 IoCs/hr</div>
                <div class="dash-stat-lbl">Status: Operational • Latency: 28ms</div>
              </div>
            </div>
          </section>

          <!-- SECTION 8: CUSTOM YARA RULES & SIGMA LOGIC REPOSITORY -->
          <section class="dash-section" aria-label="Custom YARA and Sigma Rules">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>📜</span> Custom YARA Rules & Sigma Detection Logic Vault</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Custom proprietary heuristics compiled into kernel memory scanner daemons
                  </div>
                </div>
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Compile New Rule</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Rule Identifier</th>
                      <th>Rule Format</th>
                      <th>Detection Target</th>
                      <th>Trigger Count</th>
                      <th>False Positive Rate</th>
                      <th>Compiler Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>RULE_SIGMA_041</strong></td>
                      <td>Sigma v2.1</td>
                      <td>Suspicious PowerShell DownloadCradle via WMI</td>
                      <td>12 Hits</td>
                      <td>0.00%</td>
                      <td><span class="severity-pill severity-low">Active Production</span></td>
                    </tr>
                    <tr>
                      <td><strong>RULE_SIGMA_089</strong></td>
                      <td>Sigma v2.1</td>
                      <td>Kerberos AS-REP Roasting Without Pre-Auth</td>
                      <td>4 Hits</td>
                      <td>0.00%</td>
                      <td><span class="severity-pill severity-low">Active Production</span></td>
                    </tr>
                    <tr>
                      <td><strong>RULE_YARA_012</strong></td>
                      <td>YARA v4.3</td>
                      <td>Reflective DLL PE Header Injected Memory Bytes</td>
                      <td>2 Hits</td>
                      <td>0.00%</td>
                      <td><span class="severity-pill severity-low">Active Production</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        </div>
"""

vulnerabilities_html = """
        <!-- MODULE 3: VULNERABILITIES & CVE INTEL (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-vulnerabilities">
          <!-- SECTION 1: HEADER & ENGINE STATUS -->
          <section class="dash-section" aria-label="Vulnerability Engine Header">
            <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(94, 234, 212, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.35); color: #fbbf24; margin-bottom: 0.35rem;">
                  <span class="badge-dot" style="background: #fbbf24;"></span> Continuous Vulnerability Harvester Active • 680 Nodes Scanned
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Vulnerability Intel & Automated Patch Prioritization
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Real-time exposure mapping prioritizing vulnerabilities based on active exploitation probability (EPSS) and CISA KEV feeds.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Run Automated Scan</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export CVE Matrix</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: VULNERABILITY EXPOSURE KPIS -->
          <section class="dash-section" aria-label="Vulnerability KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Critical Zero-Days</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">0 Critical</div>
                <div class="kpi-trend up"><span>✓ 100% Clean</span> Zero unpatched zero-days</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">High Severity Pending</span>
                  <span class="kpi-icon">⚡</span>
                </div>
                <div class="kpi-value" style="color: #fbbf24;">4 High</div>
                <div class="kpi-trend up"><span>✓ In-SLA</span> Scheduled for maintenance</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Mean Time to Patch (MTTP)</span>
                  <span class="kpi-icon">⏱️</span>
                </div>
                <div class="kpi-value">3.2 Days</div>
                <div class="kpi-trend up"><span>✓ 74% Ahead</span> Industry average 14 days</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Hardened Microservices</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">680 Hosts</div>
                <div class="kpi-trend up"><span>✓ 100% Pass</span> CIS benchmark enforced</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: PRIORITIZED CVE REMEDIATION PIPELINE TABLE -->
          <section class="dash-section" aria-label="Prioritized CVE Pipeline">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🛡️</span> Prioritized CVE Vulnerability Remediation Pipeline</h3>
                <span class="badge-tag">Zero Overdue Items</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>CVE Identifier & Description</th>
                      <th>CVSS v3.1</th>
                      <th>EPSS Exploit Prob</th>
                      <th>Affected Environment</th>
                      <th>Assigned Platform Team</th>
                      <th>Patch Window SLA</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>CVE-2026-4421 (Linux Kernel Mem Fix)</strong></td>
                      <td><span class="severity-pill severity-high">8.8 High</span></td>
                      <td>84.2% (Weaponized)</td>
                      <td>8 Kubernetes Worker Nodes</td>
                      <td>Linux Platform Eng</td>
                      <td>Sunday 02:00 UTC (Next Window)</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Stage Patch</button></td>
                    </tr>
                    <tr>
                      <td><strong>CVE-2026-1930 (OpenSSL Handshake)</strong></td>
                      <td><span class="severity-pill severity-high">7.5 High</span></td>
                      <td>42.1% (Public PoC)</td>
                      <td>4 Edge NGINX Proxies</td>
                      <td>Network Operations</td>
                      <td>Wednesday 01:00 UTC</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Stage Patch</button></td>
                    </tr>
                    <tr>
                      <td><strong>CVE-2026-3829 (Spring Expression Inj)</strong></td>
                      <td><span class="severity-pill severity-high">7.2 High</span></td>
                      <td>38.0% (PoC Published)</td>
                      <td>2 Billing API Pods</td>
                      <td>Core Engineering</td>
                      <td>Tomorrow 23:00 UTC</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Stage Patch</button></td>
                    </tr>
                    <tr>
                      <td><strong>CVE-2026-0814 (NGINX Buffer Smuggle)</strong></td>
                      <td><span class="severity-pill severity-medium">6.8 Medium</span></td>
                      <td>12.4% (Theoretical)</td>
                      <td>6 Ingress Load Balancers</td>
                      <td>Cloud Architecture</td>
                      <td>Within 7 Days SLA</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Stage Patch</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: CISA KNOWN EXPLOITED VULNERABILITIES (KEV) MATCH -->
          <section class="dash-section" aria-label="CISA KEV Catalog Match">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>🏛️</span> CISA Known Exploited Vulnerabilities (KEV) Alignment</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Federal advisory catalog tracking active ransomware and adversary exploitation campaigns
                  </div>
                </div>
                <span class="severity-pill severity-low">Zero KEV Matches</span>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong style="color: var(--primary);">Active KEV Matches</strong>
                  <div class="dash-stat-val" style="color: var(--accent);">0 Exploits</div>
                  <div class="dash-stat-lbl">Perimeter 100% immunized against federal KEV list</div>
                </div>
                <div class="dash-stat-card">
                  <strong style="color: var(--secondary);">Catalog Synchronization</strong>
                  <div class="dash-stat-val" style="font-size: 1.25rem;">Automated</div>
                  <div class="dash-stat-lbl">Synchronized daily at 06:00 UTC from cisa.gov</div>
                </div>
                <div class="dash-stat-card">
                  <strong style="color: var(--accent);">Virtual Patching Shields</strong>
                  <div class="dash-stat-val" style="color: var(--primary);">100% Active</div>
                  <div class="dash-stat-lbl">eBPF and WAF rules deployed prior to code releases</div>
                </div>
              </div>
            </div>
          </section>

          <!-- SECTION 5: SOFTWARE BILL OF MATERIALS (SBOM) AUDIT -->
          <section class="dash-section" aria-label="SBOM Dependency Audit">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📦</span> Software Bill of Materials (SBOM) & Open-Source Dependencies</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export CycloneDX SBOM</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Open-Source Package & Version</th>
                      <th>Dependency Scope</th>
                      <th>License Compliance</th>
                      <th>Vulnerability Scan</th>
                      <th>Hardening Verification</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Log4j Core v2.17.1</strong></td>
                      <td>Direct Java Runtime</td>
                      <td>Apache 2.0 (Approved)</td>
                      <td><span class="severity-pill severity-low">0 Vulnerabilities</span></td>
                      <td>JNDI Lookups Disabled by Default</td>
                    </tr>
                    <tr>
                      <td><strong>OpenSSL v3.0.8</strong></td>
                      <td>System C Crypto Library</td>
                      <td>Apache 2.0 (Approved)</td>
                      <td><span class="severity-pill severity-low">Patch Verified</span></td>
                      <td>FIPS 140-3 Hardware Engine Bound</td>
                    </tr>
                    <tr>
                      <td><strong>Jackson Databind v2.15.2</strong></td>
                      <td>Spring Boot Serialization</td>
                      <td>Apache 2.0 (Approved)</td>
                      <td><span class="severity-pill severity-low">0 Vulnerabilities</span></td>
                      <td>Polymorphic Deserialization Filtered</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 6: CONTAINER & KUBERNETES REGISTRY SCANNER -->
          <section class="dash-section" aria-label="Container Registry Scans">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>☸️</span> Container Registry & Kubernetes Image Scans</h3>
              <span class="badge-tag">CI/CD Gate 100% Pass</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Base Image: alpine:3.19</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">0 CVEs</div>
                <div class="dash-stat-lbl">Cryptographically signed via Cosign • Signed by Stackly CI</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Base Image: distroless:12</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">0 CVEs</div>
                <div class="dash-stat-lbl">Shell-less microservice runtime • Minimal attack surface</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Admission Controller Gate</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem;">Enforced</div>
                <div class="dash-stat-lbl">Blocks deployment of unsigned or vulnerable pod images</div>
              </div>
            </div>
          </section>

          <!-- SECTION 7: OFFENSIVE PENTEST FINDINGS REMEDIATION -->
          <section class="dash-section" aria-label="PenTest Findings Remediation">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>🎯</span> Red Team PenTest Findings Verification Tracker</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Empirical validation of findings from recent adversarial penetration tests
                  </div>
                </div>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Request Re-Test</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Finding Identifier</th>
                      <th>Vulnerability Category</th>
                      <th>CVSS</th>
                      <th>Affected Component</th>
                      <th>Remediation Proof of Concept</th>
                      <th>Attestation Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>PT-FIND-01</strong></td>
                      <td>BOLA / IDOR Authorization Bypass</td>
                      <td><span class="severity-pill severity-high">7.8 High</span></td>
                      <td>Partner Invoicing API</td>
                      <td>Patched with tenant-scoped JWT claims</td>
                      <td><span class="severity-pill severity-low">Re-Tested & Clean</span></td>
                    </tr>
                    <tr>
                      <td><strong>PT-FIND-02</strong></td>
                      <td>Missing DNS CAA Certificate Records</td>
                      <td><span class="severity-pill severity-low">3.2 Low</span></td>
                      <td>Public Apex Domain</td>
                      <td>Strict Let's Encrypt / DigiCert CAA added</td>
                      <td><span class="severity-pill severity-low">Re-Tested & Clean</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 8: AUTOMATED PATCH DEPLOYMENT & CANARY WINDOWS -->
          <section class="dash-section" aria-label="Patch Deployment Windows">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>⚡</span> Automated Patch Deployment & Canary Safeguard Windows</h3>
                <span class="badge-tag">Zero-Downtime Safe</span>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong>Canary Staging Window</strong>
                  <div class="dash-stat-val" style="font-size: 1.25rem;">Tuesday 03:00 UTC</div>
                  <div class="dash-stat-lbl">Routes 10% traffic • Automated health check & synthetic monitoring</div>
                </div>
                <div class="dash-stat-card">
                  <strong>Production Ring 1 (40%)</strong>
                  <div class="dash-stat-val" style="font-size: 1.25rem;">Thursday 02:00 UTC</div>
                  <div class="dash-stat-lbl">Zero-downtime rolling deployment across primary worker clusters</div>
                </div>
                <div class="dash-stat-card">
                  <strong>Production Ring 2 (50%)</strong>
                  <div class="dash-stat-val" style="font-size: 1.25rem;">Sunday 02:00 UTC</div>
                  <div class="dash-stat-lbl">Final ring rollout with automated rollback on error rate &gt; 0.05%</div>
                </div>
              </div>
            </div>
          </section>
        </div>
"""

firewall_html = """
        <!-- MODULE 4: FIREWALL & ZERO-TRUST (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-firewall">
          <!-- SECTION 1: HEADER & POLICY STATUS -->
          <section class="dash-section" aria-label="Zero-Trust Perimeter Header">
            <div style="background: linear-gradient(135deg, rgba(167, 139, 250, 0.12) 0%, rgba(56, 189, 248, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="background: rgba(167, 139, 250, 0.15); border-color: rgba(167, 139, 250, 0.35); color: #a78bfa; margin-bottom: 0.35rem;">
                  <span class="badge-dot" style="background: #a78bfa;"></span> Next-Gen Firewall Cluster Active • Mutual TLS (mTLS) Enforced
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Zero-Trust Microsegmentation & Next-Gen Perimeter Firewall
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  East-West and North-South traffic inspection policies isolating workloads and eliminating lateral pivot vectors.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Deploy Rule Changes</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Audit Perimeter</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: PERIMETER & FIREWALL DEFENSE KPIS -->
          <section class="dash-section" aria-label="Firewall KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Ingress Drops Past 24h</span>
                  <span class="kpi-icon">🧱</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">184,200</div>
                <div class="kpi-trend up"><span>✓ Blocked</span> Unauthorized port scans</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Active Microsegmentation Rules</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">1,480 Rules</div>
                <div class="kpi-trend up"><span>✓ Enforced</span> East-West Zero-Trust</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Zero-Trust Gateways (ZTNA)</span>
                  <span class="kpi-icon">🌐</span>
                </div>
                <div class="kpi-value">12 Gateways</div>
                <div class="kpi-trend up"><span>✓ 100% Uptime</span> Worldwide HA cluster</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Unauthorized Lateral Pivots</span>
                  <span class="kpi-icon">🛑</span>
                </div>
                <div class="kpi-value">0 Pivots</div>
                <div class="kpi-trend up"><span>✓ Contained</span> Blast radius 100% isolated</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: NGFW RULE ENFORCEMENT TABLE -->
          <section class="dash-section" aria-label="NGFW Enforcement Table">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🧱</span> Active Next-Gen Firewall (NGFW) Rule Enforcement Table</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Add Security Group Rule</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Rule ID & Policy Name</th>
                      <th>Direction</th>
                      <th>Source CIDR / Workload</th>
                      <th>Destination Target</th>
                      <th>Protocol / Port</th>
                      <th>Enforcement Action</th>
                      <th>Hits Past 24h</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>RULE_NGFW_001 (Bulletproof CIDR Block)</strong></td>
                      <td>Ingress</td>
                      <td>Threat Intelligence Geo-Feed</td>
                      <td>All DMZ Ingress Gateways</td>
                      <td>Any TCP/UDP</td>
                      <td><span class="severity-pill severity-critical">Drop & Blacklist</span></td>
                      <td>124,800 hits</td>
                    </tr>
                    <tr>
                      <td><strong>RULE_NGFW_004 (Database mTLS Enforce)</strong></td>
                      <td>East-West</td>
                      <td>App-Tier Kubernetes Pods</td>
                      <td>PostgreSQL RDS Cluster</td>
                      <td>TCP 5432 (mTLS Strict)</td>
                      <td><span class="severity-pill severity-low">Allow Cryptographic</span></td>
                      <td>8,420,000 hits</td>
                    </tr>
                    <tr>
                      <td><strong>RULE_NGFW_009 (External RDP/SSH Lockdown)</strong></td>
                      <td>Ingress</td>
                      <td>0.0.0.0/0 (Public Internet)</td>
                      <td>All Hybrid Workloads</td>
                      <td>TCP 22, 3389, 5985</td>
                      <td><span class="severity-pill severity-critical">Drop & Alert</span></td>
                      <td>42,100 hits</td>
                    </tr>
                    <tr>
                      <td><strong>RULE_NGFW_014 (Egress Domain Whitelist)</strong></td>
                      <td>Egress</td>
                      <td>All Microservices VPCs</td>
                      <td>Approved Cloud API Endpoints</td>
                      <td>TCP 443 (TLS 1.3)</td>
                      <td><span class="severity-pill severity-low">Allow Whitelist</span></td>
                      <td>1,240,000 hits</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: MICROSEGMENTATION TOPOLOGY & BLAST RADIUS -->
          <section class="dash-section" aria-label="Microsegmentation Topology">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>🌐</span> Inter-VPC Microsegmentation Topology & Blast Radius</h3>
              <span class="badge-tag">Zero Trust Default</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Web Ingress Tier (VPC-10)</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">WAF Scrubbed • Istio Service Proxy Active</div>
                <div class="dash-stat-lbl">Can only talk to App Tier over HTTPS mTLS • Cannot access DB</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Application Tier (VPC-20)</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Stateless Compute • Ephemeral Pod Lifecycles</div>
                <div class="dash-stat-lbl">Zero direct internet egress • Connects to DB via IAM token</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Database Tier (VPC-30)</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Air-Gapped Private Subnet • AES-256 Storage</div>
                <div class="dash-stat-lbl">Zero internet access • Replicated across Frankfurt & US-East</div>
              </div>
            </div>
          </section>

          <!-- SECTION 5: ZERO-TRUST NETWORK ACCESS (ZTNA) CONDITIONAL POLICIES -->
          <section class="dash-section" aria-label="ZTNA Policies">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🔐</span> Zero-Trust Network Access (ZTNA) Conditional Access Policies</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Edit Access Policies</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Policy Name</th>
                      <th>Condition Scope</th>
                      <th>Authentication Requirement</th>
                      <th>Posture Assessment Check</th>
                      <th>Decision</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>ZTNA-ADMIN-01</strong></td>
                      <td>Access to Cloud Infrastructure Portals</td>
                      <td>FIPS 140-3 Hardware Token (FIDO2)</td>
                      <td>EDR Sensor Active + Hardened OS</td>
                      <td><span class="severity-pill severity-low">Grant Ephemeral 60m</span></td>
                    </tr>
                    <tr>
                      <td><strong>ZTNA-CORP-04</strong></td>
                      <td>Access to Internal Code Repositories</td>
                      <td>Biometric Touch WebAuthn + SSO</td>
                      <td>Disk Encryption Verified (FileVault/BitLocker)</td>
                      <td><span class="severity-pill severity-low">Grant Standard 8h</span></td>
                    </tr>
                    <tr>
                      <td><strong>ZTNA-GUEST-09</strong></td>
                      <td>Third-Party Contractor Access</td>
                      <td>One-Time Password + Hardware Token</td>
                      <td>VDI Isolated Enclave Only</td>
                      <td><span class="severity-pill severity-low">Restricted VDI</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 6: IPS DEEP PACKET INSPECTION -->
          <section class="dash-section" aria-label="IPS Deep Packet Inspection">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🔍</span> Intrusion Prevention System (IPS) Deep Packet Inspection Stream</h3>
                <span class="badge-tag">Zero Signature Drift</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Payload Signature Match</th>
                      <th>CVSS Equivalent</th>
                      <th>Target Asset</th>
                      <th>JA3 / TLS Fingerprint</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Apache Struts OGNL Remote Code Execution</strong></td>
                      <td><span class="severity-pill severity-critical">9.8 Critical</span></td>
                      <td>App-Legacy-02</td>
                      <td>771,49195-49199-49196,0-23-65281-10-11</td>
                      <td><span class="severity-pill severity-low">Dropped at Ingress</span></td>
                    </tr>
                    <tr>
                      <td><strong>Log4j JNDI LDAP Extraction Payload</strong></td>
                      <td><span class="severity-pill severity-critical">10.0 Critical</span></td>
                      <td>Ingress Proxy 01</td>
                      <td>771,49196-49195-49200,65281-0-23-10-11</td>
                      <td><span class="severity-pill severity-low">Dropped at Ingress</span></td>
                    </tr>
                    <tr>
                      <td><strong>Path Traversal ../../etc/shadow</strong></td>
                      <td><span class="severity-pill severity-high">7.5 High</span></td>
                      <td>Doc-Upload-Pod</td>
                      <td>771,4865-4866-4867,0-23-65281-10-11</td>
                      <td><span class="severity-pill severity-low">Dropped at Ingress</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 7: CLOUD WAF & DDOS SHIELDS -->
          <section class="dash-section" aria-label="Cloud WAF and DDoS">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>🛡️</span> Web Application Firewall (WAF) & Autonomous DDoS Shields</h3>
              <span class="badge-tag">Layer 3/4/7 Protection Active</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Autonomous DDoS Scrubbing</strong>
                <div class="dash-stat-val">3.2 Tbps Cap</div>
                <div class="dash-stat-lbl">Global Anycast mitigation mesh • Sub-second SYN flood absorption</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Bot Management & Scraper Trap</strong>
                <div class="dash-stat-val">100% Automated</div>
                <div class="dash-stat-lbl">AI behavioral fingerprinting • Eliminates credential stuffing bots</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Rate Limiting Shield</strong>
                <div class="dash-stat-val">100 req / 10s</div>
                <div class="dash-stat-lbl">Strict throttling applied to authentication and password reset APIs</div>
              </div>
            </div>
          </section>

          <!-- SECTION 8: EMERGENCY KILL-SWITCH & BGP BLACKHOLE -->
          <section class="dash-section" aria-label="Emergency Kill-Switch">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>🚨</span> Emergency Network Quarantine & BGP Blackhole Controls</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Sovereign air-gap triggers requiring Level-3 Operator authorization
                  </div>
                </div>
                <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Test Kill-Switch Handshake</button>
              </div>
              <div class="dash-grid-3">
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--warning); display: block; margin-bottom: 0.25rem;">Isolate Subnet VPC-20</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Sever East-West routes to prevent lateral spread</span>
                </button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--primary); display: block; margin-bottom: 0.25rem;">Announce BGP Blackhole</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Null-route external threat IP across global transit tier</span>
                </button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--danger); display: block; margin-bottom: 0.25rem;">Revoke All Active mTLS Certs</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Forces immediate re-authentication across all workloads</span>
                </button>
              </div>
            </div>
          </section>
        </div>
"""

incidents_html = """
        <!-- MODULE 5: INCIDENT TIMELINE & DIGITAL FORENSICS (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-incidents">
          <!-- SECTION 1: HEADER & EMERGENCY RETAINER -->
          <section class="dash-section" aria-label="Forensics Header">
            <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.35); color: #ff6b6b; margin-bottom: 0.35rem;">
                  <span class="badge-dot" style="background: #ff6b6b;"></span> 1-Hour Emergency Retainer Active • Digital Forensics Lead On-Call
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Chronological Incident Timeline & Digital Forensics Command
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Court-admissible forensic evidence acquisition, cryptographic chain of custody, and post-breach mitigation hardening.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Launch Incident Bridge</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Download Evidence ZIP</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: INCIDENT RESPONSE OPERATIONAL KPIS -->
          <section class="dash-section" aria-label="Incident Response KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Mean Time to Detect (MTTD)</span>
                  <span class="kpi-icon">⏱️</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">2.1 Min</div>
                <div class="kpi-trend up"><span>✓ Sub-5 Min SLA</span> Fast heuristic correlation</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Mean Time to Contain (MTTC)</span>
                  <span class="kpi-icon">🛑</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">14.8 Min</div>
                <div class="kpi-trend up"><span>✓ Sub-15 SLA</span> Autonomous containment</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Total Q4 Incidents</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value">18 Resolved</div>
                <div class="kpi-trend up"><span>✓ 100% Contained</span> Zero data exfiltration</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Direct Financial Loss</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value">$0.00</div>
                <div class="kpi-trend up"><span>✓ Zero Loss</span> Loss prevention warranty</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: CHRONOLOGICAL INCIDENT TIMELINE -->
          <section class="dash-section" aria-label="Chronological Incident Timeline">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>⚡</span> Chronological Incident Timeline & Audit Trail</h3>
                <span class="badge-tag">Incident #INC-2026-881</span>
              </div>
              <div class="timeline-feed">
                <div class="timeline-event">
                  <div class="timeline-dot"></div>
                  <div class="timeline-time">10:14:02 UTC • Sensor Ingest (Salem Node)</div>
                  <div class="timeline-title">Anomalous Kerberoasting SPN Query Logged</div>
                  <div class="timeline-desc">Workstation-88 requested high-privilege Kerberos service tickets for Srv-SQL-01 without normal authentication flow.</div>
                </div>
                <div class="timeline-event">
                  <div class="timeline-dot"></div>
                  <div class="timeline-time">10:14:28 UTC • Correlation Engine</div>
                  <div class="timeline-title">Correlated to MITRE ATT&CK T1558.003</div>
                  <div class="timeline-desc">Behavioral matrix confirmed adversary weaponized tool pattern. Threat score elevated to 9.2 (Critical).</div>
                </div>
                <div class="timeline-event">
                  <div class="timeline-dot"></div>
                  <div class="timeline-time">10:15:02 UTC • SOAR Playbook Automated Trigger</div>
                  <div class="timeline-desc">Host Workstation-88 isolated at network switch level. Compromised Kerberos TGT ticket invalidated immediately.</div>
                </div>
                <div class="timeline-event">
                  <div class="timeline-dot"></div>
                  <div class="timeline-time">10:16:14 UTC • Tier-2 Forensics Commander Dispatched</div>
                  <div class="timeline-desc">Investigator Priya Sharma extracted volatile RAM capture via agentless write-blocker connector.</div>
                </div>
                <div class="timeline-event">
                  <div class="timeline-dot"></div>
                  <div class="timeline-time">10:28:40 UTC • Incident Resolution & Attestation</div>
                  <div class="timeline-desc">Root cause identified as weaponized email attachment. User credentials reset; workstation re-imaged with verified gold master.</div>
                </div>
              </div>
            </div>
          </section>

          <!-- SECTION 4: CRYPTOGRAPHIC EVIDENCE VAULT -->
          <section class="dash-section" aria-label="Cryptographic Evidence Vault">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🔒</span> Chain of Custody & Cryptographic Evidence Vault</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Verify Hashes</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Evidence Item ID</th>
                      <th>Evidence Type</th>
                      <th>Acquisition Timestamp</th>
                      <th>Cryptographic SHA-256 Hash</th>
                      <th>Investigator Signature</th>
                      <th>Custody Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>#EV-2026-001</strong></td>
                      <td>Volatile RAM Memory Dump</td>
                      <td>Today 10:17:10 UTC</td>
                      <td><span style="font-family: var(--font-mono); font-size: 0.775rem;">d8f3a9...b109e2</span></td>
                      <td>Priya Sharma, GCFE</td>
                      <td><span class="severity-pill severity-low">Immutable WORM Storage</span></td>
                    </tr>
                    <tr>
                      <td><strong>#EV-2026-002</strong></td>
                      <td>Bit-Stream Physical Disk Clone</td>
                      <td>Today 10:22:45 UTC</td>
                      <td><span style="font-family: var(--font-mono); font-size: 0.775rem;">4e91b5...72c801</span></td>
                      <td>Priya Sharma, GCFE</td>
                      <td><span class="severity-pill severity-low">Hardware Vault Locked</span></td>
                    </tr>
                    <tr>
                      <td><strong>#EV-2026-003</strong></td>
                      <td>Raw CloudTrail & Syslog Pcap</td>
                      <td>Today 10:14:00 UTC</td>
                      <td><span style="font-family: var(--font-mono); font-size: 0.775rem;">a12c98...ef4312</span></td>
                      <td>Stackly Automated Sensor</td>
                      <td><span class="severity-pill severity-low">Court-Admissible</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 5: MITRE ATTACK PATH RECONSTRUCTION -->
          <section class="dash-section" aria-label="Attack Path Reconstruction">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>🎯</span> MITRE ATT&CK Attack Path Visual Reconstruction</h3>
              <span class="badge-tag">Contained at Step 4</span>
            </div>
            <div class="dash-grid-4">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">1. Initial Vector</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">T1566.002 Spearphishing</div>
                <div class="dash-stat-lbl">Adversary lure email delivered via compromised external vendor</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">2. Execution Attempt</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">T1059.001 PowerShell</div>
                <div class="dash-stat-lbl">Obfuscated script executed in temporary folder</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">3. Credential Access</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">T1558.003 Kerberoast</div>
                <div class="dash-stat-lbl">SPN ticket request detected and flagged by telemetry sensor</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--warning);">4. Containment Ring</strong>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">T1021 Pivot Blocked</div>
                <div class="dash-stat-lbl">Microsegmentation dropped lateral connection • Threat terminated</div>
              </div>
            </div>
          </section>

          <!-- SECTION 6: ROOT CAUSE ANALYSIS & POST-MORTEM -->
          <section class="dash-section" aria-label="Root Cause Analysis">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📑</span> Root Cause Analysis (RCA) & Post-Mortem Repository</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export RCA Deck</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Post-Mortem ID</th>
                      <th>Root Cause Category</th>
                      <th>Business Impact</th>
                      <th>Primary Remedy Deployed</th>
                      <th>Remediation Owner</th>
                      <th>Verification</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>#RCA-2026-Q4-01</strong></td>
                      <td>Spear-Phishing Credential Re-Use</td>
                      <td>$0.00 (Zero Exfil)</td>
                      <td>FIPS 140-3 Hardware Token mandatory for all users</td>
                      <td>Elena Rostova (CISO)</td>
                      <td><span class="severity-pill severity-low">Verified Complete</span></td>
                    </tr>
                    <tr>
                      <td><strong>#RCA-2026-Q3-08</strong></td>
                      <td>Test S3 Bucket Policy Misconfiguration</td>
                      <td>$0.00 (Caught in 4m)</td>
                      <td>Automated SCP Policy blocking public bucket creations</td>
                      <td>David Chen (Cloud SRE)</td>
                      <td><span class="severity-pill severity-low">Verified Complete</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 7: STATUTORY BREACH NOTIFICATION CHECKLIST -->
          <section class="dash-section" aria-label="Statutory Notification Checklist">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>⚖️</span> Statutory Regulatory Breach Notification Timers</h3>
              <span class="badge-tag">Zero Declarable Breaches</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">EU GDPR Article 33</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">Not Triggered</div>
                <div class="dash-stat-lbl">72-Hour Data Protection Authority timer not applicable (0 PII exposed)</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">SEC Form 8-K Item 1.05</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">Not Material</div>
                <div class="dash-stat-lbl">4-Business Day SEC disclosure evaluated • No material business impact</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">HIPAA Breach Notification</strong>
                <div class="dash-stat-val" style="font-size: 1.25rem; color: var(--accent);">Not Triggered</div>
                <div class="dash-stat-lbl">Zero protected health information touched or compromised</div>
              </div>
            </div>
          </section>

          <!-- SECTION 8: POST-INCIDENT HARDENING SAFEGUARDS -->
          <section class="dash-section" aria-label="Post-Incident Hardening">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🛡️</span> Post-Incident Hardening & Compensating Verification</h3>
                <span class="severity-pill severity-low">All Controls Verified</span>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong>Egress Network Policy Tightening</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Subnet 10.0.14.0/24 locked down</div>
                  <div class="dash-stat-lbl">Verified by NGFW policy inspection • Complete</div>
                </div>
                <div class="dash-stat-card">
                  <strong>Domain Controller Kerberos Rotation</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">krbtgt account password cycled twice</div>
                  <div class="dash-stat-lbl">Golden ticket persistence fully neutralized • Complete</div>
                </div>
                <div class="dash-stat-card">
                  <strong>EDR Aggressive Kernel Sensor Mode</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Expanded to all financial workstations</div>
                  <div class="dash-stat-lbl">Memory unhooking detection active • Complete</div>
                </div>
              </div>
            </div>
          </section>
        </div>
"""

compliance_html = """
        <!-- MODULE 6: COMPLIANCE & EVIDENCE VAULT (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-compliance">
          <!-- SECTION 1: HEADER & AUDIT ENCLAVE -->
          <section class="dash-section" aria-label="Compliance Enclave Header">
            <div style="background: linear-gradient(135deg, rgba(94, 234, 212, 0.12) 0%, rgba(56, 189, 248, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.35rem;">
                  <span class="badge-dot"></span> Automated Compliance Harvester Active • 6 International Standards
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Regulatory Compliance & Cryptographic Evidence Vault
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Continuous automated evidence mapping satisfying ISO/IEC 27001:2022, SOC 2 Type II, HIPAA, PCI-DSS v4.0, and GDPR.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Export Auditor Bundle</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Attestation Letters</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: GOVERNANCE & COMPLIANCE KPIS -->
          <section class="dash-section" aria-label="Compliance KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">ISO/IEC 27001 Controls</span>
                  <span class="kpi-icon">📜</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">93 / 93</div>
                <div class="kpi-trend up"><span>✓ 100% Pass</span> Annex A controls verified</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">SOC 2 Type II Status</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">Clean Opinion</div>
                <div class="kpi-trend up"><span>✓ 0 Deficiencies</span> Ernst & Young unqualified</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">HIPAA Security Rule</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value">100% Aligned</div>
                <div class="kpi-trend up"><span>✓ Compliant</span> ePHI encryption at rest</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">GDPR Privacy Assurance</span>
                  <span class="kpi-icon">⚖️</span>
                </div>
                <div class="kpi-value">98 / 100</div>
                <div class="kpi-trend up"><span>✓ High Score</span> DPIA verified</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: INSTITUTIONAL CERTIFICATION & AUDIT TABLE -->
          <section class="dash-section" aria-label="Institutional Audit Evidence">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📜</span> Institutional Certification & Evidence Vault Table</h3>
                <span class="badge-tag">Audited Annually</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Compliance Framework</th>
                      <th>Control Domains Covered</th>
                      <th>Automated Evidence Feeds</th>
                      <th>External Audit Body</th>
                      <th>Certification Status</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>ISO/IEC 27001:2022</strong></td>
                      <td>All 93 Annex A Control Clauses</td>
                      <td>28 Live API Telemetry Connectors</td>
                      <td>BSI Group (British Standards Inst.)</td>
                      <td><span class="severity-pill severity-low">Active Certificate</span></td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>AICPA SOC 2 Type II</strong></td>
                      <td>Security, Availability, Confidentiality</td>
                      <td>Continuous Audit Trail Logs</td>
                      <td>Ernst & Young LLP</td>
                      <td><span class="severity-pill severity-low">Clean Unqualified</span></td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>PCI-DSS v4.0</strong></td>
                      <td>Cardholder Data Environment (CDE)</td>
                      <td>Network Segmentation Evidence</td>
                      <td>Schellman & Company QSA</td>
                      <td><span class="severity-pill severity-low">Attestation (AOC)</span></td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>NIST SP 800-53 Rev 5</strong></td>
                      <td>FedRAMP Moderate Security Baseline</td>
                      <td>Automated OSCAL Control Matrix</td>
                      <td>Internal Federal Audit Team</td>
                      <td><span class="severity-pill severity-low">100% Aligned</span></td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: CIS BENCHMARKS CONFIGURATION DRIFT -->
          <section class="dash-section" aria-label="CIS Benchmarks">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>☁️</span> Cloud CIS Benchmarks & Configuration Drift Monitoring</h3>
              <span class="badge-tag">Zero Configuration Drift</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">CIS AWS Foundations v2.0</strong>
                <div class="dash-stat-val" style="color: var(--accent);">99.4% Pass</div>
                <div class="dash-stat-lbl">Identity, logging, and VPC network controls 100% compliant</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">CIS Microsoft Azure Benchmark</strong>
                <div class="dash-stat-val" style="color: var(--primary);">98.8% Pass</div>
                <div class="dash-stat-lbl">Entra ID, Key Vault, and Storage accounts strictly hardened</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">CIS Kubernetes Benchmark v1.8</strong>
                <div class="dash-stat-val" style="color: var(--accent);">100.0% Pass</div>
                <div class="dash-stat-lbl">API Server, kubelet, and etcd encryption 100% compliant</div>
              </div>
            </div>
          </section>

          <!-- SECTION 5: CRYPTOGRAPHIC ASSURANCE & FIPS 140-3 CONTROLS -->
          <section class="dash-section" aria-label="Cryptographic Controls">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🔒</span> Cryptographic Assurance & FIPS 140-3 Hardware Controls</h3>
                <span class="severity-pill severity-low">Level-3 Hardware Certified</span>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong>Hardware Security Module (HSM)</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">Thales Luna PCIe HSM Enclave</div>
                  <div class="dash-stat-lbl">Zero key exportability • Physical tamper-detection sensors active</div>
                </div>
                <div class="dash-stat-card">
                  <strong>Data-At-Rest Storage Encryption</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">AES-256-GCM Master Keys</div>
                  <div class="dash-stat-lbl">Automated annual AWS KMS / Azure Key Vault master key rotation</div>
                </div>
                <div class="dash-stat-card">
                  <strong>In-Transit Telemetry Transport</strong>
                  <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.25rem 0;">TLS 1.3 with Ephemeral ECDHE</div>
                  <div class="dash-stat-lbl">Strict forward secrecy enforced on all edge ingestion gateways</div>
                </div>
              </div>
            </div>
          </section>

          <!-- SECTION 6: THIRD-PARTY VENDOR SECURITY DUE DILIGENCE -->
          <section class="dash-section" aria-label="Vendor Security Due Diligence">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🏢</span> Third-Party Sub-Processor Governance & SOC 2 Reviews</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Upload Vendor Assessment</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Sub-Processor Name</th>
                      <th>Service Function</th>
                      <th>DPA Signed</th>
                      <th>SOC 2 Type II Bridge Letter</th>
                      <th>Data Residency</th>
                      <th>Audit Approval</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Amazon Web Services Inc.</strong></td>
                      <td>Multi-Cloud Infrastructure</td>
                      <td>Yes (Standard Contractual Clauses)</td>
                      <td>Current (Valid through 2027)</td>
                      <td>EU / US Sovereign Enclaves</td>
                      <td><span class="severity-pill severity-low">Verified Approved</span></td>
                    </tr>
                    <tr>
                      <td><strong>CrowdStrike Inc.</strong></td>
                      <td>Endpoint Detection & Response</td>
                      <td>Yes (Direct Data Protection Addendum)</td>
                      <td>Current (Valid through 2027)</td>
                      <td>Frankfurt & US Cloud Enclave</td>
                      <td><span class="severity-pill severity-low">Verified Approved</span></td>
                    </tr>
                    <tr>
                      <td><strong>Cloudflare Inc.</strong></td>
                      <td>Edge WAF & DDoS Scrubbing</td>
                      <td>Yes (Strict Non-Disclosure)</td>
                      <td>Current (Valid through 2027)</td>
                      <td>Global Edge Caching Zero PII</td>
                      <td><span class="severity-pill severity-low">Verified Approved</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 7: QUARTERLY ACCESS RECERTIFICATION & SOD -->
          <section class="dash-section" aria-label="Quarterly Access Recertification">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>👥</span> Quarterly Access Recertification & Segregation of Duties</h3>
              <span class="badge-tag">Q4 Audit Cycle Complete</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Recertification Rate</strong>
                <div class="dash-stat-val">100.0%</div>
                <div class="dash-stat-lbl">1,240 / 1,240 corporate user entitlements recertified by line managers</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Orphaned Accounts Purged</strong>
                <div class="dash-stat-val">12 Accounts</div>
                <div class="dash-stat-lbl">Stale contractor accounts identified and disabled automatically</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Segregation of Duties Conflicts</strong>
                <div class="dash-stat-val" style="color: var(--accent);">0 Conflicts</div>
                <div class="dash-stat-lbl">Zero overlapping administrator/auditor privileges detected</div>
              </div>
            </div>
          </section>

          <!-- SECTION 8: EXTERNAL AUDITOR EVIDENCE BUNDLE GENERATOR -->
          <section class="dash-section" aria-label="Auditor Bundle Generator">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>📑</span> External Auditor Compliance Package & Attestation Generator</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Instant compilation of cryptographically hashed evidence packages for external audit teams
                  </div>
                </div>
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Generate Complete Package</button>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong>Package #1: Board Governance Summary</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">Executive PDF with CISO signoff & risk KPIs</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Download PDF</button>
                </div>
                <div class="dash-stat-card">
                  <strong>Package #2: Technical Audit Evidence Vault</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">ZIP archive containing API logs, configs & hashes</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Download ZIP</button>
                </div>
                <div class="dash-stat-card">
                  <strong>Package #3: Form 8-K / Statutory Filing Prep</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">Prepared regulatory filing statements & attestation</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Download Doc</button>
                </div>
              </div>
            </div>
          </section>
        </div>
"""

reports_html = """
        <!-- MODULE 7: EXECUTIVE RISK & BOARD REPORTS (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-reports">
          <!-- SECTION 1: HEADER & PUBLISHING SCHEDULE -->
          <section class="dash-section" aria-label="Reports Header">
            <div style="background: linear-gradient(135deg, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.35rem;">
                  <span class="badge-dot"></span> Executive Reporting Engine Active • Q4 Board Briefing Compiled
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Executive Risk & Board Decision Briefings
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Board-level risk quantification, FAIR financial exposure models, and historical SLA performance analytics.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Generate Board Deck (PDF)</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Schedule Presentation</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: STRATEGIC CYBER DEFENSE FINANCIAL KPIS -->
          <section class="dash-section" aria-label="Financial Cyber Defense KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Annual Cyber Defense ROI</span>
                  <span class="kpi-icon">📈</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">+340%</div>
                <div class="kpi-trend up"><span>✓ Measured</span> Return on security spend</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Averted Breach Loss</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">$14.2M</div>
                <div class="kpi-trend up"><span>✓ Ponemon Benchmark</span> Estimated averted loss</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Risk Exposure Reduction</span>
                  <span class="kpi-icon">📉</span>
                </div>
                <div class="kpi-value">-78%</div>
                <div class="kpi-trend up"><span>✓ Year-over-Year</span> Attack surface reduction</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Insurance Premium Credit</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value">22% Discount</div>
                <div class="kpi-trend up"><span>✓ Underwriter Attested</span> Cyber risk credit</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: EXECUTIVE BOARD RISK BRIEFINGS TABLE -->
          <section class="dash-section" aria-label="Executive Briefings Table">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📑</span> Executive Board Risk & Threat Briefing Digests</h3>
                <span class="badge-tag">Current Q4 Releases</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Briefing Title & Classification</th>
                      <th>Target Committee</th>
                      <th>Reporting Period</th>
                      <th>Compilation Date</th>
                      <th>File Size</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Q4 2026 Executive Cyber Risk Briefing</strong></td>
                      <td>Board of Directors & Audit Committee</td>
                      <td>July 1 – Sept 30, 2026</td>
                      <td>Today at 08:00 UTC</td>
                      <td>4.2 MB (Signed PDF)</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>Monthly Managed SOC SLA Performance Digest</strong></td>
                      <td>CISO & Client Executive IT Director</td>
                      <td>Past 30 Days</td>
                      <td>1st of Month</td>
                      <td>2.1 MB (Signed PDF)</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>Sovereign Ransomware Resilience Assurance</strong></td>
                      <td>Executive Risk Committee</td>
                      <td>Annual Assessment</td>
                      <td>Oct 2026</td>
                      <td>5.8 MB (Signed PDF)</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                    <tr>
                      <td><strong>Third-Party Supply Chain Security Review</strong></td>
                      <td>General Counsel & Procurement</td>
                      <td>Semi-Annual</td>
                      <td>Sept 2026</td>
                      <td>3.4 MB (Signed PDF)</td>
                      <td><button type="button" class="btn btn-outline btn-sm dash-action-btn">Download PDF</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: FAIR QUANTITATIVE CYBER RISK MODEL -->
          <section class="dash-section" aria-label="FAIR Risk Model">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>📊</span> FAIR Quantitative Financial Exposure Model</h3>
              <span class="badge-tag">Probable Loss Reduction: 88%</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Ransomware Scenario</strong>
                <div class="dash-stat-val" style="color: var(--accent);">$1.2M PML</div>
                <div class="dash-stat-lbl">92% Risk reduction via automated endpoint containment & zero-trust</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">Cloud Data Exfiltration Scenario</strong>
                <div class="dash-stat-val" style="color: var(--primary);">$2.4M PML</div>
                <div class="dash-stat-lbl">88% Risk reduction via ZTNA access proxies & eBPF syscall guards</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Supply Chain Pivot Scenario</strong>
                <div class="dash-stat-val" style="color: var(--accent);">$800k PML</div>
                <div class="dash-stat-lbl">85% Risk reduction via strict egress isolation & microsegmentation</div>
              </div>
            </div>
          </section>

          <!-- SECTION 5: CROSS-INDUSTRY BENCHMARK COMPARISONS -->
          <section class="dash-section" aria-label="Industry Benchmarks">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🌐</span> Cross-Industry Peer Group Resilience Scorecard</h3>
                <span class="severity-pill severity-low">Top 1% Global Tier</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Cyber Resilience Dimension</th>
                      <th>Stackly Protected Infrastructure</th>
                      <th>Global Enterprise Benchmark</th>
                      <th>Advantage Factor</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Mean Time to Detect (MTTD)</strong></td>
                      <td><strong style="color: var(--accent);">2.1 Minutes</strong></td>
                      <td>207 Days (Industry Average)</td>
                      <td><span class="severity-pill severity-low">99.9% Faster</span></td>
                    </tr>
                    <tr>
                      <td><strong>Mean Time to Contain (MTTC)</strong></td>
                      <td><strong style="color: var(--accent);">14.8 Minutes</strong></td>
                      <td>73 Days (Industry Average)</td>
                      <td><span class="severity-pill severity-low">99.8% Faster</span></td>
                    </tr>
                    <tr>
                      <td><strong>Unplanned Security Downtime</strong></td>
                      <td><strong style="color: var(--accent);">0.00%</strong></td>
                      <td>2.4% Annual Business Interruption</td>
                      <td><span class="severity-pill severity-low">Zero Downtime</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 6: SOC SLA DELIVERY TRENDLINES -->
          <section class="dash-section" aria-label="SOC SLA Trends">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>📈</span> 12-Month Operational SLA Trendlines</h3>
              <span class="badge-tag">Zero Contract Penalties</span>
            </div>
            <div class="dash-grid-3">
              <div class="dash-stat-card">
                <strong style="color: var(--primary);">Continuous Availability</strong>
                <div class="dash-stat-val">100.0%</div>
                <div class="dash-stat-lbl">12 consecutive months of flawless 24/7 eyes-on-glass SOC coverage</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--secondary);">15-Minute Critical SLA</strong>
                <div class="dash-stat-val">100.0% Met</div>
                <div class="dash-stat-lbl">Every P1 alert triaged and contained in under 15 minutes</div>
              </div>
              <div class="dash-stat-card">
                <strong style="color: var(--accent);">Warranty Penalty Claims</strong>
                <div class="dash-stat-val">$0.00</div>
                <div class="dash-stat-lbl">Zero contract penalty claims triggered across all protected clients</div>
              </div>
            </div>
          </section>

          <!-- SECTION 7: SECURITY CULTURE & HUMAN RISK REPORT -->
          <section class="dash-section" aria-label="Security Culture Report">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>👥</span> Security Culture, Training Impact & Human Risk Factor</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Export Culture Audit</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Corporate Department</th>
                      <th>Headcount</th>
                      <th>Phishing Susceptibility</th>
                      <th>Immediate Reporting Rate</th>
                      <th>Training Completion</th>
                      <th>Risk Grade</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Executive Committee & Board</strong></td>
                      <td>28 Officers</td>
                      <td>0.0% (Zero Clicks)</td>
                      <td>96.4% Reported in &lt;5 mins</td>
                      <td>100.0%</td>
                      <td><span class="severity-pill severity-low">Grade A+</span></td>
                    </tr>
                    <tr>
                      <td><strong>Finance & Accounting Core</strong></td>
                      <td>142 Staff</td>
                      <td>0.7% (1 Click, Contained)</td>
                      <td>91.2% Reported</td>
                      <td>100.0%</td>
                      <td><span class="severity-pill severity-low">Grade A</span></td>
                    </tr>
                    <tr>
                      <td><strong>Engineering & Product</strong></td>
                      <td>480 Staff</td>
                      <td>0.8% (Simulated)</td>
                      <td>89.4% Reported</td>
                      <td>99.2%</td>
                      <td><span class="severity-pill severity-low">Grade A</span></td>
                    </tr>
                    <tr>
                      <td><strong>Sales & Global Operations</strong></td>
                      <td>590 Staff</td>
                      <td>1.8% (Simulated)</td>
                      <td>81.0% Reported</td>
                      <td>97.8%</td>
                      <td><span class="severity-pill severity-low">Grade A-</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 8: ON-DEMAND CUSTOM BOARD PRESENTATION GENERATOR -->
          <section class="dash-section" aria-label="Custom Presentation Generator">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>📊</span> On-Demand Custom Board Presentation & Executive Generator</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Configure custom date ranges, target stakeholders, and slide formats
                  </div>
                </div>
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Compile Presentation Deck</button>
              </div>
              <div class="dash-grid-3">
                <div class="dash-stat-card">
                  <strong>Audience: Audit Committee</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">Focus: ISO 27001, SOC 2, HIPAA & legal warranty</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Select Preset</button>
                </div>
                <div class="dash-stat-card">
                  <strong>Audience: Chief Financial Officer</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">Focus: ROI, cyber insurance credits, loss prevention</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Select Preset</button>
                </div>
                <div class="dash-stat-card">
                  <strong>Audience: Board of Directors</strong>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin: 0.25rem 0;">Focus: Strategic resilience, threat landscape, compliance</div>
                  <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="margin-top: 0.5rem;">Select Preset</button>
                </div>
              </div>
            </div>
          </section>
        </div>
"""

users_html = """
        <!-- MODULE 8: USER ACCESS MANAGEMENT & ROLE CLEARANCES (8 DISTINCT SECTIONS) -->
        <div class="dash-module-section" id="module-users">
          <!-- SECTION 1: HEADER & IDENTITY ENCLAVE -->
          <section class="dash-section" aria-label="Identity Enclave Header">
            <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%); border: 1px solid var(--border-cyber); border-radius: var(--radius-lg); padding: clamp(1.25rem, 2vw, 1.75rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
              <div>
                <span class="badge-tag" style="margin-bottom: 0.35rem;">
                  <span class="badge-dot"></span> Zero-Trust Identity Fabric • FIPS 140-3 Hardware Token Enforcement
                </span>
                <h2 style="font-size: clamp(1.3rem, 1.8vw, 1.6rem); margin: 0.25rem 0; font-weight: 800; color: var(--text-primary);">
                  Operator Clearances & Identity Access Governance
                </h2>
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
                  Role-based access control (RBAC), Just-In-Time (JIT) ephemeral grants, and cryptographic token registry.
                </p>
              </div>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <button type="button" class="btn btn-primary btn-sm dash-action-btn">Provision New Operator</button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Audit Active Sessions</button>
              </div>
            </div>
          </section>

          <!-- SECTION 2: ACCESS GOVERNANCE KPIS -->
          <section class="dash-section" aria-label="Identity Governance KPIs">
            <div class="dash-kpi-grid">
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Active Security Operators</span>
                  <span class="kpi-icon">👥</span>
                </div>
                <div class="kpi-value" style="color: var(--primary);">14 Operators</div>
                <div class="kpi-trend up"><span>✓ Clearances Active</span> Multi-tier command</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Privileged Clearance Roles</span>
                  <span class="kpi-icon">🛡️</span>
                </div>
                <div class="kpi-value" style="color: var(--accent);">3 Roles</div>
                <div class="kpi-trend up"><span>✓ Segregated</span> CISO, SOC Lead, IT Director</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Ephemeral JIT Grants</span>
                  <span class="kpi-icon">⚡</span>
                </div>
                <div class="kpi-value">2 Active</div>
                <div class="kpi-trend up"><span>✓ Expiring &lt;60m</span> Auto-revocation active</div>
              </div>
              <div class="kpi-card js-tilt">
                <div class="kpi-top">
                  <span class="kpi-label">Inactive Stale Accounts</span>
                  <span class="kpi-icon">🔒</span>
                </div>
                <div class="kpi-value">0 Accounts</div>
                <div class="kpi-trend up"><span>✓ 100% Purged</span> Automated 30-day cleanup</div>
              </div>
            </div>
          </section>

          <!-- SECTION 3: AUTHORIZED OPERATORS & CLEARANCES TABLE -->
          <section class="dash-section" aria-label="Authorized Operators Table">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>👥</span> Authorized Operators & Clearance Levels</h3>
                <span class="badge-tag">Zero Trust Authenticated</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Operator Name</th>
                      <th>Assigned Clearance Role</th>
                      <th>Clearance Tier</th>
                      <th>Department & Division</th>
                      <th>Hardware Token ID</th>
                      <th>Last Authenticated</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Elena Rostova</strong></td>
                      <td>Chief Information Security Officer (CISO)</td>
                      <td><span class="severity-pill severity-critical">Top-Secret (TS/SCI)</span></td>
                      <td>Executive Governance Enclave</td>
                      <td>YUBI-9941-FIPS</td>
                      <td>Active Now</td>
                      <td><span class="severity-pill severity-low">Online</span></td>
                    </tr>
                    <tr>
                      <td><strong>Alex Vance</strong></td>
                      <td>Lead SOC Operations Commander</td>
                      <td><span class="severity-pill severity-high">Secret (SOC-L3)</span></td>
                      <td>24/7 Operations Command</td>
                      <td>YUBI-4182-FIPS</td>
                      <td>Active Now</td>
                      <td><span class="severity-pill severity-low">Online</span></td>
                    </tr>
                    <tr>
                      <td><strong>Sarah Jenkins</strong></td>
                      <td>Enterprise Client IT Director</td>
                      <td><span class="severity-pill severity-medium">Confidential (Org-Admin)</span></td>
                      <td>Infrastructure Operations</td>
                      <td>YUBI-1029-FIPS</td>
                      <td>Active Now</td>
                      <td><span class="severity-pill severity-low">Online</span></td>
                    </tr>
                    <tr>
                      <td><strong>Marcus Vance</strong></td>
                      <td>Senior Incident Responder</td>
                      <td><span class="severity-pill severity-high">Secret (SOC-L2)</span></td>
                      <td>Threat Hunting Unit</td>
                      <td>YUBI-7714-FIPS</td>
                      <td>14 Mins Ago</td>
                      <td><span class="severity-pill severity-low">Online</span></td>
                    </tr>
                    <tr>
                      <td><strong>Priya Sharma</strong></td>
                      <td>Digital Forensics Specialist</td>
                      <td><span class="severity-pill severity-high">Secret (SOC-L2)</span></td>
                      <td>Malware Analysis Enclave</td>
                      <td>YUBI-5529-FIPS</td>
                      <td>1 Hour Ago</td>
                      <td><span class="severity-pill severity-low">Standby</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 4: ROLE-BASED ACCESS CONTROL (RBAC) MATRIX -->
          <section class="dash-section" aria-label="RBAC Matrix">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📋</span> Role-Based Access Control (RBAC) & Clearance Matrix</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Modify Matrix</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Clearance Role</th>
                      <th>Board Briefing Signoff</th>
                      <th>Security Policy Authorization</th>
                      <th>Firewall Rule Deploy</th>
                      <th>Quarantine Kill-Switch</th>
                      <th>SLA / Asset Oversight</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Chief Information Security Officer (CISO)</strong></td>
                      <td><span style="color: var(--accent); font-weight: 800;">Full Sign-off</span></td>
                      <td><span style="color: var(--accent); font-weight: 800;">Full Authorization</span></td>
                      <td>Read-Only Audit</td>
                      <td><span style="color: var(--accent); font-weight: 800;">Executive Override</span></td>
                      <td>Full Strategic View</td>
                    </tr>
                    <tr>
                      <td><strong>Lead SOC Operations Commander</strong></td>
                      <td>Read-Only Digest</td>
                      <td>Propose Amendments</td>
                      <td><span style="color: var(--accent); font-weight: 800;">Full Production Deploy</span></td>
                      <td><span style="color: var(--accent); font-weight: 800;">Instant Execution</span></td>
                      <td>Technical Telemetry Only</td>
                    </tr>
                    <tr>
                      <td><strong>Enterprise Client IT Director</strong></td>
                      <td>Read-Only Digest</td>
                      <td>Read-Only</td>
                      <td>Read-Only Group Audit</td>
                      <td>Emergency Bridge Alert</td>
                      <td><span style="color: var(--accent); font-weight: 800;">Full Client Enclave</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 5: JUST-IN-TIME (JIT) PRIVILEGED ACCESS REQUESTS -->
          <section class="dash-section" aria-label="JIT Access Requests">
            <div class="dash-section-header">
              <h3 class="dash-section-title"><span>⏱️</span> Just-In-Time (JIT) Ephemeral Privilege Requests</h3>
              <span class="badge-tag">Zero Permanent Admin Rights</span>
            </div>
            <div class="dash-grid-2">
              <div class="dash-stat-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--primary);">Request #JIT-481 (Database Maintenance)</strong>
                  <span class="severity-pill severity-low">Approved (42m left)</span>
                </div>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.35rem 0;">
                  Operator: Marcus Vance • Justification: Apply PostgreSQL dirty page memory patch
                </div>
                <div class="dash-stat-lbl">Expires automatically at 19:42 UTC • Session fully recorded</div>
              </div>

              <div class="dash-stat-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--secondary);">Request #JIT-482 (Firewall Policy Edit)</strong>
                  <span class="severity-pill severity-low">Approved (28m left)</span>
                </div>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin: 0.35rem 0;">
                  Operator: Alex Vance • Justification: Emergency BGP null-route on bruteforce botnet
                </div>
                <div class="dash-stat-lbl">Expires automatically at 19:28 UTC • Audit log appended to SIEM</div>
              </div>
            </div>
          </section>

          <!-- SECTION 6: HARDWARE TOKEN CREDENTIAL REGISTRY -->
          <section class="dash-section" aria-label="Hardware Token Registry">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>🔑</span> FIPS 140-3 Hardware Token (YubiKey 5) Registry</h3>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn">Register New Key</button>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Token Serial Number</th>
                      <th>Token Model</th>
                      <th>Hardware Attestation</th>
                      <th>Assigned Operator</th>
                      <th>Registration Date</th>
                      <th>Key Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>YUBI-9941-FIPS</strong></td>
                      <td>YubiKey 5 NFC FIPS</td>
                      <td>FIDO2 / WebAuthn Level 3</td>
                      <td>Elena Rostova (CISO)</td>
                      <td>Jan 12, 2026</td>
                      <td><span class="severity-pill severity-low">Active & Bound</span></td>
                    </tr>
                    <tr>
                      <td><strong>YUBI-4182-FIPS</strong></td>
                      <td>YubiKey 5C NFC FIPS</td>
                      <td>FIDO2 / WebAuthn Level 3</td>
                      <td>Alex Vance (SOC Lead)</td>
                      <td>Feb 04, 2026</td>
                      <td><span class="severity-pill severity-low">Active & Bound</span></td>
                    </tr>
                    <tr>
                      <td><strong>YUBI-1029-FIPS</strong></td>
                      <td>YubiKey 5 Nano FIPS</td>
                      <td>FIDO2 / WebAuthn Level 3</td>
                      <td>Sarah Jenkins (Client Dir)</td>
                      <td>March 18, 2026</td>
                      <td><span class="severity-pill severity-low">Active & Bound</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 7: REAL-TIME AUTHENTICATION AUDIT LOG -->
          <section class="dash-section" aria-label="Authentication Audit Log">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <h3 class="dash-panel-title"><span>📜</span> Real-Time Operator Authentication & Audit Stream</h3>
                <span class="badge-tag">Zero Unauthorized Logins</span>
              </div>
              <div class="data-table-wrap">
                <table class="dash-table">
                  <thead>
                    <tr>
                      <th>Timestamp (UTC)</th>
                      <th>Operator Identity</th>
                      <th>Authentication Factor</th>
                      <th>Source IP Address</th>
                      <th>Host Device Posture</th>
                      <th>Gateway Decision</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Today 18:30:14</td>
                      <td>Elena Rostova (CISO)</td>
                      <td>FIDO2 Hardware Token Touch</td>
                      <td>10.0.1.5 (Corporate Internal)</td>
                      <td>CrowdStrike Falcon 100% Compliant</td>
                      <td><span class="severity-pill severity-low">Session Authorized</span></td>
                    </tr>
                    <tr>
                      <td>Today 18:14:02</td>
                      <td>Alex Vance (SOC Lead)</td>
                      <td>FIDO2 Hardware Token Touch</td>
                      <td>10.0.2.14 (SOC Battle Station)</td>
                      <td>Hardened Linux Workstation</td>
                      <td><span class="severity-pill severity-low">Session Authorized</span></td>
                    </tr>
                    <tr>
                      <td>Today 17:48:50</td>
                      <td>Sarah Jenkins (Client Dir)</td>
                      <td>FIDO2 Hardware Token Touch</td>
                      <td>10.0.4.88 (Apex Corporate HQ)</td>
                      <td>Encrypted macOS Tahoe Node</td>
                      <td><span class="severity-pill severity-low">Session Authorized</span></td>
                    </tr>
                    <tr>
                      <td>Today 16:12:10</td>
                      <td>Unknown Attacker</td>
                      <td>Bruteforce SSH Key Injection</td>
                      <td>194.26.29.112 (Tor Exit Relay)</td>
                      <td>No Attestation Certificate</td>
                      <td><span class="severity-pill severity-critical">Blocked & Logged</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- SECTION 8: EMERGENCY ACCESS REVOCATION CONTROLS -->
          <section class="dash-section" aria-label="Emergency Access Controls">
            <div class="dash-panel">
              <div class="dash-panel-header">
                <div>
                  <h3 class="dash-panel-title"><span>🚨</span> Emergency Session Revocation & Access Quarantine</h3>
                  <div style="font-size: 0.825rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Immediate enterprise-wide identity invalidation controls
                  </div>
                </div>
                <button type="button" class="btn btn-secondary btn-sm dash-action-btn">Test Identity Revocation</button>
              </div>
              <div class="dash-grid-3">
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--warning); display: block; margin-bottom: 0.25rem;">Terminate All Active Sessions</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Invalidate all active JWT and OAuth tokens instantly</span>
                </button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--primary); display: block; margin-bottom: 0.25rem;">Force Hardware Re-Auth</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Require physical key touch on all active terminals</span>
                </button>
                <button type="button" class="btn btn-outline btn-sm dash-action-btn" style="padding: 1rem; text-align: left; height: auto;">
                  <strong style="color: var(--danger); display: block; margin-bottom: 0.25rem;">Lock Non-Essential Clearances</strong>
                  <span style="font-size: 0.775rem; color: var(--text-muted);">Restrict console access to Level-3 Command only</span>
                </button>
              </div>
            </div>
          </section>
        </div>
"""

print("All 7 subpage modules defined successfully.")

