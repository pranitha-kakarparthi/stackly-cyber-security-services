with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .site-header from sticky to fixed
css = css.replace(
""".site-header {
  position: sticky;
  top: 1rem;
  left: 0;
  width: 100%;
  z-index: 1000;
  pointer-events: none;
  padding: 0 1rem;
  transition: all var(--transition-normal);
}""",
""".site-header {
  position: fixed;
  top: 1rem;
  left: 0;
  width: 100%;
  z-index: 1000;
  pointer-events: none;
  padding: 0 1rem;
  transition: all var(--transition-normal);
}"""
)

# 2. Update .hero-stage base definition
css = css.replace(
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
}""",
""".hero-stage {
  position: relative;
  margin: 0 !important;
  min-height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: clamp(6.5rem, 11vh, 8.25rem) 1.25rem 3.5rem;
  overflow: hidden;
  text-align: center;
}"""
)

# 3. Update .page-hero base definition (line 1410)
css = css.replace(
""".page-hero {
  position: relative;
  padding: 2.5rem 0 2rem;
  overflow: hidden;
  border-bottom: 1.5px solid var(--border-subtle);
}""",
""".page-hero {
  position: relative;
  margin: 0 !important;
  padding: clamp(6.75rem, 12vh, 8.5rem) 0 3.25rem;
  overflow: hidden;
  border-bottom: 1.5px solid var(--border-subtle);
}"""
)

# 4. Update .page-hero enhanced background definition (line 3617)
css = css.replace(
""".page-hero {
  position: relative;
  padding: 2.5rem 0 2rem;
  overflow: hidden;
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 15% 25%, rgba(122, 16, 40, 0.14) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 35%, rgba(217, 119, 6, 0.16) 0%, transparent 65%),
    radial-gradient(ellipse 80% 70% at 50% 95%, rgba(158, 42, 68, 0.09) 0%, transparent 70%);
  border-bottom: 1.5px solid var(--border-subtle);
}""",
""".page-hero {
  position: relative;
  margin: 0 !important;
  padding: clamp(6.75rem, 12vh, 8.5rem) 0 3.25rem;
  overflow: hidden;
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 15% 25%, rgba(122, 16, 40, 0.14) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 35%, rgba(217, 119, 6, 0.16) 0%, transparent 65%),
    radial-gradient(ellipse 80% 70% at 50% 95%, rgba(158, 42, 68, 0.09) 0%, transparent 70%);
  border-bottom: 1.5px solid var(--border-subtle);
}"""
)

# 5. Update .hero-stage enhanced background definition (line 3661)
css = css.replace(
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
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 50% 20%, rgba(122, 16, 40, 0.14) 0%, transparent 70%),
    radial-gradient(ellipse 65% 55% at 15% 45%, rgba(217, 119, 6, 0.15) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 50%, rgba(158, 42, 68, 0.12) 0%, transparent 65%);
}""",
""".hero-stage {
  position: relative;
  margin: 0 !important;
  min-height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: clamp(6.5rem, 11vh, 8.25rem) 1.25rem 3.5rem;
  overflow: hidden;
  text-align: center;
  background-color: var(--bg-main, #FAF7EE);
  background-image:
    radial-gradient(ellipse 75% 65% at 50% 20%, rgba(122, 16, 40, 0.14) 0%, transparent 70%),
    radial-gradient(ellipse 65% 55% at 15% 45%, rgba(217, 119, 6, 0.15) 0%, transparent 65%),
    radial-gradient(ellipse 70% 60% at 85% 50%, rgba(158, 42, 68, 0.12) 0%, transparent 65%);
}"""
)

# 6. Update HUD telemetry positioning so it sits neatly below the navbar and above breadcrumb
css = css.replace(
""".cyber-hud-telemetry.hud-left {
  top: 4px;
  left: 36px;
}

.cyber-hud-telemetry.hud-right {
  top: 4px;
  right: 36px;
}""",
""".cyber-hud-telemetry.hud-left {
  top: clamp(4.85rem, 8vh, 5.75rem);
  left: 2rem;
}

.cyber-hud-telemetry.hud-right {
  top: clamp(4.85rem, 8vh, 5.75rem);
  right: 2rem;
}"""
)

# 7. Update responsive media queries for page-hero and hero-stage
css = css.replace(
"""  /* Subpage Hero Grid Responsive Alignment */
  .page-hero {
    padding: 5.25rem 0 3rem;
  }""",
"""  /* Subpage Hero Grid Responsive Alignment */
  .page-hero {
    padding: 5.75rem 0 2.5rem;
  }"""
)

css = css.replace(
"""  .hero-stage {
    padding: 2.25rem 1rem 2.5rem;
  }""",
"""  .hero-stage {
    padding: 5.75rem 1rem 3rem;
  }"""
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css with margin-to-padding hero layout and HUD alignment")

