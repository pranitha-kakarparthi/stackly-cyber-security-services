with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

topbar_start = css.find('.dash-topbar {')
topbar_end = css.find('/* ==========================================================================\n   DASHBOARD CONTENT & MODULE PANELS', topbar_start)
print(css[topbar_start:topbar_end])

