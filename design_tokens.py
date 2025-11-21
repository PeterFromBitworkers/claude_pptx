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
TOKENIZATION_TOKENS_Y = Inches(5.2)
TOKENIZATION_TOKEN_HEIGHT = Inches(0.9)
TOKENIZATION_TOKEN_GAP = Inches(0.35)             # Gap between tokens
# Calculate x positions for 5 tokens centered
# Each token width varies, but we'll use consistent width
TOKENIZATION_TOKEN_WIDTH = Inches(2.3)
# Total width needed: 5 * 2.3 + 4 * 0.35 = 11.5 + 1.4 = 12.9
# Center: (16 - 12.9) / 2 = 1.55
TOKENIZATION_TOKEN_X_START = Inches(1.55)         # In inches (converted to Inches object)

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
TOKEN_ROW_Y_START = 2.3                           # In inches - start position
TOKEN_ROW_GAP = 1.1                               # In inches - gap between rows
TOKEN_ROW_HEIGHT = 0.75                           # In inches - height per row

# Token Box (left side)
TOKEN_BOX_X = Inches(2.2)
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
ARROW_X = Inches(5.0)
ARROW_WIDTH = Inches(0.6)
ARROW_TEXT = "→"
FONT_SIZE_ARROW = Pt(36)
FONT_COLOR_ARROW = COLOR_ACCENT_BLUE

# Vector Grid (right side, 6 cells per row)
VECTOR_GRID_X = Inches(5.9)
VECTOR_GRID_WIDTH = Inches(8.1)                   # Total width for 6 cells
VECTOR_GRID_FILL_COLOR = RGBColor(17, 24, 39)    # Background color (darker)
VECTOR_GRID_BORDER_COLOR = RGBColor(77, 171, 247)  # Accent blue border
VECTOR_GRID_BORDER_WIDTH = Pt(1)

# Vector Cell (individual number boxes)
VECTOR_CELL_WIDTH = Inches(1.2)                   # Width per cell
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
