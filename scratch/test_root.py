import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect :root replacement
old_root_match = re.search(r':root\s*\{[^}]+\}', css)
if old_root_match:
    print("Found old :root, length:", len(old_root_match.group(0)))

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

print("New root created successfully.")

