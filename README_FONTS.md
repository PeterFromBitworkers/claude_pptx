# PowerPoint Font Management Guide

> **Wichtige Erkenntnisse aus der Entwicklung**
> Dokumentiert: 2025-11-18

---

## 🎯 Zusammenfassung

PowerPoint-Präsentationen können auf verschiedenen Systemen **unterschiedlich aussehen**, wenn die verwendeten Schriftarten nicht überall installiert sind. Dieses Dokument erklärt:

1. Welche Schriftarten PowerPoint kennt
2. System-Unterschiede und Fallback-Mechanismen
3. Font-Embedding als Lösung
4. Spezielle Probleme mit Custom Fonts (z.B. Inter)

---

## 📚 Grundlagen: Schriftarten in PowerPoint

### System-Schriftarten (Standard)

PowerPoint kennt **standardmäßig nur die auf dem System installierten Schriftarten**:

**Windows Standard-Fonts:**
- Arial, Calibri, Times New Roman, Verdana, Tahoma
- Segoe UI (Windows Vista+)
- Georgia, Trebuchet MS, Comic Sans MS

**macOS Standard-Fonts:**
- Helvetica, Helvetica Neue
- Arial, Times New Roman, Courier
- San Francisco (macOS 10.11+)
- Menlo (monospace)

**Cross-Platform (auf beiden Systemen):**
- Arial
- Times New Roman
- Courier New
- Georgia
- Verdana

### Custom Fonts

**Custom Fonts** (wie Inter, Roboto, Montserrat, etc.) müssen:
1. **Auf dem System installiert** sein ODER
2. **In der PowerPoint-Datei embedded** sein

---

## ⚠️ Das Problem: System-Unterschiede

### Szenario 1: Ohne Font-Embedding

```
macOS (mit Inter installiert)           Windows (ohne Inter)
┌─────────────────────────┐            ┌─────────────────────────┐
│ BRAIN-BRIDGES           │            │ BRAIN-BRIDGES           │
│ (Inter ExtraBold)       │     →      │ (Arial - Fallback!)     │
│ ✅ Sieht gut aus        │            │ ❌ Sieht anders aus     │
└─────────────────────────┘            └─────────────────────────┘
```

**Problem:**
- PowerPoint findet "Inter" nicht auf Windows
- Verwendet automatisch Fallback-Font (meist Arial oder Calibri)
- Design ist **komplett anders**

### Szenario 2: Mit Font-Embedding

```
macOS (mit Inter installiert)           Windows (ohne Inter)
┌─────────────────────────┐            ┌─────────────────────────┐
│ BRAIN-BRIDGES           │            │ BRAIN-BRIDGES           │
│ (Inter ExtraBold)       │     →      │ (Inter ExtraBold)       │
│ ✅ Sieht gut aus        │            │ ✅ Sieht identisch aus! │
└─────────────────────────┘            └─────────────────────────┘
```

**Lösung:** Font ist in der .pptx-Datei eingebettet!

---

## 💾 Font-Embedding: Die Lösung

### Was ist Font-Embedding?

Font-Embedding bedeutet, dass die **Font-Dateien direkt in die PowerPoint-Datei (.pptx)** integriert werden. Die Präsentation enthält dann alle benötigten Schriftarten und sieht auf **jedem System identisch** aus.

### Vorteile

✅ **Konsistenz:** Präsentation sieht überall gleich aus
✅ **Unabhängigkeit:** Keine Installation auf Zielsystem nötig
✅ **Professionell:** Design bleibt wie beabsichtigt

### Nachteile

⚠️ **Dateigröße:** .pptx wird größer (pro Font ~400KB-2MB)
⚠️ **Lizenz:** Nur bei Fonts mit Embedding-Lizenz erlaubt
⚠️ **Einmal-Setup:** Muss bei jeder neuen PowerPoint aktiviert werden

### Dateigröße-Beispiel

```
Ohne Embedding:  Brain-Bridges.pptx = 2.3 MB
Mit Embedding:   Brain-Bridges.pptx = 5.8 MB (+3.5 MB für 6 Inter-Fonts)
```

