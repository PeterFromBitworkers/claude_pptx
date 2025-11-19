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
    """Slide 5: BRAIN-BRIDGES Hero Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 5)

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

    # Slide 5: BRAIN-BRIDGES Hero Slide
    create_slide_5(prs)

    # Additional slides as placeholders
    for i in range(6, 18):
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
