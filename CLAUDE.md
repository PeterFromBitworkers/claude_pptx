# CLAUDE.md - AI Assistant Instructions

> 🤖 **This file is optimized for Claude Code and other AI assistants**  
> **Human-readable docs:** See README.md  
> **Last updated:** 2025-11-17

---

## 🎯 Project Overview

**Project Type:** PowerPoint presentation generator using python-pptx  
**Goal:** Generate "Brain-Bridges" AI pitch deck (17 slides, 16:9 format)  
**Source of Truth:** Python script generates the .pptx file  
**Design System:** Documented in README.md

---

## 🏗️ Architecture

```
claude_pptx/
├── CLAUDE.md                    # ← YOU ARE HERE (AI instructions)
├── README.md                    # Human-readable design system
├── design_tokens.py            # ⭐ SINGLE SOURCE OF TRUTH (colors, fonts, layouts)
├── CHANGELOG.md                 # Version history
├── generate_pptx.py            # Main generator script (imports design_tokens)
├── slides_content.json         # Slide content data
├── requirements.txt            # Python dependencies
├── output/
│   └── Brain-Bridges.pptx      # Generated file (gitignored)
└── legacy/                      # ⚠️ DEPRECATED HTML version (see below)
    ├── dist/
    │   ├── index.html          # Complete HTML presentation (1242 lines)
    │   ├── style.css           # CSS styles
    │   ├── script.js           # JS logic
    │   └── assets/             # Images, fonts, etc.
    └── slides/
        ├── slide-01/           # Individual slide components
        │   ├── content.html    # Slide HTML
        │   └── styles.css      # Slide-specific CSS
        └── ... (slide-02 to slide-17)
```

---

## 🚀 Quick Start for AI Assistants

### 1. Understand the Project
```bash
# Read these files in this order:
cat CLAUDE.md           # This file
cat design_tokens.py    # ⭐ All design values (CRITICAL!)
cat README.md           # Human-readable documentation
cat generate_pptx.py    # Generator code
cat slides_content.json # Current slide content
```

### 2. Make Changes
```python
# To change colors/fonts/layouts: Edit design_tokens.py
# To change slide content: Edit generate_pptx.py or slides_content.json
# ALL design values come from design_tokens.py
```

### 3. Generate PowerPoint
```bash
python3 generate_pptx.py
# Output: output/Brain-Bridges.pptx
```

### 4. Commit Changes
```bash
git add .
git commit -m "feat: your change description"
git push
```

---

## 📋 Design System (CRITICAL)

### ⚠️ Single Source of Truth: `design_tokens.py`

**ALL design values are defined in `design_tokens.py`:**
- Colors (backgrounds, text, accents)
- Typography (font sizes, weights, letter-spacing)
- Layout (positions, dimensions, spacing)
- Themes (keyword color combinations)

**To change any design value:**
1. Open `design_tokens.py`
2. Modify the constant (e.g., `COLOR_ACCENT_BLUE`)
3. Save the file
4. Run `python3 generate_pptx.py`

**Example constants:**
```python
# Import in your code
from design_tokens import *

# Use constants instead of hardcoded values
COLOR_BACKGROUND_DARK       # Instead of RGBColor(17, 24, 39)
FONT_SIZE_KEYWORD           # Instead of Pt(72)
KEYWORD_Y_START             # Instead of 2.3
KEYWORD_THEME_PROBLEM       # Color array for keyword slides
```

**Full documentation:** See `design_tokens.py` for all available constants

---

## 🔧 Common Tasks

### Task 1: Add a New Slide
```python
# In generate_pptx.py, add to create_presentation():

def create_slide_N(prs):
    """Slide N: Your Title"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, N)  # N = slide number
    
    # Add your content here
    # Follow design tokens from README.md
    
    return prs

# Don't forget to call it:
create_slide_N(prs)
```

### Task 2: Update Slide Content
```python
# Option A: Edit in generate_pptx.py directly
# Option B: Edit slides_content.json and load in script

# Example JSON structure:
{
  "slide_2": {
    "title": "Organisations want AI",
    "subtitle": "but can't have it ¯\\_(ツ)_/¯",
    "problems": [...]
  }
}
```

### Task 3: Change Colors/Fonts/Layouts
```python
# 1. Open design_tokens.py
# 2. Modify the constant (e.g., COLOR_ACCENT_BLUE, FONT_SIZE_KEYWORD)
# 3. Save the file - changes apply automatically!
# 4. Test: python3 generate_pptx.py
# 5. Update CHANGELOG.md if it's a breaking change
```

