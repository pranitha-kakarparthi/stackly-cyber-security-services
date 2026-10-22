import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace :root
new_root = """:root {
  /* Complete SHIELDA-Inspired Luxury Palette: Warm Ivory & Velvet Wine */
  --bg-primary: #FAF7EE;
  --bg-secondary: #F3EFE0;
  --bg-tertiary: #EBE5D3;
  --surface-card: #FFFFFF;
  --surface-card-hover: #FFFFFF;
  --surface-elevated: #FFFFFF;
  --surface-glass: rgba(255, 255, 255, 0.88);
  --surface-dark: #3A010E;
  --surface-dark-glass: rgba(58, 1, 14, 0.75);
  
  /* Primary Brand Color: Deep Velvet Wine Crimson */
  --primary: #7A1028;
  --primary-hover: #5A0A1D;
  --primary-light: #FBECEF;
  --primary-text: #FFFFFF;
  --primary-glow: rgba(122, 16, 40, 0.25);
  
  /* Secondary Brand Color: Berry Rosewood Burgundy */
  --secondary: #9E2A44;
  --secondary-hover: #821F35;
  --secondary-light: #FDF2F4;
  --secondary-text: #FFFFFF;
  --secondary-glow: rgba(158, 42, 68, 0.22);
  
  /* Accent Color: Golden Amber / Warm Ochre */
  --accent: #D97706;
  --accent-hover: #B45309;
  --accent-text: #3A010E;
  --accent-glow: rgba(217, 119, 6, 0.25);

  /* Tactical & Status Colors */
  --warning: #D97706;
  --warning-bg: rgba(217, 119, 6, 0.12);
  --danger: #BE123C;
  --danger-bg: rgba(190, 18, 60, 0.12);
  --success: #047857;
  --success-bg: rgba(4, 120, 87, 0.12);

  /* Text Colors (High Contrast WCAG AAA Compliant) */
  --text-primary: #33050F;
  --text-secondary: #553B42;
  --text-muted: #7E646B;
  --text-inverse: #FAF7EE;

  /* Borders & Gradients */
  --border-subtle: rgba(58, 1, 14, 0.10);
  --border-cyber: rgba(122, 16, 40, 0.25);
  --border-secondary: rgba(158, 42, 68, 0.25);
  --border-focus: #7A1028;
  --gradient-iridescent: linear-gradient(135deg, #7A1028 0%, #9E2A44 50%, #D97706 100%);
  --gradient-pill-btn: linear-gradient(135deg, #7A1028 0%, #8E1734 50%, #A31E3E 100%);
  --gradient-pill-btn-hover: linear-gradient(135deg, #5A0A1D 0%, #701026 50%, #851631 100%);
  --gradient-glass-pill: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(250, 247, 238, 0.8) 100%);
  --gradient-cyber: linear-gradient(135deg, #7A1028 0%, #9E2A44 50%, #D97706 100%);
  --gradient-shield: linear-gradient(135deg, #7A1028 0%, #3A010E 100%);
  --gradient-dark: linear-gradient(180deg, #3A010E 0%, #200007 100%);
  --gradient-card: linear-gradient(145deg, #FFFFFF 0%, #FAF7EE 100%);
  --glow-box: 0 10px 30px rgba(122, 16, 40, 0.12);

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;

  /* Spacing */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  /* Transitions */
  --transition-fast: 0.18s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-smooth: 0.45s cubic-bezier(0.16, 1, 0.3, 1);
}"""

css = re.sub(r':root\s*\{[^}]+\}', new_root, css, count=1)

# 2. Update color-scheme
css = css.replace('color-scheme: dark;', 'color-scheme: light;')

# 3. Update body::before background
old_body_before = """body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: 
    radial-gradient(circle at 50% -10%, rgba(94, 234, 212, 0.09) 0%, transparent 65%),
    radial-gradient(circle at 85% 25%, rgba(167, 139, 250, 0.08) 0%, transparent 55%),
    radial-gradient(circle at 15% 75%, rgba(56, 189, 248, 0.07) 0%, transparent 50%),
    linear-gradient(rgba(255, 255, 255, 0.016) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.016) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px;
  background-position: 0 0, 0 0, 0 0, -1px -1px, -1px -1px;
  pointer-events: none;
  z-index: -1;
}"""

new_body_before = """body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: 
    radial-gradient(circle at 50% -10%, rgba(122, 16, 40, 0.05) 0%, transparent 65%),
    radial-gradient(circle at 85% 25%, rgba(158, 42, 68, 0.04) 0%, transparent 55%),
    radial-gradient(circle at 15% 75%, rgba(217, 119, 6, 0.035) 0%, transparent 50%),
    linear-gradient(rgba(58, 1, 14, 0.018) 1px, transparent 1px),
    linear-gradient(90deg, rgba(58, 1, 14, 0.018) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px;
  background-position: 0 0, 0 0, 0 0, -1px -1px, -1px -1px;
  pointer-events: none;
  z-index: -1;
}"""

