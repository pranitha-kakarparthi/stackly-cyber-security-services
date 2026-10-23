# Python script to update style.css with the rich hero background system

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the older page-hero at pos 26976 to avoid conflicting backgrounds
old_ph_1 = '''.page-hero {
  padding: 4.5rem 0 3.5rem;
  text-align: center;
  background: radial-gradient(
    circle at 50% 0%,
    rgba(122, 16, 40, 0.06) 0%,
    transparent 65%
  );
  border-bottom: 1px solid var(--border-subtle);
  position: relative;
}'''

new_ph_1 = '''.page-hero {
  position: relative;
  padding: 5.25rem 0 4rem;
  overflow: hidden;
  border-bottom: 1.5px solid var(--border-subtle);
}'''

css = css.replace(old_ph_1, new_ph_1)

# Now check the page-hero at the bottom
old_ph_2 = '''.page-hero {
  position: relative;
  padding: 4.5rem 0 3.5rem;
  overflow: hidden;
  background: linear-gradient(180deg, rgba(122, 16, 40, 0.04) 0%, rgba(250, 247, 238, 0) 100%);
  border-bottom: 1px solid var(--border-subtle);
}'''

ENHANCED_HERO_CSS = '''/* ==========================================================================
   ENHANCED CYBER HERO BACKGROUND & HUD TELEMETRY SYSTEM
   ========================================================================== */

/* Subpage Hero Stage Background Architecture */
.page-hero {
  position: relative;
  padding: 5.25rem 0 4.25rem;
  overflow: hidden;
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 15% 25%, rgba(122, 16, 40, 0.14) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 35%, rgba(217, 119, 6, 0.16) 0%, transparent 65%),
    radial-gradient(ellipse 80% 70% at 50% 95%, rgba(158, 42, 68, 0.09) 0%, transparent 70%);
  border-bottom: 1.5px solid var(--border-subtle);
}

/* Precision Drifting Coordinate Grid */
.page-hero::before {
  content: '';
  position: absolute;
  inset: -54px;
  background-image:
    linear-gradient(to right, rgba(122, 16, 40, 0.08) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(122, 16, 40, 0.08) 1px, transparent 1px);
  background-size: 54px 54px;
  -webkit-mask-image: radial-gradient(ellipse 85% 75% at 50% 40%, black 25%, transparent 85%);
  mask-image: radial-gradient(ellipse 85% 75% at 50% 40%, black 25%, transparent 85%);
  pointer-events: none;
  z-index: 1;
  animation: heroGridDrift 70s linear infinite;
}

/* Luminous Pulsing Cyber Aurora Orbs */
.page-hero::after {
  content: '';
  position: absolute;
  inset: -60px;
  background:
    radial-gradient(circle at 10% 20%, rgba(122, 16, 40, 0.16) 0%, transparent 40%),
    radial-gradient(circle at 90% 28%, rgba(245, 166, 35, 0.18) 0%, transparent 45%),
    radial-gradient(circle at 50% 85%, rgba(158, 42, 68, 0.11) 0%, transparent 48%),
    radial-gradient(circle at 75% 80%, rgba(16, 185, 129, 0.08) 0%, transparent 35%);
  pointer-events: none;
  z-index: 1;
  animation: heroAuraPulse 14s ease-in-out infinite alternate;
}

/* Homepage Hero Stage Enhanced Background */
.hero-stage {
  position: relative;
  min-height: 94vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 4.5rem 1.25rem 5rem;
  overflow: hidden;
  text-align: center;
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 50% 20%, rgba(122, 16, 40, 0.14) 0%, transparent 70%),
    radial-gradient(ellipse 65% 55% at 15% 45%, rgba(217, 119, 6, 0.15) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 50%, rgba(158, 42, 68, 0.12) 0%, transparent 65%);
}

.hero-stage::before {
  content: '';
  position: absolute;
  inset: -54px;
  background-image:
    linear-gradient(to right, rgba(122, 16, 40, 0.08) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(122, 16, 40, 0.08) 1px, transparent 1px);
  background-size: 54px 54px;
  -webkit-mask-image: radial-gradient(ellipse 85% 75% at 50% 45%, black 25%, transparent 85%);
  mask-image: radial-gradient(ellipse 85% 75% at 50% 45%, black 25%, transparent 85%);
  pointer-events: none;
  z-index: 1;
  animation: heroGridDrift 75s linear infinite;
}

.hero-stage::after {
  content: '';
  position: absolute;
  inset: -60px;
  background:
    radial-gradient(circle at 18% 30%, rgba(122, 16, 40, 0.16) 0%, transparent 42%),
    radial-gradient(circle at 82% 35%, rgba(245, 166, 35, 0.19) 0%, transparent 46%),
    radial-gradient(circle at 50% 70%, rgba(16, 185, 129, 0.09) 0%, transparent 50%);
  pointer-events: none;
  z-index: 1;
  animation: heroAuraPulse 16s ease-in-out infinite alternate;
}

/* Keyframes for Drifting Grid & Breathing Aurora */
@keyframes heroGridDrift {
  0% {
    background-position: 0 0, 0 0;
  }
  100% {
    background-position: 54px 54px, 54px 54px;
  }
}

@keyframes heroAuraPulse {
  0% {
    opacity: 0.75;
    transform: scale(1) translateY(0);
  }
  50% {
    opacity: 1;
    transform: scale(1.04) translateY(-10px);
  }
  100% {
    opacity: 0.85;
    transform: scale(0.97) translateY(8px);
  }
}

/* Decorative Technical HUD Backdrop Overlay */
.hero-cyber-backdrop {
  position: absolute;
  inset: 1.25rem 2rem;
  pointer-events: none;
  z-index: 1;
  display: block;
}

.cyber-hud-corner {
  position: absolute;
  width: 28px;
  height: 28px;
  border-color: rgba(122, 16, 40, 0.32);
  border-style: solid;
  pointer-events: none;
  transition: border-color var(--transition-base);
}

.cyber-hud-corner.corner-tl {
  top: 0;
  left: 0;
  border-width: 2px 0 0 2px;
  border-top-left-radius: 4px;
}

.cyber-hud-corner.corner-tr {
  top: 0;
  right: 0;
  border-width: 2px 2px 0 0;
  border-top-right-radius: 4px;
}

.cyber-hud-corner.corner-bl {
  bottom: 0;
  left: 0;
  border-width: 0 0 2px 2px;
  border-bottom-left-radius: 4px;
}

.cyber-hud-corner.corner-br {
  bottom: 0;
  right: 0;
  border-width: 0 2px 2px 0;
  border-bottom-right-radius: 4px;
}

.cyber-hud-telemetry {
  position: absolute;
  font-family: var(--font-mono, 'JetBrains Mono', monospace);
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  color: rgba(122, 16, 40, 0.65);
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  user-select: none;
  background: rgba(250, 247, 238, 0.75);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(122, 16, 40, 0.12);
}

.cyber-hud-telemetry.hud-left {
  top: 4px;
  left: 36px;
}

.cyber-hud-telemetry.hud-right {
  top: 4px;
  right: 36px;
}

.hud-pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 8px #10B981;
  display: inline-block;
  animation: blinkDot 1.4s infinite alternate;
}

.hud-pulse-dot.dot-amber {
  background: var(--accent-gold);
  box-shadow: 0 0 8px var(--accent-gold);
}

.hud-sep {
  color: var(--accent-gold);
  font-weight: 800;
}

.cyber-backdrop-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

@media (max-width: 992px) {
  .hero-cyber-backdrop {
    inset: 0.75rem 1rem;
  }
  .cyber-hud-telemetry {
    font-size: 0.68rem;
    padding: 3px 6px;
  }
  .cyber-hud-telemetry.hud-left {
    left: 28px;
  }
  .cyber-hud-telemetry.hud-right {
    right: 28px;
  }
}

@media (max-width: 768px) {
  .hero-cyber-backdrop {
    display: none;
  }
}
'''

if old_ph_2 in css:
    css = css.replace(old_ph_2, ENHANCED_HERO_CSS)
    print("Replaced old_ph_2 with ENHANCED_HERO_CSS")
else:
    css += "\n" + ENHANCED_HERO_CSS
    print("Appended ENHANCED_HERO_CSS")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css successfully updated with enhanced hero background system!")

