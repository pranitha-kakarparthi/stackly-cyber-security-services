with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function initMobileNav()')
idx_end = js.find('function initDynamicGreetings()', idx)
print(js[idx:idx_end])

