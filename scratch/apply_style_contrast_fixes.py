with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .nav-brand-logo
t1 = '''.nav-brand-logo {
  height: 34px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 0 10px rgba(122, 16, 40, 0.15));
  transition: transform var(--transition-fast);
}

.nav-brand:hover .nav-brand-logo {
  transform: scale(1.05);
}'''

r1 = '''.nav-brand-logo {
  height: 34px;
  width: auto;
  object-fit: contain;
  filter: brightness(0) saturate(100%) invert(13%) sepia(68%) saturate(3474%) hue-rotate(324deg) brightness(88%) contrast(97%);
  transition: transform var(--transition-fast), filter var(--transition-fast);
}

.nav-brand:hover .nav-brand-logo,
.nav-brand:focus-visible .nav-brand-logo {
  transform: scale(1.05);
  filter: brightness(0) saturate(100%) invert(18%) sepia(85%) saturate(3800%) hue-rotate(324deg) brightness(105%) contrast(105%);
}'''

assert t1 in content, 'Target 1 (.nav-brand-logo) not found'
content = content.replace(t1, r1)

# 2. Update .form-control and remove duplicate black focus
t2 = '''.form-control {
  width: 100%;
  background: #FFFFFF;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 0.85rem 1.15rem;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--text-primary);
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.03);
  transition: all var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(122, 16, 40, 0.15);
  background: #FFFFFF;
}

.form-control::placeholder {
  color: var(--text-muted);
  opacity: 0.85;
}

.form-control:focus {
  outline: none;
  border-color: var(--border-focus);
  background: #0d1427;
  box-shadow: 0 0 0 3px rgba(122, 16, 40, 0.2);
}'''

r2 = '''.form-control {
  width: 100%;
  background: #FFFFFF !important;
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 0.85rem 1.15rem;
  font-family: inherit;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--text-primary) !important;
  box-shadow: 0 2px 6px rgba(58, 1, 14, 0.03);
  transition: all var(--transition-fast);
}

.form-control:hover {
  border-color: rgba(122, 16, 40, 0.35);
  background: #FFFFFF !important;
}

.form-control:focus,
.form-control:focus-visible,
.form-control:active {
  outline: none;
  border-color: var(--primary) !important;
  background: #FFFFFF !important;
  color: var(--text-primary) !important;
  box-shadow: 0 0 0 3.5px rgba(122, 16, 40, 0.15) !important;
}

.form-control::placeholder {
  color: #7A626A;
  opacity: 1;
}

select.form-control {
  background-color: #FFFFFF !important;
  color: var(--text-primary) !important;
  cursor: pointer;
}

select.form-control option {
  background-color: #FFFFFF !important;
  color: #33050F !important;
  padding: 0.5rem;
}

select.form-control option:checked,
select.form-control option:hover {
  background-color: #F3EFE0 !important;
  color: #7A1028 !important;
}

textarea.form-control {
  resize: vertical;
  min-height: 120px;
}'''

assert t2 in content, 'Target 2 (.form-control) not found'
content = content.replace(t2, r2)

# 3. Update .error-message and .strength-bar-track
t3 = '''.error-message {
  display: none;
  font-size: 0.825rem;
  color: #ff6b6b;
  margin-top: 0.4rem;
  font-weight: 500;
}'''

r3 = '''.error-message {
  display: none;
  font-size: 0.825rem;
  color: var(--danger) !important;
  margin-top: 0.4rem;
  font-weight: 600;
}'''

assert t3 in content, 'Target 3 (.error-message) not found'
content = content.replace(t3, r3)

t4 = '''.strength-bar-track {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 0.35rem;
}'''

r4 = '''.strength-bar-track {
  width: 100%;
  height: 4px;
  background: var(--border-subtle);
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 0.35rem;
}'''

assert t4 in content, 'Target 4 (.strength-bar-track) not found'
content = content.replace(t4, r4)

# 5. Update footer section
t5 = '''.site-footer {
  background: #250109;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  color: #FAF7EE;
  border-top: 1px solid var(--border-subtle);
  padding: 4.5rem 0 2rem;
  margin-top: auto;
  position: relative;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
  gap: 3rem;
  margin-bottom: 3.5rem;
}

.footer-brand-info {
  display: flex;
  flex-direction: column;
}

.footer-logo {
  height: 38px;
  width: auto;
  margin-bottom: 1.25rem;
}

.footer-tagline {
  font-size: 0.925rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin-bottom: 1.5rem;
}

.footer-heading {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1.25rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.footer-links-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-link {
  color: var(--text-muted);
  font-size: 0.9rem;
  transition: all var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}

.footer-link:hover {
  color: var(--primary);
  transform: translateX(4px);
}

.footer-contact-info {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.footer-contact-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.875rem;
  color: var(--text-muted);
}

.footer-contact-icon {
  color: var(--primary);
  font-size: 1.1rem;
  margin-top: 0.15rem;
}

.footer-socials {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1rem;
}

.social-badge-link {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 0.95rem;
  background: var(--surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  color: var(--text-secondary);
  font-size: 0.825rem;
  font-weight: 500;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.social-badge-link:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(122, 16, 40, 0.08);
  transform: translateY(-2px);
}

.brand-social-svg {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  transition: transform var(--transition-fast), color var(--transition-fast);
}

.social-badge-link:hover .brand-social-svg {
  transform: scale(1.15);
  color: var(--primary);
}

.footer-bottom {
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}

.footer-bottom-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.footer-bottom-links a {
  color: var(--text-muted);
}

.footer-bottom-links a:hover {
  color: var(--primary);
}'''

