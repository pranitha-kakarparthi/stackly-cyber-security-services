with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """            <div class="dash-greeting">
              <span id="dash-user-greeting">Good day, Security Commander</span>
              <span class="dash-status-badge">
                <span class="badge-dot"></span> Grid Secure
              </span>
            </div>"""

replacement = """            <div class="dash-greeting">
              <span id="dash-user-greeting">Good day, Security Commander</span>
            </div>"""

if target in text:
    text = text.replace(target, replacement)
    with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Removed duplicate static badge in pages/dashboard.html")
else:
    print("WARNING: target not found in pages/dashboard.html")

