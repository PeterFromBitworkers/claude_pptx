#!/usr/bin/env python3
"""
Findet alle Inter-Font Dateien und extrahiert deren PostScript-Namen
"""
import os
from pathlib import Path
from fontTools import ttLib

def get_font_names(font_path):
    """Extrahiert alle relevanten Namen aus einer Font-Datei"""
    try:
        font = ttLib.TTFont(font_path)
        names = {}
        
        # Name table IDs:
        # 1 = Font Family
        # 2 = Font Subfamily (Regular, Bold, etc.)
        # 4 = Full Font Name
        # 6 = PostScript Name (← Das brauchen wir!)
        # 16 = Typographic Family (optional)
        # 17 = Typographic Subfamily (optional)
        
        for record in font['name'].names:
            # Nur englische Namen (Platform 1 oder 3, Language 0x409)
            if record.platformID in [1, 3] and record.langID in [0, 0x409]:
                name_id = record.nameID
                try:
                    text = record.toUnicode()
                    if name_id == 1:
                        names['family'] = text
                    elif name_id == 2:
                        names['subfamily'] = text
                    elif name_id == 4:
                        names['full_name'] = text
                    elif name_id == 6:
                        names['postscript'] = text
                    elif name_id == 16:
                        names['typo_family'] = text
                    elif name_id == 17:
                        names['typo_subfamily'] = text
                except:
                    pass
        
        font.close()
        return names
    except Exception as e:
        return {'error': str(e)}

# Suche nach Inter-Fonts im Projekt-Ordner
font_dirs = [
    Path("fonts/Inter-4.0/extras/ttf"),  # Project fonts
    Path.home() / "Library/Fonts",  # User fonts
    Path("/Library/Fonts"),  # System fonts
]

print("🔍 Suche Inter-Fonts...\n")
print("=" * 80)

inter_fonts = []

for font_dir in font_dirs:
    if font_dir.exists():
        # Finde alle Inter*.ttf und Inter*.otf Dateien
        for font_file in font_dir.glob("Inter*.ttf"):
            inter_fonts.append(font_file)
        for font_file in font_dir.glob("Inter*.otf"):
            inter_fonts.append(font_file)

if not inter_fonts:
    print("❌ Keine Inter-Fonts gefunden!")
    print("\nBitte gib den Pfad zum Inter-Font-Ordner an:")
    print("z.B. ~/Downloads/Inter-4.0/Desktop/")
else:
    print(f"✅ {len(inter_fonts)} Inter-Fonts gefunden!\n")
    
    # Sortiere nach Dateinamen
    inter_fonts.sort()
    
    # Zeige alle Fonts mit ihren PostScript-Namen
    for font_file in inter_fonts:
        names = get_font_names(font_file)
        
        if 'error' in names:
            print(f"❌ {font_file.name}: {names['error']}")
        else:
            print(f"📄 {font_file.name}")
            print(f"   Familie:     {names.get('family', 'N/A')}")
            print(f"   Stil:        {names.get('subfamily', 'N/A')}")
            print(f"   Voller Name: {names.get('full_name', 'N/A')}")
            print(f"   ✨ PostScript: {names.get('postscript', 'N/A')}")
            print()

print("=" * 80)
print("\n💡 PowerPoint braucht die 'PostScript' Namen (✨)!")
