# Update sign-in.html and sign-up.html
for p in ['pages/sign-in.html', 'pages/sign-up.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(
        '<a href="../index.html" style="display: flex; align-items: center; gap: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">',
        '<a href="../index.html" class="auth-nav-back-link" style="display: flex; align-items: center; gap: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">'
    )
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {p}")

# Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

rule_to_add = """  /* Remove redundant Back to Home at centre of page on smaller screens */
  .auth-nav-top a[href*="index.html"],
  .auth-nav-back-link {
    display: none !important;
  }

  .auth-nav-top {
    justify-content: flex-end !important;
  }
"""

target = "/* Rich Stacked Layout for Auth Pages on Smaller Screens - Never Missing Content */"
if target in css:
    css = css.replace(target, rule_to_add + "\n  " + target)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css with center back-home hiding rule on smaller screens")
else:
    print("Target not found in style.css!")

