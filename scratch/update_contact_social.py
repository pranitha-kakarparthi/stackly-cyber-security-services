with open('pages/contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_block = """            <a href="404.html" class="social-badge-link" aria-label="LinkedIn">
              <span>💼</span> LinkedIn Official
            </a>
            <a href="404.html" class="social-badge-link" aria-label="Twitter / X">
              <span>🐦</span> Twitter / X Dispatch
            </a>
            <a href="404.html" class="social-badge-link" aria-label="GitHub">
              <span>💻</span> GitHub Research
            </a>
            <a href="404.html" class="social-badge-link" aria-label="YouTube">
              <span>▶️</span> YouTube Defense Briefings
            </a>"""

new_block = """            <a href="404.html" class="social-badge-link" aria-label="LinkedIn" title="LinkedIn">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
              <span>LinkedIn Official</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="Twitter / X" title="X (Twitter)">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
              <span>Twitter / X Dispatch</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="GitHub" title="GitHub">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
                <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
              </svg>
              <span>GitHub Research</span>
            </a>
            <a href="404.html" class="social-badge-link" aria-label="YouTube" title="YouTube">
              <svg class="brand-social-svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
              </svg>
              <span>YouTube Defense Briefings</span>
            </a>"""

if old_block in c:
    c = c.replace(old_block, new_block)
    print("Replaced LF in pages/contact.html")
elif old_block.replace('\n', '\r\n') in c:
    c = c.replace(old_block.replace('\n', '\r\n'), new_block.replace('\n', '\r\n'))
    print("Replaced CRLF in pages/contact.html")
else:
    print("WARNING: old_block not found in pages/contact.html")

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated pages/contact.html")

