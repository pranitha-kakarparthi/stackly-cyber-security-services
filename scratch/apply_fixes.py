import os

# ==============================================================================
# 1. UPDATE index.html HERO SECTION
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_start = html.find('<!-- 2. ')
hero_end = html.find('<!-- 3. REAL-TIME PERIMETER SCANNER & TELEMETRY -->')

new_hero = '''<!-- 2. UNIFIED REFERENCE-INSPIRED KINETIC CYBER HERO STAGE -->
    <section class="hero-stage" aria-label="Autonomous Cyber Defense Stage">
      <!-- Ambient Holographic Floating Ribbons / Wisps -->
      <div class="ambient-ribbons-container" aria-hidden="true">
        <svg class="ambient-ribbon ribbon-top" viewBox="0 0 1200 600" fill="none" preserveAspectRatio="none">
          <path d="M-50,180 C220,40 380,320 620,160 C860,20 1020,290 1250,140" stroke="url(#iridescent-ribbon-top)" stroke-width="32" stroke-linecap="round"/>
          <path d="M-20,120 C280,20 440,260 700,110 C920,0 1060,220 1280,90" stroke="url(#iridescent-ribbon-subtle)" stroke-width="12" stroke-linecap="round" opacity="0.6"/>
          <defs>
            <linearGradient id="iridescent-ribbon-top" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#5eead4" stop-opacity="0.8" />
              <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.85" />
              <stop offset="70%" stop-color="#a78bfa" stop-opacity="0.9" />
              <stop offset="100%" stop-color="#f472b6" stop-opacity="0.75" />
            </linearGradient>
            <linearGradient id="iridescent-ribbon-subtle" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.5" />
              <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.7" />
              <stop offset="100%" stop-color="#5eead4" stop-opacity="0.6" />
            </linearGradient>
          </defs>
        </svg>
        
        <svg class="ambient-ribbon ribbon-bottom" viewBox="0 0 1200 600" fill="none" preserveAspectRatio="none">
          <path d="M-40,460 C200,320 360,540 680,390 C920,240 1040,490 1240,350" stroke="url(#iridescent-ribbon-bottom)" stroke-width="26" stroke-linecap="round"/>
          <defs>
            <linearGradient id="iridescent-ribbon-bottom" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#a78bfa" stop-opacity="0.7" />
              <stop offset="45%" stop-color="#38bdf8" stop-opacity="0.8" />
              <stop offset="100%" stop-color="#5eead4" stop-opacity="0.85" />
            </linearGradient>
          </defs>
        </svg>
      </div>

      <div class="container hero-stage-container">
        <!-- Visual & Typography Canvas Stage (Text is positioned DIRECTLY OVER the image) -->
        <div class="hero-sentinel-stage">
          <!-- Background Sentinel Graphic with Chains (Layer 1) -->
          <div class="hero-sentinel-frame js-tilt" data-tilt-max="5">
            <img src="assets/images/cyber-sentinel-chains.webp" 
                 alt="Stackly Cyber Sentinel neutralizing breaches and breaking threat chains" 
                 class="hero-sentinel-img"
                 width="1376" 
                 height="768"
                 fetchpriority="high">
            <div class="sentinel-ambient-glow" aria-hidden="true"></div>
          </div>

          <!-- Foreground Kinetic Typography (Layer 20 - ALWAYS VISIBLE OVER THE IMAGE) -->
          <div class="hero-title-overlay" aria-label="World-Leading CYBER SECURITY Powered by AI">
            <div class="kinetic-line-lead" data-animate="fade-down">World-Leading</div>
            <h1 class="hero-title-giant" data-animate="zoom-in" data-delay="100">
              <span class="gradient-mint">CYBER</span><span class="gradient-lavender">SECURITY</span>
            </h1>
            <div class="kinetic-line-sub" data-animate="fade-up" data-delay="200">
              <span class="gradient-mint">Powered</span> <span class="gradient-lavender">by AI</span>
            </div>
          </div>
        </div>

        <!-- Interactive Dock: Live Badge, Pill Actions, Real-time Subtext, Metrics -->
        <div class="hero-interactive-dock" data-animate="fade-up" data-delay="300">
          <div class="badge-tag" style="margin-bottom: 1.5rem;">
            <span class="badge-dot"></span>
            <span data-greeting data-greeting-prefix="" data-greeting-suffix=" • Autonomous Defense Active">Autonomous Defense Active</span>
          </div>

          <div class="hero-pill-actions">
            <a href="404.html" class="btn btn-pill-iridescent btn-lg">
              <span>Free Security Audit</span>
            </a>
            <a href="pages/services.html" class="btn btn-pill-glass btn-lg">
              <span>Work Process</span>
            </a>
          </div>

          <p class="hero-subtext">
            Gain real-time visibility into your systems and stop risks before they spread. Think of it as your all-in-one cyber defense command center.
          </p>

          <!-- Trust Metrics -->
          <div class="hero-trust-metrics">
            <div class="metric-item">
              <span class="metric-number">99.98%</span>
              <span class="metric-label">Threat Interception Rate</span>
            </div>
            <div class="metric-item">
              <span class="metric-number">&lt;4.2 Min</span>
              <span class="metric-label">Mean Containment Time</span>
            </div>
            <div class="metric-item">
              <span class="metric-number">2.1B+</span>
              <span class="metric-label">Events Correlated Daily</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    '''

