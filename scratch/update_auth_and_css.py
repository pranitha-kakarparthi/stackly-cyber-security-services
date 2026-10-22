import re

# ==============================================================================
# 1. UPDATE pages/sign-in.html
# ==============================================================================
with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    signin = f.read()

# Fix brand icon size and remove back to home in left part
old_header = '''      <div class="auth-banner-header">
        <a href="../index.html" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Logo" height="38" width="auto">
        </a>
        <a href="../index.html" class="btn btn-outline btn-sm">
          <span>←</span> Back to Home
        </a>
      </div>'''

new_header = '''      <div class="auth-banner-header">
        <a href="../index.html" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="auth-brand-logo" width="160" height="40">
        </a>
      </div>'''

signin_norm = signin.replace('\r\n', '\n')
old_header_norm = old_header.replace('\r\n', '\n')
if old_header_norm in signin_norm:
    signin = signin_norm.replace(old_header_norm, new_header)
    print("Updated banner header in sign-in.html")
else:
    print("Warning: old_header not found in sign-in.html")

# Update role select with "Select One"
old_role_select = '''          <select id="signin-role" name="role" class="form-control" required aria-required="true">
            <option value="Chief Information Security Officer (CISO)" selected>🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>'''

new_role_select = '''          <select id="signin-role" name="role" class="form-control" required aria-required="true" aria-describedby="signin-role-error">
            <option value="" disabled selected>Select One</option>
            <option value="Chief Information Security Officer (CISO)">🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>
          <div id="signin-role-error" class="error-message" role="alert">
            <span>❌</span> Please select a security clearance role.
          </div>'''

signin_norm = signin.replace('\r\n', '\n')
old_role_norm = old_role_select.replace('\r\n', '\n')
if old_role_norm in signin_norm:
    signin = signin_norm.replace(old_role_norm, new_role_select)
    print("Updated role select in sign-in.html with 'Select One'")
else:
    print("Warning: old_role_select not found in sign-in.html")

with open('pages/sign-in.html', 'w', encoding='utf-8') as f:
    f.write(signin)
print("pages/sign-in.html updated successfully!")


# ==============================================================================
# 2. UPDATE pages/sign-up.html
# ==============================================================================
with open('pages/sign-up.html', 'r', encoding='utf-8') as f:
    signup = f.read()

# Fix brand icon size and remove back to home in left part
signup_norm = signup.replace('\r\n', '\n')
if old_header_norm in signup_norm:
    signup = signup_norm.replace(old_header_norm, new_header)
    print("Updated banner header in sign-up.html")
else:
    print("Warning: old_header not found in sign-up.html")

# Update country code select with "Select One"
old_cc = '''            <select id="signup-country-code" class="form-control" aria-label="Select Country Code">
              <option value="+91" selected>🇮🇳 +91</option>
              <option value="+1">🇺🇸 +1</option>
              <option value="+44">🇬🇧 +44</option>
              <option value="+65">🇸🇬 +65</option>
              <option value="+61">🇦🇺 +61</option>
              <option value="+49">🇩🇪 +49</option>
            </select>'''

new_cc = '''            <select id="signup-country-code" class="form-control" aria-label="Select Country Code">
              <option value="" disabled selected>Select One</option>
              <option value="+91">🇮🇳 +91 (India)</option>
              <option value="+1">🇺🇸 +1 (USA)</option>
              <option value="+44">🇬🇧 +44 (UK)</option>
              <option value="+65">🇸🇬 +65 (Singapore)</option>
              <option value="+61">🇦🇺 +61 (Australia)</option>
              <option value="+49">🇩🇪 +49 (Germany)</option>
            </select>'''

signup_norm = signup.replace('\r\n', '\n')
old_cc_norm = old_cc.replace('\r\n', '\n')
if old_cc_norm in signup_norm:
    signup = signup_norm.replace(old_cc_norm, new_cc)
    print("Updated country code select in sign-up.html with 'Select One'")
else:
    print("Warning: old_cc not found in sign-up.html")

# Update role select with "Select One"
old_signup_role = '''          <select id="signup-role" name="role" class="form-control" required aria-required="true">
            <option value="" disabled selected>Select Security Clearance Role</option>
            <option value="Chief Information Security Officer (CISO)">🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>'''

new_signup_role = '''          <select id="signup-role" name="role" class="form-control" required aria-required="true">
            <option value="" disabled selected>Select One</option>
            <option value="Chief Information Security Officer (CISO)">🛡️ Chief Information Security Officer (CISO)</option>
            <option value="Lead SOC Operations Commander">⚡ Lead SOC Operations Commander</option>
            <option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>
          </select>'''

signup_norm = signup.replace('\r\n', '\n')
old_signup_role_norm = old_signup_role.replace('\r\n', '\n')
if old_signup_role_norm in signup_norm:
    signup = signup_norm.replace(old_signup_role_norm, new_signup_role)
    print("Updated role select in sign-up.html with 'Select One'")
else:
    print("Warning: old_signup_role not found in sign-up.html")

# Remove profile avatar option from sign-up.html
old_avatar = '''        <!-- Profile Avatar Upload (UI Only, Optional) -->
        <div class="form-group">
          <label for="signup-avatar" class="form-label">
            <span>Profile Avatar (Optional)</span>
            <span class="optional-mark">UI Demonstration</span>
          </label>
          <input type="file" id="signup-avatar" class="form-control" accept="image/*">
        </div>'''

