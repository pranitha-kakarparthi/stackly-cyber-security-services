/**
 * STACKLY CYBER SECURITY SERVICES - AUTHENTICATION & STORAGE ENGINE
 * Pure Frontend Session & Account Management using Browser LocalStorage
 * Complies with strict validations, role management, and session persistence.
 */

const STORAGE_KEYS = {
  USERS: 'stackly_cyber_users',
  CURRENT_USER: 'stackly_cyber_currentUser',
  ROLE: 'stackly_cyber_role',
  PREFERENCES: 'stackly_cyber_preferences',
  THEME: 'stackly_cyber_themeSettings',
  NOTIFICATIONS: 'stackly_cyber_notifications',
  SAVED_FORMS: 'stackly_cyber_savedForms'
};

// Seed default users for instant production demo
const DEFAULT_DEMO_USERS = [
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
];

class AuthManager {
  constructor() {
    this.initStorage();
  }

  initStorage() {
    if (!localStorage.getItem(STORAGE_KEYS.USERS)) {
      localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(DEFAULT_DEMO_USERS));
    }
    if (!localStorage.getItem(STORAGE_KEYS.THEME)) {
      localStorage.setItem(STORAGE_KEYS.THEME, JSON.stringify({ mode: 'dark', accent: 'emerald' }));
    }
  }

  getUsers() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.USERS)) || DEFAULT_DEMO_USERS;
    } catch (e) {
      return DEFAULT_DEMO_USERS;
    }
  }

  saveUser(userData) {
    const users = this.getUsers();
    users.push(userData);
    localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(users));
  }

  getCurrentUser() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.CURRENT_USER));
    } catch (e) {
      return null;
    }
  }

  login(user, rememberRole = null) {
    const role = rememberRole || user.role || 'Security Administrator';
    const session = {
      isLoggedIn: true,
      email: user.email,
      name: `${user.firstName || ''} ${user.lastName || ''}`.trim() || user.username || 'Security Officer',
      firstName: user.firstName,
      lastName: user.lastName,
      username: user.username,
      role: role,
      mobile: user.mobile,
      country: user.country,
      loginTimestamp: new Date().toISOString(),
      lastLoginTime: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    localStorage.setItem(STORAGE_KEYS.CURRENT_USER, JSON.stringify(session));
    localStorage.setItem(STORAGE_KEYS.ROLE, role);
    return session;
  }

  logout() {
    localStorage.removeItem(STORAGE_KEYS.CURRENT_USER);
    localStorage.removeItem(STORAGE_KEYS.ROLE);
  }

  isLoggedIn() {
    const user = this.getCurrentUser();
    return !!(user && user.isLoggedIn);
  }
}

const auth = new AuthManager();

// ==========================================================================
// DOM CONTROLLER FOR SIGN IN & SIGN UP FORMS
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  initPasswordToggles();
  initSignInForm();
  initSignUpForm();
});

/* Password Visibility Toggle */
function initPasswordToggles() {
  const toggleBtns = document.querySelectorAll('.password-toggle-btn');
  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const inputId = btn.getAttribute('data-target-input');
      const input = document.getElementById(inputId);
      if (!input) return;

      if (input.type === 'password') {
        input.type = 'text';
        btn.innerHTML = '👁️';
        btn.setAttribute('aria-label', 'Hide password');
      } else {
        input.type = 'password';
        btn.innerHTML = '🔒';
        btn.setAttribute('aria-label', 'Show password');
      }
    });
  });
}

/* SIGN IN FORM CONTROLLER */
function initSignInForm() {
  const form = document.getElementById('signin-form');
  if (!form) return;

  // Auto fill default test values if empty for effortless demonstration
  const emailInput = document.getElementById('signin-email');
  const passwordInput = document.getElementById('signin-password');
  const roleSelect = document.getElementById('signin-role');

  if (emailInput && !emailInput.value) {
    emailInput.value = 'admin@stackly.security';
  }
  if (passwordInput && !passwordInput.value) {
    passwordInput.value = 'Password@123';
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let firstInvalidField = null;
    let isValid = true;

    // Email validation
    const emailVal = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const emailError = document.getElementById('signin-email-error');
    if (!emailVal || !emailRegex.test(emailVal)) {
      isValid = false;
      emailInput.classList.add('has-error');
      if (emailError) emailError.style.display = 'block';
      if (!firstInvalidField) firstInvalidField = emailInput;
    } else {
      emailInput.classList.remove('has-error');
      if (emailError) emailError.style.display = 'none';
    }

    // Password validation
    const passwordVal = passwordInput.value;
    const passwordError = document.getElementById('signin-password-error');
    if (!passwordVal || passwordVal.length < 6) {
      isValid = false;
      passwordInput.classList.add('has-error');
      if (passwordError) passwordError.style.display = 'block';
      if (!firstInvalidField) firstInvalidField = passwordInput;
    } else {
      passwordInput.classList.remove('has-error');
      if (passwordError) passwordError.style.display = 'none';
    }

    // Role validation
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

    auth.login(matchedUser, selectedRole);

    // Show confirmation and redirect to dashboard
    const submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Authenticating Cyber Clearance...';
    }

    setTimeout(() => {
      window.location.href = 'dashboard.html';
    }, 500);
  });
}

