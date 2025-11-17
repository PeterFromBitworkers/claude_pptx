# Brain-Bridges PowerPoint Design System

> 📋 **Dokumentation für zukünftige Bearbeitungen und KI-Sessions**  
> Version: xii  
> Zuletzt aktualisiert: 2025-11-16

---

## 🎨 Design-Tokens

### Farben (RGB)

```css
Hintergrund:
  --background-dark: rgb(17, 24, 39)      /* Haupt-Hintergrund */
  --background-light: rgb(31, 41, 55)     /* Karten/Boxen */

Text:
  --text-white: rgb(255, 255, 255)        /* Haupttext */
  --text-gray: rgb(209, 213, 219)         /* Sekundärtext */
  --text-gray-dark: rgb(167, 171, 175)    /* Seitenzahl (mit opacity) */

Akzentfarben:
  --accent-blue: rgb(77, 171, 247)        /* #4dabf7 */
  --accent-cyan: rgb(6, 182, 212)         /* #06b6d4 */
  --accent-green: rgb(16, 185, 129)       /* #10b981 */
  --accent-red: rgb(239, 68, 68)          /* #ef4444 */
  --accent-purple: rgb(139, 92, 246)      /* #8b5cf6 */

Borders:
  --border-color: rgb(64, 64, 64)         /* #404040 */
```

### Schriftarten

```
Primary Font: System-UI / Segoe UI / Roboto / Helvetica Neue
  - Verwendet für: Alle Texte außer Code

Mono Font: SFMono-Regular / Consolas / Monaco
  - Verwendet für: Code, technische Details
```

### Schriftgrößen & Weights

```
Logo "BRAIN BRIDGES":
  - Size: 21pt
  - Weight: Bold (800)
  - Color: Weiß
  - Letter-spacing: -0.5pt (tight)
  - Position: 40px von oben, 40px von links

Seitenzahl "##/17":
  - Size: 21pt
  - Weight: Normal (400)
  - Color: rgb(167, 171, 175)
  - Position: 40px von oben, 40px von rechts
  - Alignment: Rechtsbündig

Keywords (THE, AI, PARADOX):
  - Size: 72pt
  - Weight: Light (200) - so dünn wie möglich!
  - Letter-spacing: 2pt
  - Text-transform: UPPERCASE
  - Vertical gap: ca. 100-120pt zwischen Wörtern
```

---

## 📐 Master Slide Struktur

### Haupt-Master (alle Folien)

```
Elemente die auf JEDER Folie erscheinen:

1. Hintergrund:
   - Farbe: rgb(17, 24, 39)
   - Keine Verlaufe, solid fill

2. Logo (oben links):
   - Text: "BRAIN BRIDGES"
   - Position: 0.28" von oben, 0.28" von links
   - Größe: 21pt, Bold, Weiß
   - WICHTIG: "(v: xii)" NICHT im Logo!

3. Seitenzahl (oben rechts):
   - Format: "01/17" (zweistellig mit führender Null)
   - Position: 15.1" von links, 0.28" von oben
   - Größe: 21pt, Normal, Grau
   - Rechtsbündig
```

### Layout 1: "Keyword Slide"

```
Verwendet für: Slides 1, 4, 6
Beispiel: "THE AI PARADOX"

Content-Bereich:
  - 3 separate Textboxen, vertikal zentriert
  - Jede Box: 12" breit, zentriert horizontal
  - Vertikaler Start: ca. 2.3" von oben
  - Gap zwischen Boxen: ca. 1.4"
  
Keyword-Farben (rotieren):
  Theme 1 (Problem): Rot → Blau → Grün
  Theme 2 (Solution): Blau → Cyan → Grün  
  Theme 3 (Tech): Lila → Blau → Cyan
```

### Layout 2: "Content Slide"

```
Verwendet für: Slides 2, 3, 7-16
Beispiel: "Organisations want AI"

Struktur:
  - Fixed Header (top: 1", zentriert)
    • Haupttitel: 48pt, Light, Blau
    • Subtitle: 20pt, Bold, Rot oder Grau
  
  - Content-Bereich (beginnt bei ca. 3")
    • Flexible Layouts (Grid, Liste, etc.)
    • Max-Width: ca. 1400px = 14"
```

### Layout 3: "Blank with Master"

```
Leere Folie mit nur Logo und Seitenzahl
Für custom Layouts oder Bilder
```

---

## 🎯 Keyword-Slide Farb-Themes

### Theme 1: "Problem" (Slide 1)
```css
Keyword 1: rgb(239, 68, 68)    /* Rot - THE */
Keyword 2: rgb(77, 171, 247)   /* Blau - AI */
Keyword 3: rgb(16, 185, 129)   /* Grün - PARADOX */
```

