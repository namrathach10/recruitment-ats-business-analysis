import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = PROJECT_ROOT
ui_dir = os.path.join(base_dir, "ui-ux")
pdf_path = os.path.join(ui_dir, "wireframes.pdf")

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=40,
    rightMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Custom styles
primary_color = colors.HexColor("#0f172a")
accent_color = colors.HexColor("#2563eb")
text_dark = colors.HexColor("#1e293b")
text_muted = colors.HexColor("#64748b")

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=22,
    leading=26,
    textColor=primary_color,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    "DocSub",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=12,
    leading=16,
    textColor=accent_color,
    spaceAfter=15
)

h1_style = ParagraphStyle(
    "H1",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=14,
    leading=18,
    textColor=primary_color,
    spaceBefore=10,
    spaceAfter=6
)

h2_style = ParagraphStyle(
    "H2",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    textColor=accent_color,
    spaceBefore=6,
    spaceAfter=4
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    textColor=text_dark,
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=text_dark,
    leftIndent=15,
    firstLineIndent=-10,
    spaceAfter=3
)

table_header_style = ParagraphStyle(
    "TH",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.5,
    leading=11,
    textColor=colors.white
)

table_cell_style = ParagraphStyle(
    "TD",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8,
    leading=10.5,
    textColor=text_dark
)

story = []

# =========================================================================
# COVER / HEADER
# =========================================================================
story.append(Paragraph("NOVUS ENTERPRISE APPLICANT TRACKING SYSTEM", title_style))
story.append(Paragraph("Deliverable 9: UI/UX Wireframe Concepts & Interface Mockup Specifications", subtitle_style))

# Metadata Table
meta_data = [
    [Paragraph("<b>Document Reference:</b>", table_cell_style), Paragraph("ATS-BA-DOC-009", table_cell_style),
     Paragraph("<b>Author / Role:</b>", table_cell_style), Paragraph("Lead Business Systems Analyst", table_cell_style)],
    [Paragraph("<b>Standard:</b>", table_cell_style), Paragraph("Nielsen Norman Usability Heuristics & WCAG 2.1 AA", table_cell_style),
     Paragraph("<b>Status:</b>", table_cell_style), Paragraph("Approved for Baseline (v1.0)", table_cell_style)]
]
meta_table = Table(meta_data, colWidths=[110, 160, 90, 172])
meta_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(meta_table)
story.append(Spacer(1, 12))

# =========================================================================
# 1. UX Design Philosophy & Information Architecture
# =========================================================================
story.append(Paragraph("1. Design Principles & Role-Based UX Architecture", h1_style))
story.append(Paragraph(
    "The ATS user experience is engineered to eliminate the communication gaps, high candidate abandonment (38%), "
    "and recruiter cognitive fatigue identified in the AS-IS operational state. Interfaces are partitioned into "
    "three specialized, purpose-built personas:",
    body_style
))

persona_data = [
    [Paragraph("Persona", table_header_style), Paragraph("Core User Goal", table_header_style), Paragraph("Primary Design Heuristic", table_header_style), Paragraph("Target Task Metric", table_header_style)],
    [Paragraph("<b>Candidate</b><br/>(Maya Lin)", table_cell_style), Paragraph("Submit application frictionlessly and track live progress 24/7.", table_cell_style), Paragraph("Visibility of System Status (#1) & Aesthetic Minimalism (#8).", table_cell_style), Paragraph("Application completion time &lt; 5 mins; Zero inquiry emails.", table_cell_style)],
    [Paragraph("<b>Recruiter</b><br/>(Sarah Jenkins)", table_cell_style), Paragraph("Filter, evaluate, and advance talent pipelines with bulk actions.", table_cell_style), Paragraph("Flexibility & Efficiency of Use (#7) with Kanban velocity.", table_cell_style), Paragraph("Screening review time &lt; 90 secs per candidate.", table_cell_style)],
    [Paragraph("<b>Hiring Manager</b><br/>(David Vance)", table_cell_style), Paragraph("Review structured dossiers and submit rubric ratings.", table_cell_style), Paragraph("Consistency and Standards (#4) & Error Prevention (#5).", table_cell_style), Paragraph("Scorecard turnaround &lt; 24h via mobile or desktop.", table_cell_style)]
]
p_table = Table(persona_data, colWidths=[80, 160, 160, 132])
p_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(p_table)
story.append(Spacer(1, 14))

# =========================================================================
# 2. Candidate Portal Mockup
# =========================================================================
story.append(Paragraph("2. Candidate Experience: Career Portal & Application Tracker", h1_style))
story.append(Paragraph(
    "<b>Objective:</b> Deliver total transparency into application status, direct calendar integration for self-service scheduling, "
    "and frictionless document management to eliminate candidate ghosting.",
    body_style
))

img_candidate = os.path.join(ui_dir, "candidate-portal.png")
if os.path.exists(img_candidate):
    story.append(Image(img_candidate, width=530, height=340))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Key Functional Features & UI Annotations:</b>", h2_style))
