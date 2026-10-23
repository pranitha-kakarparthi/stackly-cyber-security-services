from PIL import Image
import os

img = Image.open('assets/images/vortex-404-cosmic.webp')
img.save('assets/images/vortex-404-cosmic.webp', format='WEBP', quality=78, method=6)

size_kb = os.path.getsize('assets/images/vortex-404-cosmic.webp') / 1024
print(f"vortex-404-cosmic.webp optimized to {size_kb:.1f} KB (must be < 100 KB)")

