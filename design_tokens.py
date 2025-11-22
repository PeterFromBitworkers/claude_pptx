"""
Brain-Bridges Design System - Design Tokens
Single source of truth for all colors, typography, layouts, and spacing.

This file centralizes all design constants used in the PowerPoint generator.
Any changes to colors, fonts, or positions should be made HERE ONLY.
"""

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# =============================================================================
# COLORS
# =============================================================================

# Background Colors
COLOR_BACKGROUND_DARK = RGBColor(17, 24, 39)      # Main slide background
COLOR_BACKGROUND_LIGHT = RGBColor(31, 41, 55)     # Cards/boxes (if needed)

# Text Colors
COLOR_TEXT_WHITE = RGBColor(255, 255, 255)        # Primary text
COLOR_TEXT_GRAY = RGBColor(209, 213, 219)         # Secondary text
COLOR_TEXT_GRAY_DARK = RGBColor(167, 171, 175)    # Slide numbers, subtle text

# Accent Colors
COLOR_ACCENT_BLUE = RGBColor(77, 171, 247)        # #4dabf7
COLOR_ACCENT_CYAN = RGBColor(6, 182, 212)         # #06b6d4
COLOR_ACCENT_GREEN = RGBColor(16, 185, 129)       # #10b981
COLOR_ACCENT_RED = RGBColor(239, 68, 68)          # #ef4444
COLOR_ACCENT_PURPLE = RGBColor(139, 92, 246)      # #8b5cf6

# Border Colors
COLOR_BORDER = RGBColor(64, 64, 64)               # #404040

# =============================================================================
# TYPOGRAPHY
# =============================================================================

# Font Families (Inter PostScript Names)
# Using PostScript names (with hyphens) that PowerPoint recognizes
FONT_FAMILY_INTER_THIN = "Inter-Thin"           # font-weight: 100
FONT_FAMILY_INTER_EXTRALIGHT = "Inter-ExtraLight"  # font-weight: 200
FONT_FAMILY_INTER_LIGHT = "Inter-Light"         # font-weight: 300
FONT_FAMILY_INTER_REGULAR = "Inter-Regular"     # font-weight: 400
FONT_FAMILY_INTER_MEDIUM = "Inter-Medium"       # font-weight: 500
FONT_FAMILY_INTER_SEMIBOLD = "Inter-SemiBold"   # font-weight: 600
FONT_FAMILY_INTER_BOLD = "Inter-Bold"           # font-weight: 700
FONT_FAMILY_INTER_EXTRABOLD = "Inter-ExtraBold" # font-weight: 800
FONT_FAMILY_INTER_BLACK = "Inter-Black"         # font-weight: 900

# System Fonts
FONT_FAMILY_MONOSPACE = "Menlo"                 # Monospace for subtitle
FONT_FAMILY_FALLBACK = "Calibri"                # Fallback for PowerPoint

# Default fonts for different content types
FONT_FAMILY_PRIMARY = FONT_FAMILY_INTER_REGULAR      # Default body text (font-weight: 400)
FONT_FAMILY_KEYWORD = FONT_FAMILY_INTER_EXTRALIGHT   # Keyword slides (font-weight: 200)
FONT_FAMILY_TITLE = FONT_FAMILY_INTER_EXTRALIGHT     # Content slide titles (font-weight: 200)
FONT_FAMILY_SUBTITLE = FONT_FAMILY_MONOSPACE         # Subtitles (Menlo monospace)
FONT_FAMILY_VIOLATION = FONT_FAMILY_MONOSPACE        # Violation text (Menlo monospace)
FONT_FAMILY_STAT_NUMBER = FONT_FAMILY_INTER_EXTRALIGHT  # Large stat numbers (font-weight: 200)
FONT_FAMILY_STAT_LABEL = FONT_FAMILY_INTER_LIGHT        # Stat labels (font-weight: 300)

# Logo "BRAIN BRIDGES"
FONT_SIZE_LOGO = Pt(21)
FONT_BOLD_LOGO = True
FONT_COLOR_LOGO = COLOR_TEXT_WHITE
FONT_LETTER_SPACING_LOGO = Pt(-0.5)

# Slide Number "##/17"
FONT_SIZE_SLIDE_NUMBER = Pt(21)
FONT_BOLD_SLIDE_NUMBER = False
FONT_COLOR_SLIDE_NUMBER = COLOR_TEXT_GRAY_DARK

# Keywords (THE, AI, PARADOX)
FONT_SIZE_KEYWORD = Pt(72)
FONT_BOLD_KEYWORD = False
FONT_LETTER_SPACING_KEYWORD = Pt(2)

# Content Slide - Title
FONT_SIZE_CONTENT_TITLE = Pt(44)          # Reduced from 48 for more spacing
FONT_BOLD_CONTENT_TITLE = False
FONT_COLOR_CONTENT_TITLE = COLOR_ACCENT_BLUE

# Content Slide - Subtitle
FONT_SIZE_CONTENT_SUBTITLE = Pt(18)       # Reduced from 20 for more spacing
FONT_BOLD_CONTENT_SUBTITLE = True
FONT_COLOR_CONTENT_SUBTITLE_ALERT = COLOR_ACCENT_RED
FONT_COLOR_CONTENT_SUBTITLE_NORMAL = COLOR_TEXT_GRAY

# Problem Grid - Title
FONT_SIZE_PROBLEM_TITLE = Pt(15)          # Reduced from 16 for more spacing
FONT_BOLD_PROBLEM_TITLE = True
FONT_COLOR_PROBLEM_TITLE = COLOR_TEXT_WHITE

# Problem Grid - Description (same formatting as title)
FONT_SIZE_PROBLEM_DESC = Pt(15)           # Same as title
FONT_BOLD_PROBLEM_DESC = True             # Same as title
FONT_COLOR_PROBLEM_DESC = COLOR_TEXT_WHITE  # Same as title (white instead of gray)

# Problem Grid - Violation
FONT_SIZE_PROBLEM_VIOLATION = Pt(11)      # Increased for better visibility
FONT_BOLD_PROBLEM_VIOLATION = True
FONT_COLOR_PROBLEM_VIOLATION = COLOR_ACCENT_RED

# Placeholder Slide
FONT_SIZE_PLACEHOLDER = Pt(48)
FONT_COLOR_PLACEHOLDER = COLOR_ACCENT_BLUE

# =============================================================================
# LAYOUT - SLIDE DIMENSIONS
# =============================================================================

SLIDE_WIDTH = Inches(16)
SLIDE_HEIGHT = Inches(9)

# =============================================================================
# LAYOUT - MASTER ELEMENTS (Logo & Slide Number)
# =============================================================================

