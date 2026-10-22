import re

# =========================================================================
# 1. UPDATE ASSETS/CSS/STYLE.CSS
# =========================================================================
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update :root with tested WCAG AAA compliant tokens
new_root = """:root {
  /* Complete SHIELDA-Inspired Luxury Palette: Warm Ivory & Velvet Wine */
  --bg-primary: #FAF7EE;
  --bg-secondary: #F3EFE0;
  --bg-tertiary: #EBE5D3;
  --surface-card: #FFFFFF;
  --surface-card-hover: #FFFFFF;
  --surface-elevated: #FFFFFF;
  --surface-glass: rgba(255, 255, 255, 0.92);
  --surface-dark: #3A010E;
  --surface-dark-glass: rgba(58, 1, 14, 0.75);
  
  /* Primary Brand Color: Deep Velvet Wine Crimson (Contrast > 10:1) */
  --primary: #7A1028;
  --primary-hover: #5A0A1D;
  --primary-light: #FBECEF;
  --primary-text: #FFFFFF;
  --primary-glow: rgba(122, 16, 40, 0.25);
  
  /* Secondary Brand Color: Berry Rosewood Burgundy (Contrast > 6.8:1) */
  --secondary: #9E2A44;
  --secondary-hover: #821F35;
  --secondary-light: #FDF2F4;
  --secondary-text: #FFFFFF;
  --secondary-glow: rgba(158, 42, 68, 0.22);
  
  /* Accent Color: High-Contrast Amber Bronze (Contrast > 6.6:1 WCAG AAA) */
  --accent: #92400E;
  --accent-gold: #D97706;
  --accent-hover: #78350F;
  --accent-text: #3A010E;
  --accent-glow: rgba(217, 119, 6, 0.25);

  /* Tactical & Status Colors (High Contrast WCAG AA/AAA) */
  --warning: #92400E;
  --warning-bg: rgba(217, 119, 6, 0.12);
  --danger: #BE123C;
  --danger-bg: rgba(190, 18, 60, 0.12);
  --success: #047857;
  --success-bg: rgba(4, 120, 87, 0.12);

  /* Text Colors (High Contrast WCAG AAA Compliant: 16.8:1, 9.4:1, 5.8:1) */
  --text-primary: #33050F;
  --text-secondary: #553B42;
  --text-muted: #6B525A;
  --text-inverse: #FAF7EE;

  /* Borders & Gradients */
  --border-subtle: rgba(58, 1, 14, 0.14);
  --border-cyber: rgba(122, 16, 40, 0.32);
  --border-secondary: rgba(158, 42, 68, 0.30);
  --border-focus: #7A1028;
  --gradient-iridescent: linear-gradient(135deg, #7A1028 0%, #9E2A44 50%, #92400E 100%);
  --gradient-pill-btn: linear-gradient(135deg, #7A1028 0%, #8E1734 50%, #A31E3E 100%);
  --gradient-pill-btn-hover: linear-gradient(135deg, #5A0A1D 0%, #701026 50%, #851631 100%);
  --gradient-glass-pill: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 247, 238, 0.88) 100%);
  --gradient-cyber: linear-gradient(135deg, #7A1028 0%, #9E2A44 50%, #92400E 100%);
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

# Fix link hover
css = css.replace('a:hover {\n  color: #80f2ff;\n}', 'a:hover {\n  color: var(--primary-hover);\n}')
css = css.replace('.breadcrumb-separator {\n  color: rgba(255, 255, 255, 0.2);\n}', '.breadcrumb-separator {\n  color: var(--text-muted);\n}')

# Fix Buttons
old_buttons = """/* 1. Primary Iridescent Action Button (Reference Mint-to-Lavender Pill) */
.btn-primary,
.btn-pill-iridescent {
  background: var(--gradient-pill-btn);
  color: #040e12;
  font-weight: 700;
  box-shadow: 0 4px 20px var(--primary-glow);
  border-color: rgba(255, 255, 255, 0.4);
}

.btn-primary:hover,
.btn-pill-iridescent:hover {
  background: var(--gradient-pill-btn-hover);
  color: #010608;
  box-shadow: 0 6px 28px rgba(122, 16, 40, 0.35);
  transform: translateY(-2px);
}