if hero_start != -1 and hero_end != -1:
    html = html[:hero_start] + new_hero + html[hero_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html hero section updated successfully!')
else:
    print('Failed to find hero markers in index.html:', hero_start, hero_end)


# ==============================================================================
# 2. UPDATE assets/css/style.css
# ==============================================================================
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hero styles
h_start = css.find('/* ==========================================================================\n   UNIFIED REFERENCE-INSPIRED KINETIC CYBER HERO STAGE')
if h_start == -1:
    h_start = css.find('.hero-stage {')
h_end = css.find('/* Legacy & Subpage Hero Sections */')

new_hero_css = '''/* ==========================================================================
   UNIFIED REFERENCE-INSPIRED KINETIC CYBER HERO STAGE
   Text is positioned DIRECTLY OVER the image with z-index: 20
   Seamless, cohesive typography: World-Leading CYBER SECURITY Powered by AI
   ========================================================================== */
.hero-stage {
  position: relative;
  min-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 2.25rem 1.25rem 4.5rem;
  overflow: hidden;
  text-align: center;
}

.hero-stage-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1180px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 1. Sentinel & Typography Combined Stage */
.hero-sentinel-stage {
  position: relative;
  width: 100%;
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Background Sentinel Graphic (Layer 1) */
.hero-sentinel-frame {
  position: relative;
  width: 100%;
  max-width: 820px;
  margin: 0 auto;
  z-index: 1;
}

.hero-sentinel-img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: var(--radius-xl);
  filter: drop-shadow(0 25px 60px rgba(0, 0, 0, 0.95));
  mask-image: radial-gradient(ellipse 95% 85% at 50% 50%, black 55%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 95% 85% at 50% 50%, black 55%, transparent 100%);
}

.sentinel-ambient-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  height: 65%;
  background: radial-gradient(ellipse at center, rgba(94, 234, 212, 0.16) 0%, rgba(167, 139, 250, 0.1) 50%, transparent 75%);
  pointer-events: none;
  z-index: -1;
}

/* Foreground Kinetic Typography (Layer 20 - DIRECTLY OVER THE IMAGE) */
.hero-title-overlay {
  position: absolute;
  top: 6%;
  left: 0;
  right: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  z-index: 20 !important;
  pointer-events: none;
  user-select: none;
}

.kinetic-line-lead {
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
  background: linear-gradient(135deg, #a7f3d0 0%, #5eead4 40%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 30px rgba(94, 234, 212, 0.7)) drop-shadow(0 4px 18px rgba(0, 0, 0, 0.98));
}

.hero-title-giant .gradient-lavender,
.kinetic-line-sub .gradient-lavender {
  background: linear-gradient(135deg, #f5d0fe 0%, #c084fc 40%, #a78bfa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 30px rgba(167, 139, 250, 0.7)) drop-shadow(0 4px 18px rgba(0, 0, 0, 0.98));
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
}

/* 2. Interactive Dock: Pill Buttons, Subtext, Metrics */
.hero-interactive-dock {
  position: relative;
  z-index: 25;
  width: 100%;
  max-width: 820px;
  margin: 1rem auto 0;
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
  margin-bottom: 1.75rem;
}

.hero-subtext {
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
}
'''

if h_start != -1 and h_end != -1:
    css = css[:h_start] + new_hero_css + '\n' + css[h_end:]
    print('Hero CSS in style.css updated!')
else:
    print('Could not find hero CSS boundaries:', h_start, h_end)

# Replace 404 Vortex CSS
v_start = css.find('/* ==========================================================================\n   REFERENCE-INSPIRED 404 VORTEX STAGE')
v_end = css.find('/* ==========================================================================\n   404 ERROR PAGE STYLES')
if v_start == -1:
    v_start = css.find('.vortex-page-wrap {')

new_vortex_css = '''/* ==========================================================================
   REFERENCE-INSPIRED 404 VORTEX STAGE (Attachment Design - Cleaned)
   NO navbar, NO blockquote, high-contrast prominent "Page not found", centered
   ========================================================================== */
.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #030508;
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
  filter: drop-shadow(0 0 12px rgba(94, 234, 212, 0.45));
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
  font-size: clamp(5.5rem, 14vw, 8.5rem);
  font-weight: 800;
  line-height: 1;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow: 0 0 40px rgba(255, 255, 255, 0.5), 0 0 70px rgba(167, 139, 250, 0.4);
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
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.95), 0 0 30px rgba(94, 234, 212, 0.65);
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
}

@media (max-width: 640px) {
  .vortex-portal-stage {
    min-height: 280px;
  }
  .vortex-action-group {
    flex-direction: column;
    width: 100%;
  }
  .vortex-action-group .btn {
    width: 100%;
  }
  .hero-sentinel-stage {
    flex-direction: column;
  }
  .hero-title-overlay {
    position: relative;
    top: auto;
    margin-bottom: -3.5rem;
    z-index: 20;
  }
  .hero-title-giant {
    font-size: clamp(1.75rem, 7.5vw, 2.75rem);
    white-space: normal;
  }
}
'''

if v_start != -1 and v_end != -1:
    css = css[:v_start] + new_vortex_css + '\n' + css[v_end:]
    print('404 Vortex CSS in style.css updated!')
else:
    print('Could not find 404 CSS boundaries:', v_start, v_end)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# ==============================================================================
# 3. UPDATE 404.html (ROOT)
# ==============================================================================
root_404_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 - Page Not Found | Stackly Cyber Security Services</title>
  <meta name="description" content="The requested page could not be located on the Stackly Zero-Trust network grid.">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/animations.css">
</head>
<body style="margin: 0; min-height: 100vh; background-color: #030508;">
  <!-- Accessibility Skip Link -->
  <a href="#vortex-stage" class="skip-link">Skip to main content</a>

  <!-- Modern Viewport Loader (Pure CSS rotation, DOMContentLoaded removal) -->
  <div id="page-loader" aria-live="polite" role="status">
    <div class="loader-content">
      <div class="loader-brand">
        <img src="assets/images/logoStackly.webp" alt="Stackly Cyber Security Services" width="160" height="42">
      </div>
      <div class="loader-spinner-wrap">
        <div class="loader-spinner"></div>
        <div class="loader-pulse-ring"></div>
      </div>
      <div class="loader-text">
        <span class="loader-status-dot"></span>
        <span>Scanning Node Telemetry...</span>
      </div>
    </div>
  </div>

  <!-- Perfectly Centered Main 404 Vortex Stage (NO NAVBAR, NO FOOTER, NO BLOCKQUOTE) -->
  <main class="vortex-page-wrap" role="main">
    <!-- Centered Brand Logo Linking to index.html -->
    <div class="vortex-brand-top">
      <a href="index.html" class="vortex-brand" aria-label="Return to Stackly Home">
        <img src="assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="vortex-brand-logo" width="160" height="42">
      </a>
    </div>

    <!-- Center Cosmic Particle Vortex Stage -->
    <div class="vortex-portal-stage" id="vortex-stage">
      <div class="vortex-canvas-wrap">
        <img src="assets/images/vortex-404-cosmic.webp" alt="Cosmic particle vortex" class="vortex-bg-image" width="1376" height="768">
        <canvas id="vortex-canvas" class="vortex-interactive-canvas" width="840" height="420" aria-hidden="true"></canvas>
      </div>

      <!-- Center Typography inside Clearing -->
      <div class="vortex-center-content js-tilt" data-tilt-max="5">
        <div class="vortex-code" data-animate="zoom-in">404</div>
        <h1 class="vortex-subtitle" data-animate="fade-up" data-delay="100">Page not found</h1>
      </div>
    </div>

    <!-- Action Buttons Directly Below Vortex Stage (NO blockquote) -->
    <div class="vortex-bottom-content" data-animate="fade-up" data-delay="200">
      <div class="vortex-action-group">
        <a href="index.html" class="btn btn-pill-iridescent btn-lg">
          <span>🛡️</span> Return to Secure Home
        </a>
        <button type="button" onclick="history.back()" class="btn btn-pill-glass btn-lg">
          <span>↩️</span> Back to Previous View
        </button>
        <a href="pages/contact.html" class="btn btn-outline btn-lg">
          <span>💬</span> Report Security Anomaly
        </a>
      </div>
    </div>
  </main>

  <script src="assets/js/main.js"></script>
  <script>
    // Lightweight Ethereal Particle Swirl Engine
    (function() {
      const canvas = document.getElementById('vortex-canvas');
      if (!canvas || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      const particles = [];
      const particleCount = 85;
      const width = canvas.width;
      const height = canvas.height;
      const centerX = width / 2;
      const centerY = height / 2;

      for (let i = 0; i < particleCount; i++) {
        particles.push({
          radiusX: 110 + Math.random() * 220,
          radiusY: 45 + Math.random() * 95,
          angle: Math.random() * Math.PI * 2,
          speed: 0.003 + Math.random() * 0.006,
          size: 1 + Math.random() * 2,
          color: Math.random() > 0.4 ? 'rgba(167, 139, 250, ' : 'rgba(94, 234, 212, ',
          alpha: 0.2 + Math.random() * 0.6
        });
      }

      function render() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
          p.angle += p.speed;
          const x = centerX + Math.cos(p.angle) * p.radiusX;
          const y = centerY + Math.sin(p.angle) * p.radiusY;

          ctx.beginPath();
          ctx.arc(x, y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = p.color + p.alpha + ')';
          ctx.shadowBlur = 8;
          ctx.shadowColor = p.color + '0.8)';
          ctx.fill();
        });
        requestAnimationFrame(render);
      }
      render();
    })();
  </script>
