with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''      <div class="container" style="position: relative; z-index: 2;">
        <!-- Giant Kinetic Typography & Sentinel Composition -->
        <div class="hero-kinetic-canvas">
          <div class="kinetic-line-lead" data-animate="fade-down">
            World-Leading
          </div>
          <div class="kinetic-line-giant" data-animate="zoom-in" data-delay="100">
            CYBER SECURITY
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
        </div>'''

replacement = '''      <div class="container hero-stage-container">
        <!-- Giant Kinetic Typography & Sentinel Composition -->
        <div class="hero-kinetic-canvas">
          <!-- Centered Cyber Sentinel Graphic with Chains & 3D Tilt (Layer 1 - Background) -->
          <div class="hero-sentinel-frame js-tilt" data-tilt-max="6">
            <img src="assets/images/cyber-sentinel-chains.webp" 
                 alt="Stackly Cyber Sentinel neutralizing breaches and breaking threat chains" 
                 class="hero-sentinel-img"
                 width="1376" 
                 height="768"
                 fetchpriority="high">
            <div class="sentinel-ambient-glow" aria-hidden="true"></div>
          </div>

          <!-- Foreground Kinetic Typography Overlay (Layer 5 - 100% Visible & Readable Over & Framing Image) -->
          <div class="hero-typography-overlay" aria-label="World-Leading CYBER SECURITY Powered by AI">
            <!-- Row 1: World-Leading -->
            <div class="kinetic-line-row row-top" data-animate="fade-down">
              <span class="kinetic-word left-word">World-</span>
              <span class="kinetic-word right-word">Leading</span>
            </div>

            <!-- Row 2: CYBER SECURITY -->
            <div class="kinetic-line-row row-middle" data-animate="zoom-in" data-delay="100">
              <span class="kinetic-word left-word gradient-mint">CYBER</span>
              <span class="kinetic-word right-word gradient-lavender">SECURITY</span>
            </div>

            <!-- Row 3: Powered by AI -->
            <div class="kinetic-line-row row-bottom" data-animate="fade-up" data-delay="200">
              <span class="kinetic-word left-word gradient-mint">Powered</span>
              <span class="kinetic-word right-word gradient-lavender">by AI</span>
            </div>
          </div>
        </div>'''

if target in html:
    html = html.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html hero updated successfully!')
else:
    # Use index-based replacement
    start_tag = '<div class="hero-kinetic-canvas">'
    end_tag = '<!-- Interactive Dock: Live Badge'
    s_idx = html.find(start_tag)
    e_idx = html.find(end_tag)
    if s_idx != -1 and e_idx != -1:
        # replace from container start
        c_idx = html.rfind('<div class="container"', 0, s_idx)
        html = html[:c_idx] + replacement + '\n\n        ' + html[e_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print('index.html hero updated via index search!')
    else:
        print('Failed to find tags in index.html')

