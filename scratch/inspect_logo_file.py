from PIL import Image

im = Image.open('assets/images/logoStackly.webp')
print("logoStackly.webp size:", im.size, "mode:", im.mode)
# Sample some non-transparent pixels
pixels = list(im.getdata())
non_transparent = [p for p in pixels if len(p) < 4 or p[3] > 20]
print("Total non-transparent pixels:", len(non_transparent))
if non_transparent:
    print("Sample colors:", non_transparent[::len(non_transparent)//10][:10])

