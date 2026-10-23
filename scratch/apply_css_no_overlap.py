# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .section padding from 5.5rem to 3.5rem
css = css.replace(
""".section {
  padding: 5.5rem 0;
  position: relative;
}""",
""".section {
  padding: 3.5rem 0;
  position: relative;
}"""
)

# Update .hero-title-giant white-space to normal and flex-wrap
css = css.replace(
""".hero-title-giant {
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
}""",
""".hero-title-giant {
  font-size: clamp(2rem, 6.2vw, 4.8rem);
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.05;
  text-transform: uppercase;
  margin: 0.25rem 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  white-space: normal;
  word-break: break-word;
  max-width: 100%;
}"""
)

# In @media (max-width: 1024px), make sure hero-sentinel-stage and hero-title-overlay stack cleanly without overlap
css = css.replace(
"""  .hero-sentinel-stage {
    margin: 2rem auto 0;
  }""",
"""  .hero-sentinel-stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.25rem;
    margin: 1.25rem auto 0;
    width: 100%;
  }

  .hero-title-overlay {
    position: static;
    top: auto;
    width: 100%;
    margin-bottom: 0.75rem;
    z-index: 20;
    pointer-events: auto;
  }"""
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/css/style.css successfully")

# 2. Update dashboard.css
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dcss = f.read()

# Update .dash-panel-title to prevent squishing and enable wrapping
dcss = dcss.replace(
""".dash-panel-title {
  font-size: 1.15rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-primary);
}""",
""".dash-panel-title {
  font-size: clamp(1rem, 1.25vw, 1.15rem);
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  color: var(--text-primary);
  line-height: 1.35;
  word-break: break-word;
  max-width: 100%;
}"""
)

# Add .dash-stat-card wrapping rule if not present
stat_card_block = """.dash-stat-card {
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  transition: all var(--transition-fast);
  box-shadow: 0 4px 14px rgba(58, 1, 14, 0.03);
  min-width: 0;
  box-sizing: border-box;
}"""

stat_card_replacement = """.dash-stat-card {
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  transition: all var(--transition-fast);
  box-shadow: 0 4px 14px rgba(58, 1, 14, 0.03);
  min-width: 0;
  box-sizing: border-box;
  word-break: break-word;
  overflow-wrap: break-word;
}

.dash-stat-card > div:first-child {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.dash-stat-card [style*="font-family: var(--font-mono)"],
.dash-stat-card code,
.dash-stat-card pre {
  word-break: break-all;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}"""

if stat_card_block in dcss:
    dcss = dcss.replace(stat_card_block, stat_card_replacement)

# In @media (max-width: 1024px), ensure dash-grid-2 breaks cleanly
dcss = dcss.replace(
"""  .dash-split-grid {
    grid-template-columns: 1fr !important;
    gap: 1.5rem;
  }""",
"""  .dash-split-grid,
  .dash-grid-2 {
    grid-template-columns: 1fr !important;
    gap: 1.25rem;
  }"""
)

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(dcss)
print("Updated assets/css/dashboard.css successfully")

