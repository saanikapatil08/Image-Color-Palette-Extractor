from typing import Tuple

def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