/* SIGN UP FORM CONTROLLER */
function initSignUpForm() {
  const form = document.getElementById('signup-form');
  if (!form) return;

  const firstNameInput = document.getElementById('signup-firstname');
  const lastNameInput = document.getElementById('signup-lastname');
  const usernameInput = document.getElementById('signup-username');
  const emailInput = document.getElementById('signup-email');
  const mobileInput = document.getElementById('signup-mobile');
  const countryCodeSelect = document.getElementById('signup-country-code');
  const roleSelect = document.getElementById('signup-role');
  const countryInput = document.getElementById('signup-country');
  const addressInput = document.getElementById('signup-address');
  const passwordInput = document.getElementById('signup-password');
  const confirmPasswordInput = document.getElementById('signup-confirm-password');
  const termsCheckbox = document.getElementById('signup-terms');

  // Real-time password strength checker
  if (passwordInput) {
    passwordInput.addEventListener('input', () => {
      checkPasswordStrength(passwordInput.value);
    });
  }

  // Alphabets-only restriction on name fields
  [firstNameInput, lastNameInput].forEach(inp => {
    if (!inp) return;
    inp.addEventListener('input', () => {
      inp.value = inp.value.replace(/[^A-Za-z\s]/g, '');
    });
  });

  // Mobile number 10 digits restriction
  if (mobileInput) {
    mobileInput.addEventListener('input', () => {
      mobileInput.value = mobileInput.value.replace(/\D/g, '').slice(0, 10);
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let firstInvalid = null;
    let isValid = true;

    // 1. First Name (Letters only, mandatory)
    const fnVal = firstNameInput.value.trim();
    const fnErr = document.getElementById('signup-firstname-error');
    if (!fnVal || !/^[A-Za-z\s]+$/.test(fnVal)) {
      isValid = false;
      firstNameInput.classList.add('has-error');
      if (fnErr) fnErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = firstNameInput;
    } else {
      firstNameInput.classList.remove('has-error');
      if (fnErr) fnErr.style.display = 'none';
    }

    // 2. Last Name (Letters only, mandatory)
    const lnVal = lastNameInput.value.trim();
    const lnErr = document.getElementById('signup-lastname-error');
    if (!lnVal || !/^[A-Za-z\s]+$/.test(lnVal)) {
      isValid = false;
      lastNameInput.classList.add('has-error');
      if (lnErr) lnErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = lastNameInput;
    } else {
      lastNameInput.classList.remove('has-error');
      if (lnErr) lnErr.style.display = 'none';
    }

    // 3. Email (Mandatory)
    const emailVal = emailInput.value.trim();
    const emailErr = document.getElementById('signup-email-error');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailVal || !emailRegex.test(emailVal)) {
      isValid = false;
      emailInput.classList.add('has-error');
      if (emailErr) emailErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = emailInput;
    } else {
      emailInput.classList.remove('has-error');
      if (emailErr) emailErr.style.display = 'none';
    }

    // 4. Mobile Number (Mandatory, exact 10 digits)
    const mobileVal = mobileInput.value.trim();
    const mobileErr = document.getElementById('signup-mobile-error');
    if (!mobileVal || mobileVal.length !== 10 || !/^\d{10}$/.test(mobileVal)) {
      isValid = false;
      mobileInput.classList.add('has-error');
      if (mobileErr) mobileErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = mobileInput;
    } else {
      mobileInput.classList.remove('has-error');
      if (mobileErr) mobileErr.style.display = 'none';
    }

    // 5. Role (Mandatory)
    const roleVal = roleSelect.value;
    const roleErr = document.getElementById('signup-role-error');
    if (!roleVal) {
      isValid = false;
      roleSelect.classList.add('has-error');
      if (roleErr) roleErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = roleSelect;
    } else {
      roleSelect.classList.remove('has-error');
      if (roleErr) roleErr.style.display = 'none';
    }

    // 6. Password (Standard requirements: >=8 chars, uppercase, lowercase, number, special char)
    const passVal = passwordInput.value;
    const passErr = document.getElementById('signup-password-error');
    const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    if (!passVal || !passRegex.test(passVal)) {
      isValid = false;
      passwordInput.classList.add('has-error');
      if (passErr) passErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = passwordInput;
    } else {
      passwordInput.classList.remove('has-error');
      if (passErr) passErr.style.display = 'none';
    }

    // 7. Confirm Password (Must match)
    const confirmVal = confirmPasswordInput.value;
    const confirmErr = document.getElementById('signup-confirm-error');
    if (confirmVal !== passVal) {
      isValid = false;
      confirmPasswordInput.classList.add('has-error');
      if (confirmErr) confirmErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = confirmPasswordInput;
    } else {
      confirmPasswordInput.classList.remove('has-error');
      if (confirmErr) confirmErr.style.display = 'none';
    }

    // 8. Terms & Conditions Checkbox (Mandatory)
    const termsErr = document.getElementById('signup-terms-error');
    if (!termsCheckbox.checked) {
      isValid = false;
      if (termsErr) termsErr.style.display = 'block';
      if (!firstInvalid) firstInvalid = termsCheckbox;
    } else {
      if (termsErr) termsErr.style.display = 'none';
    }

    // Optional Address check
    if (addressInput && addressInput.value.trim().length > 0 && addressInput.value.trim().length < 5) {
      isValid = false;
      addressInput.classList.add('has-error');
      if (!firstInvalid) firstInvalid = addressInput;
    }

    if (!isValid) {
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    // Save account to localStorage
    const newUser = {
      firstName: fnVal,
      lastName: lnVal,
      username: usernameInput && usernameInput.value.trim() ? usernameInput.value.trim() : fnVal.toLowerCase(),
      email: emailVal,
      password: passVal,
      role: roleVal,
      mobile: mobileVal,
      countryCode: countryCodeSelect ? countryCodeSelect.value : '+91',
      country: countryInput ? countryInput.value.trim() : 'India',
      address: addressInput ? addressInput.value.trim() : '',
      avatar: fnVal.charAt(0).toUpperCase()
    };

    auth.saveUser(newUser);

    // Show toast and redirect to sign-in
    const successToast = document.getElementById('signup-success-toast');
    if (successToast) {
      successToast.style.display = 'block';
    }

    const submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Account Created! Redirecting...';
    }

    setTimeout(() => {
      window.location.href = 'sign-in.html';
    }, 1200);
  });
}

