import re

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace base .dash-topbar section (lines ~258 to ~407)
base_topbar_target = re.search(r'\.dash-topbar\s*\{.*?(?=\/\*\s*==+\s*\r?\n\s*DASHBOARD CONTENT)', css, re.DOTALL)
if not base_topbar_target:
    print("ERROR: could not find base .dash-topbar block")
else:
    new_base_topbar = """/* ==========================================================================
   DASHBOARD TOPBAR NAVIGATION
   Generous spacing, crystal clear typography, non-overlapping responsive flow
   ========================================================================== */
.dash-topbar {
  min-height: 84px;
  background: rgba(250, 247, 238, 0.98);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem clamp(1.25rem, 2.5vw, 2.75rem);
  position: sticky;
  top: 0;
  z-index: 1000;
  gap: clamp(1rem, 2vw, 2.25rem);
  box-sizing: border-box;
}

.dash-topbar-left {
  display: flex;
  align-items: center;
  gap: clamp(0.85rem, 1.5vw, 1.5rem);
  min-width: 0;
  flex: 1;
}

.mobile-dash-toggle {
  display: none;
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  width: 42px;
  height: 42px;
  min-width: 42px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: all var(--transition-fast);
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.05);
  font-size: 1.15rem;
}

.mobile-dash-toggle:hover {
  background: rgba(122, 16, 40, 0.08);
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-1px);
}

.dash-greeting-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  min-width: 0;
  flex: 1;
}

.dash-greeting {
  min-width: 0;
}

#dash-user-greeting {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  row-gap: 0.35rem;
  flex-wrap: wrap;
}

.dash-greeting-salute {
  font-size: clamp(1.1rem, 1.35vw, 1.3rem);
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
  white-space: nowrap;
}

.dash-status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.22rem 0.75rem;
  background: rgba(122, 16, 40, 0.08);
  border: 1px solid rgba(122, 16, 40, 0.25);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  color: var(--primary);
  font-weight: 700;
  letter-spacing: 0.02em;
  white-space: nowrap;
  line-height: 1.25;
}

.dash-timestamp {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-family: var(--font-mono);
  letter-spacing: 0.01em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: 1.35;
}

.dash-topbar-right {
  display: flex;
  align-items: center;
  gap: clamp(0.75rem, 1.25vw, 1.25rem);
  flex-shrink: 0;
}

/* Notification Bell Action Button */
.dash-notif-btn {
  width: 42px;
  height: 42px;
  min-width: 42px;
  border-radius: var(--radius-full);
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  color: var(--text-primary);
  text-decoration: none;
  position: relative;
  transition: all var(--transition-fast);
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.04);
  flex-shrink: 0;
}

.dash-notif-btn:hover {
  background: rgba(122, 16, 40, 0.06);
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(122, 16, 40, 0.08);
}

.dash-notif-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  border-radius: var(--radius-full);
  background: var(--primary);
  color: #FFFFFF;
  font-size: 0.68rem;
  font-weight: 700;
  font-family: var(--font-mono);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--bg-primary);
  box-shadow: 0 2px 5px rgba(122, 16, 40, 0.4);
}

/* User Profile Badge */
.dash-user-profile {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.4rem 1rem 0.4rem 0.5rem;
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-full);
  transition: all var(--transition-fast);
  box-shadow: 0 2px 8px rgba(58, 1, 14, 0.04);
  max-width: 290px;
  flex-shrink: 0;
}

.dash-user-profile:hover {
  background: rgba(122, 16, 40, 0.04);
  border-color: var(--border-cyber);
  box-shadow: 0 4px 12px rgba(122, 16, 40, 0.08);
}

.user-avatar-badge {
  width: 38px;
  height: 38px;
  min-width: 38px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7A1028 0%, #D97706 100%);
  color: #FFFFFF;
  font-weight: 800;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.9);
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(122, 16, 40, 0.3);
}

.user-text-info {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  min-width: 0;
  overflow: hidden;
}

.user-display-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.25;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-display-role {
  font-size: 0.74rem;
  color: var(--primary);
  font-weight: 600;
  line-height: 1.25;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 170px;
}

/* Sign Out Action Button */
#dash-signout-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1.2rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: var(--radius-full);
  white-space: nowrap;
  flex-shrink: 0;
  cursor: pointer;
  background: #FFFFFF;
  color: var(--primary);
  border: 1.5px solid var(--border-cyber);
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.04);
  transition: all var(--transition-fast);
}

#dash-signout-btn:hover {
  background: var(--primary);
  color: #FFFFFF;
  border-color: var(--primary);
  box-shadow: 0 4px 12px rgba(122, 16, 40, 0.2);
  transform: translateY(-1px);
}

#dash-signout-btn:hover .signout-svg-icon {
  stroke: #FFFFFF;
  transform: translateX(2px);
}

"""
    css = css[:base_topbar_target.start()] + new_base_topbar + css[base_topbar_target.end():]
    print("Replaced base .dash-topbar section successfully")

