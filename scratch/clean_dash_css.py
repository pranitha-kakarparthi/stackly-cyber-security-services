with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the redundant .dash-user-profile block inside 480px media query
old_block = '''  .dash-panel {
    padding: 1rem;
  }

  .dash-user-profile {
    padding: 0.25rem 0.5rem;
  }

  .dash-section {'''

new_block = '''  .dash-panel {
    padding: 1rem;
  }

  .dash-section {'''

if old_block in text:
    text = text.replace(old_block, new_block)
    with open('assets/css/dashboard.css', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned redundant .dash-user-profile block in 480px media query")
else:
    print("Pattern not found (or already cleaned)")

