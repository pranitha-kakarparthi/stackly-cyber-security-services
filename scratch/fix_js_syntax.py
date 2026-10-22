# Fix main.js
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    main_text = f.read()

# Replace the literal '\\n' with actual newline
main_text = main_text.replace('initCharacterCounters();\\n  initBackToTop();', 'initCharacterCounters();\n  initBackToTop();')

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_text)

# Fix dashboard.js
with open('assets/js/dashboard.js', 'r', encoding='utf-8') as f:
    dash_text = f.read()

dash_text = dash_text.replace('initDashboardActionButtons();\\n  initDashboardBackToTop();', 'initDashboardActionButtons();\n  initDashboardBackToTop();')

with open('assets/js/dashboard.js', 'w', encoding='utf-8') as f:
    f.write(dash_text)

print("Replaced literal \\\\n in main.js and dashboard.js")

