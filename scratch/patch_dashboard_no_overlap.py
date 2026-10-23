with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Enhance .dash-panel with min-width: 0 and overflow: hidden
css = css.replace(
""".dash-panel {
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  box-shadow: 0 4px 18px rgba(58, 1, 14, 0.04);
  width: 100%;
  box-sizing: border-box;
}""",
""".dash-panel {
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: clamp(1.15rem, 2vw, 1.75rem);
  box-shadow: 0 4px 18px rgba(58, 1, 14, 0.04);
  width: 100%;
  box-sizing: border-box;
  min-width: 0;
  overflow: hidden;
}"""
)

# Enhance mobile dashboard rules to ensure zero overlapping
rules_patch = """
/* Robust Non-Overlapping Mobile Topbar & Panel Header Controls */
.dash-panel-header > * {
  min-width: 0;
}

@media (max-width: 1024px) {
  .dash-panel-header {
    flex-wrap: wrap;
    gap: 0.75rem;
  }
  .dash-grid-3 {
    grid-template-columns: 1fr !important;
  }
}

@media (max-width: 640px) {
  .dash-topbar {
    padding: 0.75rem 0.85rem !important;
  }
  .dash-topbar-left {
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  .dash-greeting {
    font-size: 0.95rem;
  }
  .dash-status-badge {
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
  }
  .dash-topbar-right {
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: space-between;
  }
  .dash-user-profile {
    padding: 0.25rem 0.5rem;
    max-width: calc(100% - 105px);
  }
  .user-display-name {
    font-size: 0.8rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 120px;
  }
  .user-display-role {
    display: none;
  }
  #dash-signout-btn {
    padding: 0.35rem 0.75rem;
    font-size: 0.8rem;
    flex-shrink: 0;
  }
}
"""

if 'Robust Non-Overlapping Mobile Topbar' not in css:
    css += rules_patch
    with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated assets/css/dashboard.css with non-overlapping rules")
else:
    print("Rules already present")

