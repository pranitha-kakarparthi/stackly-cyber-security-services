import re

with open('pages/contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update contact-country-code
old_cc = '''                <select id="contact-country-code" class="form-control" aria-label="Select Country Dial Code">
                  <option value="+91" selected>🇮🇳 India (+91)</option>
                  <option value="+1">🇺🇸 USA (+1)</option>
                  <option value="+44">🇬🇧 UK (+44)</option>
                  <option value="+65">🇸🇬 Singapore (+65)</option>
                  <option value="+61">🇦🇺 Australia (+61)</option>
                  <option value="+49">🇩🇪 Germany (+49)</option>
                  <option value="+971">🇦🇪 UAE (+971)</option>
                </select>'''

new_cc = '''                <select id="contact-country-code" class="form-control" aria-label="Select Country Dial Code" required aria-required="true">
                  <option value="" disabled selected>Select One</option>
                  <option value="+91">🇮🇳 India (+91)</option>
                  <option value="+1">🇺🇸 USA (+1)</option>
                  <option value="+44">🇬🇧 UK (+44)</option>
                  <option value="+65">🇸🇬 Singapore (+65)</option>
                  <option value="+61">🇦🇺 Australia (+61)</option>
                  <option value="+49">🇩🇪 Germany (+49)</option>
                  <option value="+971">🇦🇪 UAE (+971)</option>
                </select>'''

# 2. Update contact-subject
old_subject = '''              <select id="contact-subject" class="form-control" required aria-required="true" aria-describedby="contact-subject-error">
                <option value="soc">24/7 Managed SOC & Threat Monitoring Inquiry</option>
                <option value="pentest">Penetration Testing / Red Team Assessment</option>
                <option value="cloud">Cloud Security & Zero Trust Architecture</option>
                <option value="incident">Emergency Incident Response Retainer</option>
                <option value="compliance">ISO 27001 / SOC 2 Compliance Audit</option>
                <option value="other">Other Sovereign Cyber Defense Inquiry</option>
              </select>'''

new_subject = '''              <select id="contact-subject" class="form-control" required aria-required="true" aria-describedby="contact-subject-error">
                <option value="" disabled selected>Select One</option>
                <option value="soc">24/7 Managed SOC & Threat Monitoring Inquiry</option>
                <option value="pentest">Penetration Testing / Red Team Assessment</option>
                <option value="cloud">Cloud Security & Zero Trust Architecture</option>
                <option value="incident">Emergency Incident Response Retainer</option>
                <option value="compliance">ISO 27001 / SOC 2 Compliance Audit</option>
                <option value="other">Other Sovereign Cyber Defense Inquiry</option>
              </select>'''

html_norm = html.replace('\r\n', '\n')
old_cc_norm = old_cc.replace('\r\n', '\n')
old_subject_norm = old_subject.replace('\r\n', '\n')

if old_cc_norm in html_norm:
    html_norm = html_norm.replace(old_cc_norm, new_cc)
    print("Updated contact-country-code with 'Select One'")

if old_subject_norm in html_norm:
    html_norm = html_norm.replace(old_subject_norm, new_subject)
    print("Updated contact-subject with 'Select One'")

# 3. Update validation script in contact.html to validate subject
old_val_check = '''        // Mobile validation (10 digits)'''
new_val_check = '''        // Subject dropdown validation (Strict: require user to select one)
        const subjectVal = subjectSelect.value;
        const subjectErr = document.getElementById('contact-subject-error');
        if (!subjectVal) {
          isValid = false;
          subjectSelect.classList.add('has-error');
          if (subjectErr) subjectErr.style.display = 'block';
          if (!firstInvalid) firstInvalid = subjectSelect;
        } else {
          subjectSelect.classList.remove('has-error');
          if (subjectErr) subjectErr.style.display = 'none';
        }

        // Mobile validation (10 digits)'''

if old_val_check in html_norm:
    html_norm = html_norm.replace(old_val_check, new_val_check, 1)
    print("Updated contact form script with subject dropdown validation")

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(html_norm)

print("pages/contact.html updated successfully!")

