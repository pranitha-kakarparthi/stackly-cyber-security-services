import re

BACKDROPS = {
    'index.html': {
        'target': '<section class="hero-stage" aria-label="Autonomous Cyber Defense Stage">',
        'insert': '''<section class="hero-stage" aria-label="Autonomous Cyber Defense Stage">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>SEC_OPS // 24.7.365</span>
            <span class="hud-sep">::</span>
            <span>ZERO_TRUST: ENFORCED</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>DEFENSE_MESH // 99.98% INTERCEPTION</span>
            <span class="hud-sep">::</span>
            <span>LATENCY: 0.8MS</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/about.html': {
        'target': '<section class="page-hero" aria-label="About Stackly Security Hero">',
        'insert': '''<section class="page-hero" aria-label="About Stackly Security Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>INTEL_DIRECTORATE // EST. 2018</span>
            <span class="hud-sep">::</span>
            <span>SPECIALISTS: 50+</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>ASSETS_DEFENDED // $8B+ ENTERPRISE VALUE</span>
            <span class="hud-sep">::</span>
            <span>GLOBAL_MESH</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/services.html': {
        'target': '<section class="page-hero" aria-label="Services Hero">',
        'insert': '''<section class="page-hero" aria-label="Services Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>DEFENSE_PORTFOLIO // 6 CORE PRACTICES</span>
            <span class="hud-sep">::</span>
            <span>FULL_SPECTRUM</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>SLA_UPTIME // 99.99% MULTI-CLOUD</span>
            <span class="hud-sep">::</span>
            <span>THREAT_INDEX: 0</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/pricing.html': {
        'target': '<section class="page-hero" aria-label="Pricing Hero">',
        'insert': '''<section class="page-hero" aria-label="Pricing Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>ENTERPRISE_TIERS // PREDICTABLE INVESTMENT</span>
            <span class="hud-sep">::</span>
            <span>TRANSPARENT</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>FINANCIAL_SLA // 99.99% GUARANTEE</span>
            <span class="hud-sep">::</span>
            <span>ZERO_INGESTION_FEES</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/contact.html': {
        'target': '<section class="page-hero" aria-label="Contact Hero">',
        'insert': '''<section class="page-hero" aria-label="Contact Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>DISPATCH_CHANNEL // 24/7 ENCRYPTED HOTLINE</span>
            <span class="hud-sep">::</span>
            <span>STANDBY</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>SLA_RESPONSE // &lt; 15 MIN GUARANTEED</span>
            <span class="hud-sep">::</span>
            <span>COMMAND_OPS</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-soc.html': {
        'target': '<section class="page-hero" aria-label="Managed SOC Hero">',
        'insert': '''<section class="page-hero" aria-label="Managed SOC Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>SIEM_CORRELATION // 4.8M EPS INGESTION</span>
            <span class="hud-sep">::</span>
            <span>ACTIVE</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>MTTD // &lt; 3 MINS • TIER 1-3 ANALYSTS</span>
            <span class="hud-sep">::</span>
            <span>SOC_DIRECTORATE</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-pentest.html': {
        'target': '<section class="page-hero" aria-label="Penetration Testing Hero">',
        'insert': '''<section class="page-hero" aria-label="Penetration Testing Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>OFFENSIVE_OPS // MITRE ATT&amp;CK MAPPING</span>
            <span class="hud-sep">::</span>
            <span>ARMED</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>ZERO_DAY_POC // 100% NON-DESTRUCTIVE</span>
            <span class="hud-sep">::</span>
            <span>RED_TEAM_SENTINEL</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-cloud-security.html': {
        'target': '<section class="page-hero" aria-label="Cloud Security Hero">',
        'insert': '''<section class="page-hero" aria-label="Cloud Security Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>MULTI_CLOUD_FABRIC // AWS • AZURE • GCP</span>
            <span class="hud-sep">::</span>
            <span>SECURED</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>ZTNA_MICROSEGMENTATION // REAL-TIME POSTURE</span>
            <span class="hud-sep">::</span>
            <span>CSPM_CIEM</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-incident-response.html': {
        'target': '<section class="page-hero" aria-label="Incident Response Hero">',
        'insert': '''<section class="page-hero" aria-label="Incident Response Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot" style="background: #ef4444; box-shadow: 0 0 8px #ef4444;"></span>
            <span>INCIDENT_COMMAND // 1-HR EMERGENCY SLA</span>
            <span class="hud-sep">::</span>
            <span>ARMED</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>CONTAINMENT_TIME // &lt; 15 MIN ACTIVE TRIAGE</span>
            <span class="hud-sep">::</span>
            <span>CRISIS_DIRECTORATE</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#ef4444" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-vulnerability-management.html': {
        'target': '<section class="page-hero" aria-label="Vulnerability Management Hero">',
        'insert': '''<section class="page-hero" aria-label="Vulnerability Management Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>CONTINUOUS_CVE_RADAR // EPSS AI SCORING</span>
            <span class="hud-sep">::</span>
            <span>TRACKING</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>SURFACE_EXPOSURES // 0 CRITICAL REMAINING</span>
            <span class="hud-sep">::</span>
            <span>AUTOMATED_HARVESTER</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    },
    'pages/service-compliance.html': {
        'target': '<section class="page-hero" aria-label="ISO 27001 Compliance Hero">',
        'insert': '''<section class="page-hero" aria-label="ISO 27001 Compliance Hero">
        <!-- Cyber Background Technical Backdrop & HUD Telemetry -->
        <div class="hero-cyber-backdrop" aria-hidden="true">
          <div class="cyber-hud-corner corner-tl"></div>
          <div class="cyber-hud-corner corner-tr"></div>
          <div class="cyber-hud-corner corner-bl"></div>
          <div class="cyber-hud-corner corner-br"></div>
          <div class="cyber-hud-telemetry hud-left">
            <span class="hud-pulse-dot"></span>
            <span>ISO_27001:2022 // 93 ANNEX A CONTROLS</span>
            <span class="hud-sep">::</span>
            <span>SYNCED</span>
          </div>
          <div class="cyber-hud-telemetry hud-right">
            <span>EVIDENCE_VAULT // 100% AUDIT READINESS</span>
            <span class="hud-sep">::</span>
            <span>CRYPTOGRAPHIC_INTEGRITY</span>
          </div>
          <svg class="cyber-backdrop-svg" viewBox="0 0 1440 480" fill="none" preserveAspectRatio="none">
            <line x1="80" y1="40" x2="1360" y2="40" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <line x1="80" y1="440" x2="1360" y2="440" stroke="rgba(122, 16, 40, 0.12)" stroke-width="1" stroke-dasharray="6 6" />
            <circle cx="120" cy="40" r="3" fill="#D97706" opacity="0.6" />
            <circle cx="720" cy="40" r="2.5" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="40" r="3" fill="#10B981" opacity="0.6" />
            <circle cx="120" cy="440" r="3" fill="#7A1028" opacity="0.5" />
            <circle cx="1320" cy="440" r="3" fill="#D97706" opacity="0.6" />
          </svg>
        </div>'''
    }
}

for path, info in BACKDROPS.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'hero-cyber-backdrop' in content:
        print(f"Skipping {path}, backdrop already present")
        continue

    if info['target'] in content:
        content = content.replace(info['target'], info['insert'], 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Injected hero-cyber-backdrop into {path}")
    else:
        print(f"[WARN] Target not found in {path}")