function checkPasswordStrength(password) {
  const bar = document.getElementById('password-strength-bar');
  const label = document.getElementById('password-strength-label');
  const ruleLen = document.getElementById('rule-length');
  const ruleUpper = document.getElementById('rule-uppercase');
  const ruleLower = document.getElementById('rule-lowercase');
  const ruleNum = document.getElementById('rule-number');
  const ruleSpecial = document.getElementById('rule-special');

  let score = 0;

  // Length
  if (password.length >= 8) {
    score++;
    if (ruleLen) ruleLen.className = 'rule-item valid';
  } else {
    if (ruleLen) ruleLen.className = 'rule-item invalid';
  }

  // Uppercase
  if (/[A-Z]/.test(password)) {
    score++;
    if (ruleUpper) ruleUpper.className = 'rule-item valid';
  } else {
    if (ruleUpper) ruleUpper.className = 'rule-item invalid';
  }

  // Lowercase
  if (/[a-z]/.test(password)) {
    score++;
    if (ruleLower) ruleLower.className = 'rule-item valid';
  } else {
    if (ruleLower) ruleLower.className = 'rule-item invalid';
  }

  // Number
  if (/\d/.test(password)) {
    score++;
    if (ruleNum) ruleNum.className = 'rule-item valid';
  } else {
    if (ruleNum) ruleNum.className = 'rule-item invalid';
  }

  // Special
  if (/[\W_]/.test(password)) {
    score++;
    if (ruleSpecial) ruleSpecial.className = 'rule-item valid';
  } else {
    if (ruleSpecial) ruleSpecial.className = 'rule-item invalid';
  }

  if (!bar || !label) return;

  if (password.length === 0) {
    bar.style.width = '0%';
    bar.style.backgroundColor = 'transparent';
    label.textContent = 'Enter a secure password';
    label.style.color = 'var(--text-muted)';
  } else if (score <= 2) {
    bar.style.width = '30%';
    bar.style.backgroundColor = '#ef4444';
    label.textContent = 'Weak password (must meet standard requirements)';
    label.style.color = '#ef4444';
  } else if (score <= 4) {
    bar.style.width = '70%';
    bar.style.backgroundColor = '#f59e0b';
    label.textContent = 'Moderate security';
    label.style.color = '#f59e0b';
  } else {
    bar.style.width = '100%';
    bar.style.backgroundColor = '#10b981';
    label.textContent = 'Strong cyber defense password';
    label.style.color = '#10b981';
  }
}

