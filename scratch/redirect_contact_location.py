with open('pages/contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

assert '<a href="#map-section" class="btn btn-outline btn-sm">View Location Map</a>' in c, "Target not found in contact.html"

c = c.replace('<a href="#map-section" class="btn btn-outline btn-sm">View Location Map</a>',
              '<a href="404.html" class="btn btn-outline btn-sm">View Location Map</a>')

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully redirected location option in contact.html to 404.html")

