import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace Hero Stage Canvas and Typography in style.css
old_hero_start = '/* Kinetic Typography Canvas */\n.hero-kinetic-canvas {'
old_hero_end = '/* Legacy & Subpage Hero Sections */'

new_hero_styles = '''/* Kinetic Typography Canvas */
.hero-stage-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
}

.hero-kinetic-canvas {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: clamp(380px, 48vw, 540px);
}

/* Sentinel Graphic with Chains (Layer 1 - Centered in Background) */
.hero-sentinel-frame {
  position: relative;
  width: min(100%, 780px);
  margin: 0 auto;
  z-index: 1;
  pointer-events: none;
}

.hero-sentinel-img {
  width: 100%;
  height: auto;
  border-radius: var(--radius-xl);
  filter: drop-shadow(0 25px 60px rgba(0, 0, 0, 0.95));
  mask-image: radial-gradient(ellipse 95% 85% at 50% 48%, black 60%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 95% 85% at 50% 48%, black 60%, transparent 100%);
}

.sentinel-ambient-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  height: 65%;
  background: radial-gradient(ellipse at center, rgba(94, 234, 212, 0.15) 0%, rgba(167, 139, 250, 0.1) 50%, transparent 75%);
  pointer-events: none;
  z-index: -1;
}

/* Foreground Kinetic Typography Overlay (Layer 5 - 100% Visible & Readable Over and Framing Image) */
.hero-typography-overlay {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  pointer-events: none;
  z-index: 5;
  user-select: none;
  padding: 0.5rem 0.5rem 1.5rem;
}

.kinetic-line-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.row-top .kinetic-word {
  font-size: clamp(2.2rem, 5.8vw, 4.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #ffffff;
  line-height: 1;
  text-shadow: 0 4px 25px rgba(0, 0, 0, 0.95), 0 0 25px rgba(255, 255, 255, 0.35);
}

.row-middle .kinetic-word {
  font-size: clamp(2.8rem, 8.5vw, 7.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.95;
  text-transform: uppercase;
}

.row-middle .gradient-mint,
.row-bottom .gradient-mint {
  background: linear-gradient(135deg, #a7f3d0 0%, #5eead4 40%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 25px rgba(94, 234, 212, 0.65)) drop-shadow(0 4px 15px rgba(0, 0, 0, 0.98));
  text-align: left;
}

.row-middle .gradient-lavender,
.row-bottom .gradient-lavender {
  background: linear-gradient(135deg, #f5d0fe 0%, #c084fc 40%, #a78bfa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 25px rgba(167, 139, 250, 0.65)) drop-shadow(0 4px 15px rgba(0, 0, 0, 0.98));
  text-align: right;
}

.row-bottom .kinetic-word {
  font-size: clamp(1.85rem, 5.2vw, 4.2rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
}

/* Interactive Dock: Pill Buttons, Subtext, Metrics */
.hero-interactive-dock {
  position: relative;
  z-index: 6;
  width: 100%;
  max-width: 820px;
  margin: 1.5rem auto 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hero-pill-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.hero-subtext {
  font-size: clamp(1.05rem, 2vw, 1.22rem);
  color: #e2e8f0;
  line-height: 1.7;
  max-width: 680px;
  margin: 0 auto 2.75rem;
  font-weight: 400;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
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
}
'''

idx1 = css.find('/* Kinetic Typography Canvas */')
idx2 = css.find('/* Legacy & Subpage Hero Sections */')

if idx1 != -1 and idx2 != -1:
    css = css[:idx1] + new_hero_styles + '\n' + css[idx2:]
    print('Hero styles updated in style.css!')
else:
    print('Failed to find hero section markers:', idx1, idx2)

# 2. Add 404 Vortex Styles
vortex_css = '''
/* ==========================================================================
   REFERENCE-INSPIRED 404 VORTEX STAGE (Attachment Design)
   Ethereal Cosmic Eye Particle Vortex, Centered 404, Philosophical Quote, Pill Actions
   ========================================================================== */
.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #030508;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 1.5rem 2.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
}

/* Minimal Top Bar (Brand on left, subtle corner links on right - NO standard navbar) */
.vortex-top-bar {
  width: 100%;
  max-width: 1200px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 10;
  padding: 0.5rem 0;
}

.vortex-brand-logo {
  height: 34px;
  width: auto;
  filter: drop-shadow(0 0 10px rgba(94, 234, 212, 0.35));
  transition: transform var(--transition-fast);
}

.vortex-brand-logo:hover {
  transform: scale(1.05);
}

.vortex-top-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.vortex-top-link {
  color: #94a3b8;
  font-size: 0.875rem;
  font-weight: 500;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.vortex-top-link:hover {
  color: var(--primary);
}

/* Central Vortex Portal Stage */
.vortex-portal-stage {
  position: relative;
  width: 100%;
  max-width: 860px;
  min-height: 420px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto 0;
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
  filter: drop-shadow(0 0 45px rgba(167, 139, 250, 0.25));
  mask-image: radial-gradient(ellipse 90% 85% at 50% 50%, black 65%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 90% 85% at 50% 50%, black 65%, transparent 100%);
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
  font-size: clamp(4.8rem, 11vw, 7.8rem);
  font-weight: 800;
  line-height: 1;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow: 0 0 35px rgba(255, 255, 255, 0.4), 0 0 65px rgba(167, 139, 250, 0.35);
  margin-bottom: 0.35rem;
}

.vortex-subtitle {
  font-size: clamp(1.05rem, 2.2vw, 1.25rem);
  font-weight: 500;
  color: #94a3b8;
  letter-spacing: 0.02em;
}

/* Bottom Content: Quote & Actions */
.vortex-bottom-content {
  width: 100%;
  max-width: 680px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 10;
  margin-top: auto;
  padding-top: 1rem;
}

.vortex-prompt-label {
  font-size: 0.825rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #64748b;
  font-weight: 600;
  margin-bottom: 0.65rem;
}

.vortex-quote {
  font-size: clamp(0.925rem, 1.8vw, 1.05rem);
  font-weight: 400;
  line-height: 1.65;
  color: #cbd5e1;
  font-style: italic;
  margin: 0 0 0.5rem;
  max-width: 580px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

.vortex-cite {
  display: block;
  font-size: 0.8rem;
  font-style: normal;
  color: #94a3b8;
  margin-bottom: 1.75rem;
  font-weight: 500;
}

.vortex-action-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

@media (max-width: 640px) {
  .vortex-portal-stage {
    min-height: 300px;
  }
  .vortex-action-group {
    flex-direction: column;
    width: 100%;
  }
  .vortex-action-group .btn {
    width: 100%;
  }
}
'''

# Find place to insert 404 vortex styles (near .error-page-wrap)
error_idx = css.find('/* ==========================================================================\n   404 ERROR PAGE STYLES')
if error_idx != -1:
    css = css[:error_idx] + vortex_css + '\n' + css[error_idx:]
    print('404 vortex styles added to style.css!')
else:
    css += '\n' + vortex_css
    print('404 vortex styles appended to style.css!')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