if old_body_before in css:
    css = css.replace(old_body_before, new_body_before)
else:
    print("WARNING: old_body_before not exact match")

# 4. Loader colors
css = css.replace('background: #030508;', 'background: #FAF7EE;')
css = css.replace('border-top: 3px solid var(--primary);', 'border-top: 3px solid var(--primary);')

# 5. Navbar floating pill
css = css.replace('background: rgba(8, 12, 22, 0.72);', 'background: rgba(250, 247, 238, 0.88);')
css = css.replace('background: rgba(8, 12, 22, 0.9);', 'background: rgba(250, 247, 238, 0.96);')
css = css.replace('border: 1px solid rgba(255, 255, 255, 0.12);', 'border: 1px solid rgba(58, 1, 14, 0.10);')
css = css.replace('box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.15);',
                  'box-shadow: 0 12px 36px rgba(58, 1, 14, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.8);')
css = css.replace('box-shadow: 0 16px 42px rgba(0, 0, 0, 0.75), 0 0 24px rgba(94, 234, 212, 0.15);',
                  'box-shadow: 0 16px 42px rgba(58, 1, 14, 0.08), 0 0 24px rgba(122, 16, 40, 0.05);')

# Dropdown menu
css = css.replace('background: rgba(11, 17, 30, 0.95);', 'background: rgba(250, 247, 238, 0.98);')
css = css.replace('box-shadow: 0 18px 45px rgba(0, 0, 0, 0.8), 0 0 25px rgba(94, 234, 212, 0.12);',
                  'box-shadow: 0 18px 45px rgba(58, 1, 14, 0.10), 0 0 25px rgba(122, 16, 40, 0.05);')
css = css.replace('border: 1px solid rgba(94, 234, 212, 0.28);', 'border: 1px solid rgba(122, 16, 40, 0.2);')

# Mobile drawer
css = css.replace('background: rgba(3, 5, 8, 0.96);', 'background: rgba(250, 247, 238, 0.98);')

# 6. Hero typography gradients & shadows
css = css.replace('background: linear-gradient(135deg, #a7f3d0 0%, #5eead4 40%, #38bdf8 100%);',
                  'background: linear-gradient(135deg, #7A1028 0%, #A61C40 50%, #D97706 100%);')
css = css.replace('background: linear-gradient(135deg, #f5d0fe 0%, #c084fc 40%, #a78bfa 100%);',
                  'background: linear-gradient(135deg, #9E2A44 0%, #C2335A 50%, #F59E0B 100%);')
css = css.replace('background: linear-gradient(135deg, #00f076 0%, #06b6d4 50%, #9333ea 100%);',
                  'background: linear-gradient(135deg, #7A1028 0%, #A61C40 50%, #D97706 100%);')

# Drop shadows for kinetic titles
css = css.replace('filter: drop-shadow(0 0 30px rgba(94, 234, 212, 0.7)) drop-shadow(0 4px 18px rgba(0, 0, 0, 0.98));',
                  'filter: drop-shadow(0 4px 20px rgba(58, 1, 14, 0.45));')
css = css.replace('filter: drop-shadow(0 0 30px rgba(167, 139, 250, 0.7)) drop-shadow(0 4px 18px rgba(0, 0, 0, 0.98));',
                  'filter: drop-shadow(0 4px 20px rgba(158, 42, 68, 0.45));')

# 7. Hero Sentinel ambient glow
css = css.replace('background: radial-gradient(ellipse at center, rgba(94, 234, 212, 0.16) 0%, rgba(167, 139, 250, 0.1) 50%, transparent 75%);',
                  'background: radial-gradient(ellipse at center, rgba(122, 16, 40, 0.15) 0%, rgba(217, 119, 6, 0.10) 50%, transparent 75%);')

# 8. Card shadows and icon wraps
css = css.replace('box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6), 0 0 25px rgba(0, 240, 118, 0.15);',
                  'box-shadow: 0 16px 36px rgba(58, 1, 14, 0.08), 0 0 25px rgba(122, 16, 40, 0.05);')
css = css.replace('box-shadow: 0 18px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 240, 118, 0.15);',
                  'box-shadow: 0 18px 40px rgba(58, 1, 14, 0.08), 0 0 20px rgba(122, 16, 40, 0.05);')
css = css.replace('box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(0, 240, 118, 0.12);',
                  'box-shadow: 0 20px 50px rgba(58, 1, 14, 0.08), 0 0 30px rgba(122, 16, 40, 0.05);')