Für unsere Präsentation ist die Dateigröße **nicht relevant** - Konsistenz ist wichtiger!

---

## 🔧 Font-Embedding aktivieren (macOS)

### Manuelle Methode (PowerPoint Einstellungen)

**Einmalig pro PowerPoint-Datei:**

1. **PowerPoint öffnen** → Präsentation öffnen
2. **PowerPoint** → **Preferences** (Command+,)
3. **Save** (Speichern) wählen
4. **"Embed fonts in the file"** aktivieren ✅
5. Option wählen:
   - **"Embed only the characters used in the presentation"** (kleiner)
   - **"Embed all characters"** (empfohlen für Editing)
6. **OK** → Datei speichern

**Screenshot-Position:**
```
PowerPoint → Preferences
    ├── General
    ├── View
    ├── Edit
    ├── Save ← HIER
    │   ├── AutoRecover
    │   ├── Font embedding
    │   │   └── ☑ Embed fonts in the file
    │   │       ├── ○ Embed only characters used
    │   │       └── ⦿ Embed all characters (recommended)
    └── ...
```

### Automatisierung (für Entwickler)

⚠️ **WICHTIG:** python-pptx unterstützt **KEIN automatisches Font-Embedding**!

**Workaround:**
1. PowerPoint mit python-pptx generieren
2. Datei öffnen in PowerPoint (macOS/Windows)
3. Manually: Preferences → Save → Embed fonts aktivieren
4. Datei speichern

**Alternativ:** PowerPoint-Template (.potx) mit Embedding erstellen und als Basis verwenden.

---

## 🎨 Inter Font: Spezialfall

### Problem: Variable Fonts vs. Static Fonts

Die Inter Font-Familie kommt in **zwei Varianten**:

#### 1. Variable Fonts (❌ NICHT kompatibel mit PowerPoint)

```
Inter-4.0/
├── InterVariable.ttf         ← Variable Font (1 Datei, alle Weights)
└── InterVariable-Italic.ttf  ← Variable Font Italic
```

**Struktur:**
- **Eine Datei** enthält alle Font-Weights (100-900)
- CSS: `font-weight: 100` bis `font-weight: 900`
- Funktioniert in: Modernen Browsern, Adobe Apps

**PowerPoint-Problem:**
- PowerPoint erkennt nur **"Inter"** als Familie
- Ignoriert Weight-Varianten (ExtraBold, Light, etc.)
- Alles sieht **gleich** aus!

#### 2. Static Fonts (✅ Kompatibel mit PowerPoint)

```
Inter-4.0/extras/ttf/
├── Inter-Thin.ttf            ← font-weight: 100
├── Inter-ExtraLight.ttf      ← font-weight: 200
├── Inter-Light.ttf           ← font-weight: 300
├── Inter-Regular.ttf         ← font-weight: 400
├── Inter-Medium.ttf          ← font-weight: 500
├── Inter-SemiBold.ttf        ← font-weight: 600
├── Inter-Bold.ttf            ← font-weight: 700
├── Inter-ExtraBold.ttf       ← font-weight: 800
└── Inter-Black.ttf           ← font-weight: 900
```

**Struktur:**
- **Separate Datei** für jedes Font-Weight
- Jedes Weight ist eine eigene "Familie"

**PowerPoint-Verwendung:**
- Font-Name: `"Inter ExtraBold"`, `"Inter Light"`, etc.
- Jedes Weight wird korrekt erkannt!

### ⚠️ KRITISCH: Nur Static Fonts installieren!

**FALSCH (verursacht Probleme):**
```bash
# Installiert Variable Fonts
~/Library/Fonts/
├── InterVariable.ttf         ← ❌ Überschreibt Static Fonts!
└── InterVariable-Italic.ttf
```

**RICHTIG:**
```bash
# NUR Static Fonts installieren
~/Library/Fonts/
├── Inter-ExtraBold.ttf       ✅
├── Inter-Bold.ttf            ✅
├── Inter-SemiBold.ttf        ✅
├── Inter-Medium.ttf          ✅
├── Inter-Light.ttf           ✅
└── Inter-ExtraLight.ttf      ✅
```

