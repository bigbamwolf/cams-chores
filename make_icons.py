"""Generate Cams Chores PWA icons with Pillow.

Produces icon-192.png, icon-512.png, icon-512-maskable.png in the same folder.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

OUT = os.path.dirname(os.path.abspath(__file__))


def make_icon(size: int, maskable: bool = False) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # BTS purple gradient (top soft lilac to bottom deep ARMY purple)
    grad = Image.new("RGB", (size, size), (201, 168, 240))
    gd = ImageDraw.Draw(grad)
    top = (201, 168, 240)
    bot = (107, 63, 160)
    for y in range(size):
        t = y / max(size - 1, 1)
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        gd.line([(0, y), (size, y)], fill=(r, g, b))
    # Diagonal magenta overlay for Euphoria sparkle
    overlay = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for x in range(size):
        t = x / max(size - 1, 1)
        od.line([(x, 0), (x, size)], fill=(208, 77, 160, int(50 * t)))
    bg = Image.alpha_composite(grad.convert("RGBA"), overlay)

    if maskable:
        img = bg
    else:
        # Rounded square mask for non-maskable
        mask = Image.new("L", (size, size), 0)
        md = ImageDraw.Draw(mask)
        radius = int(size * 0.22)
        md.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=255)
        img.paste(bg, (0, 0), mask)

    d = ImageDraw.Draw(img)

    # Soft white circle in the center
    cx = size // 2
    cy = size // 2
    inner_r = int(size * 0.32)
    d.ellipse(
        (cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r),
        fill=(255, 255, 255, 235),
    )

    # Checkmark stroke (ARMY purple)
    stroke_w = max(int(size * 0.06), 6)
    color = (155, 89, 214, 255)
    # Check: from (cx-r*0.55, cy+r*0.05) to (cx-r*0.05, cy+r*0.50) to (cx+r*0.65, cy-r*0.40)
    p1 = (cx - int(inner_r * 0.55), cy + int(inner_r * 0.05))
    p2 = (cx - int(inner_r * 0.05), cy + int(inner_r * 0.45))
    p3 = (cx + int(inner_r * 0.60), cy - int(inner_r * 0.45))
    d.line([p1, p2, p3], fill=color, width=stroke_w, joint="curve")
    # Round caps
    cap = stroke_w // 2
    for pt in (p1, p2, p3):
        d.ellipse((pt[0] - cap, pt[1] - cap, pt[0] + cap, pt[1] + cap), fill=color)

    # Tiny sparkle accents
    for sx, sy, sr in [
        (cx - int(inner_r * 1.05), cy - int(inner_r * 0.75), max(int(size * 0.018), 3)),
        (cx + int(inner_r * 1.05), cy + int(inner_r * 0.85), max(int(size * 0.022), 4)),
        (cx + int(inner_r * 1.20), cy - int(inner_r * 0.20), max(int(size * 0.014), 3)),
    ]:
        if 0 <= sx < size and 0 <= sy < size:
            d.ellipse((sx - sr, sy - sr, sx + sr, sy + sr), fill=(255, 255, 255, 220))

    return img


def main() -> None:
    for size, name in [(192, "icon-192.png"), (512, "icon-512.png")]:
        img = make_icon(size, maskable=False)
        path = os.path.join(OUT, name)
        img.save(path, "PNG")
        print("wrote", path)
    mask_img = make_icon(512, maskable=True)
    mp = os.path.join(OUT, "icon-512-maskable.png")
    mask_img.save(mp, "PNG")
    print("wrote", mp)


if __name__ == "__main__":
    main()
