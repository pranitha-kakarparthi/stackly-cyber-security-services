# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Google Fonts import at top if not present
if '@import url(\'https://fonts.googleapis.com' not in content:
    content = "@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap');\n\n" + content

# Update font variables
old_fonts = '''  /* Typography */
  --font-sans:
    "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "Courier New", monospace;'''

new_fonts = '''  /* Typography: Unified 2-Font System Across All Pages (Plus Jakarta Sans & JetBrains Mono) */
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;'''

if old_fonts in content:
    content = content.replace(old_fonts, new_fonts)
else:
    # try flexible replace
    import re
    content = re.sub(r'--font-sans:[^;]+;', "--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n  --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;", content)
    content = re.sub(r'--font-mono:[^;]+;', "--font-mono: 'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;", content)

# Change .metric-number to sans
content = content.replace('.metric-number {\n  font-size: 2.25rem;\n  font-weight: 800;\n  color: var(--primary);\n  line-height: 1.1;\n  font-family: var(--font-mono);\n}',
                          '.metric-number {\n  font-size: 2.25rem;\n  font-weight: 800;\n  color: var(--primary);\n  line-height: 1.1;\n  font-family: var(--font-sans);\n}')

# Change .sim-stat-val to sans
content = content.replace('.sim-stat-val {\n  font-family: var(--font-mono);\n  font-size: 1.65rem;',
                          '.sim-stat-val {\n  font-family: var(--font-sans);\n  font-size: 1.65rem;')

# Change .pricing-price-wrap to sans
content = content.replace('.pricing-price-wrap {\n  display: flex;\n  align-items: baseline;\n  gap: 0.35rem;\n  margin-bottom: 2rem;\n  font-family: var(--font-mono);\n}',
                          '.pricing-price-wrap {\n  display: flex;\n  align-items: baseline;\n  gap: 0.35rem;\n  margin-bottom: 2rem;\n  font-family: var(--font-sans);\n}')

# Change .error-code to sans
content = content.replace('.error-code {\n  font-family: var(--font-mono);',
                          '.error-code {\n  font-family: var(--font-sans);')

# 404 spacing and styling overhaul
old_vortex_css = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #250109;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 1.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: 1.5rem;
}

/* Background Cyber Grid & Matrix Pattern for 404 */
.vortex-page-wrap::before {
  content: "";
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(rgba(56, 189, 248, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56, 189, 248, 0.05) 1px, transparent 1px),
    radial-gradient(
      ellipse 80% 60% at 50% 50%,
      rgba(122, 16, 40, 0.12) 0%,
      rgba(217, 119, 6, 0.06) 50%,
      transparent 80%
    );
  background-size:
    40px 40px,
    40px 40px,
    100% 100%;
  background-position: center center;
  pointer-events: none;
  z-index: 1;
}

.vortex-page-wrap::after {
  content: "";
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image:
    radial-gradient(
      circle at 20px 20px,
      rgba(122, 16, 40, 0.22) 1.5px,
      transparent 2px
    ),
    radial-gradient(
      circle at 60px 60px,
      rgba(217, 119, 6, 0.22) 1.5px,
      transparent 2px
    );
  background-size: 80px 80px;
  pointer-events: none;
  z-index: 1;
}

.vortex-brand-top {
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  margin-bottom: 0.5rem;
}

.vortex-brand-logo {
  height: 38px;
  width: auto;
  filter: drop-shadow(0 0 12px rgba(122, 16, 40, 0.25));
  transition: transform var(--transition-fast);
}

.vortex-brand-logo:hover {
  transform: scale(1.05);
}

