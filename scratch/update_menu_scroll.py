with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """    overlay.classList.toggle('open', isOpen);
    document.body.classList.toggle('drawer-open', isOpen);
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  };"""

replacement = """    overlay.classList.toggle('open', isOpen);
    document.body.classList.toggle('drawer-open', isOpen);
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    if (isOpen) {
      overlay.scrollTop = 0;
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
  };"""

if target in js:
    js = js.replace(target, replacement)
elif target.replace('\n', '\r\n') in js:
    js = js.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))
else:
    print("Target not found!")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated main.js with scroll-to-top on menu open")

