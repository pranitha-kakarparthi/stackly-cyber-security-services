with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Hero section in index.html
hero_start = html.find('<!-- 2. REFERENCE-INSPIRED KINETIC CYBER HERO STAGE -->')
if hero_start == -1:
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
        <!-- Unified Kinetic Typography Title -->
        <div class="hero-unified-title" data-animate="fade-up">
          <div class="kinetic-line-lead">World-Leading</div>
          <h1 class="hero-title-giant">
            <span class="gradient-mint">CYBER</span><span class="gradient-lavender">SECURITY</span>
          </h1>
          <div class="kinetic-line-sub">
            <span class="gradient-mint">Powered</span> <span class="gradient-lavender">by AI</span>
          </div>
        </div>

        <!-- Centered Cyber Sentinel Graphic with Chains & 3D Tilt -->
        <div class="hero-sentinel-frame js-tilt" data-tilt-max="6" data-animate="zoom-in" data-delay="100">
          <img src="assets/images/cyber-sentinel-chains.webp" 
               alt="Stackly Cyber Sentinel neutralizing breaches and breaking threat chains" 
               class="hero-sentinel-img"
               width="1376" 
               height="768"
               fetchpriority="high">
          <div class="sentinel-ambient-glow" aria-hidden="true"></div>
        </div>

        <!-- Interactive Dock: Live Badge, Pill Actions, Real-time Subtext, Metrics -->
        <div class="hero-interactive-dock" data-animate="fade-up" data-delay="200">
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
    print('Hero start/end markers not found in index.html:', hero_start, hero_end)

# Now update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_css_start = css.find('/* Kinetic Typography Canvas */')
hero_css_end = css.find('/* Legacy & Subpage Hero Sections */')

new_hero_css = '''/* ==========================================================================
   UNIFIED REFERENCE-INSPIRED KINETIC CYBER HERO STAGE
   Seamless, cohesive typography: World-Leading CYBER SECURITY Powered by AI,
   centered cyber sentinel holding chains, pill CTAs, subtext, metrics.
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

/* 1. Unified Kinetic Typography Title */
.hero-unified-title {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 100%;
  margin: 0 auto 0.5rem;
  user-select: none;
}

.kinetic-line-lead {
  font-size: clamp(1.4rem, 3.6vw, 2.6rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 0.25rem;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.9), 0 0 30px rgba(255, 255, 255, 0.25);
}

.hero-title-giant {
  font-size: clamp(2.6rem, 8vw, 6.5rem);
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
  background: linear-gradient(135deg, #a7f3d0 0%, #5eead4 45%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 28px rgba(94, 234, 212, 0.55)) drop-shadow(0 4px 15px rgba(0, 0, 0, 0.95));
}

.hero-title-giant .gradient-lavender,
.kinetic-line-sub .gradient-lavender {
  background: linear-gradient(135deg, #f5d0fe 0%, #c084fc 45%, #a78bfa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 28px rgba(167, 139, 250, 0.55)) drop-shadow(0 4px 15px rgba(0, 0, 0, 0.95));
}

.kinetic-line-sub {
  font-size: clamp(1.2rem, 2.8vw, 2.1rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin-top: 0.35rem;
  display: inline-flex;
  gap: 0.45rem;
  align-items: center;
  justify-content: center;
}

/* 2. Sentinel Graphic with Chains */
.hero-sentinel-frame {
  position: relative;
  width: min(94%, 720px);
  margin: -1.25rem auto 0;
  z-index: 1;
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
  background: radial-gradient(ellipse at center, rgba(94, 234, 212, 0.16) 0%, rgba(167, 139, 250, 0.1) 50%, transparent 75%);
  pointer-events: none;
  z-index: -1;
}

/* 3. Interactive Dock: Pill Buttons, Subtext, Metrics */
.hero-interactive-dock {
  position: relative;
  z-index: 4;
  width: 100%;
  max-width: 820px;
  margin: -0.75rem auto 0;
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

if hero_css_start != -1 and hero_css_end != -1:
    css = css[:hero_css_start] + new_hero_css + '\n' + css[hero_css_end:]
    print('Hero CSS in style.css updated successfully!')
else:
    print('Hero CSS markers not found:', hero_css_start, hero_css_end)

# Also update responsive media query for hero in style.css
# Clean up obsolete kinetic-line-split / row rules in media queries
css = css.replace('.kinetic-line-split {\n    max-width: 95%;\n  }', '')
css = css.replace('.kinetic-line-split {\n    flex-direction: column;\n    gap: 0.25rem;\n  }\n\n  .kinetic-split-left,\n  .kinetic-split-right {\n    text-align: center;\n  }', '')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('style.css updated completely!')

