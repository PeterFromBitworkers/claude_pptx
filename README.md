# Brain-Bridges PowerPoint Design System

> 📋 **Human-readable design documentation** 🤖 **For AI/Claude Code:** See
> [CLAUDE.md](CLAUDE.md) Version: xii Last updated: 2025-11-17

---

## 📖 Introduction

This project generates a complete PowerPoint presentation for "Brain-Bridges"
using **python-pptx**, a Python library for creating and manipulating PowerPoint
(.pptx) files programmatically. Unlike working directly in PowerPoint where you
can define a master slide template and all slides inherit from it automatically,
python-pptx has a significant limitation: **we cannot programmatically edit the
master slide structure**.

This means we need to apply consistent styling elements—like the logo, slide
numbers, background colors, and fonts—to each individual slide through code. To
maintain consistency, we've created the `apply_master_elements()` function that
applies our "master" design to every slide we generate. This ensures that
despite the programmatic limitation, our presentation maintains a cohesive,
professional look across all 17 slides.

The design system documented below serves as the single source of truth for
colors, typography, layouts, and spacing. By following these tokens strictly, we
ensure visual consistency whether slides are generated from scratch or modified
later.

---

## 🚀 Getting Started & Deployment

### Prerequisites

- Python 3.x installed
- python-pptx library (see requirements.txt)

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Generator

```bash
# Generate a new PowerPoint presentation
python3 generate_pptx.py
```

### Output & Versioning

Each time you run the generator, a **new timestamped version** is created in the
`output/` directory:

```
output/
├── 2025_11_17___14_30_45__Brain-Bridges.pptx
├── 2025_11_17___15_26_22__Brain-Bridges.pptx
├── 2025_11_17___16_42_10__Brain-Bridges.pptx
└── Brain-Bridges_LATEST.pptx  (copy of most recent)
```

**Timestamp Format:** `YYYY_MM_DD___HH_MM_SS`

- Example: `2025_11_17___15_26_22__Brain-Bridges.pptx`
- Generated: November 17, 2025 at 15:26:22

**Why versioning?**

- Every generation creates a new version
- Never overwrites previous versions
- Easy to track changes over time
- `Brain-Bridges_LATEST.pptx` always points to the most recent version for
  convenience

### Workflow

1. Edit `generate_pptx.py` or `slides_content.json` (future)
2. Run: `python3 generate_pptx.py`
3. Check: `output/Brain-Bridges_LATEST.pptx`
4. If satisfied, commit changes to git

---

## 🎨 Design Tokens

> **⚠️ Single Source of Truth:** All design values are defined in
> [`design_tokens.py`](design_tokens.py)
>
> The values below are for **reference only**. To change colors, fonts, or
> layouts, edit `design_tokens.py` directly.

### Colors (RGB)

```css
Background:
  --background-dark: rgb(17, 24, 39)      /* Main background */
  --background-light: rgb(31, 41, 55)     /* Cards/boxes */

Text:
  --text-white: rgb(255, 255, 255)        /* Primary text */
  --text-gray: rgb(209, 213, 219)         /* Secondary text */
  --text-gray-dark: rgb(167, 171, 175)    /* Slide numbers (with opacity) */

Accent Colors:
  --accent-blue: rgb(77, 171, 247)        /* #4dabf7 */
  --accent-cyan: rgb(6, 182, 212)         /* #06b6d4 */
  --accent-green: rgb(16, 185, 129)       /* #10b981 */
  --accent-red: rgb(239, 68, 68)          /* #ef4444 */
  --accent-purple: rgb(139, 92, 246)      /* #8b5cf6 */

Borders:
  --border-color: rgb(64, 64, 64)         /* #404040 */
```

### Typography

```
Primary Font: System-UI / Segoe UI / Roboto / Helvetica Neue
  - Used for: All text except code

Mono Font: SFMono-Regular / Consolas / Monaco
  - Used for: Code, technical details
```

### Font Sizes & Weights

```
Logo "BRAIN BRIDGES":
  - Size: 21pt
  - Weight: Bold (800)
  - Color: White
  - Letter-spacing: -0.5pt (tight)
  - Position: 40px from top, 40px from left

Slide Number "##/17":
  - Size: 21pt
  - Weight: Normal (400)
  - Color: rgb(167, 171, 175)
  - Position: 40px from top, 40px from right
  - Alignment: Right-aligned

Keywords (THE, AI, PARADOX):
  - Size: 72pt
  - Weight: Light (200) - as thin as possible!
  - Letter-spacing: 2pt
  - Text-transform: UPPERCASE
  - Vertical gap: approx. 100-120pt between words
```

---

## 📐 Master Slide Structure

> **📌 Note:** Layout values (positions, dimensions) are defined in
> `design_tokens.py`

### Main Master (all slides)

```
Elements that appear on EVERY slide:

1. Background:
   - Color: rgb(17, 24, 39)
   - Solid fill (currently no gradients used)

2. Logo (top left):
   - Text: "BRAIN BRIDGES"
   - Position: 0.28" from top, 0.28" from left
   - Size: 21pt, Bold, White
   - IMPORTANT: NO "(v: xii)" in the logo!

3. Slide Number (top right):
   - Format: "01/17" (two digits with leading zero)
   - Position: 15.1" from left, 0.28" from top
   - Size: 21pt, Normal, Gray
   - Right-aligned
```

### Layout 1: "Keyword Slide"

```
Used for: Slides 1, 4, 6
Example: "THE AI PARADOX"

Content Area:
  - 3 separate textboxes, vertically centered
  - Each box: 12" wide, horizontally centered
  - Vertical start: approx. 2.3" from top
  - Gap between boxes: approx. 1.4"

Keyword Colors (rotating):
  Theme 1 (Problem): Red → Blue → Green
  Theme 2 (Solution): Blue → Cyan → Green
  Theme 3 (Tech): Purple → Blue → Cyan
```

### Layout 2: "Content Slide"

```
Used for: Slides 2, 3, 7-16
Example: "Organisations want AI"

Structure:
  - Fixed Header (top: 1", centered)
    • Main title: 48pt, Light, Blue
    • Subtitle: 20pt, Bold, Red or Gray

  - Content Area (starts at approx. 3")
    • Flexible layouts (grid, list, etc.)
    • Max-Width: approx. 1400px = 14"
```

### Layout 3: "Blank with Master"

```
Empty slide with only logo and slide number
For custom layouts or images
```

---

## 🎯 Keyword-Slide Color Themes

### Theme 1: "Problem" (Slide 1)

```css
Keyword 1: rgb(239, 68, 68)    /* Red - THE */
Keyword 2: rgb(77, 171, 247)   /* Blue - AI */
Keyword 3: rgb(16, 185, 129)   /* Green - PARADOX */
```

### Theme 2: "Solution" (Slide 4)

```css
Keyword 1: rgb(77, 171, 247)   /* Blue - SOVEREIGN */
Keyword 2: rgb(6, 182, 212)    /* Cyan - AI */
Keyword 3: rgb(16, 185, 129)   /* Green - SOLUTION */
```

### Theme 3: "Tech" (Slide 6)

```css
Keyword 1: rgb(139, 92, 246)   /* Purple - TECHNICAL */
Keyword 2: rgb(77, 171, 247)   /* Blue - DEEP */
Keyword 3: rgb(6, 182, 212)    /* Cyan - DIVE */
```

---

## 📦 Slide Overview

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
