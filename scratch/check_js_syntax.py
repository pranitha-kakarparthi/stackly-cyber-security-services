import glob
import subprocess

js_files = glob.glob('assets/js/*.js')
for f in js_files:
    res = subprocess.run(['node', '--check', f], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"SYNTAX ERROR in {f}:")
        print(res.stderr)
    else:
        print(f"{f}: Syntax OK")