# 2. Update @media (max-width: 1024px) topbar rule
css = re.sub(
    r'\.dash-topbar\s*\{\s*height:\s*auto;\s*min-height:\s*78px;\s*padding:\s*1rem\s*1\.5rem;\s*flex-wrap:\s*wrap;\s*gap:\s*1rem;\s*\}',
    '''.dash-topbar {
    min-height: 80px;
    padding: 0.9rem 1.5rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 1.25rem;
    flex-wrap: nowrap;
  }

  .user-display-role {
    max-width: 130px;
  }

  .dash-user-profile {
    max-width: 230px;
  }''',
    css
)

# 3. Update @media (max-width: 768px) topbar section
old_768_pattern = r'\.dash-topbar\s*\{\s*padding:\s*0\.85rem\s*1rem;\s*height:\s*auto;\s*min-height:\s*76px;\s*flex-direction:\s*column;\s*align-items:\s*stretch;\s*gap:\s*0\.85rem;\s*\}.*?\.dash-topbar-right\s*\{\s*width:\s*100%;\s*justify-content:\s*space-between;\s*padding-top:\s*0\.75rem;\s*border-top:\s*1px\s*solid\s*var\(--border-subtle\);\s*gap:\s*0\.75rem;\s*flex-wrap:\s*wrap;\s*\}'
new_768_replacement = '''.dash-topbar {
    padding: 0.85rem 1rem;
    min-height: auto;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }

  .dash-topbar-left {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    width: 100%;
    min-width: 0;
    flex-wrap: nowrap;
  }

  .dash-greeting-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    min-width: 0;
    flex: 1;
  }

  #dash-user-greeting {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    row-gap: 0.25rem;
  }

  .dash-greeting-salute {
    font-size: 1.05rem;
    font-weight: 700;
  }

  .dash-status-badge {
    font-size: 0.72rem;
    padding: 0.18rem 0.55rem;
  }

  .dash-timestamp {
    font-size: 0.75rem;
    line-height: 1.35;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .dash-topbar-right {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding-top: 0.65rem;
    border-top: 1px solid var(--border-subtle);
    gap: 0.65rem;
  }

  .user-display-role {
    display: none;
  }

  .dash-user-profile {
    padding: 0.3rem 0.75rem 0.3rem 0.35rem;
    gap: 0.5rem;
    max-width: 180px;
  }

  .user-display-name {
    font-size: 0.825rem;
    max-width: 110px;
  }

  #dash-signout-btn {
    padding: 0.45rem 0.95rem;
    font-size: 0.825rem;
  }'''

css, count_768 = re.subn(old_768_pattern, new_768_replacement, css, flags=re.DOTALL)
print(f"Replaced 768px topbar: {count_768}")

# 4. Update @media (max-width: 480px)
old_480_topbar_pattern = r'\.dash-topbar\s*\{\s*padding:\s*0\.75rem\s*0\.85rem;\s*\}.*?\.user-text-info\s*\{\s*display:\s*none;\s*\}'
new_480_topbar_replacement = '''.dash-topbar {
    padding: 0.75rem 0.85rem;
    gap: 0.65rem;
  }

  .mobile-dash-toggle {
    width: 38px;
    height: 38px;
    min-width: 38px;
    font-size: 1.05rem;
  }

  .dash-greeting-salute {
    font-size: 0.95rem;
  }

  .dash-status-badge {
    font-size: 0.7rem;
    padding: 0.15rem 0.5rem;
  }

  .dash-timestamp {
    font-size: 0.72rem;
  }

  .dash-notif-btn {
    width: 36px;
    height: 36px;
    min-width: 36px;
    font-size: 0.95rem;
  }

  .dash-user-profile {
    padding: 0.25rem 0.55rem 0.25rem 0.25rem;
    gap: 0.4rem;
    max-width: 140px;
  }

  .user-avatar-badge {
    width: 32px;
    height: 32px;
    min-width: 32px;
    font-size: 0.85rem;
  }

  .user-display-name {
    font-size: 0.8rem;
    max-width: 80px;
  }

  #dash-signout-btn {
    padding: 0.4rem 0.75rem;
    font-size: 0.8rem;
    gap: 0.35rem;
  }'''

css, count_480 = re.subn(old_480_topbar_pattern, new_480_topbar_replacement, css, flags=re.DOTALL)
print(f"Replaced 480px topbar: {count_480}")

# 5. Remove duplicate/conflicting @media (max-width: 640px) at the bottom and replace with clean <= 360px rule
css = re.sub(
    r'@media\s*\(max-width:\s*640px\)\s*\{.*?\}\s*$',
    '''@media (max-width: 360px) {
  .user-display-name {
    display: none;
  }

  .dash-user-profile {
    padding: 0;
    border: none;
    background: transparent;
    box-shadow: none;
  }

  .dash-user-profile:hover {
    box-shadow: none;
  }

  #dash-signout-btn .signout-text {
    display: none;
  }

  #dash-signout-btn {
    padding: 0;
    width: 36px;
    height: 36px;
    min-width: 36px;
    justify-content: center;
    border-radius: var(--radius-full);
  }

  #dash-signout-btn .signout-svg-icon {
    margin-right: 0;
  }
}
''',
    css,
    flags=re.DOTALL
)

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("dashboard.css updated successfully.")