css = css.replace('box-shadow: 0 14px 34px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 240, 118, 0.12);',
                  'box-shadow: 0 14px 34px rgba(58, 1, 14, 0.08), 0 0 20px rgba(122, 16, 40, 0.05);')
css = css.replace('box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(0, 240, 118, 0.2);',
                  'box-shadow: 0 20px 45px rgba(58, 1, 14, 0.08), 0 0 30px rgba(122, 16, 40, 0.05);')
css = css.replace('box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 25px rgba(0, 240, 118, 0.12);',
                  'box-shadow: 0 20px 50px rgba(58, 1, 14, 0.08), 0 0 25px rgba(122, 16, 40, 0.05);')

# Replace icon wrap green backgrounds with wine
css = css.replace('background: rgba(0, 240, 118, 0.1);', 'background: rgba(122, 16, 40, 0.08);')
css = css.replace('border: 1px solid rgba(0, 240, 118, 0.25);', 'border: 1px solid rgba(122, 16, 40, 0.2);')
css = css.replace('background: rgba(0, 240, 118, 0.18);', 'background: rgba(122, 16, 40, 0.14);')
css = css.replace('background: rgba(0, 240, 118, 0.08);', 'background: rgba(122, 16, 40, 0.06);')
css = css.replace('background: rgba(0, 240, 118, 0.15);', 'background: rgba(122, 16, 40, 0.10);')
css = css.replace('border: 1px solid rgba(0, 240, 118, 0.4);', 'border: 1px solid rgba(122, 16, 40, 0.3);')

# 9. Update footer
css = css.replace('background: #04070e;', """background: #250109;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  color: #FAF7EE;""")
css = css.replace('.footer-heading {\\n  font-size: 1rem;\\n  font-weight: 700;\\n  color: var(--text-primary);',
                  '.footer-heading {\\n  font-size: 1rem;\\n  font-weight: 700;\\n  color: #FAF7EE;')
css = css.replace('.footer-tagline {\\n  font-size: 0.925rem;\\n  color: var(--text-muted);',
                  '.footer-tagline {\\n  font-size: 0.925rem;\\n  color: #D4BFC4;')
css = css.replace('.footer-link {\\n  color: var(--text-muted);',
                  '.footer-link {\\n  color: #D4BFC4;')
css = css.replace('.footer-link:hover {\\n  color: var(--primary);',
                  '.footer-link:hover {\\n  color: #F5A623;')

# 10. Update auth banner side
css = css.replace('background: linear-gradient(145deg, #0a1122 0%, #060a14 100%);',
                  'background: linear-gradient(145deg, #3A010E 0%, #200007 100%);')
css = css.replace('background: rgba(13, 21, 39, 0.85);', 'background: rgba(58, 1, 14, 0.85);')

# 11. Add Back to Top button CSS & Human Face alignment rules if not already present
back_to_top_css = """
/* ==========================================================================
   BACK TO TOP FLOATING BUTTON (SHIELDA THEME)
   ========================================================================== */
.back-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 48px;
  height: 48px;
  border-radius: var(--radius-full);
  background: var(--primary);
  color: #FFFFFF;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  box-shadow: 0 8px 24px rgba(58, 1, 14, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 9999;
  opacity: 0;
  visibility: hidden;
  transform: translateY(16px);
  transition: all var(--transition-normal);
}

.back-to-top.visible {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.back-to-top:hover {
  background: var(--primary-hover);
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(122, 16, 40, 0.45);
}

.back-to-top svg {
  transition: transform var(--transition-fast);
}

.back-to-top:hover svg {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .back-to-top {
    bottom: 1.25rem;
    right: 1.25rem;
    width: 42px;
    height: 42px;
  }
}

/* ==========================================================================
   HUMAN FACES POSITIONING & RESPONSIVE FRAMING
   ========================================================================== */
.person-image-wrap img,
.hero-visual-card img,
.tilt-card img,
.testimonial-avatar,
img[src*="chief-information-security-officer"],
img[src*="cyber-security-analyst"],
img[src*="penetration-tester"],
img[src*="cloud-security-architect"],
img[src*="incident-response-commander"],
img[src*="threat-intelligence-specialist"],
img[src*="vulnerability-assessment-engineer"],
img[src*="security-compliance-auditor"],
img[src*="enterprise-client"] {
  object-fit: cover !important;
  object-position: center 20% !important;
}

.person-card:hover .person-image-wrap img {
  transform: scale(1.03) !important;
  transform-origin: center 25% !important;
}
"""

if '.back-to-top' not in css:
    css += back_to_top_css

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated assets/css/style.css successfully.")

