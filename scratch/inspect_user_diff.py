import subprocess

res = subprocess.run(['git', 'diff', '--cached', 'assets/', 'pages/', 'index.html'], capture_output=True, encoding='utf-8', errors='ignore')
diff = res.stdout

added_lines = [l for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
removed_lines = [l for l in diff.splitlines() if l.startswith('-') and not l.startswith('---')]

print(f"Total lines modified: added {len(added_lines)}, removed {len(removed_lines)}")

suspicious = []
for l in added_lines:
    if '""' in l or "''" in l:
        suspicious.append(l)

print(f"Suspicious quote lines: {len(suspicious)}")
for s in suspicious[:10]:
    print(s)

print("Diff inspection completed successfully.")

