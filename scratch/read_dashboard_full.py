with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the top 150 lines and bottom 150 lines
lines = text.splitlines()
print("Total lines in dashboard.css:", len(lines))
print("\n--- FIRST 40 LINES ---")
for l in lines[:40]:
    print(l)

print("\n--- LAST 40 LINES ---")
for l in lines[-40:]:
    print(l)

