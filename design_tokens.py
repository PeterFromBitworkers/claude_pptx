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
FONT_SIZE_CONTENT_TITLE = Pt(48)
FONT_BOLD_CONTENT_TITLE = False
FONT_COLOR_CONTENT_TITLE = COLOR_ACCENT_BLUE

# Content Slide - Subtitle
FONT_SIZE_CONTENT_SUBTITLE = Pt(20)
FONT_BOLD_CONTENT_SUBTITLE = True
FONT_COLOR_CONTENT_SUBTITLE_ALERT = COLOR_ACCENT_RED
FONT_COLOR_CONTENT_SUBTITLE_NORMAL = COLOR_TEXT_GRAY

# Problem Grid - Title
FONT_SIZE_PROBLEM_TITLE = Pt(16)
FONT_BOLD_PROBLEM_TITLE = True
FONT_COLOR_PROBLEM_TITLE = COLOR_TEXT_WHITE

# Problem Grid - Description
FONT_SIZE_PROBLEM_DESC = Pt(12)
FONT_BOLD_PROBLEM_DESC = False
FONT_COLOR_PROBLEM_DESC = COLOR_TEXT_GRAY

# Problem Grid - Violation
FONT_SIZE_PROBLEM_VIOLATION = Pt(9)
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
KEYWORD_Y_START = 2.3  # Inches (float for calculation)
KEYWORD_Y_GAP = 1.4    # Inches (float for calculation)

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

PROBLEM_GRID_X_POSITIONS = [1, 4.5, 8, 11.5]  # In inches
PROBLEM_GRID_Y_START = 3                      # In inches
PROBLEM_GRID_BOX_WIDTH = 3.2                  # In inches

# Problem Grid Item Layout
PROBLEM_TITLE_Y_OFFSET = 0                    # From y_start
PROBLEM_TITLE_HEIGHT = 0.5

PROBLEM_DESC_Y_OFFSET = 0.7                   # From y_start
PROBLEM_DESC_HEIGHT = 1.5

PROBLEM_VIOLATION_Y_OFFSET = 2.5              # From y_start
PROBLEM_VIOLATION_HEIGHT = 0.6

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
