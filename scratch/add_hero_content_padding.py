with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

rules_to_add = """
/* ==========================================================================
   LARGER SCREEN HERO TEXTUAL CONTENT PADDING & BREADCRUMB ANTI-COLLISION
   Prevents background HUD telemetry and horizontal grid lines from overlapping
   with breadcrumbs (Home / About Us) and badges on desktop and large displays.
   ========================================================================== */
@media (min-width: 992px) {
  .page-hero-grid {
    padding-top: 1.5rem;
  }

  .page-hero-content {
    padding-top: 3.25rem;
  }

  .hero-stage-container {
    padding-top: 2rem;
  }

  .breadcrumb-nav {
    margin-top: 0.5rem;
    margin-bottom: 1.25rem;
  }
}

@media (min-width: 1200px) {
  .page-hero-content {
    padding-top: 3.75rem;
  }

  .page-hero-grid {
    padding-top: 2rem;
  }
}

@media (min-width: 1440px) {
  .page-hero-content {
    padding-top: 4.25rem;
  }
}
"""

if 'LARGER SCREEN HERO TEXTUAL CONTENT PADDING' not in css:
    css += rules_to_add
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added larger screen hero textual content padding rules to style.css")
else:
    print("Rules already present")

