import glob

for fpath in glob.glob('assets/js/*.js') + glob.glob('**/*.html', recursive=True):
    if any(k in fpath for k in ['scratch', '.git']):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for term in ['dash-user-greeting', 'dash-user-timestamp', 'dash-status-badge', 'dash-user-name', 'dash-user-role', 'dash-user-avatar', 'dash-signout-btn', 'mobile-dash-toggle']:
        if term in content:
            print(f"{fpath}: found '{term}'")

