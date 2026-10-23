with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update 404 spacing
css = css.replace(
"""  padding: clamp(2.5rem, 6vh, 4.5rem) 1.5rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: clamp(1.75rem, 3.5vh, 2.75rem);""",
"""  padding: clamp(1.5rem, 4vh, 2.75rem) 1.25rem;
  box-sizing: border-box;
  position: relative;
  overflow-x: hidden;
  text-align: center;
  gap: clamp(1rem, 2.5vh, 1.75rem);"""
)

# 2. Update auth-banner-side on mobile
css = css.replace(
"""  .auth-banner-side {
    display: flex;
    flex-direction: column;
    position: static;
    height: auto;
    max-height: none;
    overflow-y: visible;
    padding: 3rem 1.5rem 2.25rem;""",
"""  .auth-banner-side {
    display: flex;
    flex-direction: column;
    position: static;
    height: auto;
    max-height: none;
    overflow-y: visible;
    padding: 1.5rem 1.25rem 1.75rem;"""
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated 404 and auth padding successfully")