</body>
</html>'''

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(root_404_html)
print('404.html updated successfully!')


# ==============================================================================
# 4. UPDATE pages/404.html
# ==============================================================================
subpage_404_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 - Page Not Found | Stackly Cyber Security Services</title>
  <meta name="description" content="The requested page could not be located on the Stackly Zero-Trust network grid.">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/animations.css">
</head>
<body style="margin: 0; min-height: 100vh; background-color: #030508;">
  <!-- Accessibility Skip Link -->
  <a href="#vortex-stage" class="skip-link">Skip to main content</a>

  <!-- Modern Viewport Loader (Pure CSS rotation, DOMContentLoaded removal) -->
  <div id="page-loader" aria-live="polite" role="status">
    <div class="loader-content">
      <div class="loader-brand">
        <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Security Services" width="160" height="42">
      </div>
      <div class="loader-spinner-wrap">
        <div class="loader-spinner"></div>
        <div class="loader-pulse-ring"></div>
      </div>
      <div class="loader-text">
        <span class="loader-status-dot"></span>
        <span>Scanning Node Telemetry...</span>
      </div>
    </div>
  </div>

  <!-- Perfectly Centered Main 404 Vortex Stage (NO NAVBAR, NO FOOTER, NO BLOCKQUOTE) -->
  <main class="vortex-page-wrap" role="main">
    <!-- Centered Brand Logo Linking to index.html -->
    <div class="vortex-brand-top">
      <a href="../index.html" class="vortex-brand" aria-label="Return to Stackly Home">
        <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="vortex-brand-logo" width="160" height="42">
      </a>
    </div>

    <!-- Center Cosmic Particle Vortex Stage -->
    <div class="vortex-portal-stage" id="vortex-stage">
      <div class="vortex-canvas-wrap">
        <img src="../assets/images/vortex-404-cosmic.webp" alt="Cosmic particle vortex" class="vortex-bg-image" width="1376" height="768">
        <canvas id="vortex-canvas" class="vortex-interactive-canvas" width="840" height="420" aria-hidden="true"></canvas>
      </div>

      <!-- Center Typography inside Clearing -->
      <div class="vortex-center-content js-tilt" data-tilt-max="5">
        <div class="vortex-code" data-animate="zoom-in">404</div>
        <h1 class="vortex-subtitle" data-animate="fade-up" data-delay="100">Page not found</h1>
      </div>
    </div>

    <!-- Action Buttons Directly Below Vortex Stage (NO blockquote) -->
    <div class="vortex-bottom-content" data-animate="fade-up" data-delay="200">
      <div class="vortex-action-group">
        <a href="../index.html" class="btn btn-pill-iridescent btn-lg">
          <span>🛡️</span> Return to Secure Home
        </a>
        <button type="button" onclick="history.back()" class="btn btn-pill-glass btn-lg">
          <span>↩️</span> Back to Previous View
        </button>
        <a href="contact.html" class="btn btn-outline btn-lg">
          <span>💬</span> Report Security Anomaly
        </a>
      </div>
    </div>
  </main>

  <script src="../assets/js/main.js"></script>
  <script>
    // Lightweight Ethereal Particle Swirl Engine
    (function() {
      const canvas = document.getElementById('vortex-canvas');
      if (!canvas || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      const particles = [];
      const particleCount = 85;
      const width = canvas.width;
      const height = canvas.height;
      const centerX = width / 2;
      const centerY = height / 2;

      for (let i = 0; i < particleCount; i++) {
        particles.push({
          radiusX: 110 + Math.random() * 220,
          radiusY: 45 + Math.random() * 95,
          angle: Math.random() * Math.PI * 2,
          speed: 0.003 + Math.random() * 0.006,
          size: 1 + Math.random() * 2,
          color: Math.random() > 0.4 ? 'rgba(167, 139, 250, ' : 'rgba(94, 234, 212, ',
          alpha: 0.2 + Math.random() * 0.6
        });
      }

      function render() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
          p.angle += p.speed;
          const x = centerX + Math.cos(p.angle) * p.radiusX;
          const y = centerY + Math.sin(p.angle) * p.radiusY;

          ctx.beginPath();
          ctx.arc(x, y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = p.color + p.alpha + ')';
          ctx.shadowBlur = 8;
          ctx.shadowColor = p.color + '0.8)';
          ctx.fill();
        });
        requestAnimationFrame(render);
      }
      render();
    })();
  </script>
</body>
</html>'''

with open('pages/404.html', 'w', encoding='utf-8') as f:
    f.write(subpage_404_html)
print('pages/404.html updated successfully!')

