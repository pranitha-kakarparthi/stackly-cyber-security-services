import re

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    initial = content
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"[{filepath}] Replaced item")
        else:
            # Try CRLF/LF variation
            old_crlf = old.replace('\n', '\r\n')
            new_crlf = new.replace('\n', '\r\n')
            if old_crlf in content:
                content = content.replace(old_crlf, new_crlf)
                print(f"[{filepath}] Replaced item (CRLF)")
            else:
                print(f"[{filepath}] WARNING: Target not found")
                
    if content != initial:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{filepath}] Successfully saved changes.")
    else:
        print(f"[{filepath}] No changes made.")

# 1. pages/about.html
about_replacements = [
    ('<div class="card-icon-wrap">🔮</div>', '<div class="card-icon-wrap">🔭</div>'),
    ('<div class="card-icon-wrap">🤝</div>', '<div class="card-icon-wrap">⚖️</div>'),
    ('<div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🏅</div>', '<div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📜</div>'),
    ('<div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🏛️</div>', '<div style="font-size: 2.5rem; margin-bottom: 0.75rem;">⚔️</div>'),
]
update_file('pages/about.html', about_replacements)

# 2. pages/contact.html
contact_social_old = """            <a href="404.html" class="btn btn-outline btn-sm">
              <span>💼</span> LinkedIn Official
            </a>
            <a href="404.html" class="btn btn-outline btn-sm">
              <span>🐦</span> Twitter / X Dispatch
            </a>
            <a href="404.html" class="btn btn-outline btn-sm">
              <span>💻</span> GitHub Research
            </a>"""

contact_social_new = """            <a href="404.html" class="btn btn-outline btn-sm" aria-label="Stackly on LinkedIn" style="display: inline-flex; align-items: center; gap: 0.5rem;">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
              <span>LinkedIn Official</span>
            </a>
            <a href="404.html" class="btn btn-outline btn-sm" aria-label="Stackly on X Twitter" style="display: inline-flex; align-items: center; gap: 0.5rem;">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
              <span>Twitter / X Dispatch</span>
            </a>
            <a href="404.html" class="btn btn-outline btn-sm" aria-label="Stackly on GitHub" style="display: inline-flex; align-items: center; gap: 0.5rem;">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
                <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0 0 22 12.017C22 6.484 17.522 2 12 2z"/>
              </svg>
              <span>GitHub Research</span>
            </a>"""

update_file('pages/contact.html', [(contact_social_old, contact_social_new)])

# 3. pages/service-pentest.html
pentest_replacements = [
    ('<div class="card-icon-wrap">🔘</div>', '<div class="card-icon-wrap">🔲</div>'),
    ('<div class="card-icon-wrap">👔</div>', '<div class="card-icon-wrap">📑</div>'),
    ('<div style="font-size: 2rem; margin-bottom: 0.5rem;">📘</div>', '<div style="font-size: 2rem; margin-bottom: 0.5rem;">🛡️</div>'),
]
update_file('pages/service-pentest.html', pentest_replacements)

# 4. pages/service-incident-response.html
ir_replacements = [
    ('<div class="card-icon-wrap">🧹</div>', '<div class="card-icon-wrap">🚫</div>'),
    ('<div style="font-size: 2rem; margin-bottom: 0.5rem;">💾</div>', '<div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>'),
]
update_file('pages/service-incident-response.html', ir_replacements)

# 5. pages/service-cloud-security.html
cloud_replacements = [
    ('<div class="card-icon-wrap">🚢</div>', '<div class="card-icon-wrap">📦</div>'),
    ("""          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <h4 class="card-title">Least-Privilege IAM</h4>""",
     """          <div class="tilt-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔑</div>
            <h4 class="card-title">Least-Privilege IAM</h4>""")
]
update_file('pages/service-cloud-security.html', cloud_replacements)

# 6. pages/services.html
services_replacements = [
    ('<span>💰</span> Compare Service Tiers', '<span>📊</span> Compare Service Tiers'),
    ('<span>🚀</span> Start 14-Day Pilot Assessment', '<span>🛡️</span> Start 14-Day Pilot Assessment'),
]
update_file('pages/services.html', services_replacements)

# 7. pages/dashboard.html
dash_replacements = [
    ('<span>🛡️</span> Request Ad-Hoc PenTest', '<span>🎯</span> Request Ad-Hoc PenTest'),
    ('<span>🔒</span> Enforce Honeypot Decoys', '<span>🍯</span> Enforce Honeypot Decoys'),
]
update_file('pages/dashboard.html', dash_replacements)

# 8. pages/sign-in.html & pages/sign-up.html
auth_replacements = [
    ('<option value="Enterprise Client IT Director">🏢 Enterprise Client IT Director</option>',
     '<option value="Enterprise Client IT Director">💼 Enterprise Client IT Director</option>')
]
update_file('pages/sign-in.html', auth_replacements)
update_file('pages/sign-up.html', auth_replacements)

print("Icon audit fixes completed!")
