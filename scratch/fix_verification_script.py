with open('scratch/final_verification.py', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("if '#FAF7EE' not in style_css or '#7A1028' not in style_css:",
              "if '#FAF7EE' not in style_css.upper() or '#7A1028' not in style_css.upper():")
c = c.replace("if '#2A010A' not in dash_css or '#FAF7EE' not in dash_css:",
              "if '#2A010A' not in dash_css.upper() or '#FAF7EE' not in dash_css.upper():")

with open('scratch/final_verification.py', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated final_verification.py to check hex tokens case-insensitively.')

