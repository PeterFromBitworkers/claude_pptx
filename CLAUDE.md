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
├── CHANGELOG.md                 # Version history
├── generate_pptx.py            # Main generator script
├── slides_content.json         # Slide content data
├── requirements.txt            # Python dependencies
└── output/
    └── Brain-Bridges.pptx      # Generated file (gitignored)
```

---

## 🚀 Quick Start for AI Assistants

### 1. Understand the Project
```bash
# Read these files in this order:
cat CLAUDE.md          # This file
cat README.md          # Design system & colors
cat slides_content.json # Current slide content
cat generate_pptx.py   # Generator code
```

### 2. Make Changes
```python
# Edit generate_pptx.py or slides_content.json
# Follow the design tokens in README.md
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

## 📋 Design Constraints (CRITICAL)

### Colors (ALWAYS use these exact RGB values)
```python
BACKGROUND_DARK = RGBColor(17, 24, 39)     # Main background
BACKGROUND_LIGHT = RGBColor(31, 41, 55)    # Cards/boxes
TEXT_WHITE = RGBColor(255, 255, 255)       # Primary text
TEXT_GRAY = RGBColor(209, 213, 219)        # Secondary text
TEXT_GRAY_DARK = RGBColor(167, 171, 175)   # Slide numbers

# Accent colors
ACCENT_BLUE = RGBColor(77, 171, 247)       # #4dabf7
ACCENT_CYAN = RGBColor(6, 182, 212)        # #06b6d4
ACCENT_GREEN = RGBColor(16, 185, 129)      # #10b981
ACCENT_RED = RGBColor(239, 68, 68)         # #ef4444
ACCENT_PURPLE = RGBColor(139, 92, 246)     # #8b5cf6
```

### Typography
```python
# Logo "BRAIN BRIDGES" (top-left, every slide)
logo_font_size = Pt(21)
logo_font_weight = "Bold"
logo_color = RGBColor(255, 255, 255)
logo_position = (Inches(0.28), Inches(0.28))

# Slide number "##/17" (top-right, every slide)
slidenum_font_size = Pt(21)
slidenum_font_weight = "Normal"
slidenum_color = RGBColor(167, 171, 175)
slidenum_position = (Inches(15.1), Inches(0.28))

# Keywords (THE, AI, PARADOX style slides)
keyword_font_size = Pt(72)
keyword_font_weight = "Light" or "Thin"  # As thin as possible!
keyword_letter_spacing = Pt(2)
keyword_uppercase = True
keyword_vertical_gap = Inches(1.4)
```

### Layout Rules
```python
# Slide dimensions
slide_width = Inches(16)
slide_height = Inches(9)

# Safe zones
margin_top = Inches(1)      # Below logo/slidenum
margin_sides = Inches(1)    # Left/right margins
content_max_width = Inches(14)
```

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

### Task 3: Change Colors/Fonts
```python
# 1. Check if change is allowed per design system (README.md)
# 2. Update the color constant at top of generate_pptx.py
# 3. Apply throughout
# 4. Update CHANGELOG.md with breaking change note
```

---

## 🎨 Slide Types & Templates

### Type 1: Keyword Slide
**Used for:** Slides 1, 4, 6  
**Example:** "THE AI PARADOX"
```python
# Three separate textboxes, vertically centered
# Each keyword: 72pt, light weight, letter-spacing 2pt
# Colors rotate per theme (see README.md)
```

### Type 2: Content Slide
**Used for:** Slides 2, 3, 7-16  
**Example:** "Organisations want AI"
```python
# Fixed header at top: 1" from top, centered
# Title: 48pt, Light, Blue
# Subtitle: 20pt, Bold, Red or Gray
# Content area: starts at 3" from top
```

### Type 3: Blank with Master
**Used for:** Custom layouts
```python
# Only logo and slide number
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
    
    Args:
        slide: The slide object
        slide_num: Current slide number (1-17)
        total_slides: Total slides (default 17)
    """
    # 1. Background
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(17, 24, 39)
    
    # 2. Logo "BRAIN BRIDGES" (top-left)
    # Position: 0.28" from top, 0.28" from left
    # Font: 21pt, Bold, White
    
    # 3. Slide number "##/17" (top-right)
    # Position: 15.1" from left, 0.28" from top
    # Font: 21pt, Normal, Gray
    # Format: "{slide_num:02d}/{total_slides:02d}"
```

---

## 🚫 Common Mistakes to Avoid

### ❌ DON'T
- Use Hex colors (#4dabf7) → Use RGBColor(77, 171, 247)
- Put "(v: xii)" in logo → Only "BRAIN BRIDGES"
- Use gradients in background → Only solid fills
- Make font weights too heavy → Use lightest available
- Forget letter-spacing on keywords → Always 2pt
- Single textbox for keywords → Separate box per word
- Edit the .pptx directly → Always regenerate from script

### ✅ DO
- Use exact RGB values from constants
- Call apply_master_elements() on every slide
- Keep fonts as light/thin as possible
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

### Issue: Colors look wrong
```python
# Check: Are you using RGBColor() not hex?
# Correct: RGBColor(77, 171, 247)
# Wrong: "#4dabf7"
```

### Issue: Fonts too heavy
```python
# python-pptx doesn't support font-weight numbers directly
# Use: paragraph.font.bold = False
# And: Use font names like "Segoe UI Light" if available
```

### Issue: Letter-spacing not working
```python
# Use character_spacing on runs, not paragraphs:
for run in paragraph.runs:
    run.font.character_spacing = Pt(2)
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

### generate_pptx.py
- Main generator script
- Contains all slide creation functions
- Imports from slides_content.json (future)

### slides_content.json (to be created)
- Stores slide content as data
- Easier to edit than Python code
- Loaded by generate_pptx.py

### README.md
- Human-readable documentation
- Design system and color reference
- Setup instructions

### CHANGELOG.md
- Version history
- Breaking changes
- Migration guides

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