signup_norm = signup.replace('\r\n', '\n')
old_avatar_norm = old_avatar.replace('\r\n', '\n')
if old_avatar_norm in signup_norm:
    signup = signup_norm.replace(old_avatar_norm, '')
    print("Removed profile avatar upload from sign-up.html")
else:
    print("Warning: old_avatar not found in sign-up.html")

with open('pages/sign-up.html', 'w', encoding='utf-8') as f:
    f.write(signup)
print("pages/sign-up.html updated successfully!")


# ==============================================================================
# 3. UPDATE assets/css/style.css FOR FIXED LEFT BANNER & BRAND LOGO SIZE
# ==============================================================================
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .auth-banner-side to be sticky/fixed
old_banner_side = '''.auth-banner-side {
  background: linear-gradient(145deg, #0a1122 0%, #060a14 100%);
  border-right: 1px solid var(--border-subtle);
  padding: 3.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}'''

new_banner_side = '''.auth-banner-side {
  background: linear-gradient(145deg, #0a1122 0%, #060a14 100%);
  border-right: 1px solid var(--border-subtle);
  padding: 3.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  z-index: 10;
}

.auth-brand-logo {
  height: 40px !important;
  width: auto !important;
  max-width: 170px !important;
  object-fit: contain;
  display: inline-block;
  filter: drop-shadow(0 0 12px rgba(94, 234, 212, 0.45));
  transition: transform var(--transition-fast);
}

.auth-brand-logo:hover {
  transform: scale(1.04);
}'''

css_norm = css.replace('\r\n', '\n')
old_banner_norm = old_banner_side.replace('\r\n', '\n')
if old_banner_norm in css_norm:
    css = css_norm.replace(old_banner_norm, new_banner_side)
    print("Updated .auth-banner-side and added .auth-brand-logo in style.css")
else:
    print("Warning: old_banner_side not found in style.css")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("assets/css/style.css updated successfully!")


# ==============================================================================
# 4. UPDATE assets/js/auth.js FOR FORM VALIDATION & DYNAMIC USERNAME
# ==============================================================================
with open('assets/js/auth.js', 'r', encoding='utf-8') as f:
    auth_js = f.read()

# Make sure login preserves entered user credentials or registers new profile
old_login_handler = '''    // Role validation
    const selectedRole = roleSelect ? roleSelect.value : 'Security Administrator';

    if (!isValid) {
      if (firstInvalidField) firstInvalidField.focus();
      return;
    }

    // Successful login simulation (Accepts any valid formatted credentials or matching demo user)
    const users = auth.getUsers();
    let matchedUser = users.find(u => u.email.toLowerCase() === emailVal.toLowerCase());

    if (!matchedUser) {
      // Create user profile for arbitrary valid credentials
      matchedUser = {
        firstName: emailVal.split('@')[0],
        lastName: 'Officer',
        email: emailVal,
        role: selectedRole
      };
    } else {
      matchedUser.role = selectedRole; // Update with selected role
    }

    auth.login(matchedUser, selectedRole);'''

new_login_handler = '''    // Role validation (Strict: require user to select one)
    const selectedRole = roleSelect ? roleSelect.value : '';
    const roleError = document.getElementById('signin-role-error');
    if (!selectedRole) {
      isValid = false;
      if (roleSelect) roleSelect.classList.add('has-error');
      if (roleError) roleError.style.display = 'block';
      if (!firstInvalidField) firstInvalidField = roleSelect;
    } else {
      if (roleSelect) roleSelect.classList.remove('has-error');
      if (roleError) roleError.style.display = 'none';
    }

    if (!isValid) {
      if (firstInvalidField) firstInvalidField.focus();
      return;
    }

    // Successful login: Name is derived directly from login credentials
    const users = auth.getUsers();
    let matchedUser = users.find(u => u.email.toLowerCase() === emailVal.toLowerCase());

    if (!matchedUser) {
      // Format username nicely from email: e.g. "john.doe" -> "John Doe"
      const rawUserPart = emailVal.split('@')[0];
      const cleanName = rawUserPart.split(/[._-]/).map(part => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase()).join(' ') || 'Security Commander';
      
      matchedUser = {
        firstName: cleanName.split(' ')[0] || cleanName,
        lastName: cleanName.split(' ').slice(1).join(' ') || 'Officer',
        name: cleanName,
        email: emailVal,
        role: selectedRole
      };
    } else {
      matchedUser.role = selectedRole;
    }

    auth.login(matchedUser, selectedRole);'''

auth_norm = auth_js.replace('\r\n', '\n')
old_login_norm = old_login_handler.replace('\r\n', '\n')
if old_login_norm in auth_norm:
    auth_js = auth_norm.replace(old_login_norm, new_login_handler)
    print("Updated login handler in auth.js with role check & dynamic credentials name")
else:
    print("Warning: old_login_handler not found in auth.js")

with open('assets/js/auth.js', 'w', encoding='utf-8') as f:
    f.write(auth_js)
print("assets/js/auth.js updated successfully!")

