with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

# Update .form-control font-family: inherit -> var(--font-sans)
style_content = style_content.replace(
    ".form-control {\n  width: 100%;\n  background: #ffffff !important;\n  border: 1.5px solid var(--border-subtle);\n  border-radius: var(--radius-md);\n  padding: 0.85rem 1.15rem;\n  font-family: inherit;",
    ".form-control {\n  width: 100%;\n  background: #ffffff !important;\n  border: 1.5px solid var(--border-subtle);\n  border-radius: var(--radius-md);\n  padding: 0.85rem 1.15rem;\n  font-family: var(--font-sans);"
)

# Add explicit form elements & code reset right after body definition
body_end = "  -moz-osx-font-smoothing: grayscale;\n}"
replacement = """  -moz-osx-font-smoothing: grayscale;
}

/* Explicit 2-Font Enforcement for Form Controls & Code Elements */
button,
input,
optgroup,
select,
textarea {
  font-family: var(--font-sans);
}

code,
kbd,
samp,
pre {
  font-family: var(--font-mono);
}"""

if "Explicit 2-Font Enforcement" not in style_content:
    style_content = style_content.replace(body_end, replacement, 1)
    print("Added explicit form controls and code element 2-font enforcement to style.css")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_content)

print("Updated style.css successfully.")