# Logo Position & Size
LOGO_X = Inches(0.28)
LOGO_Y = Inches(0.28)
LOGO_WIDTH = Inches(3)
LOGO_HEIGHT = Inches(0.4)
LOGO_TEXT = "BRAIN BRIDGES"

# Slide Number Position & Size
SLIDE_NUMBER_X = Inches(15.1)
SLIDE_NUMBER_Y = Inches(0.28)
SLIDE_NUMBER_WIDTH = Inches(0.7)
SLIDE_NUMBER_HEIGHT = Inches(0.4)

# =============================================================================
# LAYOUT - KEYWORD SLIDES (Type 1)
# =============================================================================

# Keyword Slide Layout
KEYWORD_BOX_X = Inches(2)
KEYWORD_BOX_WIDTH = Inches(12)
KEYWORD_BOX_HEIGHT = Inches(1.2)
KEYWORD_Y_START = 2.1  # Inches (float for calculation) - moved up slightly
KEYWORD_Y_GAP = 1.9    # Inches (float for calculation) - increased spacing between words

# Keyword Color Themes
KEYWORD_THEME_PROBLEM = [
    COLOR_ACCENT_RED,    # THE
    COLOR_ACCENT_BLUE,   # AI
    COLOR_ACCENT_GREEN   # PARADOX
]

KEYWORD_THEME_SOLUTION = [
    COLOR_ACCENT_BLUE,   # SOVEREIGN
    COLOR_ACCENT_CYAN,   # AI
    COLOR_ACCENT_GREEN   # SOLUTION
]

KEYWORD_THEME_TECH = [
    COLOR_ACCENT_PURPLE, # TECHNICAL
    COLOR_ACCENT_BLUE,   # DEEP
    COLOR_ACCENT_CYAN    # DIVE
]

# =============================================================================
# LAYOUT - CONTENT SLIDES (Type 2)
# =============================================================================

# Content Header Position
CONTENT_HEADER_X = Inches(1)
CONTENT_HEADER_Y = Inches(1)
CONTENT_HEADER_WIDTH = Inches(14)
CONTENT_HEADER_HEIGHT = Inches(0.8)

# Content Subtitle Position
CONTENT_SUBTITLE_X = Inches(1)
CONTENT_SUBTITLE_Y = Inches(1.8)
CONTENT_SUBTITLE_WIDTH = Inches(14)
CONTENT_SUBTITLE_HEIGHT = Inches(0.4)

# Content Area Start
CONTENT_AREA_Y_START = Inches(3)
CONTENT_MAX_WIDTH = Inches(14)

# =============================================================================
# LAYOUT - PROBLEM GRID (Slide 2)
# =============================================================================

# 2x2 Grid Layout (like Legacy HTML)
# Slide is 16" wide x 9" tall
# Perfect symmetry: horizontal gap = vertical gap, top margin = bottom margin
PROBLEM_GRID_X_POSITIONS = [2.45, 8.35]       # In inches (2 columns: left, right) - symmetric
PROBLEM_GRID_Y_POSITIONS = [2.65, 5.85]       # In inches (2 rows: top, bottom) - symmetric
PROBLEM_GRID_BOX_WIDTH = 5.2                  # In inches
PROBLEM_GRID_BOX_HEIGHT = 2.5                 # In inches
# Gap between cards: 0.7" (horizontal and vertical)
# Top margin (subtitle to cards): 0.65"
# Bottom margin (cards to slide end): 0.65"

# Problem Grid Card Styling
PROBLEM_CARD_FILL_COLOR = COLOR_BACKGROUND_LIGHT
PROBLEM_CARD_BORDER_COLOR = RGBColor(80, 80, 80)  # Subtle gray (#505050)
PROBLEM_CARD_BORDER_WIDTH = Pt(0.75)               # Thinner for subtle look
PROBLEM_CARD_CORNER_RADIUS = Inches(0.15)          # Rounded corners (12px equivalent)

# Problem Grid Icon (centered in smaller card)
PROBLEM_ICON_Y_OFFSET = 0.25                  # From y_start
PROBLEM_ICON_HEIGHT = 0.55
PROBLEM_ICON_WIDTH = Inches(0.55)             # Icon display size (slightly smaller)
PROBLEM_ICON_X_OFFSET = 2.325                 # Center offset for 5.2" wide card: (5.2 - 0.55) / 2

# Problem Grid Item Layout (adjusted for 2.5" card height)
PROBLEM_TITLE_Y_OFFSET = 0.9                  # From y_start (moved down for icon)
PROBLEM_TITLE_HEIGHT = 0.35

PROBLEM_DESC_Y_OFFSET = 1.3                   # From y_start
PROBLEM_DESC_HEIGHT = 0.65

PROBLEM_VIOLATION_Y_OFFSET = 2.0              # From y_start
PROBLEM_VIOLATION_HEIGHT = 0.28

# Problem Grid Icon Paths (PNG files, converted from SVG)
PROBLEM_ICONS = {
    "legal": "assets/icons/legal.png",
    "medical": "assets/icons/medical.png",
    "financial": "assets/icons/financial.png",
    "engineering": "assets/icons/engineering.png"
}

# =============================================================================
# LAYOUT - MARKET STATS (Slide 3)
# =============================================================================

# Large Stat Display ($1.7T)
LARGE_STAT_X = Inches(1)
LARGE_STAT_Y = Inches(2.8)                        # More space after subtitle
LARGE_STAT_WIDTH = Inches(14)
LARGE_STAT_HEIGHT = Inches(1.6)                   # Slightly smaller
LARGE_STAT_LABEL_Y = Inches(4.3)                  # More space between $1.7T and label
FONT_SIZE_LARGE_STAT_NUMBER = Pt(88)              # Reduced from 96 for better spacing
FONT_SIZE_LARGE_STAT_LABEL = Pt(15)               # Reduced from 16

# Stat Cards (4 cards in a row, centered)
# Calculation: 4 cards * 2.9" = 11.6", 3 gaps * 0.3" = 0.9", total = 12.5"
# Center: (16 - 12.5) / 2 = 1.75" from left
STAT_CARD_Y_START = 5.2                           # In inches - more space from large stat
STAT_CARD_X_POSITIONS = [1.75, 4.95, 8.15, 11.35] # In inches (centered)
STAT_CARD_WIDTH = 2.9                             # In inches
STAT_CARD_HEIGHT = 2.3                            # In inches - slightly smaller for better spacing

# Stat Card Styling
STAT_CARD_FILL_COLOR = COLOR_BACKGROUND_LIGHT
STAT_CARD_BORDER_COLOR = RGBColor(80, 80, 80)     # Subtle gray
STAT_CARD_BORDER_WIDTH = Pt(0.75)
STAT_CARD_CORNER_RADIUS = Inches(0.15)            # Rounded corners

