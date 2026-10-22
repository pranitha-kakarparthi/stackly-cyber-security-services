with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the topbar block
old_topbar = """.dash-topbar {
  height: 74px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.dash-topbar-left {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.mobile-dash-toggle {
  display: none;
  background: transparent;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  width: 38px;
  height: 38px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.dash-greeting-wrap {
  display: flex;
  flex-direction: column;
}

.dash-greeting {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dash-status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.2rem 0.6rem;
  background: rgba(0, 240, 118, 0.15);
  border: 1px solid rgba(0, 240, 118, 0.35);
  border-radius: var(--radius-full);
  font-size: 0.725rem;
  color: var(--primary);
  font-weight: 600;
}

.dash-timestamp {
  font-size: 0.775rem;
  color: var(--text-muted);
}

.dash-topbar-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.dash-user-profile {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.user-avatar-badge {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00f076 0%, #9333ea 100%);
  color: #03140a;
  font-weight: 800;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.user-text-info {
  display: flex;
  flex-direction: column;
}

.user-display-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-primary);
}

.user-display-role {
  font-size: 0.775rem;
  color: var(--primary);
}"""

new_topbar = """.dash-topbar {
  height: 82px;
  min-height: 82px;
  background: rgba(8, 12, 22, 0.96);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-cyber);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 clamp(1.25rem, 2.5vw, 2.5rem);
  position: sticky;
  top: 0;
  z-index: 1000;
  gap: clamp(1rem, 2.2vw, 2.5rem);
}

.dash-topbar-left {
  display: flex;
  align-items: center;
  gap: clamp(0.85rem, 1.5vw, 1.5rem);
  min-width: 0;
}

.mobile-dash-toggle {
  display: none;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  width: 40px;
  height: 40px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: all var(--transition-fast);
}

.mobile-dash-toggle:hover {
  background: rgba(94, 234, 212, 0.15);
  border-color: var(--primary);
  color: var(--primary);
}

.dash-greeting-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  min-width: 0;
}

.dash-greeting {
  font-size: clamp(1.05rem, 1.35vw, 1.25rem);
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-wrap: wrap;
}

.dash-status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.25rem 0.8rem;
  background: rgba(94, 234, 212, 0.12);
  border: 1px solid rgba(94, 234, 212, 0.35);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  color: var(--primary);
  font-weight: 700;
  letter-spacing: 0.02em;
  white-space: nowrap;
}

.dash-timestamp {
  font-size: 0.8rem;
  color: var(--text-muted);
  letter-spacing: 0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.dash-topbar-right {
  display: flex;
  align-items: center;
  gap: clamp(0.85rem, 1.8vw, 1.75rem);
  flex-shrink: 0;
}

.dash-user-profile {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.4rem 0.95rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-cyber);
  border-radius: var(--radius-full);
  transition: all var(--transition-fast);
}

.dash-user-profile:hover {
  background: rgba(94, 234, 212, 0.08);
  border-color: var(--primary);
}

.user-avatar-badge {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #5eead4 0%, #a78bfa 100%);
  color: #03140a;
  font-weight: 800;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.25);
  flex-shrink: 0;
}

.user-text-info {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.user-display-name {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.2;
}

.user-display-role {
  font-size: 0.76rem;
  color: var(--primary);
  font-weight: 600;
  line-height: 1.2;
}"""

if old_topbar in css:
    css = css.replace(old_topbar, new_topbar)
    print("Replaced topbar styles (LF)")
elif old_topbar.replace('\n', '\r\n') in css:
    css = css.replace(old_topbar.replace('\n', '\r\n'), new_topbar.replace('\n', '\r\n'))
    print("Replaced topbar styles (CRLF)")
else:
    print("WARNING: old_topbar not found")

# Replace media queries block
old_mq = """/* ==========================================================================
   DASHBOARD RESPONSIVENESS
   On smaller screens, when expanded, sidebar spans full width with scroll lock
   ========================================================================== */
@media (max-width: 1024px) {
  .dash-kpi-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .dash-split-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .mobile-dash-toggle {
    display: flex;
  }

  .mobile-only-btn {
    display: flex !important;
  }

  .dash-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw !important;
    height: 100vh;
    transform: translateX(-100%);
    background: #060a14;
    overflow-y: auto;
    z-index: 10000;
  }

  .dash-sidebar.mobile-open {
    transform: translateX(0);
  }

  .dash-topbar {
    padding: 0.75rem 1rem;
    height: auto;
    min-height: 70px;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .dash-topbar-left {
    gap: 0.75rem;
    width: 100%;
    justify-content: space-between;
  }

  .dash-topbar-right {
    width: 100%;
    justify-content: space-between;
    padding-top: 0.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
  }

  .dash-greeting {
    font-size: 1rem;
    flex-wrap: wrap;
  }

  .dash-content {
    padding: 1rem;
    gap: 1.5rem;
  }

  .dash-kpi-grid {
    grid-template-columns: 1fr;
  }

  .user-text-info {
    display: flex;
  }

  .user-display-name {
    font-size: 0.825rem;
  }

  .user-display-role {
    font-size: 0.725rem;
  }

  .dash-quick-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .dash-quick-actions .btn {
    width: 100%;
  }
}

@media (max-width: 375px) {
  .dash-topbar {
    padding: 0.5rem 0.75rem;
  }

  .dash-greeting {
    font-size: 0.925rem;
  }

  .dash-content {
    padding: 0.75rem;
  }

  .kpi-value {
    font-size: 1.65rem;
  }

  .user-text-info {
    display: none;
  }
}"""

