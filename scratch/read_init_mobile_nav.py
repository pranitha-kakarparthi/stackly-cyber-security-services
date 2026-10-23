with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function initMobileNav()')
print(js[idx:idx+2500])

