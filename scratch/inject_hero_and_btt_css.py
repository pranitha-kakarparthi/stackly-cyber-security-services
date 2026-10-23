with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

# 1. Enhance .back-to-top with radar pulse ring, floating motion, and arrow lift
old_btt = '''.back-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 48px;
  height: 48px;
  border-radius: var(--radius-full);
  background: var(--primary);
  color: #ffffff;
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
}'''

new_btt = '''.back-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 50px;
  height: 50px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #7A1028 0%, #A31E3E 100%);
  color: #FFFFFF;
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  box-shadow: 0 8px 26px rgba(58, 1, 14, 0.35), 0 0 16px rgba(217, 119, 6, 0.3);
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

/* Radar Sonar Pulse Ring Animation Behind Back to Top Button */
.back-to-top::before {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: var(--radius-full);
  border: 2px solid rgba(217, 119, 6, 0.65);
  box-shadow: 0 0 14px rgba(217, 119, 6, 0.4);
  animation: backToTopPulse 2.4s cubic-bezier(0.24, 0, 0.38, 1) infinite;
  pointer-events: none;
}

.back-to-top.visible {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  animation: backToTopFloat 3.5s ease-in-out infinite alternate;
}

.back-to-top:hover {
  background: linear-gradient(135deg, #5A0A1D 0%, #7A1028 100%);
  transform: translateY(-6px) scale(1.08);
  box-shadow: 0 16px 36px rgba(122, 16, 40, 0.55), 0 0 24px rgba(217, 119, 6, 0.45);
  border-color: rgba(255, 255, 255, 0.8);
}

.back-to-top svg {
  transition: transform var(--transition-fast);
}

.back-to-top:hover svg {
  animation: arrowBounce 0.8s ease-in-out infinite alternate;
}

@keyframes backToTopPulse {
  0% {
    transform: scale(0.92);
    opacity: 0.85;
    border-color: rgba(217, 119, 6, 0.85);
  }
  50% {
    transform: scale(1.3);
    opacity: 0.35;
    border-color: rgba(122, 16, 40, 0.65);
  }
  100% {
    transform: scale(1.6);
    opacity: 0;
    border-color: rgba(122, 16, 40, 0);
  }
}

@keyframes backToTopFloat {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-5px);
  }
}

@keyframes arrowBounce {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-4px);
  }
}'''

assert old_btt in style_css, "old_btt not found in style.css"
style_css = style_css.replace(old_btt, new_btt)

# 2. Add Enhanced Subpage Hero System (with Grid, Visual Frame, Radar, Laser Scan, Floating Pills)
hero_system_css = '''
/* ==========================================================================
   ENHANCED SUBPAGE HERO SYSTEM (Images, Animations & Status Telemetry)
   ========================================================================== */
.page-hero {
  position: relative;
  padding: 4.5rem 0 3.5rem;
  overflow: hidden;
  background: linear-gradient(180deg, rgba(122, 16, 40, 0.04) 0%, rgba(250, 247, 238, 0) 100%);
  border-bottom: 1px solid var(--border-subtle);
}

.page-hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  align-items: center;
  gap: 3.5rem;
  position: relative;
  z-index: 2;
}

.page-hero-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.page-hero-visual {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Holographic Cyber Image Frame */
.hero-visual-frame {
  position: relative;
  width: 100%;
  max-width: 480px;
  border-radius: var(--radius-xl);
  padding: 8px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(243, 239, 224, 0.75) 100%);
  border: 1.5px solid var(--border-cyber);
  box-shadow: 0 20px 50px rgba(58, 1, 14, 0.12), 0 0 30px rgba(122, 16, 40, 0.08);
  animation: heroFloatSoft 7s ease-in-out infinite alternate;
}

.hero-visual-frame img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  border-radius: calc(var(--radius-xl) - 6px);
  display: block;
}

/* Scanning Laser / Sweep Line Animation Across Image */
.hero-visual-frame::after {
  content: '';
  position: absolute;
  top: 8px;
  left: 8px;
  right: 8px;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, rgba(245, 166, 35, 0.85) 50%, transparent 100%);
  box-shadow: 0 0 14px rgba(245, 166, 35, 0.9);
  animation: heroScanLaser 4s linear infinite;
  pointer-events: none;
  z-index: 3;
}

/* Floating Interactive Status Badges Over Hero Visual */
.hero-floating-pill {
  position: absolute;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.95rem;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1.5px solid var(--border-cyber);
  border-radius: var(--radius-full);
  box-shadow: 0 10px 28px rgba(58, 1, 14, 0.14);
  font-size: 0.825rem;
  font-weight: 700;
  color: var(--text-primary);
  z-index: 4;
  white-space: nowrap;
}

.hero-floating-pill.pill-top-left {
  top: -14px;
  left: -18px;
  animation: floatBadgeA 5s ease-in-out infinite alternate;
}

.hero-floating-pill.pill-bottom-right {
  bottom: -14px;
  right: -18px;
  animation: floatBadgeB 6s ease-in-out infinite alternate;
}

.hero-pill-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 8px #10B981;
  animation: blinkDot 1.4s infinite alternate;
}

.hero-pill-dot.dot-amber {
  background: var(--accent-gold);
  box-shadow: 0 0 8px var(--accent-gold);
}

.hero-pill-dot.dot-wine {
  background: var(--primary);
  box-shadow: 0 0 8px var(--primary);
}

/* Ambient Radial Pulse Rings behind Hero Visual */
.hero-visual-radar {
  position: absolute;
  width: 120%;
  height: 120%;
  border-radius: 50%;
  border: 1px dashed rgba(122, 16, 40, 0.22);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  animation: rotateRing 32s linear infinite;
  z-index: 1;
}

.hero-visual-radar::after {
  content: '';
  position: absolute;
  inset: 15%;
  border-radius: 50%;
  border: 1px solid rgba(217, 119, 6, 0.22);
  animation: rotateRingRev 22s linear infinite;
}

@keyframes heroScanLaser {
  0% {
    top: 8px;
    opacity: 0;
  }
  15% {
    opacity: 1;
  }
  85% {
    opacity: 1;
  }
  100% {
    top: calc(100% - 10px);
    opacity: 0;
  }
}

@keyframes heroFloatSoft {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-8px);
  }
}

@keyframes floatBadgeA {
  0% {
    transform: translateY(0) rotate(-1deg);
  }
  100% {
    transform: translateY(-6px) rotate(1deg);
  }
}

@keyframes floatBadgeB {
  0% {
    transform: translateY(0) rotate(1deg);
  }
  100% {
    transform: translateY(6px) rotate(-1deg);
  }
}

@keyframes rotateRing {
  from {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  to {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}

@keyframes rotateRingRev {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}

@media (max-width: 992px) {
  .page-hero-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .page-hero-content {
    align-items: center;
    text-align: center;
  }
  .page-hero-visual {
    width: 100%;
    margin-top: 1rem;
  }
  .hero-floating-pill.pill-top-left {
    left: 8px;
    top: -10px;
  }
  .hero-floating-pill.pill-bottom-right {
    right: 8px;
    bottom: -10px;
  }
}
'''

style_css += hero_system_css

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)

print("Successfully injected enhanced hero CSS and back-to-top animations into style.css")