**Falls Variable Fonts installiert sind:**
```bash
# Löschen!
rm ~/Library/Fonts/InterVariable.ttf
rm ~/Library/Fonts/InterVariable-Italic.ttf
```

---

## 🔍 Debugging: Font-Probleme erkennen

### Problem: "Alle Schriftarten sehen gleich aus"

**Ursachen:**
1. ❌ Variable Fonts installiert (statt Static Fonts)
2. ❌ Font-Name falsch geschrieben
3. ❌ Font nicht im System installiert
4. ❌ PowerPoint-Cache nicht aktualisiert

**Lösung:**
```bash
# 1. Prüfen welche Fonts installiert sind
ls -la ~/Library/Fonts/ | grep Inter

# 2. Variable Fonts löschen
rm ~/Library/Fonts/InterVariable*.ttf

# 3. PowerPoint KOMPLETT beenden (Command+Q)
# 4. 5 Sekunden warten
# 5. PowerPoint neu starten
```

### Tool: Font-Namen extrahieren

Wir haben ein Tool erstellt um PostScript-Namen zu extrahieren:

```bash
python3 check_inter_fonts.py
```

**Output:**
```
📄 Inter-ExtraBold.ttf
   Familie:     Inter ExtraBold
   Stil:        Regular
   Voller Name: Inter ExtraBold
   ✨ PostScript: Inter-ExtraBold
```

**Für PowerPoint verwenden:**
- ✅ **Familie-Name (mit Leerzeichen):** `"Inter ExtraBold"`
- ❌ **PostScript-Name (mit Bindestrich):** `"Inter-ExtraBold"` (wird ignoriert)

---

## 📝 Best Practices

### 1. Font-Auswahl

**Für Cross-Platform Präsentationen:**
- ✅ Verwende System-Fonts (Arial, Calibri, etc.)
- ✅ ODER: Aktiviere Font-Embedding

**Für Custom Fonts:**
- ✅ Installiere STATIC Fonts (nicht Variable Fonts)
- ✅ Teste auf Ziel-System oder aktiviere Embedding
- ✅ Dokumentiere benötigte Fonts

### 2. Font-Installation (macOS)

**Richtige Reihenfolge:**
1. Static Fonts herunterladen (z.B. Inter extras/ttf/)
2. Prüfen ob Variable Fonts installiert sind → Löschen!
3. Static Fonts installieren (Doppelklick → Install)
4. Font Book öffnen → Prüfen welche installiert sind
5. PowerPoint neu starten

### 3. Font-Embedding Workflow

**Für Entwickler (python-pptx):**
1. PowerPoint mit Script generieren
2. Datei in PowerPoint öffnen
3. Preferences → Save → "Embed fonts" aktivieren
4. Datei speichern
5. Fertig! Datei kann verteilt werden

**Für Designer:**
1. Template erstellen mit Embedding aktiviert
2. Template als .potx speichern
3. Neue Präsentationen basieren auf Template
4. Embedding ist automatisch aktiv

---

## 🎓 Hintergrund: Font-Struktur

### Standard Font-Familien (wie Arial)

```
Arial Familie:
├── Arial Regular      (Familie: "Arial", Stil: "Regular")
├── Arial Bold         (Familie: "Arial", Stil: "Bold")
├── Arial Italic       (Familie: "Arial", Stil: "Italic")
└── Arial Bold Italic  (Familie: "Arial", Stil: "Bold Italic")
```

**PowerPoint-Verwendung:**
```python
run.font.name = "Arial"
run.font.bold = True      # Verwendet "Arial Bold"
run.font.italic = True    # Verwendet "Arial Italic"
```

### Inter Font-Familien (ungewöhnlich)

```
Inter Static Fonts:
├── Inter ExtraBold  (Familie: "Inter ExtraBold", Stil: "Regular")
├── Inter Bold       (Familie: "Inter Bold", Stil: "Regular")
├── Inter SemiBold   (Familie: "Inter SemiBold", Stil: "Regular")
├── Inter Medium     (Familie: "Inter Medium", Stil: "Regular")
├── Inter Light      (Familie: "Inter Light", Stil: "Regular")
└── Inter ExtraLight (Familie: "Inter ExtraLight", Stil: "Regular")
```

