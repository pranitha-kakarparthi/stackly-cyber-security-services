import glob
import os
import re
from html.parser import HTMLParser
from urllib.parse import urlparse

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if 'id' in attrs_dict:
            self.ids.add(attrs_dict['id'])
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append((self.getpos(), attrs_dict['href'], attrs_dict.get('aria-label', '')))

html_files = sorted(glob.glob('**/*.html', recursive=True))

parsed_files = {}
for hf in html_files:
    norm_path = os.path.normpath(hf).replace('\\', '/')
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    extractor = LinkExtractor()
    extractor.feed(content)
    parsed_files[norm_path] = extractor

print(f"Total HTML files indexed: {len(parsed_files)}")

broken_links = []
total_links_checked = 0

for file_path, extractor in parsed_files.items():
    file_dir = os.path.dirname(file_path)
    for (line, col), href, aria in extractor.links:
        href_strip = href.strip()
        if not href_strip or href_strip.startswith(('javascript:', 'mailto:', 'tel:', 'http://', 'https://')):
            continue
        
        total_links_checked += 1
        parsed = urlparse(href_strip)
        target_path = parsed.path
        fragment = parsed.fragment

        # If it's just a fragment on the same page
        if not target_path and fragment:
            if fragment not in extractor.ids:
                broken_links.append((file_path, line, href, f"Anchor #{fragment} not found in {file_path}"))
            continue

        # Resolve relative target file
        if file_dir:
            resolved_file = os.path.normpath(os.path.join(file_dir, target_path)).replace('\\', '/')
        else:
            resolved_file = os.path.normpath(target_path).replace('\\', '/')

        if not os.path.exists(resolved_file):
            broken_links.append((file_path, line, href, f"Target file '{resolved_file}' does not exist"))
        elif fragment and resolved_file in parsed_files:
            if fragment not in parsed_files[resolved_file].ids:
                broken_links.append((file_path, line, href, f"Anchor #{fragment} not found in '{resolved_file}'"))

print(f"Total internal links checked: {total_links_checked}")
if broken_links:
    print(f"\nFound {len(broken_links)} broken links:")
    for src, line, href, reason in broken_links:
        print(f"  {src}:{line} -> '{href}' ({reason})")
else:
    print("\nALL INTERNAL LINKS AND ANCHORS RESOLVED SUCCESSFULLY (0 broken links)!")