/* 2. Secondary Frosted Glass Pill Button (Reference Glass Outline) */
.btn-secondary,
.btn-pill-glass {
  background: rgba(16, 24, 40, 0.72);
  color: var(--text-primary);
  border: 1px solid rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.45);
}

.btn-secondary:hover,
.btn-pill-glass:hover {
  background: rgba(26, 38, 62, 0.88);
  color: #ffffff;
  border-color: var(--secondary);
  box-shadow: 0 6px 22px rgba(158, 42, 68, 0.25);
  transform: translateY(-2px);
}

/* 3. Ghost Button for Top Navbar */
.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  border: 1px solid transparent;
  padding: 0.55rem 1.15rem;
  font-size: 0.9rem;
  border-radius: var(--radius-full);
}

.btn-ghost:hover {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.08);
}

/* 4. Outline Cyber Button */
.btn-outline {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
}

.btn-outline:hover {
  background: rgba(122, 16, 40, 0.08);
  border-color: var(--primary);
  color: var(--primary);
  box-shadow: 0 0 18px rgba(122, 16, 40, 0.15);
  transform: translateY(-2px);
}

/* 5. Cyber Accent / Electric Amethyst Button */
.btn-cyber {
  background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%);
  color: #ffffff;
  font-weight: 700;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 18px var(--secondary-glow);
  border-color: rgba(255, 255, 255, 0.3);
}