r5 = '''.site-footer {
  background: #250109;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  color: #FAF7EE;
  padding: 4.5rem 0 2rem;
  margin-top: auto;
  position: relative;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
  gap: 3rem;
  margin-bottom: 3.5rem;
}

.footer-brand-info {
  display: flex;
  flex-direction: column;
}

.footer-logo {
  height: 38px;
  width: auto;
  margin-bottom: 1.25rem;
}

.footer-tagline {
  font-size: 0.925rem;
  color: #D1C2C6;
  line-height: 1.65;
  margin-bottom: 1.5rem;
}

.footer-heading {
  font-size: 1rem;
  font-weight: 700;
  color: #FAF7EE !important;
  margin-bottom: 1.25rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-links-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-link {
  color: #D1C2C6;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: none;
}

.footer-link:hover,
.footer-link:focus-visible {
  color: #F5A623 !important;
  transform: translateX(4px);
  text-shadow: 0 0 10px rgba(245, 166, 35, 0.3);
}

.footer-link:active {
  color: #FFFFFF !important;
  transform: translateX(2px);
}

.footer-contact-info {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.footer-contact-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.875rem;
  color: #D1C2C6;
}

.footer-contact-icon {
  color: #F5A623;
  font-size: 1.1rem;
  margin-top: 0.15rem;
}

.footer-socials {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1rem;
}

.social-badge-link {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 0.95rem;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: var(--radius-full);
  color: #FAF7EE;
  font-size: 0.825rem;
  font-weight: 600;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.social-badge-link:hover,
.social-badge-link:focus-visible {
  border-color: #F5A623;
  color: #F5A623 !important;
  background: rgba(245, 166, 35, 0.15);
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
}

.social-badge-link:active {
  color: #FFFFFF !important;
  background: rgba(122, 16, 40, 0.4);
  transform: translateY(0);
}

.brand-social-svg {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  transition: transform var(--transition-fast), color var(--transition-fast);
}

.social-badge-link:hover .brand-social-svg,
.social-badge-link:focus-visible .brand-social-svg {
  transform: scale(1.15);
  color: #F5A623 !important;
}

.footer-bottom {
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.85rem;
  color: #B09BA2;
}

.footer-bottom-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.footer-bottom-links a {
  color: #B09BA2;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-bottom-links a:hover,
.footer-bottom-links a:focus-visible {
  color: #F5A623 !important;
}

.footer-bottom-links a:active {
  color: #FFFFFF !important;
}'''

assert t5 in content, 'Target 5 (Footer) not found'
content = content.replace(t5, r5)

# 6. Update .testimonial-stars
t6 = '''.testimonial-stars {
  display: flex;
  gap: 0.25rem;
  color: #fbbf24;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}'''

r6 = '''.testimonial-stars {
  display: flex;
  gap: 0.25rem;
  color: #B45309;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}'''

assert t6 in content, 'Target 6 (.testimonial-stars) not found'
content = content.replace(t6, r6)

# 7. Update .vortex-page-wrap background
t7 = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #030508;'''

r7 = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #250109;'''

assert t7 in content, 'Target 7 (.vortex-page-wrap) not found'
content = content.replace(t7, r7)

# 8. Add .auth-banner-side .badge-tag rule
t8 = '''.auth-banner-content h1 {
  font-size: clamp(1.4rem, 2.1vw, 1.95rem);
  line-height: 1.25;
  margin-bottom: clamp(0.5rem, 1.1vh, 0.85rem);
  color: #FAF7EE !important;
}'''

r8 = '''.auth-banner-side .badge-tag {
  background: rgba(245, 166, 35, 0.15) !important;
  border-color: rgba(245, 166, 35, 0.35) !important;
  color: #F5A623 !important;
}

.auth-banner-content h1 {
  font-size: clamp(1.4rem, 2.1vw, 1.95rem);
  line-height: 1.25;
  margin-bottom: clamp(0.5rem, 1.1vh, 0.85rem);
  color: #FAF7EE !important;
}'''

assert t8 in content, 'Target 8 (Auth banner badge) not found'
content = content.replace(t8, r8)

# 9. Table row hover
t9 = '''.pricing-comparison-table tbody tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}'''

r9 = '''.pricing-comparison-table tbody tr:hover td {
  background: rgba(122, 16, 40, 0.04);
}'''

assert t9 in content, 'Target 9 (Table row hover) not found'
content = content.replace(t9, r9)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully updated all style.css targets!')