**PowerPoint-Verwendung:**
```python
run.font.name = "Inter ExtraBold"  # Familie-Name mit Leerzeichen!
run.font.bold = False              # NICHT bold, Weight ist im Font selbst
```

---

## 📊 Font-Mapping: HTML → PowerPoint

Für unser Brain-Bridges Projekt:

| Element | HTML (CSS) | PowerPoint (python-pptx) |
|---------|-----------|--------------------------|
| BRAIN-BRIDGES Titel | `font-weight: 800` | `font.name = "Inter ExtraBold"` |
| Feature-Liste | `font-weight: 300` | `font.name = "Inter Light"` |
| Subtitle (monospace) | `font-family: Menlo` | `font.name = "Menlo"` |
| Status Badge | `font-weight: 500` | `font.name = "Inter Medium"` |
| Tech Specs Labels | `font-weight: 600` | `font.name = "Inter SemiBold"` |
| Tech Specs Values | `font-weight: 700` | `font.name = "Inter Bold"` |
| Keywords | `font-weight: 200` | `font.name = "Inter ExtraLight"` |

---

## 🔗 Ressourcen

### Inter Font Download

- **Official:** https://rsms.me/inter/
- **GitHub:** https://github.com/rsms/inter/releases
- **Google Fonts:** https://fonts.google.com/specimen/Inter

**Wichtig:** Im ZIP-Archiv die Datei unter `extras/ttf/` verwenden, NICHT die Variable Fonts!

### PowerPoint Font-Dokumentation

- **Microsoft:** Font embedding in Office documents
- **python-pptx:** https://python-pptx.readthedocs.io/en/latest/api/text.html

---

## ✅ Checkliste: Projekt Setup

Für neue Entwickler oder Systeme:

- [ ] Inter Static Fonts herunterladen (`Inter-4.0/extras/ttf/`)
- [ ] Variable Fonts deinstallieren (falls vorhanden)
- [ ] Static Fonts installieren (alle .ttf Dateien aus ttf/ Ordner)
- [ ] Font Book öffnen → "Inter ExtraBold" suchen → sollte existieren
- [ ] PowerPoint neu starten
- [ ] Test-Script ausführen: `python3 test_basic_fonts.py`
- [ ] PowerPoint öffnen → Preferences → Save → "Embed fonts" aktivieren
- [ ] Brain-Bridges.pptx generieren: `python3 generate_pptx.py`
- [ ] Präsentation öffnen → Fonts prüfen
- [ ] Preferences → Save → "Embed fonts" aktivieren
- [ ] Datei speichern (jetzt mit embedded Fonts!)

---

## 🐛 Troubleshooting

### Problem: "Fonts sehen alle gleich aus"

**Diagnose:**
```bash
# Prüfe installierte Fonts
ls -la ~/Library/Fonts/ | grep Inter

# Suche nach Variable Fonts
ls -la ~/Library/Fonts/ | grep Variable
```

**Lösung:**
```bash
# Variable Fonts löschen
rm ~/Library/Fonts/InterVariable*.ttf

# PowerPoint beenden
killall "Microsoft PowerPoint"

# 5 Sekunden warten, dann neu starten
```

### Problem: "Font not found" in python-pptx

**Ursache:** Font-Name falsch geschrieben

**Lösung:** Font-Namen mit Tool prüfen:
```bash
python3 check_inter_fonts.py | grep "Inter ExtraBold" -A 3
```

Verwende den **Familie-Namen** (mit Leerzeichen), nicht den PostScript-Namen!

### Problem: "Präsentation sieht auf anderem Mac anders aus"

**Ursache:** Font-Embedding nicht aktiviert

**Lösung:**
1. PowerPoint → Preferences → Save
2. ☑ "Embed fonts in the file" aktivieren
3. Datei neu speichern

---

**Letzte Aktualisierung:** 2025-11-18
**Dokumentiert von:** Claude Code
**Projekt:** Brain-Bridges PowerPoint Generator
