from typing import List, Tuple
import colorsys
from .utils import hex_to_rgb, rgb_to_hex

def _rgb_to_hsl(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, s, l  # (h, s, l) for convenience

def _hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def complementary(hex_code: str) -> str:
    rgb = hex_to_rgb(hex_code)
    h, s, l = _rgb_to_hsl(rgb)
    h = (h + 0.5) % 1.0
    return rgb_to_hex(_hsl_to_rgb(h, s, l))

def analogous(hex_code: str, angle: float = 1/12) -> List[str]:
    # angle ≈ 30 degrees (1/12 of circle)
    rgb = hex_to_rgb(hex_code)
    h, s, l = _rgb_to_hsl(rgb)
    colors = []
    for offset in (-angle, angle):
        h2 = (h + offset) % 1.0
        colors.append(rgb_to_hex(_hsl_to_rgb(h2, s, l)))
    return colors

def triadic(hex_code: str) -> List[str]:
    rgb = hex_to_rgb(hex_code)
    h, s, l = _rgb_to_hsl(rgb)
    c1 = rgb_to_hex(_hsl_to_rgb((h + 1/3) % 1.0, s, l))
    c2 = rgb_to_hex(_hsl_to_rgb((h + 2/3) % 1.0, s, l))
    return [c1, c2]
