with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update the mobile-nav-overlay block
old_overlay = '''.mobile-nav-overlay {
  display: none;
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(250, 247, 238, 0.98);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  z-index: 1001;
  padding: 6.5rem 1.5rem 2.5rem;
  overflow-y: auto;
  opacity: 0;
  visibility: hidden;
  transition: all var(--transition-smooth);
}

.mobile-nav-overlay.open {
  opacity: 1;
  visibility: visible;
  display: flex;
  flex-direction: column;
}

.mobile-menu-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.mobile-nav-link {
  display: block;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  padding: 0.75rem 0.5rem;
  border-bottom: 1px solid var(--border-subtle);
}

.mobile-nav-link.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
}

.mobile-submenu {
  list-style: none;
  padding-left: 1.25rem;
  margin-top: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.mobile-submenu-link {
  font-size: 1rem;
  color: var(--text-secondary);
  display: block;
  padding: 0.4rem 0;
}

.mobile-actions {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin-top: auto;
  padding-top: 1.5rem;
}'''

new_overlay = '''/* ==========================================================================
   MOBILE NAVIGATION DRAWER & SYNCHRONIZED SERVICES ACCORDION
   ========================================================================== */
.mobile-nav-overlay {
  display: none;
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(250, 247, 238, 0.98);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  z-index: 1001;
  padding: 5.5rem 1.5rem 2.5rem;
  overflow-y: auto;
  opacity: 0;
  visibility: hidden;
  transition: all var(--transition-smooth);
}

.mobile-nav-overlay.open {
  opacity: 1;
  visibility: visible;
  display: flex;
  flex-direction: column;
}

.mobile-nav-brand {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.mobile-brand-link img {
  height: 36px;
  width: auto;
}

.mobile-menu-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.mobile-nav-link {
  display: block;
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  padding: 0.65rem 0.5rem;
  border-bottom: 1px solid var(--border-subtle);
  transition: color var(--transition-fast);
}

.mobile-nav-link.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
}

.mobile-dropdown-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
}

.mobile-dropdown-header .mobile-nav-link {
  border-bottom: none;
  flex: 1;
}

.mobile-dropdown-btn {
  background: rgba(122, 16, 40, 0.08);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--primary);
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  margin-right: 0.5rem;
  flex-shrink: 0;
}

.mobile-dropdown-btn:hover {
  background: rgba(122, 16, 40, 0.16);
}

.mobile-chevron {
  transition: transform var(--transition-smooth);
}

.mobile-dropdown-btn.open .mobile-chevron,
.mobile-dropdown-btn[aria-expanded="true"] .mobile-chevron {
  transform: rotate(180deg);
}

.mobile-submenu {
  list-style: none;
  padding: 0.65rem 0.25rem 0.75rem 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  transition: all var(--transition-smooth);
}

.mobile-submenu:not(.open) {
  display: none;
}

.mobile-service-card {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.75rem 0.95rem;
  background: #ffffff;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  box-shadow: 0 2px 8px rgba(58, 1, 14, 0.04);
  text-decoration: none;
  transition: all var(--transition-fast);
}

.mobile-service-card:hover,
.mobile-service-card:focus-visible {
  border-color: var(--primary);
  background: rgba(122, 16, 40, 0.03);
  transform: translateX(4px);
}

.mobile-service-icon {
  font-size: 1.35rem;
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(122, 16, 40, 0.06);
  border-radius: var(--radius-sm);
}

.mobile-service-info {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  flex: 1;
}

.mobile-service-title {
  font-size: 0.925rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.25;
}

.mobile-service-desc {
  font-size: 0.775rem;
  color: var(--text-secondary);
  line-height: 1.3;
}

.mobile-service-overview-item {
  margin-top: 0.25rem;
  padding-left: 0.25rem;
}

.mobile-overview-link {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--primary);
  text-decoration: underline;
  padding: 0.35rem 0;
}

.mobile-actions {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin-top: auto;
  padding-top: 1.5rem;
}'''

if old_overlay in css:
    css = css.replace(old_overlay, new_overlay)
    print("[OK] Replaced mobile-nav-overlay block")
else:
    print("[WARN] Could not find exact old_overlay")

