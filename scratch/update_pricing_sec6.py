NEW_PRICING_S6 = '''    <!-- SECTION 6: ENTERPRISE CUSTOM ARCHITECTURE -->
    <section class="section" aria-label="Custom Scope Inquiry">
      <div class="container">
        <div class="form-card" style="max-width: 980px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center; padding: 2.5rem;" data-animate="zoom-in">
          <div>
            <div class="badge-tag" style="margin-bottom: 1rem;">
              <span class="badge-dot"></span>
              Custom Enterprise Needs
            </div>
            <h2 style="font-size: 2rem; margin-bottom: 1rem;">Need a Custom Scoped Proposal for 1,000+ Endpoints?</h2>
            <p style="font-size: 1.05rem; margin-bottom: 2rem; color: var(--text-secondary);">
              Our security architects can tailor a bespoke blend of continuous Red Teaming, cloud compliance automation, and co-managed SOC services.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="contact.html" class="btn btn-primary btn-lg">Request Custom Quote</a>
              <a href="404.html" class="btn btn-secondary btn-lg">Contact Sales Engineering</a>
            </div>
          </div>
          <div style="position: relative; border-radius: var(--radius-lg); overflow: hidden; border: 1.5px solid var(--border-cyber); box-shadow: 0 12px 36px rgba(58, 1, 14, 0.12);">
            <img src="../assets/images/cyber-defense-command-center.webp" alt="Stackly Enterprise Defense Operations Center" width="440" height="260" style="width: 100%; height: 260px; object-fit: cover; display: block;" loading="lazy">
            <div style="position: absolute; bottom: 12px; left: 12px; background: rgba(250, 247, 238, 0.95); backdrop-filter: blur(8px); padding: 6px 12px; border-radius: var(--radius-full); font-size: 0.8rem; font-weight: 700; color: var(--primary); border: 1px solid var(--border-cyber); display: flex; align-items: center; gap: 6px;">
              <span class="hero-pill-dot"></span> Dedicated Operations Center
            </div>
          </div>
        </div>
      </div>
    </section>'''

with open('pages/pricing.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
new_text, count = re.subn(r'<section class="section" aria-label="Custom Scope Inquiry">[\s\S]*?</section>', NEW_PRICING_S6, text, count=1)
if count:
    with open('pages/pricing.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Updated pricing.html Section 6 with cyber image!")
else:
    print("Could not match Section 6 in pricing.html")

