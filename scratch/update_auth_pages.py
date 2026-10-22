import re

# ==============================================================================
# 1. UPDATE pages/sign-in.html
# ==============================================================================
with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    signin_html = f.read()

# Remove pre-filled values
signin_html = signin_html.replace('value="admin@stackly.security"', 'autofocus')
signin_html = signin_html.replace('value="Password@123"', '')

# Update role select to exactly three roles
old_role_select = '''          <select id="signin-role" name="role" class="form-control" required aria-required="true">
            <option value="Security Administrator" selected>🛡️ Security Administrator / CISO</option>
            <option value="SOC Analyst / Manager">⚡ SOC Analyst / Shift Commander</option>
            <option value="Enterprise Client">🏢 Enterprise Client / CTO</option>
            <option value="Compliance Auditor">📜 Compliance Auditor (Read-Only)</option>
          </select>'''

new_role_select = '''          <select id="signin-role" name="role" class="form-control" required aria-required="true">
            <option value="Chief Information Security Officer (CISO)" selected>🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>'''

if old_role_select in signin_html:
    signin_html = signin_html.replace(old_role_select, new_role_select)
    print("Updated roles in sign-in.html")
else:
    # Try normalized
    signin_norm = signin_html.replace('\r\n', '\n')
    old_role_norm = old_role_select.replace('\r\n', '\n')
    if old_role_norm in signin_norm:
        signin_html = signin_norm.replace(old_role_norm, new_role_select)
        print("Updated roles (normalized) in sign-in.html")
    else:
        print("Warning: could not find old_role_select in sign-in.html")

# Replace social buttons with SVG brand icons
old_social_grid = '''        <div class="social-buttons-grid">
          <a href="404.html" class="btn-social" aria-label="Sign in with Microsoft Entra">
            <span>🔷</span> Microsoft SSO
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with Google Workspace">
            <span>🔴</span> Google Workspace
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with LinkedIn">
            <span>💼</span> LinkedIn SSO
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with GitHub Enterprise">
            <span>💻</span> GitHub Enterprise
          </a>
        </div>'''

new_social_grid = '''        <div class="social-buttons-grid">
          <a href="404.html" class="btn-social" aria-label="Sign in with Microsoft Entra">
            <svg class="brand-social-svg" viewBox="0 0 23 23" width="18" height="18" aria-hidden="true">
              <path fill="#f35325" d="M1 1h10v10H1z"/>
              <path fill="#81bc06" d="M12 1h10v10H12z"/>
              <path fill="#05a6f0" d="M1 12h10v10H1z"/>
              <path fill="#ffba08" d="M12 12h10v10H12z"/>
            </svg>
            <span>Microsoft SSO</span>
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with Google Workspace">
            <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
            </svg>
            <span>Google Workspace</span>
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with LinkedIn">
            <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="#0a66c2" aria-hidden="true">
              <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
            </svg>
            <span>LinkedIn SSO</span>
          </a>
          <a href="404.html" class="btn-social" aria-label="Sign in with GitHub Enterprise">
            <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
              <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
            </svg>
            <span>GitHub Enterprise</span>
          </a>
        </div>'''

signin_norm = signin_html.replace('\r\n', '\n')
old_social_norm = old_social_grid.replace('\r\n', '\n')
if old_social_norm in signin_norm:
    signin_html = signin_norm.replace(old_social_norm, new_social_grid)
    print("Updated social grid in sign-in.html")
else:
    print("Warning: could not find old_social_grid in sign-in.html")

with open('pages/sign-in.html', 'w', encoding='utf-8') as f:
    f.write(signin_html)
print("pages/sign-in.html updated successfully!")


# ==============================================================================
# 2. UPDATE pages/sign-up.html
# ==============================================================================
with open('pages/sign-up.html', 'r', encoding='utf-8') as f:
    signup_html = f.read()