# 2. Update @media (max-width: 1024px)
old_1024 = '''/* Laptop / Desktop (<= 1024px) */
@media (max-width: 1024px) {
  .site-header {
    top: 0.75rem;
    padding: 0 0.75rem;
  }

  .site-header .navbar {
    height: 60px;
    padding: 0 1rem 0 1.25rem;
  }

  .hero-stage {
    padding: 3rem 1rem 4rem;
  }

  .hero-sentinel-stage {
    margin: 2rem auto 0;
  }

  .hero-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .cards-grid-3,
  .cards-grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }

  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .auth-wrapper {
    grid-template-columns: 1fr;
  }

  .auth-banner-side {
    display: none;
  }

  .nav-menu,
  .nav-actions {
    display: none;
  }

  .nav-toggle {
    display: flex;
  }
}'''

new_1024 = '''/* Laptop / Desktop (<= 1024px) */
@media (max-width: 1024px) {
  .site-header {
    top: 0.75rem;
    padding: 0 0.75rem;
  }

  .site-header .navbar {
    height: 60px;
    padding: 0 1rem 0 1.25rem;
  }

  .hero-stage {
    padding: 3.5rem 1rem 4rem;
  }

  .hero-sentinel-stage {
    margin: 2rem auto 0;
  }

  .hero-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .cards-grid-3,
  .cards-grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }

  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  /* Rich Stacked Layout for Auth Pages on Smaller Screens - Never Missing Content */
  .auth-wrapper {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: var(--bg-primary);
  }

  .auth-banner-side {
    display: flex;
    flex-direction: column;
    position: static;
    height: auto;
    max-height: none;
    overflow-y: visible;
    padding: 3rem 1.5rem 2.25rem;
    border-right: none;
    border-bottom: 2px solid var(--border-cyber);
    background: linear-gradient(145deg, #3a010e 0%, #200007 100%);
  }

  .auth-banner-header {
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: center;
  }

  .auth-banner-content {
    margin: 0 auto 1.5rem;
    max-width: 620px;
    text-align: center;
  }

  .auth-banner-content h1 {
    font-size: clamp(1.6rem, 5vw, 2.25rem);
    margin: 0.75rem 0 1rem;
    line-height: 1.25;
  }

  .auth-trust-list {
    text-align: left;
    margin: 1.25rem auto;
    max-width: 500px;
  }

  .auth-quote-box {
    margin: 1.25rem auto 0;
    max-width: 620px;
    text-align: center;
  }

  .auth-form-side {
    padding: 2.75rem 1.5rem 4rem;
    display: flex;
    justify-content: center;
    align-items: flex-start;
  }

  .auth-form-container {
    max-width: 520px;
    width: 100%;
    margin: 0 auto;
  }

  .nav-menu,
  .nav-actions {
    display: none;
  }

  .nav-toggle {
    display: flex;
  }
}'''

if old_1024 in css:
    css = css.replace(old_1024, new_1024)
    print("[OK] Replaced @media (max-width: 1024px) block")
else:
    print("[WARN] Could not find exact old_1024")

# 3. Update @media (max-width: 640px)
old_640 = '''@media (max-width: 640px) {
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
}'''

new_640 = '''@media (max-width: 640px) {
  .vortex-portal-stage {
    min-height: 280px;
  }
  .vortex-action-group {
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }
  .vortex-action-group .btn {
    width: 100%;
  }

  /* Homepage Sentinel Stage Clean Vertical Layout with Zero Overlap */
  .hero-sentinel-stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.25rem;
    margin-top: 1.25rem;
  }

  .hero-title-overlay {
    position: static;
    top: auto;
    width: 100%;
    margin-bottom: 0.75rem;
    z-index: 20;
    pointer-events: auto;
  }

  .hero-title-giant {
    font-size: clamp(1.85rem, 7.5vw, 2.75rem);
    white-space: normal;
    line-height: 1.15;
    word-break: break-word;
  }

  .hero-sentinel-frame {
    width: 100%;
    max-width: 520px;
    margin: 0 auto;
    position: relative;
  }

  .hero-sentinel-frame .hero-floating-pill.pill-top-left {
    top: 8px !important;
    left: 8px !important;
    font-size: 0.72rem;
    padding: 0.35rem 0.65rem;
    max-width: 82%;
  }

  .hero-sentinel-frame .hero-floating-pill.pill-bottom-right {
    bottom: 8px !important;
    right: 8px !important;
    font-size: 0.72rem;
    padding: 0.35rem 0.65rem;
    max-width: 82%;
  }

  .hero-interactive-dock {
    margin-top: 1.25rem;
    width: 100%;
  }

  /* Subpage Hero Grid Responsive Alignment */
  .page-hero {
    padding: 5.25rem 0 3rem;
  }

  .page-hero-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .page-hero-content {
    align-items: center;
    text-align: center;
  }

  .page-hero-title {
    font-size: clamp(1.75rem, 6vw, 2.5rem);
    line-height: 1.2;
    word-break: break-word;
    margin-bottom: 1rem;
  }

  .page-hero-desc {
    font-size: 0.975rem;
    line-height: 1.6;
  }

  .page-hero-visual {
    width: 100%;
    max-width: 480px;
    margin: 0 auto;
  }

  .hero-visual-frame {
    max-width: 100%;
    padding: 6px;
  }

  .hero-visual-frame img {
    height: 220px;
  }

  .hero-floating-pill {
    position: absolute;
    font-size: 0.72rem;
    padding: 0.35rem 0.65rem;
    max-width: 82%;
    white-space: normal;
    line-height: 1.25;
  }

  .hero-floating-pill.pill-top-left {
    top: -10px;
    left: 8px;
  }

  .hero-floating-pill.pill-bottom-right {
    bottom: -10px;
    right: 8px;
  }

  .hero-cyber-backdrop {
    inset: 0.5rem 0.5rem;
    display: block;
  }

  .cyber-hud-corner {
    width: 16px;
    height: 16px;
  }

  .cyber-hud-telemetry {
    font-size: 0.62rem;
    padding: 2px 6px;
  }

  .cyber-hud-telemetry.hud-right {
    display: none;
  }
}'''

