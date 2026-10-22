import re

# ==============================================================================
# 1. UPDATE pages/dashboard.html
# ==============================================================================
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove sidebar role switcher ("view as option in dashboard pages")
old_role_box = '''      <!-- Role Switcher in Sidebar (Enables seamless testing of all 3 official roles) -->
      <div class="dash-sidebar-rolebox">
        <div class="role-switcher-label">Active Security View</div>
        <select id="dash-role-selector" class="role-select-box" aria-label="Switch Role Dashboard">
          <option value="Chief Information Security Officer (CISO)">🛡️ CISO Executive View</option>
          <option value="Lead SOC Operations Commander">⚡ SOC Commander View</option>
          <option value="Enterprise Client IT Director">🏢 Enterprise Client View</option>
        </select>
      </div>'''

html_norm = html.replace('\r\n', '\n')
old_role_box_norm = old_role_box.replace('\r\n', '\n')
if old_role_box_norm in html_norm:
    html_norm = html_norm.replace(old_role_box_norm, '')
    print("Removed 'view as' rolebox from dashboard.html")
else:
    # Try alternate regex for rolebox
    html_norm = re.sub(r'<div class="dash-sidebar-rolebox">.*?</div>\s*</aside>', '</aside>', html_norm, flags=re.DOTALL)
    print("Removed 'view as' rolebox (via regex) from dashboard.html")

# Replace Sign Out button icon with modern SVG icon
old_signout_btn = '''          <!-- Primary CTA: Sign Out Button (clears session and returns to sign-in page) -->
          <button type="button" class="btn btn-secondary btn-sm" id="dash-signout-btn">
            <span>🚪</span> Sign Out
          </button>'''

new_signout_btn = '''          <!-- Primary CTA: Sign Out Button (clears session and returns to sign-in page) -->
          <button type="button" class="btn btn-secondary btn-sm" id="dash-signout-btn" aria-label="Sign Out">
            <svg class="signout-svg-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
            <span>Sign Out</span>
          </button>'''

old_so_norm = old_signout_btn.replace('\r\n', '\n')
if old_so_norm in html_norm:
    html_norm = html_norm.replace(old_so_norm, new_signout_btn)
    print("Updated Sign Out button with modern SVG icon in dashboard.html")
else:
    # Try simple button replacement
    html_norm = html_norm.replace('<span>🚪</span> Sign Out', '''<svg class="signout-svg-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg><span>Sign Out</span>''')
    print("Replaced Sign Out icon in dashboard.html")

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_norm)
print("pages/dashboard.html updated successfully!")


# ==============================================================================
# 2. UPDATE assets/css/dashboard.css FOR FIXED SIDEBAR & RESPONSIVE LAYOUT
# ==============================================================================
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dcss = f.read()

# Update .dashboard-layout, .dash-sidebar, .dash-main
dcss_norm = dcss.replace('\r\n', '\n')

old_dlayout = '''.dashboard-layout {
  display: flex;
  min-height: 100vh;
  background: var(--bg-primary);
  position: relative;
  overflow-x: hidden;
}'''

new_dlayout = '''.dashboard-layout {
  display: flex;
  height: 100vh;
  min-height: 100vh;
  overflow: hidden;
  background: var(--bg-primary);
  position: relative;
}'''

if old_dlayout in dcss_norm:
    dcss_norm = dcss_norm.replace(old_dlayout, new_dlayout)

# Update sidebar to fixed
old_sidebar_css = '''.dash-sidebar {
  width: 270px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-cyber);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  transition: width var(--transition-normal), transform var(--transition-normal);
  z-index: 1050;
  position: relative;
}'''

new_sidebar_css = '''.dash-sidebar {
  width: 270px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-cyber);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  transition: width var(--transition-normal), transform var(--transition-normal);
  z-index: 1050;
  overflow-y: auto;
}'''

if old_sidebar_css in dcss_norm:
    dcss_norm = dcss_norm.replace(old_sidebar_css, new_sidebar_css)

# Update .dash-main to scroll with margin
old_dash_main = '''.dash-main {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  overflow-y: auto;
}'''

new_dash_main = '''.dash-main {
  margin-left: 270px;
  width: calc(100% - 270px);
  height: 100vh;
  display: flex;
  flex-direction: column;
  min-width: 0;
  overflow-y: auto;
  overflow-x: hidden;
  background: var(--bg-primary);
  transition: margin-left var(--transition-normal), width var(--transition-normal);
}

.dashboard-layout.sidebar-collapsed .dash-main {
  margin-left: 76px;
  width: calc(100% - 76px);
}

.signout-svg-icon {
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.35rem;
  transition: transform var(--transition-fast), stroke var(--transition-fast);
}

#dash-signout-btn:hover .signout-svg-icon {
  transform: translateX(2px);
  stroke: var(--primary);
}'''

