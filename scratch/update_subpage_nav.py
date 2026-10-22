import glob

subpages = glob.glob('pages/*.html')

target_old = '''      <div class="nav-actions">
        <a href="sign-in.html" class="btn btn-secondary btn-sm">Sign In</a>
        <a href="sign-up.html" class="btn btn-primary btn-sm">Register</a>
      </div>'''

replacement_new = '''      <div class="nav-actions">
        <a href="sign-in.html" class="btn btn-ghost btn-sm">Log In</a>
        <a href="sign-up.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>
      </div>'''

for path in subpages:
    # Skip sign-in, sign-up, 404, dashboard as they don't have this navbar
    if any(x in path for x in ['sign-in', 'sign-up', '404', 'dashboard']):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if target_old in content:
        content = content.replace(target_old, replacement_new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated nav in', path)
    else:
        # Check if indices approach needed
        idx = content.find('<div class="nav-actions">')
        if idx != -1:
            end_idx = content.find('</div>', idx) + 6
            content = content[:idx] + replacement_new + content[end_idx:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Updated nav via index in', path)
        else:
            print('No nav-actions found in', path)

