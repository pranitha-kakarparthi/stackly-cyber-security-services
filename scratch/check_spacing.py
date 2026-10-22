import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    dash_css = f.read()

print("style.css size:", len(style_css))
print("dashboard.css size:", len(dash_css))

# Let's inspect media queries in style.css for responsive spacing
mq_list = re.findall(r'@media[^{]+\{[^}]*\}', style_css)
print("Media queries in style.css:", len(mq_list))