### Theme 2: "Solution" (Slide 4)
```css
Keyword 1: rgb(77, 171, 247)   /* Blau - SOVEREIGN */
Keyword 2: rgb(6, 182, 212)    /* Cyan - AI */
Keyword 3: rgb(16, 185, 129)   /* Grün - SOLUTION */
```

### Theme 3: "Tech" (Slide 6)
```css
Keyword 1: rgb(139, 92, 246)   /* Lila - TECHNICAL */
Keyword 2: rgb(77, 171, 247)   /* Blau - DEEP */
Keyword 3: rgb(6, 182, 212)    /* Cyan - DIVE */
```

---

## 📦 Slide-Übersicht

```
01. THE AI PARADOX (Keyword Slide - Theme 1)
02. Organisations want AI (Content - Problem Grid)
03. Market Reality (Content - Stats Carousel)
04. SOVEREIGN AI SOLUTION (Keyword Slide - Theme 2)
05. Meet the Box (Content - Hardware Specs)
06. TECHNICAL DEEP DIVE (Keyword Slide - Theme 3)
07-16. Various Content Slides
17. WHY NOW? (Content - Timeline)
```

---

## 🔧 Arbeiten mit dem Master

### Master bearbeiten in PowerPoint:

1. **Master öffnen:**
   ```
   Ansicht → Folienmaster
   (oder View → Slide Master)
   ```

2. **Haupt-Master auswählen:**
   - Oberste/größte Folie in der linken Leiste
   - Änderungen hier betreffen ALLE Folien

3. **Layout-Master auswählen:**
   - Unterhalb des Haupt-Masters
   - Änderungen nur für diesen Typ

4. **Master schließen:**
   ```
   Folienmaster → Masteransicht schließen
   ```

### Neue Folie mit Master erstellen:

1. **Folie einfügen:**
   ```
   Start → Neue Folie → Layout auswählen
   ```

2. **Seitenzahl aktualisieren:**
   - Automatisch wenn im Master konfiguriert
   - Oder manuell die Zahl anpassen

---

## 💡 Wichtige Hinweise

### DO's ✅
- Immer die exakten RGB-Werte verwenden
- Konsistente Abstände einhalten
- Schrift so dünn wie möglich (Light/200)
- Letter-spacing für Keywords beachten
- Seitenzahlen zweistellig mit führender Null

### DON'Ts ❌
- Keine "(v: xii)" im Logo auf normalen Folien
- Keine Verlaufe im Hintergrund (nur solid)
- Keine zusätzlichen Rahmen oder Schatten
- Keywords nicht mit nur einem Textfeld machen
- Font-Weight nicht zu schwer (max. Bold für Titel)

---

## 📝 Checkliste für neue Folien

```
□ Hintergrundfarbe: rgb(17, 24, 39)
□ Logo "BRAIN BRIDGES" oben links (21pt, Bold, Weiß)
□ Seitenzahl "##/17" oben rechts (21pt, Normal, Grau)
□ Richtige Farben aus Design-Tokens verwendet
□ Schriftgrößen und -gewichte konsistent
□ Abstände wie im Master definiert
□ Keine zusätzlichen Effekte/Schatten
```

---

## 🔄 Für KI-Sessions

Wenn du diese Präsentation mit Claude oder einem anderen KI-Tool bearbeitest:

1. **Diese README hochladen!**
2. Die aktuelle .pptx Datei hochladen
3. Dem KI-Tool sagen: "Lies die README und halte dich an das Design-System"

**Wichtige Info für KI:**
- python-pptx kann Master-Slides NICHT direkt bearbeiten
- Stattdessen: Master-Elemente auf jede Folie anwenden
- Die Funktion `apply_master_elements(slide, slide_num)` verwenden
- Alle Farben als RGB(r, g, b) angeben, nicht Hex

---

## 📞 Quick Reference

```python
# Standard Master-Elemente anwenden (Python)
def apply_master_elements(slide, slide_num, total=17):
    # Hintergrund
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(17, 24, 39)
    
    # Logo (0.28", 0.28", 21pt, Bold, Weiß)
    # Seitenzahl (15.1", 0.28", 21pt, Normal, Grau)
```

```vba
' VBA Referenz (falls benötigt)
ActivePresentation.SlideMaster.Background.Fill.ForeColor.RGB = RGB(17, 24, 39)
```

---

**Ende der README** • Bei Fragen: Diese Datei aktualisieren und versionieren! 🚀