# Remove pre-filled values
signup_html = signup_html.replace('value="Elena"', 'autofocus')
signup_html = signup_html.replace('value="Rostova"', '')
signup_html = signup_html.replace('value="elena_ciso"', '')
signup_html = signup_html.replace('value="elena@defense.corp"', '')
signup_html = signup_html.replace('value="9876543210"', '')
signup_html = signup_html.replace('value="India"', '')
signup_html = signup_html.replace('value="Chinna Thirupathi, Salem"', '')
signup_html = signup_html.replace('value="Password@123"', '')
signup_html = signup_html.replace('required checked', 'required')

# Update role select to exactly three roles
old_signup_role = '''          <select id="signup-role" name="role" class="form-control" required aria-required="true">
            <option value="Security Administrator" selected>🛡️ Security Administrator / CISO</option>
            <option value="SOC Analyst / Manager">⚡ SOC Analyst / Shift Commander</option>
            <option value="Enterprise Client">🏢 Enterprise Client / CTO</option>
            <option value="Compliance Auditor">📜 Compliance Auditor</option>
          </select>'''

new_signup_role = '''          <select id="signup-role" name="role" class="form-control" required aria-required="true">
            <option value="" disabled selected>Select Security Clearance Role</option>
            <option value="Chief Information Security Officer (CISO)">🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>'''

signup_norm = signup_html.replace('\r\n', '\n')
old_signup_role_norm = old_signup_role.replace('\r\n', '\n')
if old_signup_role_norm in signup_norm:
    signup_html = signup_norm.replace(old_signup_role_norm, new_signup_role)
    print("Updated roles in sign-up.html")
else:
    print("Warning: could not find old_signup_role in sign-up.html")

# Replace social buttons with SVG brand icons in sign-up.html
signup_norm = signup_html.replace('\r\n', '\n')
if old_social_norm in signup_norm:
    signup_html = signup_norm.replace(old_social_norm, new_social_grid)
    print("Updated social grid in sign-up.html")
else:
    print("Warning: could not find old_social_grid in sign-up.html")

with open('pages/sign-up.html', 'w', encoding='utf-8') as f:
    f.write(signup_html)
print("pages/sign-up.html updated successfully!")


# ==============================================================================
# 3. UPDATE assets/js/auth.js
# ==============================================================================
with open('assets/js/auth.js', 'r', encoding='utf-8') as f:
    auth_js = f.read()

# Replace DEFAULT_DEMO_USERS with the 3 official roles
old_demo_users_block = '''const DEFAULT_DEMO_USERS = [
  {
    firstName: 'Alex',
    lastName: 'Morgan',
    username: 'alex_ciso',
    email: 'admin@stackly.security',
    password: 'Password@123',
    role: 'Security Administrator',
    mobile: '9876543210',
    countryCode: '+91',
    country: 'India',
    address: 'MMR Complex, Chinna Thirupathi, Salem',
    avatar: 'A'
  },
  {
    firstName: 'Elena',
    lastName: 'Rostova',
    username: 'elena_soc',
    email: 'soc@stackly.security',
    password: 'Password@123',
    role: 'SOC Analyst / Manager',
    mobile: '9876543211',
    countryCode: '+1',
    country: 'United States',
    address: 'Cyber Defense Command Station 4',
    avatar: 'E'
  },
  {
    firstName: 'Marcus',
    lastName: 'Vance',
    username: 'marcus_client',
    email: 'client@enterprise.com',
    password: 'Password@123',
    role: 'Enterprise Client',
    mobile: '9876543212',
    countryCode: '+44',
    country: 'United Kingdom',
    address: 'FinTech Tower, London',
    avatar: 'M'
  },
  {
    firstName: 'Sarah',
    lastName: 'Chen',
    username: 'sarah_auditor',
    email: 'auditor@compliance.org',
    password: 'Password@123',
    role: 'Compliance Auditor',
    mobile: '9876543213',
    countryCode: '+65',
    country: 'Singapore',
    address: 'ISO Assurance Hub',
    avatar: 'S'
  }
];'''

