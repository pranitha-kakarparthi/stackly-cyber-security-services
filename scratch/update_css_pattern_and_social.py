with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .social-badge-link:hover and add .brand-social-svg
target_social = '''.social-badge-link:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(0, 240, 118, 0.08);
}'''

replace_social = '''.social-badge-link:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(94, 234, 212, 0.1);
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
}'''

if target_social in css:
    css = css.replace(target_social, replace_social, 1)
    print("Updated social CSS in style.css")
else:
    # Try normalized newlines
    css_norm = css.replace('\r\n', '\n')
    if target_social in css_norm:
        css = css_norm.replace(target_social, replace_social, 1)
        print("Updated social CSS (normalized) in style.css")
    else:
        print("Could not find target_social in style.css")

# 2. Add background pattern to .vortex-page-wrap
target_vortex = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #030508;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 1.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: 1.5rem;
}'''

replace_vortex = '''.vortex-page-wrap {
  min-height: 100vh;
  width: 100vw;
  background-color: #030508;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 1.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: 1.5rem;
}

/* Background Cyber Grid & Matrix Pattern for 404 */
.vortex-page-wrap::before {
  content: '';
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(56, 189, 248, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56, 189, 248, 0.05) 1px, transparent 1px),
    radial-gradient(ellipse 80% 60% at 50% 50%, rgba(94, 234, 212, 0.12) 0%, rgba(167, 139, 250, 0.06) 50%, transparent 80%);
  background-size: 40px 40px, 40px 40px, 100% 100%;
  background-position: center center;
  pointer-events: none;
  z-index: 1;
}

.vortex-page-wrap::after {
  content: '';
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 20px 20px, rgba(94, 234, 212, 0.22) 1.5px, transparent 2px),
    radial-gradient(circle at 60px 60px, rgba(167, 139, 250, 0.22) 1.5px, transparent 2px);
  background-size: 80px 80px;
  pointer-events: none;
  z-index: 1;
}'''

css_norm = css.replace('\r\n', '\n')
if target_vortex in css_norm:
    css = css_norm.replace(target_vortex, replace_vortex, 1)
    print("Added 404 background cyber grid pattern in style.css")
else:
    print("Could not find target_vortex in style.css")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css successfully updated!")