# Stat Card Text Layout (adjusted for 2.3" card height)
STAT_NUMBER_Y_OFFSET = 0.3                        # From card top - more space at top
STAT_NUMBER_HEIGHT = 0.7
FONT_SIZE_STAT_NUMBER = Pt(58)                    # Reduced from 64 for better spacing

STAT_LABEL_Y_OFFSET = 1.2                         # More space between number and label
STAT_LABEL_HEIGHT = 0.6
FONT_SIZE_STAT_LABEL = Pt(13)                     # Reduced from 14 for better spacing

STAT_SOURCE_Y_OFFSET = 1.85                       # Adjusted for increased label offset
STAT_SOURCE_HEIGHT = 0.4
FONT_SIZE_STAT_SOURCE = Pt(9)                     # Keep same size for readability
FONT_COLOR_STAT_SOURCE = COLOR_TEXT_GRAY_DARK     # Gray for subtle appearance

# =============================================================================
# LAYOUT - HERO SLIDE (Slide 5)
# =============================================================================

# Hero Grid Layout (Left/Right Split using Golden Ratio)
HERO_LEFT_X = Inches(1)
HERO_LEFT_Y = Inches(1.8)
HERO_LEFT_WIDTH = Inches(7.5)  # ~47% of slide (golden ratio-ish)
HERO_RIGHT_X = Inches(9)
HERO_RIGHT_Y = Inches(1.4)  # Higher to align with title top
HERO_RIGHT_WIDTH = Inches(6.5)

# Hero Title & Subtitle
HERO_TITLE_X = HERO_LEFT_X
HERO_TITLE_Y = HERO_LEFT_Y
HERO_TITLE_WIDTH = HERO_LEFT_WIDTH
HERO_TITLE_HEIGHT = Inches(1.2)
FONT_SIZE_HERO_TITLE = Pt(64)
FONT_FAMILY_HERO_TITLE = FONT_FAMILY_INTER_EXTRABOLD  # font-weight: 800 in HTML
FONT_BOLD_HERO_TITLE = False  # Don't use PowerPoint bold, font weight is in the font itself
FONT_LETTER_SPACING_HERO_TITLE = Pt(-0.5)  # Negative spacing like HTML (-0.025em)

HERO_SUBTITLE_X = HERO_LEFT_X
HERO_SUBTITLE_Y = Inches(3.1)
HERO_SUBTITLE_WIDTH = HERO_LEFT_WIDTH
HERO_SUBTITLE_HEIGHT = Inches(0.4)
FONT_SIZE_HERO_SUBTITLE = Pt(18)
FONT_FAMILY_HERO_SUBTITLE = FONT_FAMILY_MONOSPACE  # Monospace font (Menlo) like HTML
FONT_BOLD_HERO_SUBTITLE = True
FONT_COLOR_HERO_SUBTITLE = COLOR_ACCENT_BLUE

# Hero Features List
HERO_FEATURES_X = HERO_LEFT_X
HERO_FEATURES_Y_START = 3.8  # In inches (float for calculation)
HERO_FEATURES_WIDTH = HERO_LEFT_WIDTH
HERO_FEATURE_HEIGHT = 0.45   # Height per feature item
HERO_FEATURE_GAP = 0.48      # Gap between features
FONT_SIZE_HERO_FEATURE = Pt(15)
FONT_FAMILY_HERO_FEATURE = FONT_FAMILY_INTER_LIGHT  # font-weight: 300 in HTML
FONT_COLOR_HERO_FEATURE = COLOR_TEXT_WHITE

# Feature checkmark icon (PNG image)
HERO_FEATURE_CHECKMARK_ICON = "assets/icons/checkmark.png"
HERO_FEATURE_ICON_SIZE = Inches(0.32)  # Icon size

# Hero Product Image
HERO_IMAGE_X = HERO_RIGHT_X
HERO_IMAGE_Y = HERO_RIGHT_Y  # Align with title top
HERO_IMAGE_WIDTH = HERO_RIGHT_WIDTH
HERO_IMAGE_HEIGHT = Inches(5.5)
HERO_IMAGE_PATH = "assets/blue.png"  # Default hardware image
HERO_IMAGE_BORDER_COLOR = COLOR_ACCENT_BLUE
HERO_IMAGE_BORDER_COLOR_RGB = (77, 171, 247)  # RGB tuple for PIL (same as COLOR_ACCENT_BLUE)
HERO_IMAGE_BORDER_WIDTH = Pt(2.5)
HERO_IMAGE_CORNER_RADIUS_PX = 30  # Corner radius in pixels for PIL image processing

# Status Badge (top right INSIDE image with margin)
HERO_STATUS_MARGIN = Inches(0.2)  # Margin from image edge
HERO_STATUS_WIDTH = Inches(1.1)
HERO_STATUS_HEIGHT = Inches(0.35)
FONT_SIZE_HERO_STATUS = Pt(11)
FONT_FAMILY_HERO_STATUS = FONT_FAMILY_INTER_MEDIUM  # font-weight: 500 in HTML
FONT_COLOR_HERO_STATUS = COLOR_ACCENT_CYAN
HERO_STATUS_TEXT = "Ready"
HERO_STATUS_ICON = "assets/icons/plug.png"  # Plug icon
HERO_STATUS_ICON_SIZE = Inches(0.24)  # Larger icon

# Tech Specs (bottom INSIDE image with margins)
HERO_SPECS_MARGIN = Inches(0.2)  # Margin from image edge
HERO_SPECS_HEIGHT = Inches(0.95)  # Increased from 0.85 for better text fit
HERO_SPECS_GAP = Inches(0.12)  # Gap between cards
FONT_SIZE_HERO_SPEC_LABEL = Pt(10)  # Reduced from 14 to fit better in cards
FONT_FAMILY_HERO_SPEC_LABEL = FONT_FAMILY_INTER_SEMIBOLD  # font-weight: 600 in HTML
FONT_SIZE_HERO_SPEC_VALUE = Pt(14)  # Reduced from 18 to fit better in cards
FONT_FAMILY_HERO_SPEC_VALUE = FONT_FAMILY_INTER_BOLD  # font-weight: 700 in HTML
FONT_COLOR_HERO_SPEC_LABEL = COLOR_TEXT_GRAY
FONT_COLOR_HERO_SPEC_VALUE = COLOR_ACCENT_BLUE
FONT_BOLD_HERO_SPEC_VALUE = False  # Don't use PowerPoint bold, font weight is in the font itself

