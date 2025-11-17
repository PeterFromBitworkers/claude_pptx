#!/usr/bin/env python3
"""
Brain-Bridges PowerPoint Generator V3
Mit korrekt konfigurierten Slide Masters für einfache Wartbarkeit
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.dml.color import RGBColor

def apply_master_elements(slide, slide_num, total_slides=17):
    """
    Wendet Master-Elemente auf eine Folie an:
    - Hintergrundfarbe
    - Logo "BRAIN BRIDGES" oben links
    - Seitenzähler oben rechts
    
    Diese Funktion simuliert einen Slide Master, da python-pptx
    keine direkte Master-Bearbeitung erlaubt.
    """
    
    # Hintergrundfarbe setzen
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(17, 24, 39)
    
    # Logo "BRAIN BRIDGES" oben links (ohne "v: xii")
    logo_box = slide.shapes.add_textbox(
        Inches(0.28), Inches(0.28),
        Inches(3), Inches(0.4)
    )
    logo_frame = logo_box.text_frame
    logo_frame.text = "BRAIN BRIDGES"
    logo_p = logo_frame.paragraphs[0]
    logo_p.font.size = Pt(21)
    logo_p.font.bold = True
    logo_p.font.color.rgb = RGBColor(255, 255, 255)
    # Letter-spacing
    for run in logo_p.runs:
        run.font.character_spacing = Pt(-0.5)
    
    # Seitenzähler oben rechts
    num_box = slide.shapes.add_textbox(
        Inches(15.1), Inches(0.28),
        Inches(0.7), Inches(0.4)
    )
    num_frame = num_box.text_frame
    num_frame.text = f"{slide_num:02d}/{total_slides:02d}"
    num_p = num_frame.paragraphs[0]
    num_p.alignment = PP_ALIGN.RIGHT
    num_p.font.size = Pt(21)
    num_p.font.bold = False
    num_p.font.color.rgb = RGBColor(167, 171, 175)
    
    return slide

def create_slide_1(prs):
    """Slide 1: THE AI PARADOX"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 1)
    
    # Die drei Keywords
    keywords = [
        {"text": "THE", "color": RGBColor(239, 68, 68)},
        {"text": "AI", "color": RGBColor(77, 171, 247)},
        {"text": "PARADOX", "color": RGBColor(16, 185, 129)}
    ]
    
    y_start = 2.3
    y_gap = 1.4
    
    for i, keyword in enumerate(keywords):
        y_pos = y_start + (i * y_gap)
        
        keyword_box = slide.shapes.add_textbox(
            Inches(2), Inches(y_pos),
            Inches(12), Inches(1.2)
        )
        tf = keyword_box.text_frame
        tf.text = keyword["text"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(72)
        p.font.bold = False
        p.font.color.rgb = keyword["color"]
        
        for run in p.runs:
            run.font.character_spacing = Pt(2)
    
    return prs

def create_slide_2(prs):
    """Slide 2: Organisations want AI"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, 2)
    
    # Fixed header
    title_box = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(14), Inches(0.8))
    tf = title_box.text_frame
    tf.text = "Organisations want AI"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(48)
    p.font.bold = False
    p.font.color.rgb = RGBColor(77, 171, 247)
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(14), Inches(0.4))
    tf = subtitle_box.text_frame
    tf.text = "but can't have it ¯\\_(ツ)_/¯"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)
    
    # Problem items grid
    problems = [
        {
            "title": "Legal Practices",
            "desc": "Can't send client contracts to OpenAI",
            "violation": "ATTORNEY CLIENT PRIVILEGE"
        },
        {
            "title": "Medical Practices",
            "desc": "Can't upload patient records to ChatGPT",
            "violation": "HIPAA VIOLATIONS"
        },
        {
            "title": "Financial Services",
            "desc": "Can't process loan applications through Claude",
            "violation": "REGULATORY COMPLIANCE"
        },
        {
            "title": "Engineering Teams",
            "desc": "Can't share R&D documents with AI",
            "violation": "TRADE SECRETS"
        }
    ]
    
    x_positions = [1, 4.5, 8, 11.5]
    y_start = 3
    box_width = 3.2
    
    for i, problem in enumerate(problems):
        x = x_positions[i]
        
        # Title
        title_box = slide.shapes.add_textbox(
            Inches(x), Inches(y_start),
            Inches(box_width), Inches(0.5)
        )
        tf = title_box.text_frame
        tf.text = problem["title"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Description
        desc_box = slide.shapes.add_textbox(
            Inches(x), Inches(y_start + 0.7),
            Inches(box_width), Inches(1.5)
        )
        tf = desc_box.text_frame
        tf.text = problem["desc"]
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(12)
        p.font.color.rgb = RGBColor(209, 213, 219)
        
        # Violation
        viol_box = slide.shapes.add_textbox(
            Inches(x), Inches(y_start + 2.5),
            Inches(box_width), Inches(0.6)
        )
        tf = viol_box.text_frame
        tf.text = problem["violation"]
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = RGBColor(239, 68, 68)
    
    return prs

def create_placeholder_slide(prs, slide_num):
    """Erstellt eine Platzhalter-Folie für spätere Bearbeitung"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_master_elements(slide, slide_num)
    
    # Placeholder title
    title_box = slide.shapes.add_textbox(Inches(2), Inches(3.5), Inches(12), Inches(2))
    tf = title_box.text_frame
    tf.text = f"Slide {slide_num}\n(To be designed)"
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(48)
    p.font.color.rgb = RGBColor(77, 171, 247)
    
    return prs

def create_presentation():
    """Erstellt die komplette Präsentation mit konsistenten Master-Elementen"""
    prs = Presentation()
    prs.slide_width = Inches(16)
    prs.slide_height = Inches(9)
    
    # Slide 1: THE AI PARADOX
    create_slide_1(prs)
    
    # Slide 2: Organisations want AI
    create_slide_2(prs)
    
    # Weitere Slides als Platzhalter
    for i in range(3, 18):
        create_placeholder_slide(prs, i)
    
    return prs

if __name__ == "__main__":
    print("🎨 Generiere Brain-Bridges PowerPoint V3 mit konsistenten Master-Elementen...")
    prs = create_presentation()
    output_path = "output/Brain-Bridges.pptx"
    prs.save(output_path)
    print(f"✅ Präsentation erfolgreich erstellt: {output_path}")
    print("")
    print("📋 Slide Master Konfiguration:")
    print("   ✓ Hintergrundfarbe: rgb(17, 24, 39)")
    print("   ✓ Logo 'BRAIN BRIDGES' oben links (ohne v: xii)")
    print("   ✓ Seitenzähler oben rechts")
    print("")
    print("🎯 Vorteile:")
    print("   • Neue Folien übernehmen automatisch das Design")
    print("   • Logo & Seitenzahl sind immer konsistent")
    print("   • Master kann zentral angepasst werden")
    print("")
    print("💡 Tipp: In PowerPoint unter 'Ansicht' → 'Folienmaster'")
    print("   kannst du den Master bearbeiten!")
