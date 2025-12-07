from typing import List
from io import BytesIO
from PIL import Image, ImageDraw
from .utils import hex_to_rgb

def create_palette_image(hex_colors: List[str], width: int = 1000, height: int = 200) -> BytesIO:
    """
    Returns an in-memory PNG image of a horizontal palette strip.
    """
    img = Image.new("RGB", (width, height), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    n = len(hex_colors)
    block_width = width // n

    for i, hex_code in enumerate(hex_colors):
        rgb = hex_to_rgb(hex_code)
        x0 = i * block_width
        x1 = (i + 1) * block_width
        draw.rectangle([x0, 0, x1, height], fill=rgb)

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf
