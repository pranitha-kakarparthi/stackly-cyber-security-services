with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Check if initBackToTop already exists
if 'initBackToTop' not in text:
    # Add to DOMContentLoaded
    text = text.replace('initCharacterCounters();', 'initCharacterCounters();\\n  initBackToTop();')
    
    back_to_top_fn = """
/* ==========================================================================
   10. BACK TO TOP CONTROLLER
   Smoothly scrolls page to the top when button is clicked; shows after scrolling
   ========================================================================== */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  const handleScroll = () => {
    if (window.scrollY > 280) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
"""
    text += back_to_top_fn
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added initBackToTop to assets/js/main.js")
else:
    print("initBackToTop already present in assets/js/main.js")

