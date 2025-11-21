#!/usr/bin/env python3
"""
Brain-Bridges PowerPoint Generator V3
With correctly configured Slide Masters for easy maintenance
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from datetime import datetime
import os
import shutil
from PIL import Image, ImageDraw

# Import all design tokens (colors, fonts, layouts)
from design_tokens import *

def add_rounded_corners_to_image(image_path, corner_radius, border_color, border_width, output_path):
    """
    Add rounded corners and border to an image using PIL.

    Args:
        image_path: Path to input image
        corner_radius: Radius of corners in pixels
        border_color: RGB tuple for border (e.g., (77, 171, 247))
        border_width: Border width in pixels
        output_path: Path to save modified image
    """
    # Open image
    img = Image.open(image_path).convert("RGBA")

    # Create new image with space for border
    new_width = img.size[0] + 2 * border_width
    new_height = img.size[1] + 2 * border_width
    new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))

    # Paste original image in center
    new_img.paste(img, (border_width, border_width))

    # Create a mask with rounded corners for the entire new image
    mask = Image.new('L', (new_width, new_height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        [(0, 0), (new_width, new_height)],
        radius=corner_radius,
        fill=255
    )

    # Apply mask
    new_img.putalpha(mask)

    # Draw border
    draw = ImageDraw.Draw(new_img)
    draw.rounded_rectangle(
        [(0, 0), (new_width - 1, new_height - 1)],
        radius=corner_radius,
        outline=border_color,
        width=border_width
    )

    # Save with transparency
    new_img.save(output_path, "PNG")
    return output_path

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_KEYWORD  # Inter ExtraLight (font-weight: 200)
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

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_TITLE  # Inter ExtraLight (font-weight: 200)

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

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_SUBTITLE  # Menlo (monospace)

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
        # 2x2 Grid Layout: Calculate row and column
        row = i // 2  # 0 or 1 (top row or bottom row)
        col = i % 2   # 0 or 1 (left column or right column)

        x = Inches(PROBLEM_GRID_X_POSITIONS[col])
        y_start = Inches(PROBLEM_GRID_Y_POSITIONS[row])
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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_TITLE  # Inter ExtraLight (font-weight: 200)

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
        p.font.bold = FONT_BOLD_PROBLEM_DESC
        p.font.color.rgb = FONT_COLOR_PROBLEM_DESC

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_TITLE  # Same as title (Inter ExtraLight)

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_VIOLATION  # Menlo (monospace)

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

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_TITLE  # Inter ExtraLight (font-weight: 200)

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
    p.font.color.rgb = FONT_COLOR_CONTENT_SUBTITLE_ALERT  # Red like Slide 2

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_SUBTITLE  # Menlo monospace like Slide 2

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

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_STAT_NUMBER  # Inter ExtraLight (font-weight: 200)

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

    # CRITICAL: Font name must be set at RUN level!
    for run in p.runs:
        run.font.name = FONT_FAMILY_STAT_LABEL  # Inter Light (font-weight: 300)

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_STAT_NUMBER  # Inter ExtraLight (font-weight: 200)

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_STAT_LABEL  # Inter Light (font-weight: 300)

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_PRIMARY  # Inter Regular (small body text)

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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_KEYWORD  # Inter ExtraLight (font-weight: 200)
            run.font.character_spacing = FONT_LETTER_SPACING_KEYWORD

    return prs

def create_slide_5(prs):
    """Slide 5: BRAIN-BRIDGES Introduction (like Slide 6 but with text instead of features)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 5)

    # =========================================================================
    # LEFT SIDE: Title, Subtitle, Description Text
    # =========================================================================

    # Hero Title: "BRAIN-BRIDGES"
    title_box = slide.shapes.add_textbox(
        HERO_TITLE_X, HERO_TITLE_Y,
        HERO_TITLE_WIDTH, HERO_TITLE_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "BRAIN-BRIDGES"
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.font.name = FONT_FAMILY_HERO_TITLE
    p.font.size = FONT_SIZE_HERO_TITLE
    p.font.bold = FONT_BOLD_HERO_TITLE
    p.font.color.rgb = COLOR_ACCENT_BLUE

    for run in p.runs:
        run.font.character_spacing = FONT_LETTER_SPACING_HERO_TITLE

    # Hero Subtitle: "SOVEREIGN AI FOR ORGANISATIONS"
    subtitle_box = slide.shapes.add_textbox(
        HERO_SUBTITLE_X, HERO_SUBTITLE_Y,
        HERO_SUBTITLE_WIDTH, HERO_SUBTITLE_HEIGHT
    )
    tf = subtitle_box.text_frame
    tf.text = "SOVEREIGN AI FOR ORGANISATIONS"
    p = tf.paragraphs[0]
    p.font.name = FONT_FAMILY_HERO_SUBTITLE
    p.font.size = FONT_SIZE_HERO_SUBTITLE
    p.font.bold = FONT_BOLD_HERO_SUBTITLE
    p.font.color.rgb = FONT_COLOR_HERO_SUBTITLE

    # Description text (3 paragraphs) - positioned below subtitle
    text_box = slide.shapes.add_textbox(
        HERO_FEATURES_X, Inches(3.5),
        HERO_FEATURES_WIDTH, Inches(4.0)
    )
    tf = text_box.text_frame
    tf.word_wrap = True

    # Paragraph 1
    p1 = tf.paragraphs[0]
    p1.text = "We offer an AI Bot that enables users to have chat-like conversations about their organization. The bot has access to the organization's documents repository."
    p1.font.size = Pt(14)
    p1.font.color.rgb = COLOR_TEXT_WHITE
    p1.space_after = Pt(16)
    for run in p1.runs:
        run.font.name = FONT_FAMILY_PRIMARY

    # Paragraph 2 (with bold words)
    p2 = tf.add_paragraph()
    p2.text = "To guarantee absolute data sovereignty, privacy, and security, we design the entire system – including AI model, database and documents – for full on-premises deployment."
    p2.font.size = Pt(14)
    p2.font.color.rgb = COLOR_TEXT_WHITE
    p2.space_after = Pt(16)

    # Make specific words bold
    text2 = p2.text
    p2.clear()

    parts = [
        ("To guarantee absolute ", False),
        ("data sovereignty", True),
        (", ", False),
        ("privacy", True),
        (", and ", False),
        ("security", True),
        (", we design the entire system – including AI model, database and documents – for full on-premises deployment.", False)
    ]

    for text, is_bold in parts:
        run = p2.add_run()
        run.text = text
        run.font.name = FONT_FAMILY_PRIMARY
        run.font.size = Pt(14)
        run.font.bold = is_bold
        run.font.color.rgb = COLOR_TEXT_WHITE

    # Paragraph 3
    p3 = tf.add_paragraph()
    p3.text = "Everything is delivered as a compact, ready-to-use system – just plug in and start."
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_TEXT_WHITE
    for run in p3.runs:
        run.font.name = FONT_FAMILY_PRIMARY

    # =========================================================================
    # RIGHT SIDE: Product Image with Status Badge (NO TECH SPECS)
    # =========================================================================

    # Get actual image dimensions for aspect ratio
    img_actual_height = HERO_IMAGE_HEIGHT

    try:
        pil_img = Image.open(HERO_IMAGE_PATH)
        img_width_px, img_height_px = pil_img.size
        aspect_ratio = img_height_px / img_width_px
        img_actual_height = HERO_IMAGE_WIDTH * aspect_ratio
    except Exception as e:
        print(f"⚠️  Warning: Could not get image dimensions: {e}")

    # Process image: add rounded corners and border
    try:
        os.makedirs("temp", exist_ok=True)
        border_width_px = int(HERO_IMAGE_BORDER_WIDTH.pt * 1.33)
        rounded_image_path = "temp/hero_image_rounded.png"
        add_rounded_corners_to_image(
            HERO_IMAGE_PATH,
            HERO_IMAGE_CORNER_RADIUS_PX,
            HERO_IMAGE_BORDER_COLOR_RGB,
            border_width_px,
            rounded_image_path
        )

        product_img = slide.shapes.add_picture(
            rounded_image_path,
            HERO_IMAGE_X, HERO_IMAGE_Y,
            width=HERO_IMAGE_WIDTH
        )
        img_actual_height = product_img.height
    except Exception as e:
        print(f"⚠️  Warning: Could not load/process hero image: {e}")
        try:
            product_img = slide.shapes.add_picture(
                HERO_IMAGE_PATH,
                HERO_IMAGE_X, HERO_IMAGE_Y,
                width=HERO_IMAGE_WIDTH
            )
            img_actual_height = product_img.height
        except:
            pass

    # NO Status Badge on Slide 5 (only image)

    return prs

def create_slide_6(prs):
    """Slide 6: BRAIN-BRIDGES Hero Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 6)

    # =========================================================================
    # LEFT SIDE: Title, Subtitle, Features
    # =========================================================================

    # Hero Title: "BRAIN-BRIDGES"
    # Note: PowerPoint gradient text is complex, using solid blue color
    title_box = slide.shapes.add_textbox(
        HERO_TITLE_X, HERO_TITLE_Y,
        HERO_TITLE_WIDTH, HERO_TITLE_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "BRAIN-BRIDGES"
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.font.name = FONT_FAMILY_HERO_TITLE  # Inter-ExtraBold (font-weight: 800)
    p.font.size = FONT_SIZE_HERO_TITLE
    p.font.bold = FONT_BOLD_HERO_TITLE
    p.font.color.rgb = COLOR_ACCENT_BLUE  # Solid blue (gradient not reliable in pptx)

    # Apply negative letter-spacing (like HTML version)
    for run in p.runs:
        run.font.character_spacing = FONT_LETTER_SPACING_HERO_TITLE

    # Hero Subtitle: "SOVEREIGN AI FOR ORGANISATIONS"
    subtitle_box = slide.shapes.add_textbox(
        HERO_SUBTITLE_X, HERO_SUBTITLE_Y,
        HERO_SUBTITLE_WIDTH, HERO_SUBTITLE_HEIGHT
    )
    tf = subtitle_box.text_frame
    tf.text = "SOVEREIGN AI FOR ORGANISATIONS"
    p = tf.paragraphs[0]
    p.font.name = FONT_FAMILY_HERO_SUBTITLE  # Menlo (monospace font)
    p.font.size = FONT_SIZE_HERO_SUBTITLE
    p.font.bold = FONT_BOLD_HERO_SUBTITLE
    p.font.color.rgb = FONT_COLOR_HERO_SUBTITLE

    # Hero Features List (6 items - 5 with checkmarks, last with plug icon)
    features = [
        ("Multi-Model Support (Mistral, Llama, Gemma, others)", "check"),
        ("PostgreSQL with pgvector (Enterprise-Ready)", "check"),
        ("Production Ready Webinterface", "check"),
        ("Nomic Embeddings (Multi-Language)", "check"),
        ("MCP-Compatible Agent Framework", "check"),
        ("Zero-Config Deployment", "plug")  # Plug icon for last item
    ]

    for i, (feature_text, icon_type) in enumerate(features):
        y_pos = Inches(HERO_FEATURES_Y_START + i * HERO_FEATURE_GAP)

        # Add underline extending to image (drawn FIRST, behind text)
        # Made thinner and more subtle
        line_y = y_pos + Inches(HERO_FEATURE_HEIGHT) - Inches(0.02)
        line_start_x = HERO_FEATURES_X
        line_end_x = HERO_IMAGE_X + Inches(0.2)  # Extend a bit into image area

        underline = slide.shapes.add_connector(
            1,  # MSO_CONNECTOR_TYPE.STRAIGHT
            line_start_x, line_y,
            line_end_x, line_y
        )
        # Thinner and more washed out
        underline.line.color.rgb = RGBColor(77, 171, 247)  # Blue
        underline.line.width = Pt(0.75)  # Reduced from 1.5
        underline.line.fill.solid()
        underline.line.fill.fore_color.rgb = RGBColor(77, 171, 247)
        underline.line.fill.transparency = 0.85  # More transparent (85% vs 80%)

        # Icon (checkmark or plug)
        try:
            icon_x = HERO_FEATURES_X
            icon_y_center = y_pos + Inches(HERO_FEATURE_HEIGHT / 2)
            icon_y = icon_y_center - (HERO_FEATURE_ICON_SIZE / 2)

            # Use plug icon for last item, checkmark for others
            icon_path = HERO_STATUS_ICON if icon_type == "plug" else HERO_FEATURE_CHECKMARK_ICON

            icon = slide.shapes.add_picture(
                icon_path,
                icon_x, icon_y,
                width=HERO_FEATURE_ICON_SIZE
            )
        except Exception as e:
            print(f"⚠️  Warning: Could not load icon: {e}")

        # Feature text box (next to icon)
        text_x = HERO_FEATURES_X + HERO_FEATURE_ICON_SIZE + Inches(0.15)  # Gap after icon
        text_width = HERO_FEATURES_WIDTH - HERO_FEATURE_ICON_SIZE - Inches(0.15)

        feature_box = slide.shapes.add_textbox(
            text_x, y_pos,
            text_width, Inches(HERO_FEATURE_HEIGHT)
        )
        tf = feature_box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE  # Vertically center text to align with icon

        # Feature text (white)
        p = tf.paragraphs[0]
        p.font.name = FONT_FAMILY_HERO_FEATURE  # Inter-Light (font-weight: 300)
        p.font.size = FONT_SIZE_HERO_FEATURE
        p.font.color.rgb = FONT_COLOR_HERO_FEATURE
        p.text = feature_text

    # =========================================================================
    # RIGHT SIDE: Product Image with border, Status Badge, Tech Specs
    # =========================================================================

    # Get actual image dimensions for aspect ratio
    img_actual_height = HERO_IMAGE_HEIGHT

    try:
        pil_img = Image.open(HERO_IMAGE_PATH)
        img_width_px, img_height_px = pil_img.size
        aspect_ratio = img_height_px / img_width_px
        img_actual_height = HERO_IMAGE_WIDTH * aspect_ratio
    except Exception as e:
        print(f"⚠️  Warning: Could not get image dimensions: {e}")

    # Process image: add rounded corners and border
    try:
        # Create temp directory if it doesn't exist
        os.makedirs("temp", exist_ok=True)

        # Convert border width from Pt to pixels (approximate: 1pt ≈ 1.33px)
        border_width_px = int(HERO_IMAGE_BORDER_WIDTH.pt * 1.33)

        # Create rounded corner version of image with border
        rounded_image_path = "temp/hero_image_rounded.png"
        add_rounded_corners_to_image(
            HERO_IMAGE_PATH,
            HERO_IMAGE_CORNER_RADIUS_PX,
            HERO_IMAGE_BORDER_COLOR_RGB,
            border_width_px,
            rounded_image_path
        )

        # Add image with rounded corners and border
        product_img = slide.shapes.add_picture(
            rounded_image_path,
            HERO_IMAGE_X, HERO_IMAGE_Y,
            width=HERO_IMAGE_WIDTH
        )

        # Get actual image dimensions after adding
        img_actual_height = product_img.height
    except Exception as e:
        print(f"⚠️  Warning: Could not load/process hero image: {e}")
        # Fallback: use original image without rounded corners
        try:
            product_img = slide.shapes.add_picture(
                HERO_IMAGE_PATH,
                HERO_IMAGE_X, HERO_IMAGE_Y,
                width=HERO_IMAGE_WIDTH
            )
            img_actual_height = product_img.height
        except:
            pass

    # Calculate positions for cards INSIDE the image
    img_bottom = HERO_IMAGE_Y + img_actual_height
    img_right = HERO_IMAGE_X + HERO_IMAGE_WIDTH

    # Status Badge: INSIDE image at top right with margin
    status_x = img_right - HERO_STATUS_WIDTH - HERO_STATUS_MARGIN
    status_y = HERO_IMAGE_Y + HERO_STATUS_MARGIN

    status_shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        status_x, status_y,
        HERO_STATUS_WIDTH, HERO_STATUS_HEIGHT
    )
    # Semi-transparent effect using slightly lighter color
    fill = status_shape.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(25, 32, 45)  # Lighter dark background for semi-transparent effect
    status_shape.line.color.rgb = COLOR_ACCENT_CYAN
    status_shape.line.width = Pt(1)

    # Plug icon and text - CENTERED in badge
    # Icon left side, text right side, both vertically centered
    badge_center_y = status_y + (HERO_STATUS_HEIGHT / 2)

    try:
        # Icon (left-center of badge)
        icon_x = status_x + Inches(0.15)
        icon_y = badge_center_y - (HERO_STATUS_ICON_SIZE / 2)

        plug_icon = slide.shapes.add_picture(
            HERO_STATUS_ICON,
            icon_x, icon_y,
            width=HERO_STATUS_ICON_SIZE
        )
    except Exception as e:
        print(f"⚠️  Warning: Could not load plug icon: {e}")

    # Text (right of icon, centered)
    text_x = status_x + Inches(0.33)
    text_box = slide.shapes.add_textbox(
        text_x, status_y,
        HERO_STATUS_WIDTH - Inches(0.33), HERO_STATUS_HEIGHT
    )
    tf = text_box.text_frame
    tf.text = HERO_STATUS_TEXT
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE  # Vertically center text to align with icon
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_FAMILY_HERO_STATUS  # Inter-Medium (font-weight: 500)
    p.font.size = FONT_SIZE_HERO_STATUS
    p.font.bold = True
    p.font.color.rgb = FONT_COLOR_HERO_STATUS

    # Tech Specs (3 columns: Processor, Memory, Users) INSIDE image at bottom
    spec_labels = ["PROCESSOR", "MEMORY", "USERS"]
    spec_values = [
        HERO_SPECS_CONFIG["processor"],
        HERO_SPECS_CONFIG["memory"],
        HERO_SPECS_CONFIG["users"]
    ]

    # Calculate card width: (image_width - 2*margin - 2*gap) / 3
    total_card_width = HERO_IMAGE_WIDTH - (2 * HERO_SPECS_MARGIN)
    single_card_width = (total_card_width - (2 * HERO_SPECS_GAP)) / 3

    # Cards at bottom of image with margin
    specs_y = img_bottom - HERO_SPECS_HEIGHT - HERO_SPECS_MARGIN

    for i, (label, value) in enumerate(zip(spec_labels, spec_values)):
        x_pos = HERO_IMAGE_X + HERO_SPECS_MARGIN + i * (single_card_width + HERO_SPECS_GAP)

        # Spec card background with rounded corners - SEMI-TRANSPARENT effect
        spec_card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x_pos, specs_y,
            single_card_width, HERO_SPECS_HEIGHT
        )
        # Semi-transparent effect using slightly lighter color (transparency doesn't work reliably)
        fill = spec_card.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(25, 32, 45)  # Lighter dark background for semi-transparent effect

        # Blue border
        spec_card.line.color.rgb = COLOR_ACCENT_BLUE
        spec_card.line.width = Pt(0.75)

        # Rounded corners
        spec_card.adjustments[0] = 0.05

        # Label (top)
        label_box = slide.shapes.add_textbox(
            x_pos, specs_y + Inches(0.18),
            single_card_width, Inches(0.25)
        )
        tf = label_box.text_frame
        tf.text = label
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_HERO_SPEC_LABEL
        p.font.color.rgb = FONT_COLOR_HERO_SPEC_LABEL
        p.font.bold = True

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_HERO_SPEC_LABEL  # Inter-SemiBold (font-weight: 600)

        # Value (bottom)
        value_box = slide.shapes.add_textbox(
            x_pos, specs_y + Inches(0.48),
            single_card_width, Inches(0.4)
        )
        tf = value_box.text_frame
        tf.text = value
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_HERO_SPEC_VALUE
        p.font.color.rgb = FONT_COLOR_HERO_SPEC_VALUE
        p.font.bold = FONT_BOLD_HERO_SPEC_VALUE

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_HERO_SPEC_VALUE  # Inter-Bold (font-weight: 700)

    return prs

def create_slide_7(prs):
    """Slide 7: TECHNICAL DEEP DIVE"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 7)

    # The three keywords - using KEYWORD_THEME_TECH
    keywords = [
        {"text": "TECHNICAL", "color": KEYWORD_THEME_TECH[0]},
        {"text": "DEEP", "color": KEYWORD_THEME_TECH[1]},
        {"text": "DIVE", "color": KEYWORD_THEME_TECH[2]}
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

        # CRITICAL: Font name must be set at RUN level!
        for run in p.runs:
            run.font.name = FONT_FAMILY_KEYWORD  # Inter ExtraLight (font-weight: 200)
            run.font.character_spacing = FONT_LETTER_SPACING_KEYWORD

    return prs

def create_slide_8(prs):
    """Slide 8: Tokenization Intro - A Sample from legal domain"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 8)

    # Title: "A Sample from legal domain:"
    title_box = slide.shapes.add_textbox(
        TOKENIZATION_TITLE_X, TOKENIZATION_TITLE_Y,
        TOKENIZATION_TITLE_WIDTH, TOKENIZATION_TITLE_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "A Sample from legal domain:"
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_TOKENIZATION_TITLE
    p.font.color.rgb = FONT_COLOR_TOKENIZATION_TITLE
    for run in p.runs:
        run.font.name = FONT_FAMILY_TOKENIZATION_TITLE

    # Arrow down
    arrow_box = slide.shapes.add_textbox(
        TOKENIZATION_ARROW_X, TOKENIZATION_ARROW_Y,
        TOKENIZATION_ARROW_WIDTH, TOKENIZATION_ARROW_HEIGHT
    )
    tf = arrow_box.text_frame
    tf.text = TOKENIZATION_ARROW_TEXT
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_TOKENIZATION_ARROW
    p.font.color.rgb = FONT_COLOR_TOKENIZATION_ARROW

    # Token boxes in horizontal row
    for i, token_text in enumerate(TOKENIZATION_TOKENS):
        x_pos = TOKENIZATION_TOKEN_X_START + (i * (TOKENIZATION_TOKEN_WIDTH + TOKENIZATION_TOKEN_GAP))

        # Create token box
        token_box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x_pos, TOKENIZATION_TOKENS_Y,
            TOKENIZATION_TOKEN_WIDTH, TOKENIZATION_TOKEN_HEIGHT
        )
        token_box.fill.solid()
        token_box.fill.fore_color.rgb = TOKENIZATION_TOKEN_FILL_COLOR
        token_box.line.color.rgb = TOKENIZATION_TOKEN_BORDER_COLOR
        token_box.line.width = TOKENIZATION_TOKEN_BORDER_WIDTH

        # Token text
        tf = token_box.text_frame
        tf.text = token_text
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_TOKENIZATION_TOKEN
        p.font.color.rgb = FONT_COLOR_TOKENIZATION_TOKEN
        for run in p.runs:
            run.font.name = FONT_FAMILY_TOKENIZATION_TOKEN

    return prs

def create_slide_9(prs):
    """Slide 9: Vector Embeddings (Token → Vector Lookup)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 9)

    # Create each token row (Wit, nesses, must, tell, nothing)
    for i, token_info in enumerate(TOKEN_DATA):
        y_pos = TOKEN_ROW_Y_START + (i * TOKEN_ROW_GAP)

        # Token box (left side)
        token_box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            TOKEN_BOX_X, Inches(y_pos),
            TOKEN_BOX_WIDTH, TOKEN_BOX_HEIGHT
        )
        token_box.fill.solid()
        token_box.fill.fore_color.rgb = TOKEN_BOX_FILL_COLOR
        token_box.line.color.rgb = TOKEN_BOX_BORDER_COLOR
        token_box.line.width = TOKEN_BOX_BORDER_WIDTH

        # Token text
        tf = token_box.text_frame
        tf.text = token_info["token"]
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_TOKEN
        p.font.color.rgb = FONT_COLOR_TOKEN
        for run in p.runs:
            run.font.name = FONT_FAMILY_TOKEN

        # Arrow (center)
        arrow_box = slide.shapes.add_textbox(
            ARROW_X, Inches(y_pos),
            ARROW_WIDTH, TOKEN_BOX_HEIGHT
        )
        tf = arrow_box.text_frame
        tf.text = ARROW_TEXT
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_ARROW
        p.font.color.rgb = FONT_COLOR_ARROW

        # Vector cells (right side, 6 cells)
        for j, vector_value in enumerate(token_info["vectors"]):
            cell_x = VECTOR_GRID_X + (j * (VECTOR_CELL_WIDTH + VECTOR_CELL_GAP))

            # Create vector cell box
            vector_cell = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                cell_x, Inches(y_pos),
                VECTOR_CELL_WIDTH, TOKEN_BOX_HEIGHT
            )
            vector_cell.fill.solid()
            vector_cell.fill.fore_color.rgb = VECTOR_CELL_FILL_COLOR
            vector_cell.line.color.rgb = VECTOR_CELL_BORDER_COLOR
            vector_cell.line.width = VECTOR_CELL_BORDER_WIDTH

            # Vector value text
            tf = vector_cell.text_frame
            tf.text = vector_value
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            p.font.size = FONT_SIZE_VECTOR
            p.font.color.rgb = FONT_COLOR_VECTOR

            # Last cell ("...") should be accent color
            if vector_value == "...":
                p.font.color.rgb = COLOR_ACCENT_BLUE

            for run in p.runs:
                run.font.name = FONT_FAMILY_VECTOR

    return prs

