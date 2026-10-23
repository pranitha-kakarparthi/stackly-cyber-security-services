import re

# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .auth-banner-header block in base styles
base_header_old = """.auth-banner-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 2;
}"""

base_header_new = """.auth-banner-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 1rem;
  z-index: 2;
  margin-bottom: 1.5rem;
}

.auth-brand-link {
  display: inline-flex;
  align-items: center;
}

.auth-banner-back-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full, 9999px);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #faf7ee !important;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  white-space: nowrap;
  backdrop-filter: blur(8px);
  transition: all var(--transition-fast, 0.2s ease);
}

.auth-banner-back-btn:hover,
.auth-banner-back-btn:focus-visible {
  background: rgba(245, 166, 35, 0.22);
  border-color: rgba(245, 166, 35, 0.7);
  color: #f5a623 !important;
  transform: translateX(-3px);
  outline: none;
}

.auth-banner-back-btn svg {
  transition: transform var(--transition-fast, 0.2s ease);
}

.auth-banner-back-btn:hover svg {
  transform: translateX(-2px);
}"""

if base_header_old in css:
    css = css.replace(base_header_old, base_header_new)
elif base_header_old.replace('\n', '\r\n') in css:
    css = css.replace(base_header_old.replace('\n', '\r\n'), base_header_new.replace('\n', '\r\n'))
else:
    print("Warning: base_header_old not found directly!")

# Replace .auth-banner-header in media query (around line 3007)
mq_header_old = """  .auth-banner-header {
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: center;
  }"""

mq_header_new = """  .auth-banner-header {
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    gap: 1rem;
  }"""

if mq_header_old in css:
    css = css.replace(mq_header_old, mq_header_new)
elif mq_header_old.replace('\n', '\r\n') in css:
    css = css.replace(mq_header_old.replace('\n', '\r\n'), mq_header_new.replace('\n', '\r\n'))
else:
    print("Warning: mq_header_old not found directly!")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/css/style.css successfully")

# 2. Update pages/sign-in.html
with open('pages/sign-in.html', 'r', encoding='utf-8') as f:
    signin = f.read()

target_signin = """      <div class="auth-banner-header">
        <a href="../index.html" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="auth-brand-logo" width="160" height="40">
        </a>
      </div>"""

replacement_signin = """      <div class="auth-banner-header">
        <a href="../index.html" class="auth-brand-link" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="auth-brand-logo" width="160" height="40">
        </a>
        <a href="../index.html" class="auth-banner-back-btn" aria-label="Back to Stackly Homepage">
          <svg width="15" height="15" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-5-5a1 1 0 010-1.414l5-5a1 1 0 011.414 1.414L6.414 8H17a1 1 0 110 2H6.414l3.293 3.293a1 1 0 010 1.414z" clip-rule="evenodd" />
          </svg>
          <span>Back to Home</span>
        </a>
      </div>"""

if target_signin in signin:
    signin = signin.replace(target_signin, replacement_signin)
elif target_signin.replace('\n', '\r\n') in signin:
    signin = signin.replace(target_signin.replace('\n', '\r\n'), replacement_signin.replace('\n', '\r\n'))
else:
    print("Warning: target_signin not found directly!")

with open('pages/sign-in.html', 'w', encoding='utf-8') as f:
    f.write(signin)
print("Updated pages/sign-in.html successfully")

# 3. Update pages/sign-up.html
with open('pages/sign-up.html', 'r', encoding='utf-8') as f:
    signup = f.read()

target_signup = """      <div class="auth-banner-header">
        <a href="../index.html" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="auth-brand-logo" width="160" height="40">
        </a>
      </div>"""

replacement_signup = """      <div class="auth-banner-header">
        <a href="../index.html" class="auth-brand-link" aria-label="Return to Stackly Home">
          <img src="../assets/images/logoStackly.webp" alt="Stackly Cyber Defense Logo" class="auth-brand-logo" width="160" height="40">
        </a>
        <a href="../index.html" class="auth-banner-back-btn" aria-label="Back to Stackly Homepage">
          <svg width="15" height="15" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-5-5a1 1 0 010-1.414l5-5a1 1 0 011.414 1.414L6.414 8H17a1 1 0 110 2H6.414l3.293 3.293a1 1 0 010 1.414z" clip-rule="evenodd" />
          </svg>
          <span>Back to Home</span>
        </a>
      </div>"""

if target_signup in signup:
    signup = signup.replace(target_signup, replacement_signup)
elif target_signup.replace('\n', '\r\n') in signup:
    signup = signup.replace(target_signup.replace('\n', '\r\n'), replacement_signup.replace('\n', '\r\n'))
else:
    print("Warning: target_signup not found directly!")

with open('pages/sign-up.html', 'w', encoding='utf-8') as f:
    f.write(signup)
print("Updated pages/sign-up.html successfully")