/* Central Vortex Portal Stage */
.vortex-portal-stage {
  position: relative;
  width: 100%;
  max-width: 860px;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.vortex-canvas-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.vortex-bg-image {
  width: 100%;
  max-width: 820px;
  height: auto;
  object-fit: contain;
  opacity: 0.88;
  filter: drop-shadow(0 0 45px rgba(122, 16, 40, 0.25));
  mask-image: radial-gradient(
    ellipse 90% 85% at 50% 50%,
    black 65%,
    transparent 100%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 90% 85% at 50% 50%,
    black 65%,
    transparent 100%
  );
  animation: floatGentle 8s ease-in-out infinite alternate;
}

.vortex-interactive-canvas {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 840px;
  height: 100%;
  pointer-events: none;
}

/* Centered 404 Text Inside Vortex Clearing */
.vortex-center-content {
  position: relative;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  user-select: none;
}

.vortex-code {
  font-family: var(--font-sans);
  font-size: clamp(5.5rem, 14vw, 8.5rem);
  font-weight: 800;
  line-height: 1;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow:
    0 0 40px rgba(255, 255, 255, 0.8),
    0 0 70px rgba(217, 119, 6, 0.35);
  margin-bottom: 0.4rem;
}

/* HIGH-CONTRAST, PROMINENT "Page not found" TITLE */
.vortex-subtitle {
  font-size: clamp(1.6rem, 4.2vw, 2.5rem);
  font-weight: 700;
  color: #ffffff !important;
  letter-spacing: -0.01em;
  line-height: 1.2;
  margin: 0;
  text-shadow:
    0 4px 20px rgba(58, 1, 14, 0.65),
    0 0 30px rgba(217, 119, 6, 0.45);
}

/* Action Buttons Container (NO blockquote) */
.vortex-bottom-content {
  width: 100%;
  max-width: 680px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 10;
  margin-top: 1rem;
}

.vortex-action-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}'''

new_vortex_css = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #250109;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: clamp(2.5rem, 6vh, 4.5rem) 1.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: clamp(1.75rem, 3.5vh, 2.75rem);
}

/* Background Cyber Grid & Matrix Pattern for 404 (Warm Amber & Velvet Wine Harmonized) */
.vortex-page-wrap::before {
  content: "";
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(rgba(217, 119, 6, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(217, 119, 6, 0.05) 1px, transparent 1px),
    radial-gradient(
      ellipse 80% 65% at 50% 50%,
      rgba(122, 16, 40, 0.28) 0%,
      rgba(217, 119, 6, 0.08) 50%,
      transparent 80%
    );
  background-size:
    48px 48px,
    48px 48px,
    100% 100%;
  background-position: center center;
  pointer-events: none;
  z-index: 1;
}

.vortex-page-wrap::after {
  content: "";
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image:
    radial-gradient(
      circle at 24px 24px,
      rgba(217, 119, 6, 0.18) 1.5px,
      transparent 2px
    ),
    radial-gradient(
      circle at 72px 72px,
      rgba(122, 16, 40, 0.22) 1.5px,
      transparent 2px
    );
  background-size: 96px 96px;
  pointer-events: none;
  z-index: 1;
}

.vortex-brand-top {
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  margin-bottom: clamp(0.75rem, 1.5vh, 1.5rem);
}

.vortex-brand-logo {
  height: 42px;
  width: auto;
  filter: drop-shadow(0 0 14px rgba(245, 166, 35, 0.35));
  transition: transform var(--transition-fast);
}

.vortex-brand-logo:hover {
  transform: scale(1.05);
}

/* Central Vortex Portal Stage */
.vortex-portal-stage {
  position: relative;
  width: 100%;
  max-width: 880px;
  min-height: clamp(360px, 46vh, 460px);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: clamp(0.5rem, 1.5vh, 1.5rem) auto;
  padding: 1rem 0;
}

.vortex-canvas-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.vortex-bg-image {
  width: 100%;
  max-width: 840px;
  height: 100%;
  max-height: 460px;
  object-fit: contain;
  opacity: 0.95;
  filter: drop-shadow(0 0 45px rgba(122, 16, 40, 0.35));
  mask-image: radial-gradient(
    ellipse 85% 80% at 50% 50%,
    black 50%,
    transparent 98%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 85% 80% at 50% 50%,
    black 50%,
    transparent 98%
  );
  animation: floatGentle 8s ease-in-out infinite alternate;
}

.vortex-interactive-canvas {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 840px;
  height: 100%;
  pointer-events: none;
}

/* Centered 404 Text Inside Vortex Clearing */
.vortex-center-content {
  position: relative;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  user-select: none;
  padding: 1.25rem;
}

.vortex-code {
  font-family: var(--font-sans);
  font-size: clamp(5.5rem, 13vw, 8.5rem);
  font-weight: 800;
  line-height: 1;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow:
    0 0 35px rgba(255, 255, 255, 0.85),
    0 0 70px rgba(245, 166, 35, 0.45);
  margin-bottom: 0.85rem;
}

/* HIGH-CONTRAST, PROMINENT "Page not found" TITLE */
.vortex-subtitle {
  font-size: clamp(1.6rem, 3.8vw, 2.35rem);
  font-weight: 700;
  color: #ffffff !important;
  letter-spacing: -0.01em;
  line-height: 1.25;
  margin: 0;
  text-shadow:
    0 4px 20px rgba(37, 1, 9, 0.85),
    0 0 30px rgba(245, 166, 35, 0.55);
}

/* Action Buttons Container (NO blockquote) */
.vortex-bottom-content {
  width: 100%;
  max-width: 780px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 10;
  margin-top: clamp(1.5rem, 3vh, 2.5rem);
  padding-bottom: 1rem;
}

.vortex-action-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  flex-wrap: wrap;
}'''

if old_vortex_css in content:
    content = content.replace(old_vortex_css, new_vortex_css)
    print("Replaced 404 vortex CSS in style.css")
else:
    print("Warning: old_vortex_css not matched exactly, checking diff...")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update dashboard.css
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dash_content = f.read()

# Add Google Fonts import at top if not present
if '@import url(\'https://fonts.googleapis.com' not in dash_content:
    dash_content = "@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap');\n\n" + dash_content

dash_content = dash_content.replace('.kpi-value {\n  font-size: 2rem;\n  font-weight: 800;\n  font-family: var(--font-mono);',
                                    '.kpi-value {\n  font-size: 2rem;\n  font-weight: 800;\n  font-family: var(--font-sans);')
dash_content = dash_content.replace('.dash-stat-value {\n  font-size: 1.5rem;\n  font-weight: 800;\n  font-family: var(--font-mono);',
                                    '.dash-stat-value {\n  font-size: 1.5rem;\n  font-weight: 800;\n  font-family: var(--font-sans);')

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Updated style.css and dashboard.css font & 404 spacing rules!")

