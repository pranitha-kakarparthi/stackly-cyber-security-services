/**
 * STACKLY CYBER SECURITY SERVICES - DASHBOARD CONTROLLER
 * Session Authorization, Role Adaptation, Dynamic Time Greeting,
 * Sidebar Collapse & Mobile Full-Screen Drawer, and 404 Action Button Handlers.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Session Guard Check
  const currentUser = checkAuthSession();
  if (!currentUser) return;

  // 2. Render User Details & Dynamic Greeting
  renderUserTopBar(currentUser);
  initSidebarControls();
  initRoleSwitcher(currentUser);
  initDashboardModules(currentUser.role);
  initDashboardActionButtons();
});

/* Session Authentication Guard */
function checkAuthSession() {
  try {
    const sessionStr = localStorage.getItem('stackly_cyber_currentUser');
    if (!sessionStr) {
      window.location.href = 'sign-in.html';
      return null;
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

/* Render User Details & Time-Aware Greeting */
function renderUserTopBar(user) {
  const greetingEl = document.getElementById('dash-user-greeting');
  const nameEl = document.getElementById('dash-user-name');
  const roleEl = document.getElementById('dash-user-role');
  const avatarEl = document.getElementById('dash-user-avatar');
  const timestampEl = document.getElementById('dash-user-timestamp');

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
    greetingEl.textContent = `${timeGreeting}, ${user.name || 'Security Commander'}`;
  }
  if (nameEl) {
    nameEl.textContent = user.name || user.email;
  }
  if (roleEl) {
    roleEl.textContent = user.role || 'Security Administrator';
  }
  if (avatarEl) {
    const initials = (user.name || user.email || 'SC').charAt(0).toUpperCase();
    avatarEl.textContent = initials;
  }
  if (timestampEl) {
    const loginTime = user.lastLoginTime || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    timestampEl.textContent = `Session Active • Last Authenticated: Today at ${loginTime}`;
  }

  // Sign out button
  const signoutBtn = document.getElementById('dash-signout-btn');
  if (signoutBtn) {
    signoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      localStorage.removeItem('stackly_cyber_currentUser');
      localStorage.removeItem('stackly_cyber_role');
      window.location.href = 'sign-in.html';
    });
  }
}

/* Sidebar Toggle & Mobile Full-Screen Drawer */
function initSidebarControls() {
  const sidebar = document.getElementById('dash-sidebar');
  const collapseBtn = document.getElementById('sidebar-collapse-btn');
  const mobileToggle = document.getElementById('mobile-dash-toggle');
  const mobileCloseBtn = document.getElementById('mobile-sidebar-close-btn');

  if (collapseBtn && sidebar) {
    collapseBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
      const isCollapsed = sidebar.classList.contains('collapsed');
      collapseBtn.setAttribute('aria-expanded', !isCollapsed);
    });
  }

  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = sidebar.classList.toggle('mobile-open');
      document.body.classList.toggle('drawer-open', isOpen);
    });
  }

  if (mobileCloseBtn && sidebar) {
    mobileCloseBtn.addEventListener('click', () => {
      sidebar.classList.remove('mobile-open');
      document.body.classList.remove('drawer-open');
    });
  }
}

/* Role Selector to dynamically adapt dashboard view */
function initRoleSwitcher(currentUser) {
  const roleSelect = document.getElementById('dash-role-selector');
  if (!roleSelect) return;

  roleSelect.value = currentUser.role || 'Security Administrator';

  roleSelect.addEventListener('change', () => {
    const newRole = roleSelect.value;
    currentUser.role = newRole;
    localStorage.setItem('stackly_cyber_currentUser', JSON.stringify(currentUser));
    localStorage.setItem('stackly_cyber_role', newRole);
    renderUserTopBar(currentUser);
    initDashboardModules(newRole);
  });
}

/* Show Role-Specific Sections & Tab Navigation */
function initDashboardModules(role) {
  const currentRole = role || 'Security Administrator';
  
  // Show/Hide role specific content containers
  const adminView = document.getElementById('view-role-admin');
  const socView = document.getElementById('view-role-soc');
  const clientView = document.getElementById('view-role-client');
  const auditorView = document.getElementById('view-role-auditor');

  const views = [adminView, socView, clientView, auditorView];
  views.forEach(v => {
    if (v) v.style.display = 'none';
  });

  if (currentRole.includes('Admin') && adminView) {
    adminView.style.display = 'block';
  } else if (currentRole.includes('SOC') && socView) {
    socView.style.display = 'block';
  } else if (currentRole.includes('Client') && clientView) {
    clientView.style.display = 'block';
  } else if (currentRole.includes('Auditor') && auditorView) {
    auditorView.style.display = 'block';
  } else if (adminView) {
    adminView.style.display = 'block';
  }

  // Sidebar item tab switching
  const navItems = document.querySelectorAll('.dash-nav-item');
  navItems.forEach(item => {
    item.addEventListener('click', () => {
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

      // Close mobile sidebar if open
      const sidebar = document.getElementById('dash-sidebar');
      if (sidebar && sidebar.classList.contains('mobile-open')) {
        sidebar.classList.remove('mobile-open');
        document.body.classList.remove('drawer-open');
      }
    });
  });
}

/* Ensure all action buttons inside dashboard redirect to 404 page */
function initDashboardActionButtons() {
  const actionButtons = document.querySelectorAll('.dash-action-btn, [data-action="404"]');
  actionButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.location.href = '404.html';
    });
  });
}

