with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_loader_css = """#page-loader {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background-color: #050811;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 99999;
  transition: opacity 0.4s ease, visibility 0.4s ease;
}

#page-loader.loaded {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}"""

new_loader_css = """#page-loader {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background-color: var(--bg-primary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 99999;
  transition: opacity 0.4s ease, visibility 0.4s ease;
  animation: loaderAutoDismiss 0.4s ease 1.8s forwards;
}

@keyframes loaderAutoDismiss {
  0%, 75% {
    opacity: 1;
    visibility: visible;
  }
  100% {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
  }
}

#page-loader.loaded {
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  display: none !important;
}"""

if old_loader_css in css:
    css = css.replace(old_loader_css, new_loader_css)
    print("Replaced old_loader_css in style.css")
else:
    # try flexible regex replacement
    import re
    css = re.sub(
        r'#page-loader\s*\{[^}]+\}\s*#page-loader\.loaded\s*\{[^}]+\}',
        new_loader_css,
        css,
        count=1
    )
    print("Replaced loader via regex in style.css")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