story.append(Paragraph("• <b>Visual 5-Stage Gate Progress Tracker:</b> Real-time synchronization displaying exact active status with date stamps and pulse indicator.", bullet_style))
story.append(Paragraph("• <b>Action-Required Notification Banner:</b> Context-sensitive call-to-action allowing immediate self-service panel interview slot booking.", bullet_style))
story.append(Paragraph("• <b>Transparent Audit Trail:</b> Detailed timestamps informing the candidate of recruiter actions and OCR document verification.", bullet_style))
story.append(Paragraph("• <b>GDPR / CCPA Self-Service:</b> In-app rights management permitting 1-click personal data export or profile erasure.", bullet_style))

story.append(PageBreak())

# =========================================================================
# 3. Recruiter Kanban Pipeline Dashboard
# =========================================================================
story.append(Paragraph("3. Recruiter Experience: Interactive Kanban Pipeline Dashboard", h1_style))
story.append(Paragraph(
    "<b>Objective:</b> High-density desktop workspace enabling recruiters to manage 50+ active applicants across multi-stage funnels "
    "via drag-and-drop, automated AI match scoring, and quick filters.",
    body_style
))

img_recruiter = os.path.join(ui_dir, "recruiter-dashboard.png")
if os.path.exists(img_recruiter):
    story.append(Image(img_recruiter, width=530, height=335))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Key Functional Features & UI Annotations:</b>", h2_style))
story.append(Paragraph("• <b>Multi-Column Visual Pipeline:</b> Real-time candidate counts and status cards (Applied, Screened, Shortlisted, Interview, Offer).", bullet_style))
story.append(Paragraph("• <b>Algorithmic Match Scoring Pill:</b> Visual match percentages (e.g., 96%, 88%) computed against requisition required skills.", bullet_style))
story.append(Paragraph("• <b>SLA & In-Stage Aging Counters:</b> Automatic visual flags highlighting candidates idling past defined SLA thresholds.", bullet_style))
story.append(Paragraph("• <b>Multi-Source Tagging:</b> Immediate identification of sourcing channel (LinkedIn, Referral, Careers, Indeed) for source optimization.", bullet_style))

story.append(PageBreak())

# =========================================================================
# 4. Hiring Manager Evaluation & Scorecard
# =========================================================================
story.append(Paragraph("4. Hiring Manager Experience: Standardized Evaluation Scorecard", h1_style))
story.append(Paragraph(
    "<b>Objective:</b> Eliminate subjective hiring bias and interview feedback delays with a calibrated 1-to-5 competency rubric, "
    "pre-populated candidate dossier, and one-click recommendation capture.",
    body_style
))

img_hm = os.path.join(ui_dir, "hiring-manager.png")
if os.path.exists(img_hm):
    story.append(Image(img_hm, width=530, height=340))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Key Functional Features & UI Annotations:</b>", h2_style))
story.append(Paragraph("• <b>Dual-Pane Review Architecture:</b> Candidate work history, verified skills, and original resume displayed alongside the rating form.", bullet_style))
story.append(Paragraph("• <b>Calibrated 1-5 Competency Rubric:</b> Strict behavioral anchors for Technical Architecture, Problem Solving, and Collaboration.", bullet_style))
story.append(Paragraph("• <b>Clear Recommendation Radios:</b> Mandatory selection (Strong Hire, Hire, Hold, Reject) preventing ambiguous verbal feedback.", bullet_style))
story.append(Paragraph("• <b>Mobile-First Optimization:</b> Form designed for rapid 2-minute completion on mobile smartphones immediately following interviews.", bullet_style))

story.append(Spacer(1, 10))

# =========================================================================
# 5. Usability Validation & Design System Tokens
# =========================================================================
story.append(Paragraph("5. Usability Metrics & Design System Token Specifications", h1_style))
story.append(Paragraph(
    "To ensure high adoption across non-technical hiring managers and high-velocity talent teams, the design adheres to "
    "strict usability benchmarks and enterprise design tokens:",
    body_style
))

tokens_data = [
    [Paragraph("Category", table_header_style), Paragraph("Specification / Token", table_header_style), Paragraph("Target Benchmark / Value", table_header_style)],
    [Paragraph("<b>Typography</b>", table_cell_style), Paragraph("Inter / System Sans-Serif font family (12pt body, 16pt h2, 24pt h1)", table_cell_style), Paragraph("Optimal legibility across high-density desktop & mobile.", table_cell_style)],
    [Paragraph("<b>Color Palette</b>", table_cell_style), Paragraph("Primary Navy (#0F172A), Action Blue (#2563EB), Success (#10B981), Warning (#F59E0B)", table_cell_style), Paragraph("Contrast ratio &gt; 4.5:1 meeting WCAG 2.1 Level AA.", table_cell_style)],
    [Paragraph("<b>System Usability (SUS)</b>", table_cell_style), Paragraph("Standardized 10-question System Usability Scale post-pilot survey", table_cell_style), Paragraph("Target SUS Score &gt;= 85 (Grade A+ Industry Standard).", table_cell_style)],
    [Paragraph("<b>Accessibility</b>", table_cell_style), Paragraph("Full keyboard navigation, ARIA landmarks, screen reader alt tags", table_cell_style), Paragraph("100% WCAG 2.1 AA certified compliance.", table_cell_style)]
]
t_table = Table(tokens_data, colWidths=[120, 240, 172])
t_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(t_table)

doc.build(story)
print(f"Wireframes PDF successfully created at: {pdf_path}")
