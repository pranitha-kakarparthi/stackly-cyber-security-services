import glob

for fpath in glob.glob('scratch/*.py'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for term in ['dash-user-greeting', 'dash-status-badge', 'renderUserTopBar', 'dash-topbar']:
        if term in content:
            print(f"{fpath}: found '{term}'")

