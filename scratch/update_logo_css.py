import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_block = """.nav-brand-logo {
  height: 34px;
  width: auto;
  object-fit: contain;
  filter: brightness(0) saturate(100%) invert(13%) sepia(68%) saturate(3474%)
    hue-rotate(324deg) brightness(88%) contrast(97%);
  transition:
    transform var(--transition-fast),
    filter var(--transition-fast);
}

.nav-brand:hover .nav-brand-logo,
.nav-brand:focus-visible .nav-brand-logo {
  transform: scale(1.05);
  filter: brightness(0) saturate(100%) invert(18%) sepia(85%) saturate(3800%)
    hue-rotate(324deg) brightness(105%) contrast(105%);
}"""

new_block = """.nav-brand-logo {
  height: 36px;
  width: auto;
  object-fit: contain;
  transition: transform var(--transition-fast), opacity var(--transition-fast);
}

.nav-brand:hover .nav-brand-logo,
.nav-brand:focus-visible .nav-brand-logo {
  transform: scale(1.04);
  opacity: 0.88;
}"""

if old_block in css:
    css = css.replace(old_block, new_block)
    print("Replaced with LF")
elif old_block.replace('\n', '\r\n') in css:
    css = css.replace(old_block.replace('\n', '\r\n'), new_block.replace('\n', '\r\n'))
    print("Replaced with CRLF")
else:
    print("Old block not found!")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

