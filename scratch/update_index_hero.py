import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update nav-actions
old_nav = '''      <div class="nav-actions">
        <a href="pages/sign-in.html" class="btn btn-secondary btn-sm">Sign In</a>
        <a href="pages/sign-up.html" class="btn btn-primary btn-sm">Register</a>
      </div>'''

new_nav = '''      <div class="nav-actions">
        <a href="pages/sign-in.html" class="btn btn-ghost btn-sm">Log In</a>
        <a href="pages/sign-up.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>
      </div>'''

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print('Nav actions updated')
else:
    idx_nav = html.find('<div class="nav-actions">')
    if idx_nav != -1:
        end_nav = html.find('</div>', idx_nav) + 6
        html = html[:idx_nav] + new_nav + html[end_nav:]
        print('Nav actions updated via indices')

# Update Hero section
hero_start = html.find('<!-- 2. HERO SECTION -->')
hero_end = html.find('<!-- 3. REAL-TIME PERIMETER SCANNER & TELEMETRY -->')

new_hero = '''<!-- 2. REFERENCE-INSPIRED KINETIC CYBER HERO STAGE -->
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

      <div class="container" style="position: relative; z-index: 2;">
        <!-- Giant Kinetic Typography & Sentinel Composition -->
        <div class="hero-kinetic-canvas">
          <div class="kinetic-line-lead" data-animate="fade-down">
            World-Leading
          </div>
          <div class="kinetic-line-giant" data-animate="zoom-in" data-delay="100">
            CYBERSECURITY
          </div>
          <div class="kinetic-line-split" data-animate="fade-up" data-delay="200">
            <span class="kinetic-split-left">Powered</span>
            <span class="kinetic-split-right">by AI</span>
          </div>

          <!-- Centered Cyber Sentinel Graphic with Chains & 3D Tilt -->
          <div class="hero-sentinel-frame js-tilt" data-tilt-max="7">
            <img src="assets/images/cyber-sentinel-chains.webp" 
                 alt="Stackly Cyber Sentinel neutralizing breaches and breaking threat chains" 
                 class="hero-sentinel-img"
                 width="1376" 
                 height="768"
                 fetchpriority="high">
            <div class="sentinel-ambient-glow" aria-hidden="true"></div>
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
    print('Hero stage updated successfully!')
else:
    print('Failed to find hero section boundaries:', hero_start, hero_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