# Tech Specs Data (Configuration 1: Blue)
HERO_SPECS_CONFIG = {
    "processor": "M4 Pro 20-core",
    "memory": "64 GB memory",
    "users": "~20 Users"
}

# =============================================================================
# LAYOUT - TOKENIZATION INTRO SLIDE (Slide 8)
# =============================================================================

# "A Sample from legal domain:" title at top
TOKENIZATION_TITLE_X = Inches(1)
TOKENIZATION_TITLE_Y = Inches(2.5)
TOKENIZATION_TITLE_WIDTH = Inches(14)
TOKENIZATION_TITLE_HEIGHT = Inches(1)
FONT_SIZE_TOKENIZATION_TITLE = Pt(56)             # 3.5rem equivalent
FONT_FAMILY_TOKENIZATION_TITLE = FONT_FAMILY_INTER_EXTRALIGHT  # font-weight: 200
FONT_COLOR_TOKENIZATION_TITLE = COLOR_TEXT_WHITE

# Arrow down
TOKENIZATION_ARROW_X = Inches(7.5)
TOKENIZATION_ARROW_Y = Inches(3.8)
TOKENIZATION_ARROW_WIDTH = Inches(1)
TOKENIZATION_ARROW_HEIGHT = Inches(0.8)
TOKENIZATION_ARROW_TEXT = "↓"
FONT_SIZE_TOKENIZATION_ARROW = Pt(64)             # 4rem equivalent
FONT_COLOR_TOKENIZATION_ARROW = COLOR_ACCENT_BLUE

# Token boxes in horizontal row (5 tokens)
# ALIGNED WITH SLIDES 9 & 10: Total width = 12", Start X = 2"
TOKENIZATION_TOKENS_Y = Inches(5.2)
TOKENIZATION_TOKEN_HEIGHT = Inches(0.9)
TOKENIZATION_TOKEN_GAP = Inches(0.125)            # Gap between tokens (calculated)
# Total width: 12", 5 tokens
# Token Width = (12 - 4*0.125) / 5 = 11.5 / 5 = 2.3"
TOKENIZATION_TOKEN_WIDTH = Inches(2.3)
TOKENIZATION_TOKEN_X_START = Inches(2)            # Aligned with slides 9 & 10

# Token box styling
TOKENIZATION_TOKEN_FILL_COLOR = RGBColor(31, 41, 55)
TOKENIZATION_TOKEN_BORDER_COLOR = COLOR_ACCENT_BLUE
TOKENIZATION_TOKEN_BORDER_WIDTH = Pt(2)
TOKENIZATION_TOKEN_CORNER_RADIUS = Inches(0.1)    # 12px equivalent
FONT_SIZE_TOKENIZATION_TOKEN = Pt(29)             # 1.8rem equivalent
FONT_FAMILY_TOKENIZATION_TOKEN = FONT_FAMILY_INTER_EXTRALIGHT  # font-weight: 200
FONT_COLOR_TOKENIZATION_TOKEN = COLOR_TEXT_WHITE

# Token data for slide 8
TOKENIZATION_TOKENS = ["Wit", "nesses", "must", "tell", "nothing"]

# =============================================================================
# LAYOUT - VECTOR EMBEDDINGS SLIDE (Slide 9)
# =============================================================================

# Tokenization Row Layout (5 rows: Wit, nesses, must, tell, nothing)
# Each row has: [Token Box] → [Vector Grid with 6 cells]
# ALIGNED WITH SLIDES 8 & 10: Total width = 12", Start X = 2"
TOKEN_ROW_Y_START = 2.3                           # In inches - start position
TOKEN_ROW_GAP = 1.1                               # In inches - gap between rows
TOKEN_ROW_HEIGHT = 0.75                           # In inches - height per row

# Token Box (left side)
TOKEN_BOX_X = Inches(2)                           # Aligned with slides 8 & 10
TOKEN_BOX_WIDTH = Inches(2.5)
TOKEN_BOX_HEIGHT = Inches(0.75)
TOKEN_BOX_FILL_COLOR = RGBColor(31, 41, 55)       # rgba(31, 41, 55, 0.8) from CSS
TOKEN_BOX_BORDER_COLOR = COLOR_ACCENT_BLUE        # var(--accent-color)
TOKEN_BOX_BORDER_WIDTH = Pt(2)
TOKEN_BOX_CORNER_RADIUS = Inches(0.1)             # 12px equivalent
FONT_SIZE_TOKEN = Pt(22)
FONT_FAMILY_TOKEN = FONT_FAMILY_INTER_EXTRALIGHT  # font-weight: 200
FONT_COLOR_TOKEN = COLOR_TEXT_WHITE

# Arrow (center)
ARROW_X = Inches(4.7)                             # 2 + 2.5 + 0.2 gap
ARROW_WIDTH = Inches(0.6)
ARROW_TEXT = "→"
FONT_SIZE_ARROW = Pt(36)
FONT_COLOR_ARROW = COLOR_ACCENT_BLUE

# Vector Grid (right side, 6 cells per row)
VECTOR_GRID_X = Inches(5.5)                       # 4.7 + 0.6 + 0.2 gap
VECTOR_GRID_WIDTH = Inches(8.5)                   # Total width: 2 + 12 - 5.5 = 8.5"
VECTOR_GRID_FILL_COLOR = RGBColor(17, 24, 39)    # Background color (darker)
VECTOR_GRID_BORDER_COLOR = RGBColor(77, 171, 247)  # Accent blue border
VECTOR_GRID_BORDER_WIDTH = Pt(1)

# Vector Cell (individual number boxes)
VECTOR_CELL_WIDTH = Inches(1.29)                  # Width per cell (8.5 - 5*0.15) / 6
VECTOR_CELL_GAP = Inches(0.15)                    # Gap between cells
VECTOR_CELL_FILL_COLOR = RGBColor(31, 41, 55)    # Light background
VECTOR_CELL_BORDER_COLOR = RGBColor(60, 80, 100)  # Subtle border (darker than accent)
VECTOR_CELL_BORDER_WIDTH = Pt(1)
VECTOR_CELL_CORNER_RADIUS = Inches(0.03)          # 4px equivalent
FONT_SIZE_VECTOR = Pt(13)
FONT_FAMILY_VECTOR = FONT_FAMILY_MONOSPACE        # Monospace for numbers
FONT_COLOR_VECTOR = COLOR_TEXT_GRAY

# Token data for slide 8
TOKEN_DATA = [
    {"token": "Wit", "vectors": ["0.23", "-0.15", "0.87", "-0.42", "0.66", "..."]},
    {"token": "nesses", "vectors": ["0.45", "-0.67", "0.12", "0.89", "-0.34", "..."]},
    {"token": "must", "vectors": ["-0.56", "0.78", "-0.23", "0.41", "0.92", "..."]},
    {"token": "tell", "vectors": ["0.18", "-0.45", "0.73", "-0.28", "0.54", "..."]},
    {"token": "nothing", "vectors": ["0.67", "-0.12", "0.39", "0.85", "-0.71", "..."]}
]

