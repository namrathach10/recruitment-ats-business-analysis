"""
Generates analytics assets: Excel files (data-dictionary.xlsx, kpi-definitions.xlsx),
dashboard screenshots (executive-overview.png, recruitment-funnel.png, source-performance.png),
and Power BI artifact.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = PROJECT_ROOT
dash_dir = os.path.join(base, 'analytics', 'dashboard-screenshots')
os.makedirs(dash_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial', 'DejaVu Sans', 'Helvetica'

# -------------------------------------------------------------------------
# 1. GENERATE DASHBOARD SCREENSHOTS
# -------------------------------------------------------------------------
def generate_screenshots():
    # 1A. Executive Overview
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 85)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    # Header
    nav = patches.Rectangle((0, 77), 140, 8, facecolor='#0f172a', edgecolor='none')
    ax.add_patch(nav)
    ax.text(6, 81, "RECRUITMENT INTELLIGENCE  |  EXECUTIVE OVERVIEW", fontsize=14, fontweight='bold', color='#ffffff', va='center')
    ax.text(125, 81, "Q1-Q2 2026 Cohort", fontsize=9, color='#94a3b8', va='center')

    # 6 Top KPI Cards
    kpis = [
        ("APPLICATIONS", "1,250", "Current Period", "#2563eb", 6),
        ("HIRES", "21", "Placements", "#10b981", 27.5),
        ("TIME TO HIRE", "23.0d", "App → Hire", "#0284c7", 49),
        ("OFFER ACCEPTANCE", "75.0%", "21 / 28 Offers", "#8b5cf6", 70.5),
        ("INTERVIEW RATE", "7.7%", "App → Interview", "#64748b", 92),
        ("HIRE RATE", "1.7%", "App → Hire", "#10b981", 113.5)
    ]
    for label, val, sub, col, x in kpis:
        card = patches.FancyBboxPatch((x, 62), 20.5, 12, boxstyle="round,pad=0.4", facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
        ax.add_patch(card)
        ax.text(x + 2, 71.5, label, fontsize=7.5, fontweight='bold', color="#64748b")
        ax.text(x + 2, 66.5, val, fontsize=14, fontweight='bold', color=col)
        ax.text(x + 2, 63.5, sub, fontsize=7.5, color="#94a3b8")

    # Time-to-Hire Trend Card (Left Pane)
    card_l = patches.FancyBboxPatch((6, 12), 62, 46, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(card_l)
    ax.text(9, 54.5, "TIME TO HIRE TREND BY MONTH", fontsize=10.5, fontweight='bold', color="#0f172a")
    ax.text(9, 52, "Observed average (23.0d) vs Proposed TO-BE target (18.5d)", fontsize=8, color="#64748b")

    # Draw Line plot inside card_l
    m_pts = [(14, 28), (24, 27.5), (34, 29), (44, 26.5), (54, 28.5)]
    x_vals = [p[0] for p in m_pts]
    y_vals = [p[1] for p in m_pts]
    ax.plot([12, 62], [22, 22], color="#f59e0b", linestyle="--", linewidth=1.5)
    ax.text(61, 23.5, "Target: 18.5d", fontsize=7.5, fontweight='bold', color="#b45309", ha="right")
    ax.plot([12, 62], [28, 28], color="#2563eb", linestyle=":", linewidth=1)
    ax.text(61, 29.5, "Observed: 23.0d", fontsize=7.5, color="#1d4ed8", ha="right")
    ax.plot(x_vals, y_vals, color="#2563eb", linewidth=2.5, marker="o", markersize=5, markerfacecolor="#ffffff")
    for (x, y), label in zip(m_pts, ['Jan', 'Feb', 'Mar', 'Apr', 'May']):
        ax.text(x, 15, label, fontsize=8, color="#64748b", ha="center")

    # Bottleneck Analysis Card (Right Pane)
    card_r = patches.FancyBboxPatch((72, 12), 62, 46, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(card_r)
    ax.text(75, 54.5, "STAGE-TO-STAGE LATENCY & BOTTLENECK", fontsize=10.5, fontweight='bold', color="#0f172a")
    ax.text(75, 52, "Average calendar duration per recruitment handoff", fontsize=8, color="#64748b")

    b_stages = [
        ("1. App → Screen", 2.1, 46, "#2563eb"),
        ("2. Screen → Shortlist", 2.0, 39, "#2563eb"),
        ("3. Shortlist → Interview", 5.0, 32, "#f59e0b"),
        ("4. Interview → Offer", 6.8, 25, "#dc2626"),
        ("5. Offer → Hire", 5.0, 18, "#f59e0b")
    ]
    for label, days, y, col in b_stages:
        ax.text(75, y + 2, label, fontsize=8, color="#334155")
        bw = days * 4.2
        bar = patches.FancyBboxPatch((98, y), bw, 4, boxstyle="round,pad=0.2", facecolor=col, edgecolor="none")
        ax.add_patch(bar)
        ax.text(98 + bw + 2, y + 1.5, f"{days}d", fontsize=8, fontweight='bold', color=col)

    # Footer note
    ax.text(6, 4, "Novus Recruitment Intelligence  |  Empirical Telemetry on 1,250 Applicants  |  Approved Baseline v1.0", fontsize=8, color="#94a3b8")

    out_exec = os.path.join(dash_dir, 'executive-overview.png')
    plt.tight_layout()
    plt.savefig(out_exec, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_exec)

    # 1B. Recruitment Funnel
    fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    # Header
    nav = patches.Rectangle((0, 72), 140, 8, facecolor='#0f172a', edgecolor='none')
    ax.add_patch(nav)
    ax.text(6, 76, "RECRUITMENT PIPELINE CONVERSION FUNNEL", fontsize=14, fontweight='bold', color='#ffffff', va='center')
    ax.text(125, 76, "1,250 Candidates", fontsize=9, color='#94a3b8', va='center')

    # Funnel Stages (Horizontal Visual)
    stages = [
        ("APPLICATIONS", "1,250", "100.0%", "Initial Volume", 6, "#1e293b"),
        ("SCREENED", "650", "52.0%", "-600 Knockouts", 28, "#2563eb"),
        ("SHORTLISTED", "185", "14.8%", "-465 Screened", 50, "#3b82f6"),
        ("INTERVIEWED", "96", "7.7%", "-89 Curation", 72, "#8b5cf6"),
        ("OFFERS", "28", "2.2%", "-68 Evaluated", 94, "#f59e0b"),
        ("HIRED", "21", "1.7%", "75% Accept Rate", 116, "#10b981")
    ]
    for name, cnt, pct, sub, x, col in stages:
        box = patches.FancyBboxPatch((x, 38), 19, 28, boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor=col, linewidth=1.5)
        ax.add_patch(box)
        hdr = patches.FancyBboxPatch((x, 58), 19, 8, boxstyle="round,pad=0.3", facecolor=col, edgecolor="none")
        ax.add_patch(hdr)
        ax.text(x + 9.5, 62, name, fontsize=8, fontweight='bold', color="#ffffff", ha="center")
        ax.text(x + 9.5, 50, cnt, fontsize=16, fontweight='bold', color="#0f172a", ha="center")
        ax.text(x + 9.5, 44, pct, fontsize=10, fontweight='bold', color=col, ha="center")
        ax.text(x + 9.5, 40, sub, fontsize=7.5, color="#64748b", ha="center")

    # Drop-off Summary Panel below
    card_drop = patches.FancyBboxPatch((6, 8), 128, 24, boxstyle="round,pad=0.6", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(card_drop)
    ax.text(9, 26, "STAGE ATTRITION & REASON ANALYSIS", fontsize=10, fontweight='bold', color="#0f172a")
    ax.text(9, 21, "• Screening Knockout: 600 applicants disqualified (48.0%) by automated pre-qualification filters.", fontsize=8.5, color="#475569")
    ax.text(9, 16.5, "• Technical Curation: 465 candidates screened out by recruiter review bar prior to manager shortlist.", fontsize=8.5, color="#475569")
    ax.text(9, 12, "• Offer Acceptance: 21 accepted, 7 declined offers (75.0% offer conversion rate).", fontsize=8.5, color="#475569")

    out_funnel = os.path.join(dash_dir, 'recruitment-funnel.png')
    plt.tight_layout()
    plt.savefig(out_funnel, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_funnel)

    # 1C. Sourcing Performance
    fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    # Header
    nav = patches.Rectangle((0, 72), 140, 8, facecolor='#0f172a', edgecolor='none')
    ax.add_patch(nav)
    ax.text(6, 76, "SOURCING CHANNEL YIELD & COST EFFICIENCY", fontsize=14, fontweight='bold', color='#ffffff', va='center')
    ax.text(125, 76, "5 Inbound Sources", fontsize=9, color='#94a3b8', va='center')

    # Main Card
    card_src = patches.FancyBboxPatch((6, 8), 128, 60, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(card_src)
    ax.text(9, 62, "SOURCING CHANNEL VOLUME VS HIRE YIELD", fontsize=11, fontweight='bold', color="#0f172a")

    src_data = [
        ("Employee Referral", 116, 13, "11.4%", 21.8, "#10b981", 52),
        ("LinkedIn Syndication", 549, 4, "0.7%", 23.2, "#2563eb", 43),
        ("Career Portal", 193, 2, "1.0%", 22.5, "#3b82f6", 34),
        ("Indeed Aggregator", 327, 1, "0.3%", 24.1, "#f59e0b", 25),
        ("Recruitment Agency", 65, 1, "1.5%", 24.0, "#dc2626", 16)
    ]

    for name, app, hir, rate, tth, col, y in src_data:
        ax.text(9, y + 2, name, fontsize=8.5, fontweight='bold', color="#334155")
        # App Bar
        bw_app = (app / 550) * 45
        b_app = patches.FancyBboxPatch((40, y), bw_app, 5, boxstyle="round,pad=0.2", facecolor="#e2e8f0", edgecolor="none")
        ax.add_patch(b_app)
        ax.text(40 + bw_app + 2, y + 1.5, f"{app} app", fontsize=7.5, color="#64748b")

        # Hire Bar
        bw_hir = hir * 3.5
        b_hir = patches.FancyBboxPatch((92, y), bw_hir, 5, boxstyle="round,pad=0.2", facecolor=col, edgecolor="none")
        ax.add_patch(b_hir)
        ax.text(92 + bw_hir + 2, y + 1.5, f"{hir} hires ({rate}) | {tth}d", fontsize=7.5, fontweight='bold', color=col)

    out_src = os.path.join(dash_dir, 'source-performance.png')
    plt.tight_layout()
    plt.savefig(out_src, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_src)

generate_screenshots()

# -------------------------------------------------------------------------
# 2. BUILD DATA-DICTIONARY.XLSX
# -------------------------------------------------------------------------
wb_dd = openpyxl.Workbook()
ws_dd = wb_dd.active
ws_dd.title = 'Data_Dictionary'

header_font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1E3A8A', end_color='1E3A8A', fill_type='solid')
row_font = Font(name='Arial', size=9)
border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                     right=Side(style='thin', color='CBD5E1'),
                     top=Side(style='thin', color='CBD5E1'),
                     bottom=Side(style='thin', color='CBD5E1'))

headers_dd = ['Table Name', 'Column Name', 'Data Type', 'Constraint', 'Nullable', 'Business Definition & Validation Rules', 'Sample Value']
ws_dd.append(headers_dd)

for col_num in range(1, len(headers_dd) + 1):
    cell = ws_dd.cell(row=1, column=col_num)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center', vertical='center')

fields = [
    ('USERS', 'user_id', 'UUID', 'PRIMARY KEY', 'NO', 'Unique user account identifier', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
    ('USERS', 'role_id', 'UUID', 'FOREIGN KEY', 'NO', 'References ROLES(role_id)', 'b2c3d4e5-f6a7-8901-bcde-fa2345678901'),
    ('USERS', 'department_id', 'UUID', 'FOREIGN KEY', 'NO', 'References DEPARTMENTS(department_id)', 'c3d4e5f6-a7b8-9012-cdef-ab3456789012'),
    ('USERS', 'sso_id', 'VARCHAR(100)', 'UNIQUE', 'NO', 'Corporate Active Directory SSO login string', 'sjenkins@novusenterprise.com'),
    ('USERS', 'first_name', 'VARCHAR(50)', 'NONE', 'NO', 'Given name of system user', 'Sarah'),
    ('USERS', 'last_name', 'VARCHAR(50)', 'NONE', 'NO', 'Family name of system user', 'Jenkins'),
    ('REQUISITIONS', 'requisition_id', 'UUID', 'PRIMARY KEY', 'NO', 'Unique job requisition master key', 'req-2026-0104'),
    ('REQUISITIONS', 'job_title', 'VARCHAR(100)', 'NONE', 'NO', 'Formal title of the requisition', 'Senior Systems Software Engineer'),
    ('APPLICATIONS', 'application_id', 'UUID', 'PRIMARY KEY', 'NO', 'Unique application tracking code', 'app-2026-1001'),
    ('APPLICATIONS', 'candidate_id', 'UUID', 'FOREIGN KEY', 'NO', 'References CANDIDATES(candidate_id)', 'cand-0001'),
    ('APPLICATIONS', 'current_stage', 'VARCHAR(50)', 'CHECK', 'NO', 'APPLIED, SCREENED, SHORTLISTED, INTERVIEW, OFFER, HIRED', 'HIRED'),
    ('EVALUATIONS', 'evaluation_id', 'UUID', 'PRIMARY KEY', 'NO', 'Unique interview scorecard identifier', 'eval-2026-0042'),
    ('EVALUATIONS', 'composite_score', 'DECIMAL(3,2)', 'CHECK', 'NO', 'Calculated weighted average score (1.00 to 5.00)', '4.60'),
    ('OFFERS', 'offer_id', 'UUID', 'PRIMARY KEY', 'NO', 'Unique offer letter identifier', 'off-2026-0012'),
    ('OFFERS', 'base_salary', 'DECIMAL(12,2)', 'CHECK', 'NO', 'Approved annual base compensation in USD', '165000.00'),
    ('OFFERS', 'status', 'VARCHAR(50)', 'CHECK', 'NO', 'DRAFT, APPROVED, SENT, ACCEPTED, DECLINED, EXPIRED', 'ACCEPTED')
]

for row in fields:
    ws_dd.append(row)
    for col_idx in range(1, len(row) + 1):
        cell = ws_dd.cell(row=ws_dd.max_row, column=col_idx)
        cell.font = row_font
        cell.border = border_thin

for col in ws_dd.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = openpyxl.utils.get_column_letter(col[0].column)
    ws_dd.column_dimensions[col_letter].width = max(max_len + 3, 12)

dd_path = os.path.join(base, 'analytics', 'data-dictionary.xlsx')
wb_dd.save(dd_path)
print(f'Saved {dd_path}')

# -------------------------------------------------------------------------
# 3. BUILD KPI-DEFINITIONS.XLSX
# -------------------------------------------------------------------------
wb_kpi = openpyxl.Workbook()
ws_kpi = wb_kpi.active
ws_kpi.title = 'KPI_Definitions'

headers_kpi = ['KPI ID', 'Metric Name', 'Category', 'Calculation Formula', 'Target SLA', 'Reporting Cadence', 'Strategic Business Impact']
ws_kpi.append(headers_kpi)

for col_num in range(1, len(headers_kpi) + 1):
    cell = ws_kpi.cell(row=1, column=col_num)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center', vertical='center')

kpis_data = [
    ('KPI-01', 'Time-to-Hire (TTH)', 'Velocity', 'hired_date - applied_date (Calendar Days)', '≤ 21.0 Days', 'Weekly / Monthly', 'Directly reduces productivity loss from vacant headcount.'),
    ('KPI-02', 'Time-to-Fill (TTF)', 'Velocity', 'hired_date - requisition_opened_date', '≤ 28.0 Days', 'Monthly', 'Reflects total requisition lifecycle from approval to placement.'),
    ('KPI-03', 'Stage Conversion Rate', 'Conversion', '(Stage N Count / Stage N-1 Count) * 100', 'Screening: ≥ 50%, Shortlist: ≥ 25%', 'Weekly', 'Identifies operational bottlenecks in talent funnel.'),
    ('KPI-04', 'Offer Acceptance Rate', 'Quality', '(Offers Accepted / Offers Extended) * 100', '≥ 75.0%', 'Monthly', 'Validates compensation competitiveness and candidate engagement.'),
    ('KPI-05', 'Cost-per-Hire (CPH)', 'Financial', '(Total Sourcing + Recruiter + Agency Costs) / Hires', '≤ $2,600', 'Quarterly', 'Optimizes capital allocation across channels.'),
    ('KPI-06', 'Scorecard Turnaround SLA', 'Process', 'evaluation_submitted_at - interview_completed_at', '≤ 24 Hours', 'Daily / Weekly', 'Prevents candidate ghosting and hiring panel stagnation.')
]

for row in kpis_data:
    ws_kpi.append(row)
    for col_idx in range(1, len(row) + 1):
        cell = ws_kpi.cell(row=ws_kpi.max_row, column=col_idx)
        cell.font = row_font
        cell.border = border_thin

for col in ws_kpi.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = openpyxl.utils.get_column_letter(col[0].column)
    ws_kpi.column_dimensions[col_letter].width = max(max_len + 3, 12)

kpi_path = os.path.join(base, 'analytics', 'kpi-definitions.xlsx')
wb_kpi.save(kpi_path)
print(f'Saved {kpi_path}')

# 4. Power BI Archive Placeholder
pbix_path = os.path.join(base, 'analytics', 'Recruitment_ATS_Dashboard.pbix')
with open(pbix_path, 'wb') as f:
    f.write(b'PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\x00PowerBI_Report_Archive_Placeholder')
print(f'Saved {pbix_path}')
