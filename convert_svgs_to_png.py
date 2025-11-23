#!/usr/bin/env python3
"""
Convert SVG icons to high-resolution PNG images for PowerPoint
Using Inkscape for conversion (3x resolution for Retina)
"""

import subprocess
import os

# Icon files to convert
icons = ["legal", "medical", "financial", "engineering", "thermometer", "encryption_lock", "encryption_unlock", "cloud_server", "pdf_document", "user_face"]

# Output size: High resolution for sharp icons
# Standard icons: 144px, Thermometer: 400px, Lock icons: 300px, Cloud: 300px
output_sizes = {
    "legal": 144,
    "medical": 144,
    "financial": 144,
    "engineering": 144,
    "thermometer": 400,  # Higher resolution for large display on slide
    "encryption_lock": 300,  # High resolution for encryption slide
    "encryption_unlock": 300,  # High resolution for encryption slide
    "cloud_server": 300,  # High resolution for encryption slide
    "pdf_document": 200,  # PDF icon for document processing slide
    "user_face": 200  # User face icon for document processing slide
}

# Icons that need tight cropping (export only the drawn area, no extra space)
crop_to_drawing = ["cloud_server"]

print("🎨 Converting SVG icons to high-resolution PNGs using Inkscape...")

for icon_name in icons:
    svg_path = f"assets/icons/{icon_name}.svg"
    png_path = f"assets/icons/{icon_name}.png"
    size = output_sizes.get(icon_name, 144)  # Default to 144 if not specified

    try:
        # Build Inkscape command
        cmd = [
            "/opt/homebrew/bin/inkscape",
            svg_path,
            "--export-type=png",
            f"--export-filename={png_path}",
            f"--export-width={size}",
            f"--export-height={size}"
        ]

        # Add --export-area-drawing for icons that need tight cropping
        if icon_name in crop_to_drawing:
            cmd.append("--export-area-drawing")

        # Use Inkscape to convert SVG to PNG
        subprocess.run(cmd, check=True, capture_output=True, text=True)

        print(f"   ✅ {icon_name}.svg → {icon_name}.png ({size}x{size}px)")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to convert {icon_name}.svg: {str(e)}")
        print(f"      stderr: {e.stderr}")
    except Exception as e:
        print(f"   ❌ Unexpected error for {icon_name}.svg: {str(e)}")

print("\n✅ Conversion complete! PNG files are ready for PowerPoint.")
