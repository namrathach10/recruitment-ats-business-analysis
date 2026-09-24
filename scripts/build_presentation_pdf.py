import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = PROJECT_ROOT
pres_dir = os.path.join(base_dir, "presentation")
os.makedirs(pres_dir, exist_ok=True)
pdf_path = os.path.join(pres_dir, "ATS-Executive-Presentation.pdf")

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    leftMargin=36,
    rightMargin=36,
    topMargin=28,
    bottomMargin=28
)

styles = getSampleStyleSheet()

# Colors
navy_header = colors.HexColor("#0f172a")
accent_blue = colors.HexColor("#2563eb")
dark_slate = colors.HexColor("#1e293b")
gray_muted = colors.HexColor("#64748b")
card_bg = colors.HexColor("#f8fafc")
border_col = colors.HexColor("#cbd5e1")

# Styles
title_slide_title = ParagraphStyle(
    "TitleSlideTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=26,
    leading=32,
    textColor=navy_header,
    spaceAfter=10
)

title_slide_sub = ParagraphStyle(
    "TitleSlideSub",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=14,
    leading=18,
    textColor=accent_blue,
    spaceAfter=15
)

slide_header_style = ParagraphStyle(
    "SlideHeader",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=22,
    textColor=navy_header,
    spaceAfter=3
)

slide_sub_style = ParagraphStyle(
    "SlideSub",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    textColor=accent_blue,
    spaceAfter=10
)

body_text = ParagraphStyle(
    "SlideBody",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    textColor=dark_slate,
    spaceAfter=6
)

bullet_item = ParagraphStyle(
    "SlideBullet",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=dark_slate,
    leftIndent=12,
    firstLineIndent=-8,
    spaceAfter=4
)

th_style = ParagraphStyle(
    "TH",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.5,
    leading=11,
    textColor=colors.white
)

td_style = ParagraphStyle(
    "TD",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8,
    leading=10.5,
    textColor=dark_slate
)

story = []

