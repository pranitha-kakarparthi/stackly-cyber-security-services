import re

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\'][^>]*>', text)
print("Scripts in pages/dashboard.html:", scripts)
print("Has page-loader in dashboard.html:", 'id="page-loader"' in text)