if old_640 in css:
    css = css.replace(old_640, new_640)
    print("[OK] Replaced @media (max-width: 640px) block")
else:
    print("[WARN] Could not find exact old_640")

# 4. Update @media (max-width: 425px)
old_425 = '''/* Mobile Large (<= 425px) */
@media (max-width: 425px) {
  .hero-pill-actions {
    flex-direction: column;
    width: 100%;
  }

  .hero-pill-actions .btn {
    width: 100%;
  }

  .container,
  .container-narrow {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .btn {
    width: 100%;
  }

  .hero-cta-group {
    flex-direction: column;
    width: 100%;
  }

  .hero-cta-group .btn {
    width: 100%;
  }

  .hero-floating-pill {
    position: static;
    margin-bottom: 0.85rem;
    display: inline-flex;
  }

  .hero-visual-card {
    padding: 1.25rem 1rem;
  }

  .form-card {
    padding: 1.5rem 1rem;
  }

  .phone-input-group {
    grid-template-columns: 1fr;
  }

  .sim-content-grid {
    grid-template-columns: 1fr;
  }

  .social-buttons-grid {
    grid-template-columns: 1fr;
  }

  .cyber-sim-box {
    padding: 1.5rem 1rem;
  }

  #sim-perimeter-form {
    grid-template-columns: 1fr !important;
  }

  #sim-perimeter-form .btn {
    width: 100%;
  }
}'''

new_425 = '''/* Mobile Large (<= 425px) */
@media (max-width: 425px) {
  .hero-pill-actions {
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }

  .hero-pill-actions .btn {
    width: 100%;
  }

  .container,
  .container-narrow {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .hero-cta-group {
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }

  .hero-cta-group .btn {
    width: 100%;
  }

  .page-hero-content div[style*="display: flex"] {
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }

  .page-hero-content div[style*="display: flex"] .btn {
    width: 100%;
  }

  .hero-visual-frame img {
    height: 190px;
  }

  .hero-floating-pill {
    font-size: 0.68rem;
    padding: 0.3rem 0.55rem;
    max-width: 80%;
  }

  .hero-visual-card {
    padding: 1.25rem 1rem;
  }

  .form-card {
    padding: 1.5rem 1rem;
  }

  .auth-form-card {
    padding: 1.75rem 1.15rem;
  }

  .phone-input-group {
    grid-template-columns: 1fr;
  }

  .sim-content-grid {
    grid-template-columns: 1fr;
  }

  .social-buttons-grid {
    grid-template-columns: 1fr;
  }

  .cyber-sim-box {
    padding: 1.5rem 1rem;
  }

  #sim-perimeter-form {
    grid-template-columns: 1fr !important;
  }

  #sim-perimeter-form .btn {
    width: 100%;
  }
}'''

if old_425 in css:
    css = css.replace(old_425, new_425)
    print("[OK] Replaced @media (max-width: 425px) block")
else:
    print("[WARN] Could not find exact old_425")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css successfully updated with all mobile responsive improvements!")