# =============================================================================
# LAYOUT - ATTENTION MATRIX SLIDE (Slide 10)
# =============================================================================

# Title (using content header style)
ATTENTION_TITLE_X = Inches(1)
ATTENTION_TITLE_Y = Inches(1)
ATTENTION_TITLE_WIDTH = Inches(14)
ATTENTION_TITLE_HEIGHT = Inches(0.8)
FONT_SIZE_ATTENTION_TITLE = Pt(44)
FONT_FAMILY_ATTENTION_TITLE = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_ATTENTION_TITLE = COLOR_ACCENT_BLUE

# Attention Matrix Grid (6x6 grid = 1 header row + 5 data rows, 1 header col + 5 data cols)
# ALIGNED WITH SLIDES 8 & 9: Total width = 12", Start X = 2"
ATTENTION_MATRIX_X = Inches(2)                    # Aligned with slides 8 & 9
ATTENTION_MATRIX_Y = Inches(2.6)                  # Increased spacing below title
ATTENTION_CELL_WIDTH = Inches(1.9)                # Cell width (12" - 5*0.12") / 6 = 1.9"
ATTENTION_CELL_HEIGHT = Inches(0.8)               # Cell height
ATTENTION_CELL_GAP = Inches(0.12)                 # Gap between cells

# Cell styling
ATTENTION_CELL_BORDER_COLOR = RGBColor(77, 171, 247)  # Accent blue border
ATTENTION_CELL_BORDER_WIDTH = Pt(1)
ATTENTION_CELL_CORNER_RADIUS = Inches(0.067)      # 8px equivalent

# Header cell (token headers)
ATTENTION_HEADER_FILL_COLOR = RGBColor(38, 66, 96)  # rgba(77, 171, 247, 0.15) approximation
ATTENTION_HEADER_BORDER_COLOR = COLOR_ACCENT_BLUE
FONT_SIZE_ATTENTION_HEADER = Pt(18)               # 1.1rem
FONT_FAMILY_ATTENTION_HEADER = FONT_FAMILY_INTER_REGULAR
FONT_COLOR_ATTENTION_HEADER = COLOR_TEXT_WHITE

# Score cell
FONT_SIZE_ATTENTION_SCORE = Pt(16)                # 1rem
FONT_FAMILY_ATTENTION_SCORE = FONT_FAMILY_MONOSPACE
FONT_COLOR_ATTENTION_SCORE_DEFAULT = COLOR_TEXT_WHITE

# Score colors (heatmap)
# High scores (0.8-0.9): Green
ATTENTION_SCORE_HIGH_FILL = RGBColor(16, 185, 129)    # #10b981 green
ATTENTION_SCORE_HIGH_BORDER = RGBColor(16, 185, 129)
ATTENTION_SCORE_HIGH_COLOR = RGBColor(255, 255, 255)

# Medium scores (0.05-0.08): Blue
ATTENTION_SCORE_MED_FILL = RGBColor(48, 86, 122)      # rgba(77, 171, 247, 0.25) approximation
ATTENTION_SCORE_MED_BORDER = COLOR_ACCENT_BLUE
ATTENTION_SCORE_MED_COLOR = COLOR_ACCENT_BLUE

# Low-medium scores (0.02-0.04): Light blue
ATTENTION_SCORE_LOW_MED_FILL = RGBColor(38, 66, 96)   # rgba(77, 171, 247, 0.15) approximation
ATTENTION_SCORE_LOW_MED_BORDER = RGBColor(77, 171, 247)
ATTENTION_SCORE_LOW_MED_COLOR = RGBColor(77, 171, 247)

# Very low scores (0.01): Gray
ATTENTION_SCORE_LOW_FILL = RGBColor(40, 42, 47)       # rgba(156, 163, 175, 0.1) approximation
ATTENTION_SCORE_LOW_BORDER = RGBColor(100, 103, 110)  # rgba(156, 163, 175, 0.3)
ATTENTION_SCORE_LOW_COLOR = RGBColor(156, 163, 175)

# Footnote
ATTENTION_FOOTNOTE_X = Inches(2)                  # Aligned with matrix
ATTENTION_FOOTNOTE_Y = Inches(8.1)                # Below matrix (adjusted for new spacing)
ATTENTION_FOOTNOTE_WIDTH = Inches(12)             # Same width as matrix
ATTENTION_FOOTNOTE_HEIGHT = Inches(0.4)
FONT_SIZE_ATTENTION_FOOTNOTE = Pt(14)             # 0.9rem
FONT_COLOR_ATTENTION_FOOTNOTE = RGBColor(209, 213, 219)
ATTENTION_FOOTNOTE_TEXT = "Relevance after Softmax normalization"

# Attention matrix data (6x6 grid)
ATTENTION_TOKENS = ["Wit", "nesses", "must", "tell", "nothing"]
ATTENTION_MATRIX_DATA = [
    [0.89, 0.07, 0.02, 0.01, 0.01],  # Wit
    [0.08, 0.85, 0.05, 0.01, 0.01],  # nesses
    [0.02, 0.03, 0.91, 0.02, 0.02],  # must
    [0.01, 0.02, 0.06, 0.87, 0.04],  # tell
    [0.01, 0.02, 0.05, 0.04, 0.88],  # nothing
]

# =============================================================================
# LAYOUT - NEXT WORD PREDICTION SLIDE (Slide 11)
# =============================================================================

# Title (using content header style)
PREDICTION_TITLE_X = Inches(1)
PREDICTION_TITLE_Y = Inches(1)
PREDICTION_TITLE_WIDTH = Inches(14)
PREDICTION_TITLE_HEIGHT = Inches(0.8)
FONT_SIZE_PREDICTION_TITLE = Pt(44)
FONT_FAMILY_PREDICTION_TITLE = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_PREDICTION_TITLE = COLOR_ACCENT_BLUE

# ALIGNED WITH SLIDES 8, 9, 10: Total width = 12", Start X = 2", End X = 14"
PREDICTION_CONTENT_X = Inches(2)
PREDICTION_CONTENT_WIDTH = Inches(12)
PREDICTION_CONTENT_RIGHT = Inches(14)                 # Right edge for all elements

