with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inline space-between without wrap
target = 'style="display: flex; justify-content: space-between; align-items: center;"'
replacement = 'style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;"'

count = html.count(target)
html = html.replace(target, replacement)
print(f"Replaced {count} instances of space-between without wrap in dashboard.html")

target2 = 'style="display: flex; justify-content: space-between;"'
replacement2 = 'style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;"'
count2 = html.count(target2)
html = html.replace(target2, replacement2)
print(f"Replaced {count2} instances of target2")

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pages/dashboard.html")

