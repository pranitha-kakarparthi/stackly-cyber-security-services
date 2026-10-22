import glob

files = ['index.html'] + glob.glob('pages/*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()

    prefix = "pages/" if f == "index.html" else ""

    # Restore in nav-actions
    html = html.replace(
        f'<a href="404.html" class="btn btn-ghost btn-sm">Log In</a>',
        f'<a href="{prefix}sign-in.html" class="btn btn-ghost btn-sm">Log In</a>'
    )
    html = html.replace(
        f'<a href="../404.html" class="btn btn-ghost btn-sm">Log In</a>',
        f'<a href="sign-in.html" class="btn btn-ghost btn-sm">Log In</a>'
    )
    html = html.replace(
        f'<a href="404.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>',
        f'<a href="{prefix}sign-up.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>'
    )
    html = html.replace(
        f'<a href="../404.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>',
        f'<a href="sign-up.html" class="btn btn-pill-iridescent btn-sm">Get Started</a>'
    )

    # Restore in mobile-actions
    html = html.replace(
        f'<a href="404.html" class="btn btn-secondary btn-block">Sign In</a>',
        f'<a href="{prefix}sign-in.html" class="btn btn-secondary btn-block">Sign In</a>'
    )
    html = html.replace(
        f'<a href="../404.html" class="btn btn-secondary btn-block">Sign In</a>',
        f'<a href="sign-in.html" class="btn btn-secondary btn-block">Sign In</a>'
    )
    html = html.replace(
        f'<a href="404.html" class="btn btn-primary btn-block">Register Account</a>',
        f'<a href="{prefix}sign-up.html" class="btn btn-primary btn-block">Register Account</a>'
    )
    html = html.replace(
        f'<a href="../404.html" class="btn btn-primary btn-block">Register Account</a>',
        f'<a href="sign-up.html" class="btn btn-primary btn-block">Register Account</a>'
    )

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(html)

print("Restored header & mobile drawer auth links!")

