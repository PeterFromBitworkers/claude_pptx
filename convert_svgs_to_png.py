#!/usr/bin/env python3
"""
Convert SVG icons to high-resolution PNG images for PowerPoint
Using Inkscape for conversion (3x resolution for Retina)
"""

import subprocess
import os

# Icon files to convert
icons = ["legal", "medical", "financial", "engineering"]

# Output size: 3x for high DPI (48px base * 3 = 144px)
output_size = 144

print("🎨 Converting SVG icons to high-resolution PNGs using Inkscape...")

for icon_name in icons:
    svg_path = f"assets/icons/{icon_name}.svg"
    png_path = f"assets/icons/{icon_name}.png"

    try:
        # Use Inkscape to convert SVG to PNG
        subprocess.run([
            "/opt/homebrew/bin/inkscape",
            svg_path,
            "--export-type=png",
            f"--export-filename={png_path}",
            f"--export-width={output_size}",
            f"--export-height={output_size}"
        ], check=True, capture_output=True, text=True)

        print(f"   ✅ {icon_name}.svg → {icon_name}.png ({output_size}x{output_size}px)")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to convert {icon_name}.svg: {str(e)}")
        print(f"      stderr: {e.stderr}")
    except Exception as e:
        print(f"   ❌ Unexpected error for {icon_name}.svg: {str(e)}")

print("\n✅ Conversion complete! PNG files are ready for PowerPoint.")
