with open('pages/contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove pre-filled values
html = html.replace('value="Rachel Adams"', '')
html = html.replace('value="rachel@enterprise-defense.com"', '')
html = html.replace('value="9876543210"', '')
html = html.replace('>We are seeking a 24/7 Managed SOC provider to ingest AWS CloudTrail and CrowdStrike telemetry for 150 endpoints.</textarea>', '></textarea>')

# 2. Update contact form submission script
old_script = '''        // Success state
        if (successToast) successToast.style.display = 'block';
        const submitBtn = document.getElementById('contact-submit-btn');
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = 'Transmission Dispatched!';
        }'''

new_script = '''        // Success state & Automatic Form Reset
        if (successToast) successToast.style.display = 'block';
        contactForm.reset();
        const charCount = document.getElementById('contact-char-count');
        if (charCount) charCount.textContent = '0 / 500 characters';
        
        const submitBtn = document.getElementById('contact-submit-btn');
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerHTML = '<span>✓</span> Transmission Successfully Dispatched!';
          setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<span>🔒</span> Encrypt & Transmit Message';
          }, 3500);
        }'''

if old_script in html:
    html = html.replace(old_script, new_script)
    print("Replaced script successfully in contact.html")
else:
    # Try normalized
    html_norm = html.replace('\r\n', '\n')
    old_script_norm = old_script.replace('\r\n', '\n')
    if old_script_norm in html_norm:
        html = html_norm.replace(old_script_norm, new_script)
        print("Replaced script (normalized) in contact.html")
    else:
        print("Warning: could not find old_script in contact.html")

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("pages/contact.html updated!")

