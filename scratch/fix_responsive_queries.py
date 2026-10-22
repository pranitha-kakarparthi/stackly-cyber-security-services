with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix max-width: 1024px
css = css.replace(
'''  .hero-sentinel-frame {
    margin-top: clamp(-7rem, -9vw, -3rem);
  }''',
'''  .hero-sentinel-frame {
    margin-top: -1rem;
    width: min(94%, 620px);
  }'''
)

# Fix max-width: 768px
css = css.replace(
'''  .hero-sentinel-frame {
    margin-top: -3.5rem;
  }

  .hero-interactive-dock {
    margin-top: 0.5rem;
  }''',
'''  .hero-sentinel-frame {
    margin-top: 0;
    width: 100%;
    max-width: 520px;
  }

  .hero-interactive-dock {
    margin-top: 0.5rem;
  }'''
)

# Fix max-width: 425px
css = css.replace(
'''  .hero-sentinel-frame {
    margin-top: -1.75rem;
  }''',
'''  .hero-sentinel-frame {
    margin-top: 0.25rem;
    width: 100%;
  }'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Cleaned up responsive media queries for hero sentinel frame!')