---

## 🎨 Slide Types & Templates

### Type 1: Keyword Slide
**Used for:** Slides 1, 4, 6
**Example:** "THE AI PARADOX"
```python
# Uses: KEYWORD_* constants from design_tokens.py
# Three separate textboxes, vertically centered
# Colors: KEYWORD_THEME_PROBLEM, KEYWORD_THEME_SOLUTION, KEYWORD_THEME_TECH
```

### Type 2: Content Slide
**Used for:** Slides 2, 3, 7-16
**Example:** "Organisations want AI"
```python
# Uses: CONTENT_* and FONT_SIZE_CONTENT_* constants
# Fixed header at top with title and subtitle
# Content area below for flexible layouts
```

### Type 3: Blank with Master
**Used for:** Custom layouts
```python
# Only logo and slide number (from apply_master_elements)
# Completely custom content area
```

---

## 📐 Master Elements (apply_master_elements function)

**EVERY slide must call this function:**
```python
def apply_master_elements(slide, slide_num, total_slides=17):
    """
    Applies consistent master elements to a slide.
    Call this FIRST when creating any slide.

    Uses design_tokens.py for all values:
    - Background: COLOR_BACKGROUND_DARK
    - Logo: LOGO_* constants (position, size, font)
    - Slide number: SLIDE_NUMBER_* constants

    Args:
        slide: The slide object
        slide_num: Current slide number (1-17)
        total_slides: Total slides (default 17)
    """
    # Applies: background color, logo, slide number
    # All values from design_tokens.py
```

---

## 🚫 Common Mistakes to Avoid

### ❌ DON'T
- Hardcode colors/fonts/positions → Use design_tokens.py constants
- Modify values in generate_pptx.py → Change them in design_tokens.py
- Put "(v: xii)" in logo → Only "BRAIN BRIDGES"
- Use gradients in background → Only solid fills (currently)
- Single textbox for keywords → Separate box per word
- Edit the .pptx directly → Always regenerate from script

### ✅ DO
- Import and use constants from design_tokens.py
- Call apply_master_elements() on every slide
- Change design values in ONE place (design_tokens.py)
- Use separate textboxes for each keyword
- Update CHANGELOG.md for any changes
- Test generation after changes: `python3 generate_pptx.py`
- Commit with descriptive messages

---

## 🔄 Workflow for Changes

1. **Read context:**
   ```bash
   cat CLAUDE.md README.md
   git log --oneline -10
   ```

2. **Make changes:**
   - Edit `generate_pptx.py` or `slides_content.json`
   - Follow design system (README.md)
   - Keep consistency with existing slides

3. **Test:**
   ```bash
   python3 generate_pptx.py
   # Check output/Brain-Bridges.pptx
   ```

4. **Document:**
   - Update CHANGELOG.md
   - Add clear commit message

5. **Commit:**
   ```bash
   git add .
   git commit -m "type: description"
   git push
   ```

---

## 📝 Commit Message Convention

```
feat: Add slide 3 with stats carousel
fix: Correct keyword colors on slide 1
docs: Update README with new color tokens
style: Adjust spacing on slide 2
refactor: Extract slide creation to separate functions
chore: Update dependencies
```

---

## 🐛 Debugging Tips

### Issue: Colors/fonts look wrong
```python
# Check: Are you importing from design_tokens?
from design_tokens import *

# Correct: COLOR_ACCENT_BLUE
# Wrong: RGBColor(77, 171, 247) hardcoded
```

### Issue: Changes not appearing
```python
# 1. Check you're modifying design_tokens.py (not generate_pptx.py)
# 2. Save the file
# 3. Regenerate: python3 generate_pptx.py
# 4. Check output/Brain-Bridges_LATEST.pptx
```

### Issue: Import errors
```python
# Make sure design_tokens.py is in the same directory
# Check the import statement at top of generate_pptx.py:
from design_tokens import *
```

### Issue: Slide numbers wrong
```python
# Make sure you're calling:
apply_master_elements(slide, correct_slide_number, 17)
# Not:
apply_master_elements(slide, wrong_number)
```

---

## 🎯 Current Status

**Completed:**
- ✅ Slide 1: THE AI PARADOX (keyword slide)
- ✅ Slide 2: Organisations want AI (content slide)
- ✅ Design system documented
- ✅ Master elements function
- ✅ Git repository setup

