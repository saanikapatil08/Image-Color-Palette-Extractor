from typing import List
import json

def export_as_json(hex_colors: List[str]) -> str:
    data = {f"color_{i+1}": c for i, c in enumerate(hex_colors)}
    return json.dumps(data, indent=2)

def export_as_css(hex_colors: List[str]) -> str:
    lines = [":root {"]
    for i, c in enumerate(hex_colors):
        lines.append(f"  --color-{i+1}: {c};")
    lines.append("}")
    return "\n".join(lines)

def export_as_tailwind(hex_colors: List[str]) -> str:
    lines = ['// tailwind.config.js snippet', 'module.exports = {', '  theme: {', '    extend: {', '      colors: {']
    for i, c in enumerate(hex_colors):
        lines.append(f"        palette{i+1}: '{c}',")
    lines.extend(['      }', '    }', '  }', '};'])
    return "\n".join(lines)