def make_footer(slide_num, total_slides=10):
    t_data = [
        [Paragraph(f"<b>NOVUS ENTERPRISE ATS PROPOSAL</b> | Reference: ATS-BA-DOC-010 | Lead Business Systems Analyst", td_style),
         Paragraph(f"Slide {slide_num} of {total_slides}", ParagraphStyle("Right", parent=td_style, alignment=2))]
    ]
    t = Table(t_data, colWidths=[580, 140])
    t.setStyle(TableStyle([
        ('LINEABOVE', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    return t

# =========================================================================
# SLIDE 1: Title Slide
# =========================================================================
story.append(Spacer(1, 40))
story.append(Paragraph("MODERNIZING ENTERPRISE TALENT ACQUISITION", title_slide_title))
story.append(Paragraph("Business Process Analysis & Information System Proposal for an Enterprise ATS", title_slide_sub))
story.append(Paragraph("<b>Role:</b> Lead Business Systems Analyst   |   <b>Target Audience:</b> Executive Leadership, VP Talent & CTO", body_text))
story.append(Paragraph("<b>Scope:</b> End-to-End Business Analysis, Architecture, Data Model, Analytics, and Implementation Proposal", body_text))
story.append(Spacer(1, 20))

meta_card = [
    [Paragraph("Project Baseline", th_style), Paragraph("Governance & Compliance", th_style), Paragraph("Financial Impact", th_style)],
    [
        Paragraph("• Baseline Time-to-Hire: 42 Days<br/>• Target Time-to-Hire: 21 Days<br/>• 10 Formal Analysis Deliverables<br/>• Synthetic Dataset: 1,250 Candidates", td_style),
        Paragraph("• EEOC / OFCCP Compliance Audits<br/>• GDPR / CCPA Data Rights<br/>• Calibrated Anti-Bias Scorecards<br/>• Role-Based Access Control (RBAC)", td_style),
        Paragraph("• Annual Operational Drag: $730,000<br/>• Proposed Net Savings: $525,000/yr<br/>• 3-Year Expected ROI: 3.4x<br/>• Payback Period: 7.2 Months", td_style)
    ]
]
t_meta = Table(meta_card, colWidths=[240, 240, 240])
t_meta.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), navy_header),
    ('BACKGROUND', (0,1), (-1,1), card_bg),
    ('BOX', (0,0), (-1,-1), 1, border_col),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_meta)
story.append(Spacer(1, 40))
story.append(make_footer(1))
story.append(PageBreak())

# =========================================================================
# SLIDE 2: Strategic Business Case & Financial Problem
# =========================================================================
story.append(Paragraph("Executive Business Case: The Cost of Operational Friction", slide_header_style))
story.append(Paragraph("Legacy hiring operations result in talent leakage, extreme cycle times, and inflated agency reliance.", slide_sub_style))

row_metrics = [
    [Paragraph("<b>42 Days</b><br/><font color='#64748b'>Avg Time-to-Hire (vs 22 Ind Avg)</font>", ParagraphStyle("C", parent=td_style, alignment=1, fontSize=11, leading=14)),
     Paragraph("<b>38% Drop-Off</b><br/><font color='#64748b'>Candidate Funnel Abandonment</font>", ParagraphStyle("C", parent=td_style, alignment=1, fontSize=11, leading=14)),
     Paragraph("<b>$4,850</b><br/><font color='#64748b'>Cost-per-Hire (Excess Agency Fees)</font>", ParagraphStyle("C", parent=td_style, alignment=1, fontSize=11, leading=14)),
     Paragraph("<b>$730,000</b><br/><font color='#64748b'>Annual Financial Drag</font>", ParagraphStyle("C", parent=td_style, alignment=1, fontSize=11, leading=14))]
]
t_kpi = Table(row_metrics, colWidths=[180, 180, 180, 180])
t_kpi.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#eff6ff")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#bfdbfe")),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#dbeafe")),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(t_kpi)
story.append(Spacer(1, 12))

story.append(Paragraph("<b>Key Findings from Operational Discovery:</b>", ParagraphStyle("SubH", parent=slide_header_style, fontSize=11, leading=14)))
story.append(Paragraph("• <b>Manual Resume Intake & Disjointed Spreadsheets:</b> 65% of recruiter effort consumed by data entry, resume parsing errors, and untracked emails.", bullet_item))
story.append(Paragraph("• <b>Scheduling Friction Bottleneck:</b> Coordinating panel interviews takes 4.8 calendar days on average due to back-and-forth manual email exchanges.", bullet_item))
story.append(Paragraph("• <b>Delayed Hiring Manager Scorecards:</b> Average scorecard turnaround is 3.8 days; 30% of top candidates accept competing offers while waiting.", bullet_item))
story.append(Paragraph("• <b>Severe Compliance & Reporting Exposure:</b> No centralized audit log for EEO/OFCCP compliance; manual spreadsheet reporting takes 40+ hours per quarter.", bullet_item))

story.append(Spacer(1, 20))
story.append(make_footer(2))
story.append(PageBreak())

# =========================================================================
# SLIDE 3: AS-IS Process Flow & Bottlenecks
# =========================================================================
story.append(Paragraph("AS-IS Process Baseline: Operational Inefficiencies", slide_header_style))
story.append(Paragraph("Multi-tool fragmentation causes candidate ghosting, data loss, and extended cycle delays.", slide_sub_style))

img_asis = os.path.join(base_dir, "diagrams/as-is-process.png")
if os.path.exists(img_asis):
    story.append(Image(img_asis, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Primary Bottlenecks:</b> Email-based intake | 4.8-day calendar bottleneck | Unstructured interview feedback | High drop-off at screening.", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(3))
story.append(PageBreak())

# =========================================================================
# SLIDE 4: TO-BE Target Architecture & Automated Workflow
# =========================================================================
story.append(Paragraph("TO-BE Target Operating Model: Automated & Integrated Workflow", slide_header_style))
story.append(Paragraph("Streamlined 5-stage pipeline driven by automated intake, self-service scheduling, and real-time syncing.", slide_sub_style))

img_tobe = os.path.join(base_dir, "diagrams/to-be-process.png")
if os.path.exists(img_tobe):
    story.append(Image(img_tobe, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Transformations:</b> Automated resume parsing & knockout scoring | Candidate self-service calendar booking | Mobile rubric scorecards & e-Signatures.", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(4))
story.append(PageBreak())

# =========================================================================
# SLIDE 5: System Requirements & Scope Baseline
# =========================================================================
story.append(Paragraph("System Requirements & Functional Scope Baseline", slide_header_style))
story.append(Paragraph("Structured into 5 functional modules and validated non-functional architectural baselines.", slide_sub_style))

img_usecase = os.path.join(base_dir, "diagrams/use-case-diagram.png")
if os.path.exists(img_usecase):
    story.append(Image(img_usecase, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Core Modules:</b> Requisition Governance | Sourcing & Parsing | Pipeline Management | Scheduling & Evaluation | Offer & Onboarding.", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(5))
story.append(PageBreak())

# =========================================================================
# SLIDE 6: Enterprise Data Model & Entity Architecture
# =========================================================================
story.append(Paragraph("Enterprise Data Model: Relational Entity Architecture", slide_header_style))
story.append(Paragraph("Normalized 3NF relational schema enforcing strict referential integrity, auditability, and analytics readiness.", slide_sub_style))

img_erd = os.path.join(base_dir, "diagrams/erd.png")
if os.path.exists(img_erd):
    story.append(Image(img_erd, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Core Relational Entities:</b> Requisition (1:N) Applications (1:N) Interviews (1:N) Scorecards (1:1) Offers (1:1) Hires.", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(6))
story.append(PageBreak())

# =========================================================================
# SLIDE 7: C4 Microservices Architecture & System Integrations
# =========================================================================
story.append(Paragraph("System Architecture: Cloud-Native Microservices (C4 Container)", slide_header_style))
story.append(Paragraph("Event-driven architecture with resilient asynchronous integrations (Kafka, REST, Webhooks).", slide_sub_style))

img_c4 = os.path.join(base_dir, "diagrams/c4-container.png")
if os.path.exists(img_c4):
    story.append(Image(img_c4, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Enterprise Connectors:</b> Workday HRIS | Google Workspace / Outlook 365 | LinkedIn / Indeed Job Boards | DocuSign e-Sign.", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(7))
story.append(PageBreak())

# =========================================================================
# SLIDE 8: Real-Time BI Analytics & Recruitment Funnel
# =========================================================================
story.append(Paragraph("Data Analytics Framework: Funnel Velocity & KPIs", slide_header_style))
story.append(Paragraph("Power BI telemetry tracking 1,250 candidates across stage conversion, cost, and sourcing ROI.", slide_sub_style))

img_funnel = os.path.join(base_dir, "analytics/dashboard-screenshots/recruitment-funnel.png")
if os.path.exists(img_funnel):
    story.append(Image(img_funnel, width=680, height=330))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Dataset Insights:</b> 1,250 Applicants -> 650 Screened (52%) -> 185 Shortlisted (28%) -> 96 Interviewed (52%) -> 28 Offers -> 21 Hires (75% Acceptance).", body_text))

story.append(Spacer(1, 10))
story.append(make_footer(8))
story.append(PageBreak())

# =========================================================================
# SLIDE 9: Implementation Roadmap & Change Management
# =========================================================================
story.append(Paragraph("Phased Implementation Roadmap & Change Enablement", slide_header_style))
story.append(Paragraph("Structured 24-week rollout minimizing disruption, ensuring data integrity and high user adoption.", slide_sub_style))

phases_data = [
    [Paragraph("Phase & Duration", th_style), Paragraph("Core Scope & Key Deliverables", th_style), Paragraph("Milestone & Gate Criteria", th_style)],
    [
        Paragraph("<b>Phase 1: Foundation</b><br/>(Weeks 1 - 6)", td_style),
        Paragraph("• Infrastructure setup, RDS PostgreSQL provisioning, Kafka event bus<br/>• Core Workday HRIS & Active Directory SSO integration<br/>• RBAC security matrix & data dictionary baseline", td_style),
        Paragraph("Gate 1: SSO & Workday Master Data Sync validated in Sandbox.", td_style)
    ],
    [
        Paragraph("<b>Phase 2: Core ATS</b><br/>(Weeks 7 - 14)", td_style),
        Paragraph("• Requisition management, automated resume intake & parsing<br/>• Interactive Recruiter Kanban pipeline & interview calendar sync<br/>• Mobile scorecard rubric & e-Signature integration", td_style),
        Paragraph("Gate 2: UAT sign-off by Talent Acquisition & Engineering Hiring Panel.", td_style)
    ],
    [
        Paragraph("<b>Phase 3: Rollout & Analytics</b><br/>(Weeks 15 - 24)", td_style),
        Paragraph("• Power BI executive dashboard deployment & data pipeline sync<br/>• Pilot rollout with Engineering & Sales departments<br/>• User training, change management enablement, enterprise cutover", td_style),
        Paragraph("Gate 3: 100% production cutover & legacy spreadsheet decommissioning.", td_style)
    ]
]
t_phases = Table(phases_data, colWidths=[130, 430, 160])
t_phases.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), navy_header),
    ('BACKGROUND', (0,1), (-1,1), card_bg),
    ('BACKGROUND', (0,2), (-1,2), colors.white),
    ('BACKGROUND', (0,3), (-1,3), card_bg),
    ('BOX', (0,0), (-1,-1), 1, border_col),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
]))
story.append(t_phases)
story.append(Spacer(1, 12))
story.append(Paragraph("<b>Change Management Strategy:</b> Role-based training workshops (Recruiters, Hiring Managers, HR Ops), quick-reference job aids, and proactive feedback loops.", body_text))

story.append(Spacer(1, 20))
story.append(make_footer(9))
story.append(PageBreak())

# =========================================================================
# SLIDE 10: Financial ROI & Strategic Recommendation
# =========================================================================
story.append(Paragraph("Business Value, Financial ROI & Final Recommendation", slide_header_style))
story.append(Paragraph("Compelling economics: $525,000 net annual savings, 3.4x 3-year ROI, and 7.2-month payback.", slide_sub_style))

roi_cards = [
    [Paragraph("<b>Financial Returns</b>", th_style), Paragraph("<b>Operational Outcomes</b>", th_style), Paragraph("<b>Strategic Advantage</b>", th_style)],
    [
        Paragraph("• Agency spend reduced by 60% ($290k/yr)<br/>• Recruiter productivity up 40% ($150k/yr)<br/>• Scheduling labor reduced 80% ($85k/yr)<br/>• <b>Total Net Benefit: $525,000 / year</b><br/>• Implementation Capex: $210,000<br/>• Payback Period: <b>7.2 Months</b>", td_style),
        Paragraph("• Time-to-Hire slashed from 42 to <b>21 Days</b><br/>• Candidate drop-off cut from 38% to <b>12%</b><br/>• Scorecard turnaround from 3.8d to <b>&lt; 24h</b><br/>• Offer acceptance rate lifted to <b>75%+</b><br/>• Candidate NPS increased from +12 to <b>+65</b>", td_style),
        Paragraph("• Enterprise compliance with full EEO audit logs<br/>• Automated candidate rediscovery database<br/>• Competitive advantage in securing top tech talent<br/>• Scalable architecture supporting 500+ hires/yr", td_style)
    ]
]
t_roi = Table(roi_cards, colWidths=[240, 240, 240])
t_roi.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), navy_header),
    ('BACKGROUND', (0,1), (-1,1), card_bg),
    ('BOX', (0,0), (-1,-1), 1, border_col),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_roi)
story.append(Spacer(1, 14))

story.append(Paragraph("<b>Recommendation:</b> Approve Phase 1 capital expenditure ($210k) to commence infrastructure build and Workday integration.", ParagraphStyle("Rec", parent=slide_header_style, fontSize=11, leading=14, textColor=accent_blue)))

story.append(Spacer(1, 30))
story.append(make_footer(10))

doc.build(story)
print(f"Presentation PDF successfully generated at: {pdf_path}")
