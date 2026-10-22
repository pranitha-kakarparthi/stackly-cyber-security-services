import re, glob

def check_html_classes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    classes = set()
    for m in re.finditer(r'class=["\']([^"\']+)["\']', text):
        classes.update(m.group(1).split())
    return classes

print('Sign-in classes:', sorted(check_html_classes('pages/sign-in.html')))
print('Sign-up classes:', sorted(check_html_classes('pages/sign-up.html')))
print('Contact classes:', sorted(check_html_classes('pages/contact.html')))

