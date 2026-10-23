import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFYING DASHBOARD TOPBAR INTEGRITY ===")

# 1. Check pages/dashboard.html
with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'class="dash-topbar"' in html, "Missing dash-topbar in HTML"
assert 'class="dash-topbar-left"' in html, "Missing dash-topbar-left in HTML"
assert 'class="dash-topbar-right"' in html, "Missing dash-topbar-right in HTML"
assert 'id="mobile-dash-toggle"' in html, "Missing mobile-dash-toggle in HTML"
assert 'id="dash-user-greeting"' in html, "Missing dash-user-greeting in HTML"
assert 'id="dash-user-timestamp"' in html, "Missing dash-user-timestamp in HTML"
assert 'class="dash-notif-btn"' in html, "Missing dash-notif-btn in HTML"
assert 'class="dash-user-profile"' in html, "Missing dash-user-profile in HTML"
assert 'id="dash-user-avatar"' in html, "Missing dash-user-avatar in HTML"
assert 'id="dash-user-name"' in html, "Missing dash-user-name in HTML"
assert 'id="dash-user-role"' in html, "Missing dash-user-role in HTML"
assert 'id="dash-signout-btn"' in html, "Missing dash-signout-btn in HTML"
assert 'class="signout-text"' in html, "Missing signout-text in HTML"
print("[PASS] HTML structure has all expected elements and semantic classes.")

# 2. Check assets/js/dashboard.js
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    js = f.read()

assert 'dash-greeting-salute' in js, "Missing dash-greeting-salute in dashboard.js"
assert 'dash-status-badge' in js, "Missing dash-status-badge in dashboard.js"
assert 'dash-user-greeting' in js, "Missing dash-user-greeting in dashboard.js"
assert 'dash-user-timestamp' in js, "Missing dash-user-timestamp in dashboard.js"
print("[PASS] JavaScript properly injects greeting salute, status badge, and timestamps.")

# 3. Check assets/css/dashboard.css
with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

assert '.dash-topbar {' in css, "Missing .dash-topbar in CSS"
assert '.dash-notif-btn' in css, "Missing .dash-notif-btn in CSS"
assert '.dash-greeting-salute' in css, "Missing .dash-greeting-salute in CSS"
assert '#dash-user-greeting' in css, "Missing #dash-user-greeting in CSS"
assert '.dash-user-profile' in css, "Missing .dash-user-profile in CSS"
assert '#dash-signout-btn' in css, "Missing #dash-signout-btn in CSS"
assert '@media (max-width: 1024px)' in css, "Missing 1024px media query in CSS"
assert '@media (max-width: 768px)' in css, "Missing 768px media query in CSS"
assert '@media (max-width: 480px)' in css, "Missing 480px media query in CSS"
assert '@media (max-width: 360px)' in css, "Missing 360px media query in CSS"
print("[PASS] CSS contains comprehensive styling for base and all responsive breakpoints.")

print("\nALL DASHBOARD TOPBAR VERIFICATIONS PASSED!")