if old_dash_main in dcss_norm:
    dcss_norm = dcss_norm.replace(old_dash_main, new_dash_main)

# Update responsive media query for mobile/tablet
old_mobile_sidebar = '''@media (max-width: 1024px) {
  .dash-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    height: 100vh;
    transform: translateX(-100%);
    box-shadow: 20px 0 50px rgba(0, 0, 0, 0.8);
  }'''

new_mobile_sidebar = '''@media (max-width: 1024px) {
  .dashboard-layout {
    height: auto;
    overflow: visible;
  }
  .dash-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    height: 100vh;
    transform: translateX(-100%);
    box-shadow: 20px 0 50px rgba(0, 0, 0, 0.8);
  }
  .dash-main {
    margin-left: 0 !important;
    width: 100% !important;
    height: auto;
    overflow-y: visible;
  }'''

if old_mobile_sidebar in dcss_norm:
    dcss_norm = dcss_norm.replace(old_mobile_sidebar, new_mobile_sidebar)

with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
    f.write(dcss_norm)
print("assets/css/dashboard.css updated successfully!")


# ==============================================================================
# 3. UPDATE assets/js/dashboard.js (DYNAMIC USERNAME & THREE ROLES)
# ==============================================================================
new_dashboard_js = '''/**
 * STACKLY CYBER SECURITY SERVICES - DASHBOARD CONTROLLER
 * Session Authorization, 3 Dedicated Role Dashboards, Dynamic Time Greeting,
 * Fixed Sidebar Collapse & Mobile Drawer, and Credentials-Dependent Username.
 */

const ROLE_METADATA = {
  'Chief Information Security Officer (CISO)': {
    defaultName: 'Elena Rostova',
    title: 'Chief Information Security Officer (CISO)',
    avatar: 'E',
    viewId: 'view-role-ciso',
    status: 'Executive Governance Enclave Active'
  },
  'Lead SOC Operations Commander': {
    defaultName: 'Alex Vance',
    title: 'Lead SOC Operations Commander',
    avatar: 'A',
    viewId: 'view-role-soc',
    status: 'Live 52k EPS Sensor Stream Active'
  },
  'Enterprise Client IT Director': {
    defaultName: 'Sarah Jenkins',
    title: 'Enterprise Client IT Director',
    avatar: 'S',
    viewId: 'view-role-client',
    status: 'Protected Infrastructure Online'
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // 1. Session Guard Check
  const currentUser = checkAuthSession();
  if (!currentUser) return;

  // Normalize role to one of the 3 supported roles
  normalizeUserRole(currentUser);

  // 2. Render User Details strictly based on login credentials
  renderUserTopBar(currentUser);
  initSidebarControls();
  initDashboardModules(currentUser.role);
  initDashboardActionButtons();
});

/* Normalize any legacy role into the 3 official roles */
function normalizeUserRole(user) {
  const currentRole = user.role || '';
  if (currentRole.includes('SOC') || currentRole.includes('Analyst') || currentRole.includes('Commander')) {
    user.role = 'Lead SOC Operations Commander';
  } else if (currentRole.includes('Client') || currentRole.includes('Enterprise') || currentRole.includes('Director')) {
    user.role = 'Enterprise Client IT Director';
  } else {
    user.role = 'Chief Information Security Officer (CISO)';
  }
}

/* Session Authentication Guard */
function checkAuthSession() {
  try {
    const sessionStr = localStorage.getItem('stackly_cyber_currentUser');
    if (!sessionStr) {
      // Default fallback session if accessed directly
      const defaultUser = {
        isLoggedIn: true,
        name: 'Elena Rostova',
        role: 'Chief Information Security Officer (CISO)',
        email: 'ciso@stackly.security'
      };
      localStorage.setItem('stackly_cyber_currentUser', JSON.stringify(defaultUser));
      localStorage.setItem('stackly_cyber_role', defaultUser.role);
      return defaultUser;
    }
    const user = JSON.parse(sessionStr);
    if (!user || !user.isLoggedIn) {
      window.location.href = 'sign-in.html';
      return null;
    }
    return user;
  } catch (e) {
    window.location.href = 'sign-in.html';
    return null;
  }
}

/* Render User Details strictly based on login credentials */
function renderUserTopBar(user) {
  const greetingEl = document.getElementById('dash-user-greeting');
  const nameEl = document.getElementById('dash-user-name');
  const roleEl = document.getElementById('dash-user-role');
  const avatarEl = document.getElementById('dash-user-avatar');
  const timestampEl = document.getElementById('dash-user-timestamp');

  const meta = ROLE_METADATA[user.role] || ROLE_METADATA['Chief Information Security Officer (CISO)'];

  // User name is dependent strictly on login credentials
  const displayName = user.name || (user.firstName ? `${user.firstName} ${user.lastName || ''}`.trim() : null) || user.username || (user.email ? user.email.split('@')[0] : meta.defaultName);
  const initials = displayName.charAt(0).toUpperCase() || 'O';

  // Dynamic greeting based on current local hour
  const hour = new Date().getHours();
  let timeGreeting = 'Good day';
  if (hour >= 5 && hour < 12) {
    timeGreeting = 'Good morning';
  } else if (hour >= 12 && hour < 17) {
    timeGreeting = 'Good afternoon';
  } else if (hour >= 17 && hour < 22) {
    timeGreeting = 'Good evening';
  } else {
    timeGreeting = 'Good night';
  }

  if (greetingEl) {
    greetingEl.innerHTML = `${timeGreeting}, <strong>${displayName}</strong> <span class="dash-status-badge"><span class="badge-dot"></span> ${meta.status}</span>`;
  }
  if (nameEl) {
    nameEl.textContent = displayName;
  }
  if (roleEl) {
    roleEl.textContent = user.role;
  }
  if (avatarEl) {
    avatarEl.textContent = initials;
  }
  if (timestampEl) {
    const loginTime = user.lastLoginTime || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    timestampEl.textContent = `Zero-Trust Session Active • Authenticated: Today at ${loginTime}`;
  }

  // Sign out button
  const signoutBtn = document.getElementById('dash-signout-btn');
  if (signoutBtn) {
    signoutBtn.onclick = (e) => {
      e.preventDefault();
      localStorage.removeItem('stackly_cyber_currentUser');
      localStorage.removeItem('stackly_cyber_role');
      window.location.href = 'sign-in.html';
    };
  }
}

/* Sidebar Toggle & Mobile Full-Screen Drawer */
function initSidebarControls() {
  const sidebar = document.getElementById('dash-sidebar');
  const layout = document.querySelector('.dashboard-layout');
  const collapseBtn = document.getElementById('sidebar-collapse-btn');
  const mobileToggle = document.getElementById('mobile-dash-toggle');
  const mobileCloseBtn = document.getElementById('mobile-sidebar-close-btn');

  if (collapseBtn && sidebar) {
    collapseBtn.onclick = () => {
      sidebar.classList.toggle('collapsed');
      if (layout) layout.classList.toggle('sidebar-collapsed');
      const isCollapsed = sidebar.classList.contains('collapsed');
      collapseBtn.setAttribute('aria-expanded', !isCollapsed);
    };
  }

  if (mobileToggle && sidebar) {
    mobileToggle.onclick = () => {
      const isOpen = sidebar.classList.toggle('mobile-open');
      document.body.classList.toggle('drawer-open', isOpen);
    };
  }

  if (mobileCloseBtn && sidebar) {
    mobileCloseBtn.onclick = () => {
      sidebar.classList.remove('mobile-open');
      document.body.classList.remove('drawer-open');
    };
  }
}

/* Show Role-Specific Dedicated Dashboard & Sidebar Tab Switching */
function initDashboardModules(role) {
  const currentRole = role || 'Chief Information Security Officer (CISO)';
  
  // Show ONLY the dedicated dashboard for the logged in user's role
  const cisoView = document.getElementById('view-role-ciso');
  const socView = document.getElementById('view-role-soc');
  const clientView = document.getElementById('view-role-client');

  if (cisoView) cisoView.style.display = 'none';
  if (socView) socView.style.display = 'none';
  if (clientView) clientView.style.display = 'none';

  if (currentRole.includes('SOC') || currentRole.includes('Commander')) {
    if (socView) socView.style.display = 'block';
  } else if (currentRole.includes('Client') || currentRole.includes('Director')) {
    if (clientView) clientView.style.display = 'block';
  } else {
    if (cisoView) cisoView.style.display = 'block';
  }

  // Sidebar item tab switching
  const navItems = document.querySelectorAll('.dash-nav-item');
  navItems.forEach(item => {
    item.onclick = () => {
      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');

      const targetSectionId = item.getAttribute('data-target-module');
      if (targetSectionId) {
        document.querySelectorAll('.dash-module-section').forEach(sec => {
          sec.classList.remove('active');
        });
        const targetSec = document.getElementById(targetSectionId);
        if (targetSec) targetSec.classList.add('active');
      }

      // Close mobile drawer on item click
      const sidebar = document.getElementById('dash-sidebar');
      if (sidebar && sidebar.classList.contains('mobile-open')) {
        sidebar.classList.remove('mobile-open');
        document.body.classList.remove('drawer-open');
      }
    };
  });
}

/* Ensure all action buttons inside dashboard redirect to 404 page */
function initDashboardActionButtons() {
  const actionButtons = document.querySelectorAll('.dash-action-btn, [data-action="404"]');
  actionButtons.forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      window.location.href = '404.html';
    };
  });
}
'''

with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
    f.write(new_dashboard_js)
print("assets/js/dashboard.js updated successfully!")

