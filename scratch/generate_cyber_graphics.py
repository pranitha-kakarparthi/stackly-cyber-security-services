from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import math, os

def create_cyber_graphic(title, subtitle, icon_type, filename):
    w, h = 960, 560
    # Create base dark velvet wine gradient background
    img = Image.new('RGB', (w, h), color=(37, 1, 9))
    draw = ImageDraw.Draw(img)
    
    # 1. Subtle cyber grid
    grid_size = 40
    for x in range(0, w, grid_size):
        draw.line([(x, 0), (x, h)], fill=(58, 1, 14), width=1)
    for y in range(0, h, grid_size):
        draw.line([(0, y), (w, y)], fill=(58, 1, 14), width=1)
        
    # 2. Glowing radial circles
    cx, cy = w // 2, h // 2
    for r in range(240, 40, -30):
        alpha = int(25 + (240 - r) * 0.4)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(122, 16, 40), width=1)
    
    # 3. Concentric dashed rings & technical angles
    for r in [180, 140, 100]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(217, 119, 6), width=2)
        
    # Radar sweep lines
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle)
        x2 = cx + int(220 * math.cos(rad))
        y2 = cy + int(220 * math.sin(rad))
        draw.line([(cx, cy), (x2, y2)], fill=(122, 16, 40), width=1)

    # 4. Central Shield / Emblems based on icon_type
    shield_pts = [
        (cx, cy - 80),
        (cx + 65, cy - 40),
        (cx + 65, cy + 30),
        (cx, cy + 90),
        (cx - 65, cy + 30),
        (cx - 65, cy - 40)
    ]
    draw.polygon(shield_pts, fill=(122, 16, 40), outline=(245, 166, 35))
    
    # Inner shield
    inner_pts = [
        (cx, cy - 65),
        (cx + 50, cy - 30),
        (cx + 50, cy + 22),
        (cx, cy + 70),
        (cx - 50, cy + 22),
        (cx - 50, cy - 30)
    ]
    draw.polygon(inner_pts, fill=(58, 1, 14), outline=(217, 119, 6))

    # Center icon symbol
    if icon_type == 'cloud':
        # Cloud node circles
        draw.ellipse([cx - 30, cy - 10, cx + 10, cy + 25], fill=(245, 166, 35))
        draw.ellipse([cx - 10, cy - 25, cx + 30, cy + 15], fill=(245, 166, 35))
        draw.ellipse([cx + 5, cy - 5, cx + 35, cy + 25], fill=(245, 166, 35))
        draw.rectangle([cx - 20, cy + 10, cx + 25, cy + 25], fill=(245, 166, 35))
    elif icon_type == 'incident':
        # Lightning bolt / Warning triage
        bolt_pts = [
            (cx + 5, cy - 40),
            (cx - 20, cy),
            (cx - 2, cy),
            (cx - 10, cy + 40),
            (cx + 20, cy - 5),
            (cx + 2, cy - 5)
        ]
        draw.polygon(bolt_pts, fill=(245, 166, 35), outline=(255, 255, 255))
    elif icon_type == 'vulnerability':
        # Crosshair / Radar target
        draw.ellipse([cx - 25, cy - 25, cx + 25, cy + 25], outline=(245, 166, 35), width=3)
        draw.line([(cx - 35, cy), (cx + 35, cy)], fill=(245, 166, 35), width=2)
        draw.line([(cx, cy - 35), (cx, cy + 35)], fill=(245, 166, 35), width=2)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 255, 255))
    elif icon_type == 'compliance':
        # Checkmark & Seal
        check_pts = [
            (cx - 22, cy - 2),
            (cx - 8, cy + 16),
            (cx + 24, cy - 20),
            (cx + 20, cy - 24),
            (cx - 8, cy + 8),
            (cx - 18, cy - 6)
        ]
        draw.polygon(check_pts, fill=(245, 166, 35), outline=(255, 255, 255))

    # Corner telemetry brackets
    bracket_len = 35
    pad = 25
    # Top-left
    draw.line([(pad, pad), (pad + bracket_len, pad)], fill=(217, 119, 6), width=2)
    draw.line([(pad, pad), (pad, pad + bracket_len)], fill=(217, 119, 6), width=2)
    # Top-right
    draw.line([(w - pad, pad), (w - pad - bracket_len, pad)], fill=(217, 119, 6), width=2)
    draw.line([(w - pad, pad), (w - pad, pad + bracket_len)], fill=(217, 119, 6), width=2)
    # Bottom-left
    draw.line([(pad, h - pad), (pad + bracket_len, h - pad)], fill=(217, 119, 6), width=2)
    draw.line([(pad, h - pad), (pad, h - pad - bracket_len)], fill=(217, 119, 6), width=2)
    # Bottom-right
    draw.line([(w - pad, h - pad), (w - pad - bracket_len, h - pad)], fill=(217, 119, 6), width=2)
    draw.line([(w - pad, h - pad), (w - pad, h - pad - bracket_len)], fill=(217, 119, 6), width=2)

    # Save as webp with high quality and < 100 KB
    save_path = os.path.join('assets/images', filename)
    img.save(save_path, format='WEBP', quality=88, method=6)
    size_kb = os.path.getsize(save_path) / 1024
    print(f"Created {save_path}: {size_kb:.1f} KB")

create_cyber_graphic("Cloud Zero Trust", "Architecture", 'cloud', 'cloud-zero-trust-defense-architecture.webp')
create_cyber_graphic("Incident Response", "Containment Matrix", 'incident', 'incident-response-containment-matrix.webp')
create_cyber_graphic("Vulnerability Management", "Radar", 'vulnerability', 'vulnerability-management-scanner.webp')
create_cyber_graphic("ISO 27001 Compliance", "Evidence Vault", 'compliance', 'iso-compliance-security-vault.webp')

