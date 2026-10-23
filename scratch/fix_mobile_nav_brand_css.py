with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """.mobile-nav-brand {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: flex-start;
}"""

replacement = """.mobile-nav-brand {
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.mobile-nav-close-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.42rem 0.95rem;
  border-radius: var(--radius-full);
  background: rgba(122, 16, 40, 0.08);
  border: 1px solid rgba(122, 16, 40, 0.2);
  color: var(--primary);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.mobile-nav-close-btn:hover,
.mobile-nav-close-btn:focus-visible {
  background: var(--primary);
  color: #FAF7EE;
  border-color: var(--primary);
  transform: scale(1.04);
}"""

if target in css:
    css = css.replace(target, replacement)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated mobile-nav-brand in style.css successfully")
else:
    print("Target not found!")

