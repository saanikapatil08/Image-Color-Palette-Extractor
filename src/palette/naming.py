import colorsys
from .utils import hex_to_rgb


def name_for_color(hex_code: str) -> str:
    """
    Generate a simple, human-friendly color name based on HSL.

    - Detects neutrals (White / Light Gray / Gray / Dark Gray / Almost Black)
      when saturation is low.
    - Uses hue ranges to pick families like Red, Orange, Yellow, Brown, Green,
      Teal, Cyan, Blue, Indigo, Purple, Magenta, Pink.
    - Adds lightness adjectives: Very Light, Light, Dark, Very Dark.
    """

    # --- RGB → HSL ---
    r, g, b = hex_to_rgb(hex_code)
    r_f, g_f, b_f = [c / 255.0 for c in (r, g, b)]
    # colorsys: (h, l, s) with h in [0,1), l,s in [0,1]
    h, l, s = colorsys.rgb_to_hls(r_f, g_f, b_f)

    # --- 1) Neutral colors (low saturation) ---
    if s < 0.12:
        if l > 0.92:
            return "White"
        elif l > 0.75:
            return "Light Gray"
        elif l > 0.55:
            return "Gray"
        elif l > 0.35:
            return "Dark Gray"
        else:
            return "Almost Black"

    # --- 2) Hue-based base color name ---
    deg = h * 360.0

    if deg < 12 or deg >= 348:
        base = "Red"
    elif deg < 35:
        base = "Orange"
    elif deg < 65:
        base = "Yellow"
    elif deg < 95:
        base = "Lime"
    elif deg < 150:
        base = "Green"
    elif deg < 180:
        base = "Teal"
    elif deg < 210:
        base = "Cyan"
    elif deg < 235:
        base = "Blue"
    elif deg < 270:
        base = "Indigo"
    elif deg < 300:
        base = "Purple"
    elif deg < 330:
        base = "Magenta"
    else:
        base = "Pink"

    # --- 3) Special handling for Browns & Pinks ---

    # Light-ish reds / magentas become Pink
    if base in ["Red", "Magenta"] and l > 0.70:
        base = "Pink"

    # Dark/medium reds-oranges-yellows with not-too-high saturation → Brown
    if base in ["Red", "Orange", "Yellow"] and l < 0.60 and s < 0.80:
        base = "Brown"

    # --- 4) Lightness adjectives ---
    if l > 0.82:
        prefix = "Very Light "
    elif l > 0.65:
        prefix = "Light "
    elif l < 0.18:
        prefix = "Very Dark "
    elif l < 0.32:
        prefix = "Dark "
    else:
        prefix = ""

    return prefix + base
