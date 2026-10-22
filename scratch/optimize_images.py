import os
from PIL import Image

image_dir = 'assets/images'
print("Auditing and optimizing all images in assets/images...")

for filename in os.listdir(image_dir):
    filepath = os.path.join(image_dir, filename)
    if not os.path.isfile(filepath):
        continue
    
    size_kb = os.path.getsize(filepath) / 1024
    if size_kb >= 95:
        print(f"Compressing {filename} ({size_kb:.1f} KB)...")
        with Image.open(filepath) as img:
            # Try saving with quality reduction
            quality = 85
            while quality >= 30:
                temp_path = filepath + '.tmp.webp'
                img.save(temp_path, 'WEBP', quality=quality, method=6)
                new_size = os.path.getsize(temp_path) / 1024
                if new_size < 95:
                    os.replace(temp_path, filepath)
                    print(f"  Optimized {filename} to {new_size:.1f} KB (quality={quality})")
                    break
                else:
                    os.remove(temp_path)
                    quality -= 5
            
            # If still > 95 KB, resize dimensions slightly
            if os.path.getsize(filepath) / 1024 >= 95:
                w, h = img.size
                new_w, new_h = int(w * 0.85), int(h * 0.85)
                resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                resized.save(filepath, 'WEBP', quality=80, method=6)
                final_size = os.path.getsize(filepath) / 1024
                print(f"  Resized & optimized {filename} to {final_size:.1f} KB")

print("\n--- Final Image Audit ---")
all_under_100 = True
for filename in os.listdir(image_dir):
    filepath = os.path.join(image_dir, filename)
    if os.path.isfile(filepath):
        size_kb = os.path.getsize(filepath) / 1024
        status = "OK (<100KB)" if size_kb < 100 else "EXCEEDS!"
        print(f"{filename:50} : {size_kb:.1f} KB [{status}]")
        if size_kb >= 100:
            all_under_100 = False

print(f"\nAll images under 100 KB: {all_under_100}")

