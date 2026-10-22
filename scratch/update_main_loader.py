with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_loader_fn = """function initLoader() {
  const loader = document.getElementById('page-loader');
  if (!loader) return;

  const dismissLoader = () => {
    loader.classList.add('loaded');
    setTimeout(() => {
      loader.remove();
    }, 450);
  };

  // Immediate dismiss if interactive, plus fallback
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(dismissLoader, 300);
  } else {
    window.addEventListener('load', dismissLoader);
    setTimeout(dismissLoader, 1500); // 1.5s max fallback prevention
  }
}"""

new_loader_fn = """function initLoader() {
  const loader = document.getElementById('page-loader');
  if (!loader) return;

  const dismissLoader = () => {
    loader.classList.add('loaded');
    setTimeout(() => {
      try {
        loader.remove();
      } catch (e) {
        loader.style.display = 'none';
      }
    }, 400);
  };

  // Immediate dismiss if interactive, plus fallback
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(dismissLoader, 100);
  } else {
    window.addEventListener('DOMContentLoaded', dismissLoader, { once: true });
    window.addEventListener('load', dismissLoader, { once: true });
    setTimeout(dismissLoader, 800);
  }
}

// Immediately trigger if script evaluates after DOM ready
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initLoader();
}"""

if old_loader_fn in text:
    text = text.replace(old_loader_fn, new_loader_fn)
    print("Replaced old_loader_fn in main.js")
else:
    print("WARNING: old_loader_fn not found exact match")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(text)

