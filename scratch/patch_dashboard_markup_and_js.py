import re

# 1. Update pages/dashboard.html
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()

# Update notification button class and add badge
old_notif = '''          <!-- Notification Bell Icon (redirects to 404 as requested) -->
          <a href="404.html" class="sidebar-collapse-toggle" aria-label="View Security Notifications" title="3 High Severity Alerts">
            <span>🔔</span>
          </a>'''

new_notif = '''          <!-- Notification Bell Icon (redirects to 404 as requested) -->
          <a href="404.html" class="dash-notif-btn" aria-label="View Security Notifications" title="3 High Severity Alerts">
            <span class="dash-notif-icon">🔔</span>
            <span class="dash-notif-badge" aria-hidden="true">3</span>
          </a>'''

if old_notif in dash_html:
    dash_html = dash_html.replace(old_notif, new_notif)
    print("Updated notification bell in pages/dashboard.html")
else:
    print("WARN: old_notif not found in pages/dashboard.html")

# Update signout button to have signout-text span for clean mobile responsiveness
old_signout = '''          <!-- Primary CTA: Sign Out Button (clears session and returns to sign-in page) -->
          <button type="button" class="btn btn-secondary btn-sm" id="dash-signout-btn" aria-label="Sign Out">
            <svg class="signout-svg-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
            <span>Sign Out</span>
          </button>'''

new_signout = '''          <!-- Primary CTA: Sign Out Button (clears session and returns to sign-in page) -->
          <button type="button" class="btn btn-secondary btn-sm" id="dash-signout-btn" aria-label="Sign Out">
            <svg class="signout-svg-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
            <span class="signout-text">Sign Out</span>
          </button>'''

if old_signout in dash_html:
    dash_html = dash_html.replace(old_signout, new_signout)
    print("Updated signout button in pages/dashboard.html")
else:
    print("WARN: old_signout not found in pages/dashboard.html")

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_html)

# 2. Update assets/js/dashboard.js
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

old_js_greeting = 'greetingEl.innerHTML = `${timeGreeting}, <strong>${displayName}</strong> <span class="dash-status-badge"><span class="badge-dot"></span> ${meta.status}</span>`;'
new_js_greeting = 'greetingEl.innerHTML = `<span class="dash-greeting-salute">${timeGreeting}, <strong>${displayName}</strong></span><span class="dash-status-badge"><span class="badge-dot"></span> ${meta.status}</span>`;'

if old_js_greeting in js_content:
    js_content = js_content.replace(old_js_greeting, new_js_greeting)
    print("Updated greeting injection in assets/js/dashboard.js")
else:
    print("WARN: old_js_greeting not found in assets/js/dashboard.js")

with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Dashboard HTML and JS updated.")

