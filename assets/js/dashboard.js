/**
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
  initDashboardBackToTop();
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
      if (window.innerWidth <= 1024) {
        sidebar.classList.remove('mobile-open');
        document.body.classList.remove('drawer-open');
      } else {
        sidebar.classList.toggle('collapsed');
        if (layout) layout.classList.toggle('sidebar-collapsed');
        const isCollapsed = sidebar.classList.contains('collapsed');
        collapseBtn.setAttribute('aria-expanded', !isCollapsed);
      }
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

  const backdrop = document.getElementById('dash-drawer-backdrop');
  if (backdrop && sidebar) {
    backdrop.onclick = () => {
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

      // Automatically scroll page to top upon clicking sidebar menu option
      const dashMainArea = document.getElementById('dash-main-area') || document.querySelector('.dash-main');
      if (dashMainArea) {
        dashMainArea.scrollTo({ top: 0, behavior: 'smooth' });
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });

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

/* ==========================================================================
   DASHBOARD BACK TO TOP CONTROLLER
   Scrolls .dash-main and window to top smoothly
   ========================================================================== */
function initDashboardBackToTop() {
  const btn = document.getElementById('back-to-top');
  const dashMain = document.getElementById('dash-main-area') || document.querySelector('.dash-main');
  if (!btn) return;

  const checkScroll = () => {
    const scrollPos = (dashMain ? dashMain.scrollTop : 0) || window.scrollY || 0;
    if (scrollPos > 250) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  };

  if (dashMain) {
    dashMain.addEventListener('scroll', checkScroll, { passive: true });
  }
  window.addEventListener('scroll', checkScroll, { passive: true });
  checkScroll();

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    if (dashMain) {
      dashMain.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