new_mq = """/* ==========================================================================
   DASHBOARD RESPONSIVENESS & ALIGNMENT PERFECTION ACROSS ALL SCREENS
   CRITICAL FIX: Reset margin-left and width on .dash-main for all <= 1024px screens
   ========================================================================== */

/* Drawer Backdrop for Mobile */
.dash-drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(3, 7, 18, 0.75);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 9999;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-normal);
}

body.drawer-open .dash-drawer-backdrop {
  opacity: 1;
  pointer-events: auto;
}

/* Tablet Landscape & Small Desktop (<= 1024px) */
@media (max-width: 1024px) {
  .dash-main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100vw !important;
    min-width: 0 !important;
  }

  .dash-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: min(300px, 85vw) !important;
    max-width: 85vw;
    height: 100vh;
    transform: translateX(-100%);
    background: #060a14;
    overflow-y: auto;
    z-index: 10000;
    box-shadow: 10px 0 50px rgba(0, 0, 0, 0.85);
    transition: transform var(--transition-normal);
  }

  .dash-sidebar.mobile-open {
    transform: translateX(0);
  }

  .mobile-dash-toggle {
    display: flex;
  }

  .mobile-only-btn {
    display: flex !important;
  }

  .dash-kpi-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }
  
  .dash-split-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .dash-grid-4 {
    grid-template-columns: repeat(2, 1fr) !important;
  }

  .dash-grid-3 {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

/* Tablet Portrait & Mobile Devices (<= 768px) */
@media (max-width: 768px) {
  .dash-main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100vw !important;
    min-width: 0 !important;
  }

  .dash-topbar {
    padding: 0.85rem 1.15rem;
    height: auto;
    min-height: 76px;
    flex-direction: column;
    align-items: stretch;
    gap: 0.85rem;
  }

  .dash-topbar-left {
    width: 100%;
    justify-content: flex-start;
    gap: 0.85rem;
  }

  .dash-greeting {
    font-size: 1.05rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .dash-topbar-right {
    width: 100%;
    justify-content: space-between;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    gap: 0.75rem;
  }

  .dash-content {
    padding: 1.25rem 1rem;
    gap: 1.75rem;
    width: 100%;
    max-width: 100vw;
    box-sizing: border-box;
  }

  .dash-kpi-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .dash-grid-2,
  .dash-grid-3,
  .dash-grid-4,
  .cards-grid-2,
  .cards-grid-3,
  .cards-grid-4,
  .dash-split-grid {
    grid-template-columns: 1fr !important;
    gap: 1.25rem;
  }

  .dash-panel {
    padding: 1.25rem;
  }

  .dash-panel-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .dash-panel-header .btn,
  .dash-panel-header > div:last-child {
    width: 100%;
    justify-content: flex-start;
  }

  .dash-quick-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }

  .dash-quick-actions .btn {
    width: 100%;
    justify-content: center;
  }

  .user-text-info {
    display: flex;
  }

  .user-display-name {
    font-size: 0.85rem;
  }

  .user-display-role {
    font-size: 0.72rem;
  }
}

/* Compact Mobile (<= 480px) */
@media (max-width: 480px) {
  .dash-topbar {
    padding: 0.75rem 0.85rem;
  }

  .dash-greeting {
    font-size: 0.95rem;
  }

  .dash-timestamp {
    font-size: 0.72rem;
  }

  .dash-content {
    padding: 1rem 0.75rem;
    gap: 1.25rem;
  }

  .kpi-value {
    font-size: 1.75rem;
  }

  .user-text-info {
    display: none;
  }

  .dash-panel {
    padding: 1rem;
  }

  .dash-user-profile {
    padding: 0.25rem 0.5rem;
  }
}"""

if old_mq in css:
    css = css.replace(old_mq, new_mq)
    print("Replaced media queries (LF)")
elif old_mq.replace('\n', '\r\n') in css:
    css = css.replace(old_mq.replace('\n', '\r\n'), new_mq.replace('\n', '\r\n'))
    print("Replaced media queries (CRLF)")
else:
    print("WARNING: old_mq not found")

# Also add helper classes for section layouts
extra_styles = """
/* Additional Layout Helpers for Multi-Section Dashboard */
.dash-section {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.dash-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.dash-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.dash-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.dash-stat-card {
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  transition: all var(--transition-fast);
}

.dash-stat-card:hover {
  border-color: var(--border-cyber);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.dash-stat-val {
  font-size: 1.5rem;
  font-weight: 800;
  font-family: var(--font-mono);
  color: var(--text-primary);
  line-height: 1.2;
}

.dash-stat-lbl {
  font-size: 0.8rem;
  color: var(--text-muted);
}
"""

if '.dash-stat-card' not in css:
    css += extra_styles
    print("Added helper classes for multi-section dashboard")

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved assets/css/dashboard.css successfully")