def create_slide_10(prs):
    """Slide 10: Attention is all you need - Attention Matrix"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 10)

    # Title
    title_box = slide.shapes.add_textbox(
        ATTENTION_TITLE_X, ATTENTION_TITLE_Y,
        ATTENTION_TITLE_WIDTH, ATTENTION_TITLE_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "Attention is all you need"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_ATTENTION_TITLE
    p.font.color.rgb = FONT_COLOR_ATTENTION_TITLE
    for run in p.runs:
        run.font.name = FONT_FAMILY_ATTENTION_TITLE

    # Helper function to get score color
    def get_score_style(score):
        """Returns (fill_color, border_color, text_color) for a given score"""
        if score >= 0.8:
            return (ATTENTION_SCORE_HIGH_FILL, ATTENTION_SCORE_HIGH_BORDER, ATTENTION_SCORE_HIGH_COLOR)
        elif score >= 0.05:
            return (ATTENTION_SCORE_MED_FILL, ATTENTION_SCORE_MED_BORDER, ATTENTION_SCORE_MED_COLOR)
        elif score >= 0.02:
            return (ATTENTION_SCORE_LOW_MED_FILL, ATTENTION_SCORE_LOW_MED_BORDER, ATTENTION_SCORE_LOW_MED_COLOR)
        else:
            return (ATTENTION_SCORE_LOW_FILL, ATTENTION_SCORE_LOW_BORDER, ATTENTION_SCORE_LOW_COLOR)

    # Create 6x6 grid (header row + 5 data rows, header col + 5 data cols)
    # Row 0: Header row
    # Col 0: Empty top-left cell
    # Cols 1-5: Token headers (Wit, nesses, must, tell, nothing)

    # Empty top-left cell (transparent, no content)
    # (We skip creating it since it's just empty space)

    # Header row: Token headers (columns)
    for col_idx, token in enumerate(ATTENTION_TOKENS):
        x_pos = ATTENTION_MATRIX_X + ((col_idx + 1) * (ATTENTION_CELL_WIDTH + ATTENTION_CELL_GAP))
        y_pos = ATTENTION_MATRIX_Y

        cell = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x_pos, y_pos,
            ATTENTION_CELL_WIDTH, ATTENTION_CELL_HEIGHT
        )
        cell.fill.solid()
        cell.fill.fore_color.rgb = ATTENTION_HEADER_FILL_COLOR
        cell.line.color.rgb = ATTENTION_HEADER_BORDER_COLOR
        cell.line.width = ATTENTION_CELL_BORDER_WIDTH

        tf = cell.text_frame
        tf.text = token
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_ATTENTION_HEADER
        p.font.color.rgb = FONT_COLOR_ATTENTION_HEADER
        for run in p.runs:
            run.font.name = FONT_FAMILY_ATTENTION_HEADER

    # Data rows (rows 1-5)
    for row_idx, (row_token, row_scores) in enumerate(zip(ATTENTION_TOKENS, ATTENTION_MATRIX_DATA)):
        y_pos = ATTENTION_MATRIX_Y + ((row_idx + 1) * (ATTENTION_CELL_HEIGHT + ATTENTION_CELL_GAP))

        # Row header (token name)
        x_pos = ATTENTION_MATRIX_X
        cell = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x_pos, y_pos,
            ATTENTION_CELL_WIDTH, ATTENTION_CELL_HEIGHT
        )
        cell.fill.solid()
        cell.fill.fore_color.rgb = ATTENTION_HEADER_FILL_COLOR
        cell.line.color.rgb = ATTENTION_HEADER_BORDER_COLOR
        cell.line.width = ATTENTION_CELL_BORDER_WIDTH

        tf = cell.text_frame
        tf.text = row_token
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = FONT_SIZE_ATTENTION_HEADER
        p.font.color.rgb = FONT_COLOR_ATTENTION_HEADER
        for run in p.runs:
            run.font.name = FONT_FAMILY_ATTENTION_HEADER

        # Score cells
        for col_idx, score in enumerate(row_scores):
            x_pos = ATTENTION_MATRIX_X + ((col_idx + 1) * (ATTENTION_CELL_WIDTH + ATTENTION_CELL_GAP))

            fill_color, border_color, text_color = get_score_style(score)

            cell = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x_pos, y_pos,
                ATTENTION_CELL_WIDTH, ATTENTION_CELL_HEIGHT
            )
            cell.fill.solid()
            cell.fill.fore_color.rgb = fill_color
            cell.line.color.rgb = border_color
            cell.line.width = ATTENTION_CELL_BORDER_WIDTH

            tf = cell.text_frame
            tf.text = f"{score:.2f}"
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            p.font.size = FONT_SIZE_ATTENTION_SCORE
            p.font.color.rgb = text_color
            for run in p.runs:
                run.font.name = FONT_FAMILY_ATTENTION_SCORE

    # Footnote
    footnote_box = slide.shapes.add_textbox(
        ATTENTION_FOOTNOTE_X, ATTENTION_FOOTNOTE_Y,
        ATTENTION_FOOTNOTE_WIDTH, ATTENTION_FOOTNOTE_HEIGHT
    )
    tf = footnote_box.text_frame
    tf.text = ATTENTION_FOOTNOTE_TEXT
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    p.font.size = FONT_SIZE_ATTENTION_FOOTNOTE
    p.font.color.rgb = FONT_COLOR_ATTENTION_FOOTNOTE
    p.font.italic = True

    return prs

def create_slide_11(prs):
    """Slide 11: Next word prediction"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 11)

    # Title
    title_box = slide.shapes.add_textbox(
        PREDICTION_TITLE_X, PREDICTION_TITLE_Y,
        PREDICTION_TITLE_WIDTH, PREDICTION_TITLE_HEIGHT
    )
    tf = title_box.text_frame
    tf.text = "Next word prediction"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PREDICTION_TITLE
    p.font.color.rgb = FONT_COLOR_PREDICTION_TITLE
    for run in p.runs:
        run.font.name = FONT_FAMILY_PREDICTION_TITLE

    # Context Vector Bar
    vector_bar = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        PREDICTION_CONTENT_X, PREDICTION_VECTOR_Y,
        PREDICTION_CONTENT_WIDTH, PREDICTION_VECTOR_HEIGHT
    )
    vector_bar.fill.solid()
    vector_bar.fill.fore_color.rgb = PREDICTION_VECTOR_FILL_COLOR
    vector_bar.line.color.rgb = PREDICTION_VECTOR_BORDER_COLOR
    vector_bar.line.width = PREDICTION_VECTOR_BORDER_WIDTH

    # Context Vector Label (inside bar, top with equal margin)
    label_box = slide.shapes.add_textbox(
        PREDICTION_CONTENT_X + PREDICTION_VECTOR_MARGIN,
        PREDICTION_VECTOR_Y + PREDICTION_VECTOR_MARGIN,
        PREDICTION_CONTENT_WIDTH - (2 * PREDICTION_VECTOR_MARGIN), Inches(0.25)
    )
    tf = label_box.text_frame
    tf.text = "CONTEXT VECTOR"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PREDICTION_VECTOR_LABEL
    p.font.color.rgb = FONT_COLOR_PREDICTION_VECTOR_LABEL
    for run in p.runs:
        run.font.name = FONT_FAMILY_INTER_REGULAR

    # Vector Segments (10 colored rectangles, evenly distributed with equal margins)
    # Calculate available width: 12" - left margin - right margin
    available_width = PREDICTION_CONTENT_WIDTH.inches - (2 * PREDICTION_VECTOR_MARGIN.inches)
    # Calculate segment width: (available_width - 9 gaps) / 10 segments
    segment_width = (available_width - (9 * PREDICTION_SEGMENT_GAP.inches)) / PREDICTION_SEGMENT_COUNT
    # Position segments with equal margin from top of label and bottom of box
    segments_y = PREDICTION_VECTOR_Y + PREDICTION_VECTOR_MARGIN + Inches(0.25) + PREDICTION_VECTOR_MARGIN

    for i, color in enumerate(PREDICTION_SEGMENT_COLORS):
        segment_x = PREDICTION_CONTENT_X + PREDICTION_VECTOR_MARGIN + (i * (Inches(segment_width) + PREDICTION_SEGMENT_GAP))

        segment = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            segment_x, segments_y,
            Inches(segment_width), PREDICTION_SEGMENT_HEIGHT
        )
        segment.fill.solid()
        segment.fill.fore_color.rgb = color
        segment.line.color.rgb = color

    # Temperature Parameter Display (left side)
    # Label "Temperature"
    temp_label_box = slide.shapes.add_textbox(
        PREDICTION_TEMP_X, PREDICTION_TEMP_Y,
        PREDICTION_TEMP_WIDTH, Inches(0.4)
    )
    tf = temp_label_box.text_frame
    tf.text = "Temperature"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PREDICTION_TEMP_LABEL
    p.font.color.rgb = FONT_COLOR_PREDICTION_TEMP_LABEL
    for run in p.runs:
        run.font.name = FONT_FAMILY_INTER_REGULAR

    # Value "0.8"
    temp_value_box = slide.shapes.add_textbox(
        PREDICTION_TEMP_X, PREDICTION_TEMP_Y + Inches(0.5),
        PREDICTION_TEMP_WIDTH, Inches(0.8)
    )
    tf = temp_value_box.text_frame
    tf.text = f"{PREDICTION_TEMP_VALUE:.1f}"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PREDICTION_TEMP_VALUE
    p.font.color.rgb = FONT_COLOR_PREDICTION_TEMP_VALUE
    p.font.bold = True
    for run in p.runs:
        run.font.name = FONT_FAMILY_INTER_REGULAR

    # Arrow down
    arrow_box = slide.shapes.add_textbox(
        PREDICTION_CONTENT_X + (PREDICTION_CONTENT_WIDTH / 2) - Inches(0.3),
        PREDICTION_ARROW_Y,
        Inches(0.6), Inches(0.5)
    )
    tf = arrow_box.text_frame
    tf.text = PREDICTION_ARROW_TEXT
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = FONT_SIZE_PREDICTION_ARROW
    p.font.color.rgb = FONT_COLOR_PREDICTION_ARROW

    # Helper function to get fill color
    def get_fill_color(category):
        if category == "highest":
            return PREDICTION_FILL_HIGHEST
        elif category == "high":
            return PREDICTION_FILL_HIGH
        elif category == "medium":
            return PREDICTION_FILL_MEDIUM
        else:  # low, lowest
            return PREDICTION_FILL_LOW

    # Probability bars
    for i, pred_data in enumerate(PREDICTION_DATA):
        y_pos = PREDICTION_PROB_Y_START + (i * (PREDICTION_PROB_BAR_HEIGHT + PREDICTION_PROB_GAP))

        # Token label (left side, right-aligned text)
        label_box = slide.shapes.add_textbox(
            PREDICTION_PROB_LABEL_X, y_pos,
            PREDICTION_PROB_LABEL_WIDTH, PREDICTION_PROB_BAR_HEIGHT
        )
        tf = label_box.text_frame
        tf.text = pred_data["token"]
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        p.font.size = FONT_SIZE_PREDICTION_TOKEN

        # Highest token gets green color
        if pred_data["category"] == "highest":
            p.font.color.rgb = FONT_COLOR_PREDICTION_TOKEN_HIGHEST
            p.font.bold = True
        else:
            p.font.color.rgb = FONT_COLOR_PREDICTION_TOKEN

        for run in p.runs:
            run.font.name = FONT_FAMILY_PREDICTION_TOKEN

        # Probability bar background (right-aligned at fixed position)
        bar_bg = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            PREDICTION_PROB_BAR_X, y_pos,
            PREDICTION_PROB_BAR_WIDTH, PREDICTION_PROB_BAR_HEIGHT
        )
        bar_bg.fill.solid()
        bar_bg.fill.fore_color.rgb = PREDICTION_PROB_BAR_FILL_COLOR
        bar_bg.line.color.rgb = PREDICTION_PROB_BAR_BORDER_COLOR
        bar_bg.line.width = PREDICTION_PROB_BAR_BORDER_WIDTH

        # Probability fill (proportional to probability, left-aligned within bar)
        fill_width = PREDICTION_PROB_BAR_WIDTH.inches * pred_data["probability"]
        if fill_width > 0.1:  # Only draw if visible
            bar_fill = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                PREDICTION_PROB_BAR_X, y_pos,
                Inches(fill_width), PREDICTION_PROB_BAR_HEIGHT
            )
            bar_fill.fill.solid()
            bar_fill.fill.fore_color.rgb = get_fill_color(pred_data["category"])
            bar_fill.line.color.rgb = get_fill_color(pred_data["category"])

        # Probability value (right side of bar, always at same position)
        value_box = slide.shapes.add_textbox(
            PREDICTION_PROB_BAR_X + PREDICTION_PROB_BAR_WIDTH - Inches(0.8), y_pos,
            Inches(0.7), PREDICTION_PROB_BAR_HEIGHT
        )
        tf = value_box.text_frame
        tf.text = f"{pred_data['probability']:.2f}"
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        p.font.size = FONT_SIZE_PREDICTION_VALUE
        p.font.color.rgb = FONT_COLOR_PREDICTION_VALUE
        p.font.bold = True
        for run in p.runs:
            run.font.name = FONT_FAMILY_PREDICTION_VALUE

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

    # Slide 5: TO BE DESIGNED
    create_slide_5(prs)

    # Slide 6: BRAIN-BRIDGES Hero Slide
    create_slide_6(prs)

    # Slide 7: TECHNICAL DEEP DIVE
    create_slide_7(prs)

    # Slide 8: Tokenization Intro - A Sample from legal domain
    create_slide_8(prs)

    # Slide 9: Vector Embeddings (Token → Vector Lookup)
    create_slide_9(prs)

    # Slide 10: Attention is all you need
    create_slide_10(prs)

    # Slide 11: Next word prediction
    create_slide_11(prs)

    # Additional slides as placeholders
    for i in range(12, 18):
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
