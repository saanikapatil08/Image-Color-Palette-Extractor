from .utils import hex_to_rgb

def _relative_luminance(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def contrast_ratio(hex1: str, hex2: str) -> float:
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    L1 = _relative_luminance(rgb1)
    L2 = _relative_luminance(rgb2)
    lighter = max(L1, L2)
    darker = min(L1, L2)
    return (lighter + 0.05) / (darker + 0.05)

def wcag_rating(ratio: float) -> str:
    if ratio >= 7:
        return "AAA"
    elif ratio >= 4.5:
        return "AA"
    elif ratio >= 3:
        return "AA Large"
    else:
        return "Fail"