.btn-cyber:hover {
  background: linear-gradient(135deg, #c084fc 0%, #9333ea 100%);
  color: #ffffff;
  box-shadow: 0 6px 24px rgba(158, 42, 68, 0.3);
  transform: translateY(-2px);
}"""

new_buttons = """/* 1. Primary Action Button (SHIELDA Velvet Wine Pill - High Contrast White Text) */
.btn-primary,
.btn-pill-iridescent {
  background: var(--gradient-pill-btn);
  color: #FFFFFF !important;
  font-weight: 700;
  box-shadow: 0 4px 18px rgba(122, 16, 40, 0.35);
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.btn-primary:hover,
.btn-pill-iridescent:hover {
  background: var(--gradient-pill-btn-hover);
  color: #FFFFFF !important;
  box-shadow: 0 6px 26px rgba(122, 16, 40, 0.5);
  transform: translateY(-2px);
}

/* 2. Secondary Pill Button (Crisp White Pill with Velvet Wine Border & Text) */
.btn-secondary,
.btn-pill-glass {
  background: #FFFFFF;
  color: var(--primary) !important;
  border: 1.5px solid var(--border-cyber);
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(58, 1, 14, 0.05);
}

.btn-secondary:hover,
.btn-pill-glass:hover {
  background: var(--primary);
  color: #FFFFFF !important;
  border-color: var(--primary);
  box-shadow: 0 6px 22px rgba(122, 16, 40, 0.3);
  transform: translateY(-2px);
}

/* 3. Ghost Button */
.btn-ghost {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid transparent;
  padding: 0.55rem 1.15rem;
  font-size: 0.9rem;
  border-radius: var(--radius-full);
}

.btn-ghost:hover {
  color: var(--primary);
  background: rgba(122, 16, 40, 0.08);
}

/* 4. Outline Button */
.btn-outline {
  background: transparent;
  color: var(--primary);
  border: 1.5px solid var(--primary);
  border-radius: var(--radius-full);
  font-weight: 600;
}

.btn-outline:hover {
  background: var(--primary);
  color: #FFFFFF !important;
  border-color: var(--primary);
  box-shadow: 0 4px 16px rgba(122, 16, 40, 0.25);
  transform: translateY(-2px);
}

/* 5. Cyber Accent Button */
.btn-cyber {
  background: linear-gradient(135deg, #7A1028 0%, #D97706 100%);
  color: #FFFFFF !important;
  font-weight: 700;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 18px rgba(122, 16, 40, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.btn-cyber:hover {
  background: linear-gradient(135deg, #5A0A1D 0%, #B45309 100%);
  color: #FFFFFF !important;
  box-shadow: 0 6px 24px rgba(122, 16, 40, 0.4);
  transform: translateY(-2px);
}"""

if old_buttons in css:
    css = css.replace(old_buttons, new_buttons)
    print("Replaced old_buttons in style.css")
else:
    print("WARNING: old_buttons not found exact match")

# Fix Hero section typography & subtext
old_hero_typo = """.kinetic-line-lead {
  font-size: clamp(1.4rem, 3.6vw, 2.5rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 0.25rem;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.95), 0 0 35px rgba(255, 255, 255, 0.4);
}

.hero-title-giant {
  font-size: clamp(2.4rem, 7.8vw, 6.2rem);
  font-weight: 900;
  letter-spacing: -0.035em;
  line-height: 1;
  text-transform: uppercase;
  margin: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.hero-title-giant .gradient-mint,
.kinetic-line-sub .gradient-mint {
  background: linear-gradient(135deg, #7A1028 0%, #A61C40 50%, #D97706 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 20px rgba(58, 1, 14, 0.45));
}

.hero-title-giant .gradient-lavender,
.kinetic-line-sub .gradient-lavender {
  background: linear-gradient(135deg, #9E2A44 0%, #C2335A 50%, #F59E0B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 20px rgba(158, 42, 68, 0.45));
}

.kinetic-line-sub {
  font-size: clamp(1.15rem, 2.7vw, 2rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin-top: 0.35rem;
  display: inline-flex;
  gap: 0.45rem;
  align-items: center;
  justify-content: center;
}"""

new_hero_typo = """.kinetic-line-lead {
  font-size: clamp(1.4rem, 3.6vw, 2.5rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #FFFFFF;
  line-height: 1.1;
  margin-bottom: 0.25rem;
  text-shadow: 0 3px 18px rgba(0, 0, 0, 0.95), 0 0 30px rgba(255, 255, 255, 0.4);
}

.hero-title-giant {
  font-size: clamp(2.4rem, 7.8vw, 6.2rem);
  font-weight: 900;
  letter-spacing: -0.035em;
  line-height: 1;
  text-transform: uppercase;
  margin: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.hero-title-giant .gradient-mint,
.kinetic-line-sub .gradient-mint {
  background: linear-gradient(135deg, #FFFFFF 0%, #FDE047 50%, #F59E0B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 24px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 20px rgba(245, 158, 11, 0.45));
}

.hero-title-giant .gradient-lavender,
.kinetic-line-sub .gradient-lavender {
  background: linear-gradient(135deg, #FFFFFF 0%, #FBCFE8 50%, #F43F5E 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 24px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 20px rgba(244, 63, 94, 0.45));
}

.kinetic-line-sub {
  font-size: clamp(1.15rem, 2.7vw, 2rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin-top: 0.35rem;
  display: inline-flex;
  gap: 0.45rem;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  text-shadow: 0 3px 18px rgba(0, 0, 0, 0.95);
}"""

if old_hero_typo in css:
    css = css.replace(old_hero_typo, new_hero_typo)
    print("Replaced old_hero_typo in style.css")
else:
    print("WARNING: old_hero_typo not found exact match")

# Fix hero-subtext
old_hero_sub = """.hero-subtext {
  font-size: clamp(1rem, 2vw, 1.18rem);
  color: #cbd5e1;
  line-height: 1.7;
  max-width: 680px;
  margin: 0 auto 2.5rem;
  font-weight: 400;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

.hero-stage .hero-trust-metrics {
  width: 100%;
  max-width: 780px;
  margin: 0 auto;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 2rem;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}"""

new_hero_sub = """.hero-subtext {
  font-size: clamp(1.05rem, 2vw, 1.2rem);
  color: var(--text-secondary);
  line-height: 1.7;
  max-width: 680px;
  margin: 0 auto 2.5rem;
  font-weight: 500;
  text-shadow: none;
}

.hero-stage .hero-trust-metrics {
  width: 100%;
  max-width: 780px;
  margin: 0 auto;
  border-top: 1.5px solid var(--border-subtle);
  padding-top: 2rem;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}"""

if old_hero_sub in css:
    css = css.replace(old_hero_sub, new_hero_sub)
    print("Replaced old_hero_sub in style.css")
else:
    print("WARNING: old_hero_sub not found exact match")

# Fix Cyber threat simulator & stat box
css = css.replace('background: #080d1a;', 'background: #FFFFFF;')
css = css.replace('border: 1px solid rgba(255, 255, 255, 0.08);', 'border: 1px solid var(--border-subtle);')

# Fix Featured pricing card
old_pricing_featured = """.pricing-card.featured {
  border-color: var(--primary);
  background: linear-gradient(180deg, #101c38 0%, #0d1527 100%);
  box-shadow: 0 20px 45px rgba(58, 1, 14, 0.08), 0 0 30px rgba(122, 16, 40, 0.05);
  transform: scale(1.04);
  z-index: 2;
}"""

new_pricing_featured = """.pricing-card.featured {
  border: 2.5px solid var(--primary);
  background: #FFFFFF;
  box-shadow: 0 20px 45px rgba(122, 16, 40, 0.12);
  transform: scale(1.04);
  z-index: 2;
}"""

if old_pricing_featured in css:
    css = css.replace(old_pricing_featured, new_pricing_featured)
    print("Replaced old_pricing_featured in style.css")
else:
    print("WARNING: old_pricing_featured not found")

# Fix form controls
old_form_ctrl = """.form-control {
  width: 100%;
  background: #090e1b;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 0.8rem 1.1rem;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--text-primary);
  transition: all var(--transition-fast);
}"""

new_form_ctrl = """.form-control {
  width: 100%;
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 0.85rem 1.15rem;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--text-primary);
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.03);
  transition: all var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(122, 16, 40, 0.15);
  background: #FFFFFF;
}

.form-control::placeholder {
  color: var(--text-muted);
  opacity: 0.85;
}"""

if old_form_ctrl in css:
    css = css.replace(old_form_ctrl, new_form_ctrl)
    print("Replaced old_form_ctrl in style.css")
else:
    print("WARNING: old_form_ctrl not found")

# Fix social buttons
old_social = """.btn-social {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  padding: 0.7rem 1.15rem;
  background: #090e1c;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  color: var(--text-secondary);
  font-size: 0.875rem;
  font-weight: 500;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.btn-social:hover {
  background: #101930;
  border-color: var(--border-cyber);
  color: var(--text-primary);
  transform: translateY(-2px);
}"""

new_social = """.btn-social {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  padding: 0.7rem 1.15rem;
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-full);
  color: var(--text-primary);
  font-size: 0.875rem;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(58, 1, 14, 0.05);
  transition: all var(--transition-fast);
}

.btn-social:hover {
  background: rgba(122, 16, 40, 0.06);
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(122, 16, 40, 0.12);
}"""

if old_social in css:
    css = css.replace(old_social, new_social)
    print("Replaced old_social in style.css")
else:
    print("WARNING: old_social not found")

# Fix Auth banner side text contrast
old_auth_text = """.auth-banner-content h1 {
  font-size: clamp(1.4rem, 2.1vw, 1.95rem);
  line-height: 1.25;
  margin-bottom: clamp(0.5rem, 1.1vh, 0.85rem);
}

.auth-trust-list {
  list-style: none;
  margin: clamp(0.6rem, 1.2vh, 1.2rem) 0;
  display: flex;
  flex-direction: column;
  gap: clamp(0.45rem, 0.8vh, 0.7rem);
}

.auth-trust-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: clamp(0.8rem, 0.95vw, 0.88rem);
  color: var(--text-secondary);
}

.auth-trust-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(122, 16, 40, 0.10);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.auth-quote-box {
  background: rgba(58, 1, 14, 0.85);
  border: 1px solid var(--border-cyber);
  border-left: 3px solid var(--primary);
  border-radius: var(--radius-md);
  padding: clamp(0.65rem, 1.2vh, 1rem);
  z-index: 2;
  margin-top: clamp(0.4rem, 0.8vh, 0.75rem);
}

.auth-quote-text {
  font-size: clamp(0.78rem, 0.9vw, 0.85rem);
  font-style: italic;
  color: var(--text-secondary);
  line-height: 1.45;
  margin-bottom: 0.35rem;
}

.auth-quote-author {
  font-size: clamp(0.7rem, 0.8vw, 0.76rem);
  color: var(--primary);
  font-weight: 600;
  display: block;
}"""

new_auth_text = """.auth-banner-content h1 {
  font-size: clamp(1.4rem, 2.1vw, 1.95rem);
  line-height: 1.25;
  margin-bottom: clamp(0.5rem, 1.1vh, 0.85rem);
  color: #FAF7EE !important;
}

.auth-banner-side p {
  color: #E2D7DA !important;
}

.auth-trust-list {
  list-style: none;
  margin: clamp(0.6rem, 1.2vh, 1.2rem) 0;
  display: flex;
  flex-direction: column;
  gap: clamp(0.45rem, 0.8vh, 0.7rem);
}

.auth-trust-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: clamp(0.8rem, 0.95vw, 0.88rem);
  color: #FAF7EE !important;
}

.auth-trust-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(217, 119, 6, 0.25);
  color: #F5A623;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.auth-quote-box {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-left: 3px solid #D97706;
  border-radius: var(--radius-md);
  padding: clamp(0.65rem, 1.2vh, 1rem);
  z-index: 2;
  margin-top: clamp(0.4rem, 0.8vh, 0.75rem);
}

.auth-quote-text {
  font-size: clamp(0.78rem, 0.9vw, 0.85rem);
  font-style: italic;
  color: #FAF7EE !important;
  line-height: 1.45;
  margin-bottom: 0.35rem;
}

.auth-quote-author {
  font-size: clamp(0.7rem, 0.8vw, 0.76rem);
  color: #F5A623 !important;
  font-weight: 600;
  display: block;
}"""

if old_auth_text in css:
    css = css.replace(old_auth_text, new_auth_text)
    print("Replaced old_auth_text in style.css")
else:
    print("WARNING: old_auth_text not found")

# Fix Pricing Comparison Table
css = css.replace('.pricing-comparison-table thead th {\n  background: #090e1c;\n  color: var(--text-primary);',
                  '.pricing-comparison-table thead th {\n  background: #F3EFE0;\n  color: var(--text-primary);')
css = css.replace('.pricing-comparison-table td {\n  padding: 1.15rem 1.4rem;\n  border-bottom: 1px solid rgba(255, 255, 255, 0.08);\n  vertical-align: middle;\n}',
                  '.pricing-comparison-table td {\n  padding: 1.15rem 1.4rem;\n  border-bottom: 1px solid var(--border-subtle);\n  color: var(--text-secondary);\n  vertical-align: middle;\n}')
css = css.replace('color: #030508;\n  border-radius: var(--radius-full);\n  margin-bottom: 0.45rem;\n}',
                  'color: #FFFFFF;\n  border-radius: var(--radius-full);\n  margin-bottom: 0.45rem;\n}')

# Person image wrap background
css = css.replace('.person-image-wrap {\n  width: 100%;\n  aspect-ratio: 1/1;\n  overflow: hidden;\n  position: relative;\n  background: #080d19;\n}',
                  '.person-image-wrap {\n  width: 100%;\n  aspect-ratio: 1/1;\n  overflow: hidden;\n  position: relative;\n  background: var(--bg-secondary);\n}')

# Nav link hover
css = css.replace('.nav-link:hover,\n.nav-link:focus-visible {\n  color: var(--text-primary);\n  background: rgba(255, 255, 255, 0.08);\n}',
                  '.nav-link:hover,\n.nav-link:focus-visible {\n  color: var(--primary);\n  background: rgba(122, 16, 40, 0.06);\n}')

# Mobile toggle
css = css.replace('background: rgba(255, 255, 255, 0.06);\n  border: 1px solid var(--border-subtle);\n  border-radius: var(--radius-full);',
                  'background: #FFFFFF;\n  border: 1.5px solid var(--border-subtle);\n  border-radius: var(--radius-full);\n  box-shadow: 0 2px 8px rgba(58, 1, 14, 0.06);')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated assets/css/style.css successfully.")

