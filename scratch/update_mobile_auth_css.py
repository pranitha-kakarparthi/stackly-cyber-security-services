with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """  #sim-perimeter-form .btn {
    width: 100%;
  }
}"""

addition = """  #sim-perimeter-form .btn {
    width: 100%;
  }

  .auth-banner-header {
    flex-wrap: wrap;
    gap: 0.75rem;
    justify-content: space-between;
  }

  .auth-banner-header .auth-brand-logo {
    width: 130px;
    height: auto;
  }

  .auth-banner-back-btn {
    padding: 0.35rem 0.75rem;
    font-size: 0.775rem;
  }
}"""

if target in css:
    css = css.replace(target, addition)
elif target.replace('\n', '\r\n') in css:
    css = css.replace(target.replace('\n', '\r\n'), addition.replace('\n', '\r\n'))
else:
    print("Target not found!")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated 425px rules successfully")