# Context Vector Bar (top)
PREDICTION_VECTOR_Y = Inches(2.6)
PREDICTION_VECTOR_HEIGHT = Inches(1.15)         # 0.2 + 0.25 + 0.2 + 0.3 + 0.2 = 1.15"
PREDICTION_VECTOR_FILL_COLOR = COLOR_BACKGROUND_LIGHT
PREDICTION_VECTOR_BORDER_COLOR = COLOR_BORDER
PREDICTION_VECTOR_BORDER_WIDTH = Pt(1)

# Context Vector Label and Segments - EQUAL MARGINS ALL AROUND
PREDICTION_VECTOR_MARGIN = Inches(0.2)          # Equal margin on all sides (top, bottom, left, right)
PREDICTION_VECTOR_LABEL_HEIGHT = Inches(0.25)   # Label height
FONT_SIZE_PREDICTION_VECTOR_LABEL = Pt(14)      # 0.85rem uppercase
FONT_COLOR_PREDICTION_VECTOR_LABEL = COLOR_TEXT_GRAY

# Vector Segments (10 colored segments, evenly distributed)
PREDICTION_SEGMENT_HEIGHT = Inches(0.3)         # 22px
PREDICTION_SEGMENT_GAP = Inches(0.1)            # Gap between segments
PREDICTION_SEGMENT_COUNT = 10                   # Number of segments
PREDICTION_SEGMENT_COLORS = [
    COLOR_ACCENT_BLUE,      # #4dabf7
    COLOR_ACCENT_CYAN,      # #06b6d4
    COLOR_ACCENT_GREEN,     # #10b981
    COLOR_ACCENT_PURPLE,    # #8b5cf6
    RGBColor(245, 158, 11), # #f59e0b orange
    COLOR_ACCENT_RED,       # #ef4444
    COLOR_ACCENT_BLUE,      # repeat
    COLOR_ACCENT_CYAN,
    COLOR_ACCENT_GREEN,
    COLOR_ACCENT_PURPLE
]

# Temperature Thermometer Icon (left side, spans from but to no)
PREDICTION_THERMO_ICON = "assets/icons/thermometer.png"
PREDICTION_THERMO_X = Inches(2)                 # Left-aligned with Context Vector Box
# Height calculated dynamically: spans all 6 bars + 5 gaps
# = 6 * PREDICTION_PROB_BAR_HEIGHT + 5 * PREDICTION_PROB_GAP
PREDICTION_THERMO_HEIGHT = Inches(3.63)         # 6*0.48 + 5*0.15 = 2.88 + 0.75
# Y position = same as first bar (but)
PREDICTION_THERMO_Y = Inches(4.6)               # Same as PREDICTION_PROB_Y_START
# Width: Don't specify - let PowerPoint maintain aspect ratio

# Arrow down
PREDICTION_ARROW_Y = Inches(4.0)                # Adjusted for new vector box height (2.6 + 1.15 + 0.25)
PREDICTION_ARROW_TEXT = "↓"
FONT_SIZE_PREDICTION_ARROW = Pt(40)             # 2.5rem
FONT_COLOR_PREDICTION_ARROW = COLOR_ACCENT_BLUE

# Probability bars (RIGHT-ALIGNED at 14")
PREDICTION_PROB_Y_START = Inches(4.6)
PREDICTION_PROB_GAP = Inches(0.15)              # 10px gap
PREDICTION_PROB_BAR_HEIGHT = Inches(0.48)       # 36px
PREDICTION_PROB_BAR_WIDTH = Inches(8)           # Width for the bar
PREDICTION_PROB_BAR_X = Inches(6)               # Bar starts at 6", ends at 14" (right-aligned)
PREDICTION_PROB_LABEL_WIDTH = Inches(3.8)       # Width for token label (enough for "unless")
PREDICTION_PROB_LABEL_GAP = Inches(0.2)         # Gap between label and bar
PREDICTION_PROB_LABEL_X = Inches(2)             # Label starts at 2" (aligned with context vector box)

# Probability bar styling
PREDICTION_PROB_BAR_FILL_COLOR = COLOR_BACKGROUND_LIGHT
PREDICTION_PROB_BAR_BORDER_COLOR = COLOR_BORDER
PREDICTION_PROB_BAR_BORDER_WIDTH = Pt(1)

# Token label styling
FONT_SIZE_PREDICTION_TOKEN = Pt(18)             # 1.1rem
FONT_FAMILY_PREDICTION_TOKEN = FONT_FAMILY_INTER_REGULAR
FONT_COLOR_PREDICTION_TOKEN = COLOR_TEXT_GRAY

# Probability value styling
FONT_SIZE_PREDICTION_VALUE = Pt(16)
FONT_FAMILY_PREDICTION_VALUE = FONT_FAMILY_MONOSPACE
FONT_COLOR_PREDICTION_VALUE = COLOR_TEXT_WHITE

# Probability fill colors (gradients approximated as solid colors)
PREDICTION_FILL_HIGHEST = COLOR_ACCENT_GREEN    # Green for highest
PREDICTION_FILL_HIGH = COLOR_ACCENT_BLUE        # Blue for high
PREDICTION_FILL_MEDIUM = COLOR_ACCENT_PURPLE    # Purple for medium
PREDICTION_FILL_LOW = RGBColor(107, 114, 128)   # Gray for low/lowest

# Token color for highest
FONT_COLOR_PREDICTION_TOKEN_HIGHEST = COLOR_ACCENT_GREEN

# Prediction data (token, probability, category)
PREDICTION_DATA = [
    {"token": "but", "probability": 0.62, "category": "highest"},
    {"token": "to", "probability": 0.18, "category": "high"},
    {"token": "unless", "probability": 0.09, "category": "medium"},
    {"token": "about", "probability": 0.06, "category": "medium"},
    {"token": "when", "probability": 0.03, "category": "low"},
    {"token": "no", "probability": 0.02, "category": "lowest"}
]

# =============================================================================
# LAYOUT - AUTOREGRESSION SLIDES (Slides 12-15, one per step)
# =============================================================================

# Title
AUTOREGRESS_TITLE_X = Inches(2.5)
AUTOREGRESS_TITLE_Y = Inches(1.2)
AUTOREGRESS_TITLE_WIDTH = Inches(11)
AUTOREGRESS_TITLE_HEIGHT = Inches(0.8)
FONT_SIZE_AUTOREGRESS_TITLE = Pt(44)
FONT_FAMILY_AUTOREGRESS_TITLE = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_AUTOREGRESS_TITLE = COLOR_ACCENT_BLUE