**TODO:**
- ⏳ Slide 3-17: Need to be designed
- ⏳ Extract content to slides_content.json
- ⏳ Add configuration file for easy customization
- ⏳ Create helper functions for common patterns

---

## 🤝 Working with Human

**When user asks for changes:**
1. Confirm understanding
2. Show what will change
3. Make changes
4. Generate new file
5. Explain what was done
6. Provide git commands to commit

**When user wants to add content:**
1. Ask for content/layout preferences
2. Suggest which slide type to use
3. Create/modify script
4. Generate and show result
5. Iterate based on feedback

---

## 📚 Key Files Reference

### design_tokens.py ⭐
- **Single source of truth** for all design values
- Colors, fonts, positions, layouts, themes
- Change design values HERE ONLY
- Imported by generate_pptx.py

### generate_pptx.py
- Main generator script
- Contains all slide creation functions
- Imports design_tokens.py for all styling
- Imports from slides_content.json (future)

### README.md
- Human-readable documentation
- Design system reference (points to design_tokens.py)
- Setup and deployment instructions

### CLAUDE.md
- AI assistant instructions (this file)
- Workflow and best practices
- References design_tokens.py for design values

### slides_content.json (to be created)
- Stores slide content as data
- Easier to edit than Python code
- Loaded by generate_pptx.py

### CHANGELOG.md
- Version history
- Breaking changes
- Migration guides

---

## 📦 Legacy HTML Version (Reference Only)

> ⚠️ **DEPRECATED:** The `legacy/` folder contains the **abandoned HTML version** of this presentation.
> **DO NOT use or modify these files!** They exist only for reference.

### Why HTML was abandoned:
- Initial approach: Build presentation using HTML/CSS/JS
- Worked well initially: Design looked great, animations smooth
- Problem: Small changes became cumbersome (editing HTML, rebuilding, etc.)
- Solution: Back to PowerPoint via python-pptx for easier editing

### Legacy folder structure:
```bash
legacy/
├── dist/
│   ├── index.html          # Complete presentation (1242 lines)
│   ├── style.css           # All styles (76KB)
│   ├── script.js           # Navigation logic (27KB)
│   └── assets/             # Images, fonts, etc.
└── slides/
    ├── slide-01/           # Individual slide components
    │   ├── content.html    # Slide HTML
    │   └── styles.css      # Slide-specific styles
    └── ... (slide-02 to slide-17, all 17 slides)
```

### What you can extract from legacy/:
- ✅ **Content**: Text, titles, bullet points
- ✅ **Layout ideas**: How elements were positioned
- ✅ **Design intent**: Color choices, typography
- ✅ **Complete slide list**: All 17 slides are there

### How to use legacy files:
```bash
# View the complete HTML presentation
open legacy/dist/index.html

# Read individual slide content
cat legacy/slides/slide-01/content.html

# Extract content for recreation in PowerPoint
# Example: Copy text from HTML and paste into generate_pptx.py
```

### ⚠️ Important notes:
- **DO NOT** modify files in `legacy/`
- **DO NOT** try to sync HTML with PowerPoint
- **DO** use it as reference for content and design
- **DO** extract text/structure when building new slides
- The HTML version is frozen in time - it represents what was achieved before switching to PowerPoint

### For detailed history:
See README.md "Project History" section for full context.

---

## 🔗 External Resources

**python-pptx Documentation:**
- https://python-pptx.readthedocs.io/
- Presentation: https://python-pptx.readthedocs.io/en/latest/api/presentation.html
- Slides: https://python-pptx.readthedocs.io/en/latest/api/slides.html
- Shapes: https://python-pptx.readthedocs.io/en/latest/api/shapes.html
- Text: https://python-pptx.readthedocs.io/en/latest/api/text.html

**Color Conversion:**
```python
# Hex to RGB
hex_color = "#4dabf7"
r = int(hex_color[1:3], 16)  # 77
g = int(hex_color[3:5], 16)  # 171
b = int(hex_color[5:7], 16)  # 247
rgb_color = RGBColor(r, g, b)
```

---

## ⚡ Performance Tips

- Reuse slide layouts when possible
- Create helper functions for repeated patterns
- Use constants for all colors/sizes
- Profile with `time python3 generate_pptx.py`

---

**END OF CLAUDE.MD** • Keep this file updated! 🤖
