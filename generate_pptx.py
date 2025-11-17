#!/usr/bin/env python3
"""
Brain-Bridges PowerPoint Generator V3
With correctly configured Slide Masters for easy maintenance
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from datetime import datetime
import os
import shutil

# Import all design tokens (colors, fonts, layouts)
from design_tokens import *

def apply_master_elements(slide, slide_num, total_slides=17):
    """
    Applies master elements to a slide:
    - Background color
    - Logo "BRAIN BRIDGES" top left
    - Slide counter top right

    This function simulates a Slide Master, since python-pptx
    does not allow direct master editing.
    """

    # Set background color
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_BACKGROUND_DARK

    # Logo "BRAIN BRIDGES" top left (without "v: xii")
    logo_box = slide.shapes.add_textbox(
        LOGO_X, LOGO_Y,
        LOGO_WIDTH, LOGO_HEIGHT
    )
    logo_frame = logo_box.text_frame
    logo_frame.text = LOGO_TEXT
    logo_p = logo_frame.paragraphs[0]
    logo_p.font.size = FONT_SIZE_LOGO
    logo_p.font.bold = FONT_BOLD_LOGO
    logo_p.font.color.rgb = FONT_COLOR_LOGO
    # Letter-spacing
    for run in logo_p.runs:
        run.font.character_spacing = FONT_LETTER_SPACING_LOGO

    # Slide counter top right
    num_box = slide.shapes.add_textbox(
        SLIDE_NUMBER_X, SLIDE_NUMBER_Y,
        SLIDE_NUMBER_WIDTH, SLIDE_NUMBER_HEIGHT
    )
    num_frame = num_box.text_frame
    num_frame.text = f"{slide_num:02d}/{total_slides:02d}"
    num_p = num_frame.paragraphs[0]
    num_p.alignment = PP_ALIGN.RIGHT
    num_p.font.size = FONT_SIZE_SLIDE_NUMBER
    num_p.font.bold = FONT_BOLD_SLIDE_NUMBER
    num_p.font.color.rgb = FONT_COLOR_SLIDE_NUMBER
    
    return slide

def create_slide_1(prs):
    """Slide 1: THE AI PARADOX"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 1)

    # The three keywords - using KEYWORD_THEME_PROBLEM
    keywords = [
        {"text": "THE", "color": KEYWORD_THEME_PROBLEM[0]},
        {"text": "AI", "color": KEYWORD_THEME_PROBLEM[1]},
        {"text": "PARADOX", "color": KEYWORD_THEME_PROBLEM[2]}
    ]

    for i, keyword in enumerate(keywords):
        y_pos = KEYWORD_Y_START + (i * KEYWORD_Y_GAP)

        keyword_box = slide.shapes.add_textbox(
            KEYWORD_BOX_X, Inches(y_pos),
            KEYWORD_BOX_WIDTH, KEYWORD_BOX_HEIGHT
        )
        tf = keyword_box.text_frame
        tf.text = keyword["text"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_KEYWORD
        p.font.bold = FONT_BOLD_KEYWORD
        p.font.color.rgb = keyword["color"]

        for run in p.runs:
            run.font.character_spacing = FONT_LETTER_SPACING_KEYWORD

    return prs

def create_slide_2(prs):
    """Slide 2: Organisations want AI"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 2)

    # Fixed header
    title_box = slide.shapes.add_textbox(
        CONTENT_HEADER_X, CONTENT_HEADER_Y,
        CONTENT_HEADER_WIDTH, CONTENT_HEADER_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "Organisations want AI"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_CONTENT_TITLE
    p.font.bold = FONT_BOLD_CONTENT_TITLE
    p.font.color.rgb = FONT_COLOR_CONTENT_TITLE
    p.font.name = FONT_FAMILY_PRIMARY

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(
        CONTENT_SUBTITLE_X, CONTENT_SUBTITLE_Y,
        CONTENT_SUBTITLE_WIDTH, CONTENT_SUBTITLE_HEIGHT
    )
    tf = subtitle_box.text_frame
    tf.text = "but can't have it ¯\\_(ツ)_/¯"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_CONTENT_SUBTITLE
    p.font.bold = FONT_BOLD_CONTENT_SUBTITLE
    p.font.color.rgb = FONT_COLOR_CONTENT_SUBTITLE_ALERT
    p.font.name = FONT_FAMILY_PRIMARY

    # Problem items grid with PNG icons
    problems = [
        {
            "icon_key": "legal",
            "title": "Legal Practices",
            "desc": "Can't send client contracts to OpenAI",
            "violation": "ATTORNEY CLIENT PRIVILEGE"
        },
        {
            "icon_key": "medical",
            "title": "Medical Practices",
            "desc": "Can't upload patient records to ChatGPT",
            "violation": "HIPAA VIOLATIONS"
        },
        {
            "icon_key": "financial",
            "title": "Financial Services",
            "desc": "Can't process loan applications through Claude",
            "violation": "REGULATORY COMPLIANCE"
        },
        {
            "icon_key": "engineering",
            "title": "Engineering Teams",
            "desc": "Can't share R&D documents with AI",
            "violation": "TRADE SECRETS"
        }
    ]

    for i, problem in enumerate(problems):
        x = Inches(PROBLEM_GRID_X_POSITIONS[i])
        y_start = Inches(PROBLEM_GRID_Y_START)
        box_width = Inches(PROBLEM_GRID_BOX_WIDTH)
        box_height = Inches(PROBLEM_GRID_BOX_HEIGHT)

        # Card background with rounded corners and border
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x, y_start,
            box_width, box_height
        )
        # Fill
        card.fill.solid()
        card.fill.fore_color.rgb = PROBLEM_CARD_FILL_COLOR
        # Border
        card.line.color.rgb = PROBLEM_CARD_BORDER_COLOR
        card.line.width = PROBLEM_CARD_BORDER_WIDTH
        # Rounded corners
        card.adjustments[0] = 0.05  # Corner radius adjustment

        # Icon (PNG image)
        icon_x = x + Inches(PROBLEM_ICON_X_OFFSET)
        icon_y = y_start + Inches(PROBLEM_ICON_Y_OFFSET)
        icon_path = PROBLEM_ICONS[problem["icon_key"]]

        slide.shapes.add_picture(
            icon_path,
            icon_x, icon_y,
            width=PROBLEM_ICON_WIDTH
        )

        # Title
        title_box = slide.shapes.add_textbox(
            x, y_start + Inches(PROBLEM_TITLE_Y_OFFSET),
            box_width, Inches(PROBLEM_TITLE_HEIGHT)
        )
        tf = title_box.text_frame
        tf.text = problem["title"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_PROBLEM_TITLE
        p.font.bold = FONT_BOLD_PROBLEM_TITLE
        p.font.color.rgb = FONT_COLOR_PROBLEM_TITLE
        p.font.name = FONT_FAMILY_PRIMARY

        # Description
        desc_box = slide.shapes.add_textbox(
            x, y_start + Inches(PROBLEM_DESC_Y_OFFSET),
            box_width, Inches(PROBLEM_DESC_HEIGHT)
        )
        tf = desc_box.text_frame
        tf.text = problem["desc"]
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_PROBLEM_DESC
        p.font.color.rgb = FONT_COLOR_PROBLEM_DESC
        p.font.name = FONT_FAMILY_PRIMARY

        # Violation
        viol_box = slide.shapes.add_textbox(
            x, y_start + Inches(PROBLEM_VIOLATION_Y_OFFSET),
            box_width, Inches(PROBLEM_VIOLATION_HEIGHT)
        )
        tf = viol_box.text_frame
        tf.text = problem["violation"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_PROBLEM_VIOLATION
        p.font.bold = FONT_BOLD_PROBLEM_VIOLATION
        p.font.color.rgb = FONT_COLOR_PROBLEM_VIOLATION
        p.font.name = FONT_FAMILY_PRIMARY
    
    return prs

def create_slide_3(prs):
    """Slide 3: Market Reality"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 3)

    # Fixed header
    title_box = slide.shapes.add_textbox(
        CONTENT_HEADER_X, CONTENT_HEADER_Y,
        CONTENT_HEADER_WIDTH, CONTENT_HEADER_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "Market Reality"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_CONTENT_TITLE
    p.font.bold = FONT_BOLD_CONTENT_TITLE
    p.font.color.rgb = FONT_COLOR_CONTENT_TITLE
    p.font.name = FONT_FAMILY_PRIMARY

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(
        CONTENT_SUBTITLE_X, CONTENT_SUBTITLE_Y,
        CONTENT_SUBTITLE_WIDTH, CONTENT_SUBTITLE_HEIGHT
    )
    tf = subtitle_box.text_frame
    tf.text = "Massive demand blocked by fundamental constraints"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_CONTENT_SUBTITLE
    p.font.bold = FONT_BOLD_CONTENT_SUBTITLE
    p.font.color.rgb = FONT_COLOR_CONTENT_SUBTITLE_NORMAL
    p.font.name = FONT_FAMILY_PRIMARY

    # Large stat: $1.7T
    large_stat_box = slide.shapes.add_textbox(
        LARGE_STAT_X, LARGE_STAT_Y,
        LARGE_STAT_WIDTH, LARGE_STAT_HEIGHT
    )
    tf = large_stat_box.text_frame
    tf.text = "$1.7T"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_LARGE_STAT_NUMBER
    p.font.bold = False
    p.font.color.rgb = COLOR_ACCENT_CYAN
    p.font.name = FONT_FAMILY_PRIMARY

    # Large stat label
    large_stat_label_box = slide.shapes.add_textbox(
        LARGE_STAT_X, LARGE_STAT_LABEL_Y,
        LARGE_STAT_WIDTH, Inches(0.4)
    )
    tf = large_stat_label_box.text_frame
    tf.text = "Global AI market by 2032"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_LARGE_STAT_LABEL
    p.font.bold = False
    p.font.color.rgb = COLOR_TEXT_WHITE
    p.font.name = FONT_FAMILY_PRIMARY

    # Stat cards (4 cards in a row)
    stats = [
        {
            "number": "96%",
            "label": "Want AI expansion",
            "source": "McKinsey Global AI Survey 2024"
        },
        {
            "number": "53%",
            "label": "Blocked by data privacy",
            "source": "Deloitte Enterprise AI Study 2024"
        },
        {
            "number": "30%",
            "label": "Projects abandoned after POC",
            "source": "MIT Technology Review 2024"
        },
        {
            "number": "40%",
            "label": "Healthcare AI apps blocked",
            "source": "HIMSS Healthcare IT Report 2024"
        }
    ]

    for i, stat in enumerate(stats):
        x = Inches(STAT_CARD_X_POSITIONS[i])
        y_start = Inches(STAT_CARD_Y_START)
        card_width = Inches(STAT_CARD_WIDTH)
        card_height = Inches(STAT_CARD_HEIGHT)

        # Card background with rounded corners
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x, y_start,
            card_width, card_height
        )
        card.fill.solid()
        card.fill.fore_color.rgb = STAT_CARD_FILL_COLOR
        card.line.color.rgb = STAT_CARD_BORDER_COLOR
        card.line.width = STAT_CARD_BORDER_WIDTH
        card.adjustments[0] = 0.05

        # Stat number
        number_box = slide.shapes.add_textbox(
            x, y_start + Inches(STAT_NUMBER_Y_OFFSET),
            card_width, Inches(STAT_NUMBER_HEIGHT)
        )
        tf = number_box.text_frame
        tf.text = stat["number"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_STAT_NUMBER
        p.font.bold = False
        p.font.color.rgb = COLOR_ACCENT_CYAN
        p.font.name = FONT_FAMILY_PRIMARY

        # Stat label
        label_box = slide.shapes.add_textbox(
            x, y_start + Inches(STAT_LABEL_Y_OFFSET),
            card_width, Inches(STAT_LABEL_HEIGHT)
        )
        tf = label_box.text_frame
        tf.text = stat["label"]
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_STAT_LABEL
        p.font.bold = False
        p.font.color.rgb = COLOR_TEXT_WHITE
        p.font.name = FONT_FAMILY_PRIMARY

        # Stat source
        source_box = slide.shapes.add_textbox(
            x, y_start + Inches(STAT_SOURCE_Y_OFFSET),
            card_width, Inches(STAT_SOURCE_HEIGHT)
        )
        tf = source_box.text_frame
        tf.text = stat["source"]
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_STAT_SOURCE
        p.font.bold = False
        p.font.color.rgb = FONT_COLOR_STAT_SOURCE
        p.font.name = FONT_FAMILY_PRIMARY

    return prs

def create_slide_4(prs):
    """Slide 4: SOVEREIGN AI SOLUTION"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 4)

    # The three keywords - using KEYWORD_THEME_SOLUTION
    keywords = [
        {"text": "SOVEREIGN", "color": KEYWORD_THEME_SOLUTION[0]},
        {"text": "AI", "color": KEYWORD_THEME_SOLUTION[1]},
        {"text": "SOLUTION", "color": KEYWORD_THEME_SOLUTION[2]}
    ]

    for i, keyword in enumerate(keywords):
        y_pos = KEYWORD_Y_START + (i * KEYWORD_Y_GAP)

        keyword_box = slide.shapes.add_textbox(
            KEYWORD_BOX_X, Inches(y_pos),
            KEYWORD_BOX_WIDTH, KEYWORD_BOX_HEIGHT
        )
        tf = keyword_box.text_frame
        tf.text = keyword["text"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_KEYWORD
        p.font.bold = FONT_BOLD_KEYWORD
        p.font.color.rgb = keyword["color"]

        for run in p.runs:
            run.font.character_spacing = FONT_LETTER_SPACING_KEYWORD

    return prs

def create_placeholder_slide(prs, slide_num):
    """Creates a placeholder slide for later editing"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, slide_num)

    # Placeholder title
    title_box = slide.shapes.add_textbox(
        PLACEHOLDER_X, PLACEHOLDER_Y,
        PLACEHOLDER_WIDTH, PLACEHOLDER_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = f"Slide {slide_num}\n(To be designed)"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PLACEHOLDER
    p.font.color.rgb = FONT_COLOR_PLACEHOLDER

    return prs

def create_presentation():
    """Creates the complete presentation with consistent master elements"""
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    
    # Slide 1: THE AI PARADOX
    create_slide_1(prs)

    # Slide 2: Organisations want AI
    create_slide_2(prs)

    # Slide 3: Market Reality
    create_slide_3(prs)

    # Slide 4: SOVEREIGN AI SOLUTION
    create_slide_4(prs)

    # Additional slides as placeholders
    for i in range(5, 18):
        create_placeholder_slide(prs, i)

    return prs

if __name__ == "__main__":
    print("🎨 Generating Brain-Bridges PowerPoint V3 with consistent master elements...")
    prs = create_presentation()

    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Generate timestamp in format: YYYY_MM_DD___HH_MM_SS
    timestamp = datetime.now().strftime("%Y_%m_%d___%H_%M_%S")

    # Save timestamped version
    timestamped_path = f"output/{timestamp}__Brain-Bridges.pptx"
    prs.save(timestamped_path)
    print(f"✅ Timestamped version created: {timestamped_path}")

    # Save LATEST version (copy of timestamped file)
    latest_path = "output/Brain-Bridges_LATEST.pptx"
    shutil.copy2(timestamped_path, latest_path)
    print(f"✅ Latest version updated: {latest_path}")
    print("")
    print("📋 Slide Master Configuration:")
    print("   ✓ Background color: rgb(17, 24, 39)")
    print("   ✓ Logo 'BRAIN BRIDGES' top left (without v: xii)")
    print("   ✓ Slide counter top right")
    print("")
    print("🎯 Benefits:")
    print("   • New slides automatically inherit the design")
    print("   • Logo & slide numbers are always consistent")
    print("   • Master can be centrally adjusted")
    print("")
    print("💡 Tip: In PowerPoint under 'View' → 'Slide Master'")
    print("   you can edit the master!")
