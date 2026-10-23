with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update drawer-open styles
css = css.replace(
"""body.drawer-open {
  overflow: hidden !important;
  touch-action: none;
}""",
"""html.drawer-open,
body.drawer-open {
  overflow: hidden !important;
  position: fixed !important;
  width: 100% !important;
  height: 100% !important;
  touch-action: none !important;
}"""
)

# 2. Update .mobile-nav-overlay
css = css.replace(
""".mobile-nav-overlay {
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
}""",
""".mobile-nav-overlay {
  display: none;
  position: fixed !important;
  inset: 0 !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  max-height: 100vh !important;
  max-height: 100dvh !important;
  background: rgba(250, 247, 238, 0.98);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  z-index: 1001;
  padding: 5rem 1.5rem 2.5rem;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  touch-action: pan-y !important;
  overscroll-behavior: contain;
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--transition-normal), visibility var(--transition-normal);
}"""
)

# 3. Spacing adjustments: remove extra padding at top and bottom
# Update .hero-stage in line 1044
css = css.replace(
""".hero-stage {
  position: relative;
  min-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 4.25rem 1.25rem 4.5rem;
  overflow: hidden;
  text-align: center;
}""",
""".hero-stage {
  position: relative;
  min-height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 2.25rem 1.25rem 2.5rem;
  overflow: hidden;
  text-align: center;
}"""
)

# Update .hero-stage in line 3595
css = css.replace(
""".hero-stage {
  position: relative;
  min-height: 94vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 4.5rem 1.25rem 5rem;
  overflow: hidden;
  text-align: center;""",
""".hero-stage {
  position: relative;
  min-height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 2.25rem 1.25rem 2.5rem;
  overflow: hidden;
  text-align: center;"""
)

# Update .page-hero in line 1368
css = css.replace(
""".page-hero {
  position: relative;
  padding: 5.25rem 0 4rem;
  overflow: hidden;
  border-bottom: 1.5px solid var(--border-subtle);
}""",
""".page-hero {
  position: relative;
  padding: 2.5rem 0 2rem;
  overflow: hidden;
  border-bottom: 1.5px solid var(--border-subtle);
}"""
)

# Update .page-hero in line 3551
css = css.replace(
""".page-hero {
  position: relative;
  padding: 5.25rem 0 4.25rem;
  overflow: hidden;""",
""".page-hero {
  position: relative;
  padding: 2.5rem 0 2rem;
  overflow: hidden;"""
)

# Update .site-footer in line 2808
css = css.replace(
""".site-footer {
  background: #250109;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  color: #faf7ee;
  padding: 4.5rem 0 2rem;
  margin-top: auto;
  position: relative;
}""",
""".site-footer {
  background: #250109;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  color: #faf7ee;
  padding: 2.75rem 0 1.5rem;
  margin-top: auto;
  position: relative;
}"""
)

# Update .footer-bottom in line 2883
css = css.replace(
""".footer-bottom {
  margin-top: 3.5rem;
  padding-top: 2rem;""",
""".footer-bottom {
  margin-top: 2rem;
  padding-top: 1.25rem;"""
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css with scroll lock, drawer properties, and tightened top/bottom spacing")

