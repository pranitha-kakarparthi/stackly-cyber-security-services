from PIL import Image
import numpy as np

# Load the original vortex image
img = Image.open('assets/images/vortex-404-cosmic.webp').convert('RGB')
arr = np.array(img, dtype=np.float32)

# Normalize to 0..1
arr_norm = arr / 255.0

# Current bright colors are blue/navy: [63, 64, 114]
# Target theme:
# Background is #250109 -> RGB [37, 1, 9] / 255 = [0.145, 0.004, 0.035]
# Deep nebula is Velvet Wine Crimson #7A1028 -> [122, 16, 40]
# Bright cosmic core/particles are Cyber Amber #F5A623 -> [245, 166, 35] and Gold #FDE047 -> [253, 224, 71]
# Pure white stars -> [255, 255, 255]

# Calculate luminance of each pixel
luminance = 0.2126 * arr_norm[:, :, 0] + 0.7152 * arr_norm[:, :, 1] + 0.0722 * arr_norm[:, :, 2]

# Also consider distance from center for radial vignetting to seamlessly blend edges into #250109
h, w, _ = arr.shape
y, x = np.ogrid[:h, :w]
cy, cx = h / 2.0, w / 2.0
# Normalized radial distance from center (0 at center, 1 at edge)
dist = np.sqrt(((x - cx) / cx) ** 2 + ((y - cy) / cy) ** 2)
# Vignette factor: 1 in inner area, smoothly decays to 0 at edges
vignette = np.clip(1.0 - (dist - 0.45) / 0.50, 0.0, 1.0)
vignette = vignette ** 1.5  # smooth cosine-like curve

bg_color = np.array([37.0, 1.0, 9.0], dtype=np.float32) / 255.0  # #250109

# Map luminance to our new luxury color palette:
# Low luminance (< 0.15): blends from bg_color [37, 1, 9] into deep wine [122, 16, 40]
# Mid luminance (0.15 - 0.55): vibrant velvet wine and berry magenta [170, 25, 60] -> [217, 119, 6]
# High luminance (0.55 - 0.85): glowing amber gold [245, 166, 35] -> [254, 215, 170]
# Ultra luminance (> 0.85): sparkling white-gold stars [255, 255, 255]

out = np.zeros_like(arr_norm)

for i in range(h):
    lum_row = luminance[i]
    vig_row = vignette[i]
    
    # We construct colors based on luminance curves:
    # Red channel: strong across all luminances
    r_chan = np.where(lum_row < 0.2, 
                      bg_color[0] + (122.0/255.0 - bg_color[0]) * (lum_row / 0.2),
                      np.where(lum_row < 0.6,
                               122.0/255.0 + (245.0/255.0 - 122.0/255.0) * ((lum_row - 0.2) / 0.4),
                               245.0/255.0 + (1.0 - 245.0/255.0) * ((lum_row - 0.6) / 0.4)))
    
    # Green channel: low for wine, rises for amber and bright stars
    g_chan = np.where(lum_row < 0.2,
                      bg_color[1] + (16.0/255.0 - bg_color[1]) * (lum_row / 0.2),
                      np.where(lum_row < 0.6,
                               16.0/255.0 + (166.0/255.0 - 16.0/255.0) * ((lum_row - 0.2) / 0.4),
                               166.0/255.0 + (1.0 - 166.0/255.0) * ((lum_row - 0.6) / 0.4)))
    
    # Blue channel: wine has some blue, amber has low blue, white stars have high blue
    b_chan = np.where(lum_row < 0.2,
                      bg_color[2] + (40.0/255.0 - bg_color[2]) * (lum_row / 0.2),
                      np.where(lum_row < 0.6,
                               40.0/255.0 + (35.0/255.0 - 40.0/255.0) * ((lum_row - 0.2) / 0.4),
                               35.0/255.0 + (1.0 - 35.0/255.0) * ((lum_row - 0.6) / 0.4)))
    
    # Blend with background color according to vignette
    out[i, :, 0] = bg_color[0] + (r_chan - bg_color[0]) * vig_row
    out[i, :, 1] = bg_color[1] + (g_chan - bg_color[1]) * vig_row
    out[i, :, 2] = bg_color[2] + (b_chan - bg_color[2]) * vig_row

out_uint8 = np.clip(out * 255.0, 0, 255).astype(np.uint8)

# Check edges of the newly generated image
edge_top = out_uint8[0, :, :].mean(axis=0)
edge_bottom = out_uint8[-1, :, :].mean(axis=0)
edge_left = out_uint8[:, 0, :].mean(axis=0)
edge_right = out_uint8[:, -1, :].mean(axis=0)

print('New Top Edge average RGB:', edge_top.astype(int), 'Expected ~ [37, 1, 9]')
print('New Bottom Edge average RGB:', edge_bottom.astype(int), 'Expected ~ [37, 1, 9]')
print('New Left Edge average RGB:', edge_left.astype(int), 'Expected ~ [37, 1, 9]')
print('New Right Edge average RGB:', edge_right.astype(int), 'Expected ~ [37, 1, 9]')

# Save new vortex image
result_img = Image.fromarray(out_uint8)
result_img.save('assets/images/vortex-404-cosmic.webp', format='WEBP', quality=92)
print('Successfully saved remapped vortex-404-cosmic.webp in application velvet wine & amber palette!')