new_demo_users_block = '''const DEFAULT_DEMO_USERS = [
  {
    firstName: 'Elena',
    lastName: 'Rostova',
    username: 'elena_ciso',
    email: 'ciso@stackly.security',
    password: 'Password@123',
    role: 'Chief Information Security Officer (CISO)',
    mobile: '9876543210',
    countryCode: '+1',
    country: 'United States',
    address: 'Global Cyber Command Station 1',
    avatar: 'E'
  },
  {
    firstName: 'Alex',
    lastName: 'Vance',
    username: 'alex_soc',
    email: 'soc@stackly.security',
    password: 'Password@123',
    role: 'Lead SOC Operations Commander',
    mobile: '9876543211',
    countryCode: '+91',
    country: 'India',
    address: 'MMR Complex, Chinna Thirupathi, Salem',
    avatar: 'A'
  },
  {
    firstName: 'Sarah',
    lastName: 'Jenkins',
    username: 'sarah_client',
    email: 'client@enterprise.com',
    password: 'Password@123',
    role: 'Enterprise Client IT Director',
    mobile: '9876543212',
    countryCode: '+44',
    country: 'United Kingdom',
    address: 'FinTech Enclave, London',
    avatar: 'S'
  }
];'''

auth_norm = auth_js.replace('\r\n', '\n')
old_demo_norm = old_demo_users_block.replace('\r\n', '\n')
if old_demo_norm in auth_norm:
    auth_js = auth_norm.replace(old_demo_norm, new_demo_users_block)
    print("Updated DEFAULT_DEMO_USERS in auth.js")
else:
    print("Warning: could not find old_demo_users_block in auth.js")

# In initSignInForm(): REMOVE automatic filling of values, and focus on first field
old_signin_init = '''  // Auto fill default test values if empty for effortless demonstration
  const emailInput = document.getElementById('signin-email');
  const passwordInput = document.getElementById('signin-password');
  const roleSelect = document.getElementById('signin-role');

  if (emailInput && !emailInput.value) {
    emailInput.value = 'admin@stackly.security';
  }
  if (passwordInput && !passwordInput.value) {
    passwordInput.value = 'Password@123';
  }'''

new_signin_init = '''  const emailInput = document.getElementById('signin-email');
  const passwordInput = document.getElementById('signin-password');
  const roleSelect = document.getElementById('signin-role');

  // Strict: Empty form initially and autofocus first input field
  if (emailInput) {
    emailInput.value = '';
    setTimeout(() => { emailInput.focus(); }, 100);
  }
  if (passwordInput) {
    passwordInput.value = '';
  }'''

auth_norm = auth_js.replace('\r\n', '\n')
old_signin_init_norm = old_signin_init.replace('\r\n', '\n')
if old_signin_init_norm in auth_norm:
    auth_js = auth_norm.replace(old_signin_init_norm, new_signin_init)
    print("Updated initSignInForm in auth.js")
else:
    print("Warning: could not find old_signin_init in auth.js")

# In initSignUpForm(): ensure first field is focused
old_signup_init = '''  const firstNameInput = document.getElementById('signup-firstname');'''
new_signup_init = '''  const firstNameInput = document.getElementById('signup-firstname');
  if (firstNameInput) {
    firstNameInput.value = '';
    setTimeout(() => { firstNameInput.focus(); }, 100);
  }'''

auth_norm = auth_js.replace('\r\n', '\n')
if old_signup_init in auth_norm:
    auth_js = auth_norm.replace(old_signup_init, new_signup_init, 1)
    print("Updated initSignUpForm in auth.js")
else:
    print("Warning: could not find old_signup_init in auth.js")

# Update default role fallback to CISO
auth_js = auth_js.replace("'Security Administrator'", "'Chief Information Security Officer (CISO)'")
auth_js = auth_js.replace('"Security Administrator"', '"Chief Information Security Officer (CISO)"')

with open('assets/js/auth.js', 'w', encoding='utf-8') as f:
    f.write(auth_js)
print("assets/js/auth.js updated successfully!")