# Subtitle (e.g., "Step 1: Original Input")
AUTOREGRESS_SUBTITLE_X = Inches(2.5)
AUTOREGRESS_SUBTITLE_Y = Inches(2.1)
AUTOREGRESS_SUBTITLE_WIDTH = Inches(11)
AUTOREGRESS_SUBTITLE_HEIGHT = Inches(0.4)
FONT_SIZE_AUTOREGRESS_SUBTITLE = Pt(18)
FONT_FAMILY_AUTOREGRESS_SUBTITLE = FONT_FAMILY_INTER_REGULAR
FONT_COLOR_AUTOREGRESS_SUBTITLE = COLOR_ACCENT_BLUE

# Token row (horizontally centered on slide)
AUTOREGRESS_TOKEN_Y = Inches(3.5)                 # Vertically centered
AUTOREGRESS_TOKEN_WIDTH = Inches(1.3)             # Width per token
AUTOREGRESS_TOKEN_HEIGHT = Inches(0.6)
AUTOREGRESS_TOKEN_GAP = Inches(0.15)              # Gap between tokens
AUTOREGRESS_TOKEN_FILL_COLOR = RGBColor(31, 41, 55)
AUTOREGRESS_TOKEN_BORDER_COLOR = RGBColor(77, 171, 247)
AUTOREGRESS_TOKEN_BORDER_WIDTH = Pt(1.5)
FONT_SIZE_AUTOREGRESS_TOKEN = Pt(20)
FONT_FAMILY_AUTOREGRESS_TOKEN = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_AUTOREGRESS_TOKEN = COLOR_TEXT_WHITE

# New token styling (green)
AUTOREGRESS_TOKEN_NEW_FILL = RGBColor(16, 185, 129)
AUTOREGRESS_TOKEN_NEW_BORDER = COLOR_ACCENT_GREEN
FONT_COLOR_AUTOREGRESS_TOKEN_NEW = COLOR_ACCENT_GREEN

# LLM Arrow (horizontal: → LLM →)
AUTOREGRESS_LLM_ARROW = "→ LLM →"
AUTOREGRESS_LLM_ARROW_WIDTH = Inches(1.8)         # Width for LLM arrow box
AUTOREGRESS_LLM_ARROW_GAP = Inches(0.3)           # Gap before/after arrow
FONT_SIZE_AUTOREGRESS_LLM_ARROW = Pt(32)
FONT_COLOR_AUTOREGRESS_LLM_ARROW = COLOR_ACCENT_BLUE

# Completion message (Slide 15 only)
AUTOREGRESS_COMPLETION_Y = Inches(5.5)
FONT_SIZE_AUTOREGRESS_COMPLETION = Pt(16)
FONT_FAMILY_AUTOREGRESS_COMPLETION = FONT_FAMILY_INTER_REGULAR
FONT_COLOR_AUTOREGRESS_COMPLETION = COLOR_ACCENT_GREEN

# Data for each slide
AUTOREGRESS_STEP_1 = {
    "title": "Autoregression",
    "subtitle": "Step 1: Original Input",
    "tokens": ["Wit", "nesses", "must", "tell", "nothing"],
    "new_token_index": None,
    "predicted": "but"
}

AUTOREGRESS_STEP_2 = {
    "title": "Autoregression",
    "subtitle": "Step 2: Extended Input",
    "tokens": ["Wit", "nesses", "must", "tell", "nothing", "but"],
    "new_token_index": 5,  # "but" is new
    "predicted": "the"
}

AUTOREGRESS_STEP_3 = {
    "title": "Autoregression",
    "subtitle": "Step 3: Extended Again",
    "tokens": ["Wit", "nesses", "must", "tell", "nothing", "but", "the"],
    "new_token_index": 6,  # "the" is new
    "predicted": "truth"
}

AUTOREGRESS_STEP_FINAL = {
    "title": "Autoregression",
    "subtitle": "Complete Sentence",
    "tokens": ["Wit", "nesses", "must", "tell", "nothing", "but", "the", "truth"],
    "new_token_index": 7,  # "truth" is new
    "predicted": None  # No prediction on final slide
}

# =============================================================================
# SLIDE 17 - SECURITY CONFLICT COMPARISON
# =============================================================================

# Title
SECURITY_TITLE_X = Inches(1)
SECURITY_TITLE_Y = Inches(1.2)
SECURITY_TITLE_WIDTH = Inches(14)
SECURITY_TITLE_HEIGHT = Inches(0.8)
FONT_SIZE_SECURITY_TITLE = Pt(44)
FONT_FAMILY_SECURITY_TITLE = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_SECURITY_TITLE = COLOR_ACCENT_BLUE

# Two-column layout (card containers)
SECURITY_CARD_WIDTH = Inches(6.5)
SECURITY_CARD_HEIGHT = Inches(5.5)
SECURITY_CARD_GAP = Inches(0.5)
SECURITY_CARD_Y = Inches(2.5)
SECURITY_CARD_LEFT_X = Inches(1)
SECURITY_CARD_RIGHT_X = Inches(8.5)

# Card styling
SECURITY_CARD_BORDER_WIDTH = Pt(2)
SECURITY_CARD_FILL_COLOR = RGBColor(31, 41, 55)  # Slightly lighter than background

# Column titles (inside cards)
SECURITY_COL_TITLE_Y_OFFSET = 0.3  # From top of card
FONT_SIZE_SECURITY_COL_TITLE = Pt(26)
FONT_FAMILY_SECURITY_COL_TITLE = FONT_FAMILY_INTER_REGULAR
SECURITY_COL_TITLE_HEIGHT = Inches(0.5)

# Icon placeholder area
SECURITY_ICON_Y_OFFSET = 1.0  # From top of card
SECURITY_ICON_HEIGHT = Inches(1.2)

# Flow steps (3 per column, inside cards)
SECURITY_STEP_HEIGHT = Inches(0.6)
SECURITY_STEP_GAP = Inches(0.25)
SECURITY_STEP_Y_START_OFFSET = 2.5  # From top of card
SECURITY_STEP_X_OFFSET = 0.4  # From left edge of card
FONT_SIZE_SECURITY_STEP_NUMBER = Pt(20)
FONT_SIZE_SECURITY_STEP_TEXT = Pt(15)
FONT_FAMILY_SECURITY_STEP = FONT_FAMILY_INTER_REGULAR

# Colors
COLOR_SECURITY_CLOUD = RGBColor(239, 68, 68)  # Red #ef4444
COLOR_SECURITY_LOCAL = COLOR_ACCENT_GREEN      # Green #10b981

# Icons
SECURITY_CLOUD_ICON = "assets/icons/cloud_server.png"
SECURITY_LOCAL_ICON = "assets/icons/local_server.png"
SECURITY_ICON_WIDTH = Inches(2)

# Data
SECURITY_CLOUD_STEPS = [
    "Data leaves your premises",
    "Decrypted on external GPUs",
    "Results returned to you"
]

