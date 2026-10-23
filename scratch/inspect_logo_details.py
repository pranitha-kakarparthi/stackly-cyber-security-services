from PIL import Image

im = Image.open('assets/images/logoStackly.webp')
print("Image format:", im.format, "size:", im.size, "mode:", im.mode)
# Find bounding box of non-empty alpha
bbox = im.getbbox()
print("Bounding box:", bbox)
cropped = im.crop(bbox)
print("Cropped size:", cropped.size)

