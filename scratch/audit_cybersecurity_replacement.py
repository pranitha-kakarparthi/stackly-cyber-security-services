import os, glob, re

# 1. Search for any remaining instances of "cybersecurity" (case-insensitive)
found_instances = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'scratch' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css', '.js', '.json', '.md', '.txt')):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            for idx, line in enumerate(lines):
                # Search for cybersecurity as a single word (case-insensitive)
                matches = re.findall(r'cybersecurity', line, re.I)
                if matches:
                    found_instances.append((fpath, idx + 1, line.strip()))

print(f"=== REMAINING 'CYBERSECURITY' INSTANCES ({len(found_instances)}) ===")
for path, line_no, content in found_instances:
    print(f"{path}:{line_no}: {content[:100]}")

# 2. Check for broken URLs, broken image paths, broken class names, broken IDs
print("\n=== CHECKING FOR BROKEN REFERENCES ===")
broken_issues = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Check for "cyber security" in href, src, id, class
            # E.g. href="...cyber security..." or src="...cyber security..."
            broken_hrefs = re.findall(r'(href=["\'][^"\']*cyber\s+security[^"\']*["\'])', content, re.I)
            if broken_hrefs:
                broken_issues.append((fpath, "href with space", broken_hrefs))
            broken_srcs = re.findall(r'(src=["\'][^"\']*cyber\s+security[^"\']*["\'])', content, re.I)
            if broken_srcs:
                broken_issues.append((fpath, "src with space", broken_srcs))
            broken_ids = re.findall(r'(id=["\'][^"\']*cyber\s+security[^"\']*["\'])', content, re.I)
            if broken_ids:
                broken_issues.append((fpath, "id with space", broken_ids))
            broken_classes = re.findall(r'(class=["\'][^"\']*cyber\s+security[^"\']*["\'])', content, re.I)
            # class can have multiple classes separated by space, but e.g. .cyber-security might have become .cyber security
            # let's check CSS selectors
            if file.endswith('.css'):
                css_broken = re.findall(r'(\.[\w-]*cyber\s+security[\w-]*)', content, re.I)
                if css_broken:
                    broken_issues.append((fpath, "CSS selector split", css_broken))

if broken_issues:
    print(f"Found {len(broken_issues)} broken references:")
    for b in broken_issues:
        print(b)
else:
    print("No broken href, src, id, or css selectors found!")