SECURITY_LOCAL_STEPS = [
    "Data stays in your building",
    "Processed on your hardware",
    "Remains within your control"
]

# =============================================================================
# SLIDE 18 - THE ENCRYPTION DILEMMA
# =============================================================================

# Title
ENCRYPTION_TITLE_X = Inches(1)
ENCRYPTION_TITLE_Y = Inches(0.8)
ENCRYPTION_TITLE_WIDTH = Inches(14)
ENCRYPTION_TITLE_HEIGHT = Inches(0.6)
FONT_SIZE_ENCRYPTION_TITLE = Pt(48)
FONT_FAMILY_ENCRYPTION_TITLE = FONT_FAMILY_INTER_EXTRALIGHT
FONT_COLOR_ENCRYPTION_TITLE = COLOR_ACCENT_BLUE

# Subtitle
ENCRYPTION_SUBTITLE_Y = Inches(1.5)
FONT_SIZE_ENCRYPTION_SUBTITLE = Pt(16)
FONT_COLOR_ENCRYPTION_SUBTITLE = COLOR_TEXT_GRAY

# Stage Cards Layout (smaller cards, better spacing)
ENCRYPTION_CARD_WIDTH = Inches(5.3)
ENCRYPTION_CARD_HEIGHT = Inches(3.2)
ENCRYPTION_CARD_BORDER_WIDTH = Pt(1.5)
ENCRYPTION_CARD_FILL_COLOR = RGBColor(31, 41, 55)

# Bottom row (Steps 1 & 2) - more space between cards
ENCRYPTION_BOTTOM_Y = Inches(5.3)
ENCRYPTION_LEFT_X = Inches(0.8)
ENCRYPTION_RIGHT_X = Inches(9.9)

# Top center (Step 3) - smaller and centered
ENCRYPTION_TOP_Y = Inches(2.2)
ENCRYPTION_TOP_X = Inches(5.35)  # Centered (16 - 5.3) / 2
ENCRYPTION_TOP_CARD_WIDTH = Inches(5.3)
ENCRYPTION_TOP_CARD_HEIGHT = Inches(2.6)

# Step number (outside cards, blue circles)
ENCRYPTION_STEP_NUMBER_SIZE = Inches(0.65)
ENCRYPTION_STEP_NUMBER_Y_OFFSET_OUTSIDE = -0.8  # Above card
ENCRYPTION_STEP_NUMBER_X_CENTER_OFFSET = 2.325  # Center of card (5.3 / 2 - 0.65 / 2)
FONT_SIZE_ENCRYPTION_STEP_NUMBER = Pt(22)
COLOR_ENCRYPTION_STEP_NUMBER_BG = COLOR_ACCENT_BLUE
COLOR_ENCRYPTION_STEP_NUMBER_TEXT = COLOR_TEXT_WHITE

# Stage header inside card
ENCRYPTION_STAGE_TITLE_Y_OFFSET = 0.15
ENCRYPTION_STAGE_TITLE_X_OFFSET = 0.4
FONT_SIZE_ENCRYPTION_STAGE_TITLE = Pt(18)
FONT_FAMILY_ENCRYPTION_STAGE_TITLE = FONT_FAMILY_INTER_REGULAR

# Icon area
ENCRYPTION_ICON_WIDTH = Inches(1.2)
ENCRYPTION_ICON_Y_OFFSET = 0.15  # Same as title, placed at right side

# Data blocks with background (styled boxes)
ENCRYPTION_DATA_Y_OFFSET = 0.9
ENCRYPTION_DATA_BLOCK_WIDTH = Inches(1.5)
ENCRYPTION_DATA_BLOCK_HEIGHT = Inches(0.4)
ENCRYPTION_DATA_BLOCK_GAP_X = Inches(0.2)
ENCRYPTION_DATA_BLOCK_GAP_Y = Inches(0.15)
ENCRYPTION_DATA_START_X_OFFSET = 0.4
ENCRYPTION_DATA_BLOCK_BORDER_WIDTH = Pt(1)
ENCRYPTION_DATA_BLOCK_FILL_ALPHA = 0.1  # Subtle background
FONT_SIZE_ENCRYPTION_DATA = Pt(12)

# Stage description at bottom
ENCRYPTION_DESC_Y_OFFSET = 2.7  # From top of card
FONT_SIZE_ENCRYPTION_DESC = Pt(12)

# Processing text (for Step 3)
ENCRYPTION_PROCESSING_Y_OFFSET = 1.3
FONT_SIZE_ENCRYPTION_PROCESSING = Pt(24)

# Colors
COLOR_ENCRYPTION_ENCRYPTED = RGBColor(239, 68, 68)  # Red #ef4444
COLOR_ENCRYPTION_DECRYPTED = RGBColor(251, 191, 36)  # Yellow/Amber #fbbf24
COLOR_ENCRYPTION_INFERENCE = COLOR_ACCENT_GREEN      # Green #10b981

# Icons
ENCRYPTION_LOCK_ICON = "assets/icons/encryption_lock.png"
ENCRYPTION_UNLOCK_ICON = "assets/icons/encryption_unlock.png"
ENCRYPTION_CLOUD_ICON = "assets/icons/cloud_server.png"  # Reuse from Slide 17

# Data
ENCRYPTION_ENCRYPTED_BLOCKS = ["♦7k9mR2p", "nQ4▲B1zL", "wE8†Y3sM", "fG2hJ6◈N", "aM9▼R4pL", "vN3s✤8wK"]
ENCRYPTION_DECRYPTED_BLOCKS = ["Witnesses", "must", "tell", "nothing,", "but", "the"]

# =============================================================================
# LAYOUT - PLACEHOLDER SLIDES
# =============================================================================

PLACEHOLDER_X = Inches(2)
PLACEHOLDER_Y = Inches(3.5)
PLACEHOLDER_WIDTH = Inches(12)
PLACEHOLDER_HEIGHT = Inches(2)

# =============================================================================
# SAFE ZONES & MARGINS
# =============================================================================

MARGIN_TOP = Inches(1)       # Below logo/slide number
MARGIN_SIDES = Inches(1)     # Left/right margins
MARGIN_BOTTOM = Inches(0.5)  # Bottom margin

# =============================================================================
# HELPER DATA STRUCTURES
# =============================================================================

# Keyword Themes Dictionary (for easy access)
KEYWORD_THEMES = {
    "problem": KEYWORD_THEME_PROBLEM,
    "solution": KEYWORD_THEME_SOLUTION,
    "tech": KEYWORD_THEME_TECH
}

# Slide Layout Types
LAYOUT_TYPE_KEYWORD = "keyword"
LAYOUT_TYPE_CONTENT = "content"
LAYOUT_TYPE_BLANK = "blank"
