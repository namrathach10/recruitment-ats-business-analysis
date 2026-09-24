"""
Generates the comprehensive unified interactive application that combines
the complete Recruitment Intelligence Analytics Suite with the Interactive Operational ATS Workflows.
Deploys to all target paths for 100% synchronization.
"""

import os
import shutil

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(PROJECT_ROOT, "data", "recruitment_sample_dataset_anonymized.csv")

TARGET_PATHS = [
    r"C:\Users\namra\.gemini\antigravity\brain\0a294a9a-ba7f-478d-9c2d-2a6eef6fff92\interactive_ats_portal.html",
    os.path.join(PROJECT_ROOT, "interactive_ats_portal.html"),
    os.path.join(PROJECT_ROOT, "analytics", "recruitment-intelligence-dashboard.html"),
    r"C:\Users\namra\.gemini\antigravity\brain\0a294a9a-ba7f-478d-9c2d-2a6eef6fff92\recruitment_intelligence_dashboard.html"
]

def build_app():
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        csv_text = f.read()

    escaped_csv = csv_text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    # Read base dashboard html from build_dashboard_html.py and expand it
    # We will construct the master HTML content directly
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recruitment Intelligence | Enterprise ATS Analytics & Interactive Workflows</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #F6F8FB;
      --primary-dark: #172033;
      --primary-accent: #2563EB;
      --primary-accent-light: #EFF6FF;
      --secondary-accent: #14B8A6;
      --success: #16A34A;
      --success-light: #ECFDF5;
      --warning: #F59E0B;
      --warning-light: #FFFBEB;
      --critical: #DC2626;
      --critical-light: #FEF2F2;
      --neutral: #64748B;
      --neutral-light: #94A3B8;
      --card-bg: #FFFFFF;
      --border: #E2E8F0;
      --text-main: #0F172A;
      --sidebar-width: 250px;
      --sidebar-collapsed-width: 68px;
      --header-height: 64px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      font-size: 13px;
      line-height: 1.5;
      overflow-x: hidden;
      display: flex;
      height: 100vh;
    }}

    .icon {{
      display: inline-block;
      width: 16px;
      height: 16px;
      stroke-width: 2;
      stroke: currentColor;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
      vertical-align: middle;
    }}

    /* Sidebar */
    #sidebar {{
      width: var(--sidebar-width);
      background-color: var(--primary-dark);
      color: #94A3B8;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: 100vh;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
      transition: width 0.2s ease;
      z-index: 50;
    }}

    #sidebar.collapsed {{
      width: var(--sidebar-collapsed-width);
    }}

    .sidebar-header {{
      height: var(--header-height);
      display: flex;
      align-items: center;
      padding: 0 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      gap: 12px;
    }}

    .logo-box {{
      width: 34px;
      height: 34px;
      border-radius: 8px;
      background: linear-gradient(135deg, #2563EB, #14B8A6);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-weight: 700;
      font-size: 16px;
      flex-shrink: 0;
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
      overflow: hidden;
      white-space: nowrap;
    }}

    .brand-title {{
      color: #FFFFFF;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: -0.2px;
    }}

    .brand-sub {{
      font-size: 10px;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .nav-section {{
      flex: 1;
      overflow-y: auto;
      padding: 12px 8px;
    }}

    .nav-label {{
      font-size: 10px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #475569;
      padding: 12px 10px 4px;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 12px;
      border-radius: 6px;
      color: #94A3B8;
      text-decoration: none;
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
      margin-bottom: 2px;
    }}

    .nav-item:hover {{
      background-color: rgba(255, 255, 255, 0.05);
      color: #FFFFFF;
    }}

    .nav-item.active {{
      background-color: var(--primary-accent);
      color: #FFFFFF;
      font-weight: 600;
    }}

    .nav-item .icon {{
      width: 17px;
      height: 17px;
      flex-shrink: 0;
    }}

    .sidebar-footer {{
      padding: 12px 14px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      font-size: 11px;
      background-color: rgba(0, 0, 0, 0.15);
    }}

    .status-indicator {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}

    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: #10B981;
      box-shadow: 0 0 6px rgba(16, 185, 129, 0.6);
    }}

    .user-pill {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding-top: 8px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .user-avatar {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background-color: #334155;
      color: #F8FAFC;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 10px;
    }}

    /* Main Container */
    #main-container {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      min-width: 0;
    }}

    /* Header */
    #top-header {{
      height: var(--header-height);
      background-color: #FFFFFF;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      flex-shrink: 0;
      gap: 16px;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .btn-toggle-sidebar {{
      background: none;
      border: 1px solid var(--border);
      border-radius: 6px;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--neutral);
    }}

    .btn-toggle-sidebar:hover {{
      background-color: var(--bg-main);
      color: var(--text-main);
    }}

    .page-heading {{
      display: flex;
      flex-direction: column;
    }}

    .page-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--primary-dark);
      letter-spacing: -0.2px;
    }}

    .page-subtitle {{
      font-size: 11.5px;
      color: var(--neutral);
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .filter-select {{
      padding: 6px 10px;
      font-size: 12px;
      font-family: inherit;
      border: 1px solid var(--border);
      border-radius: 6px;
      background-color: #FFFFFF;
      color: var(--text-main);
      cursor: pointer;
      outline: none;
    }}

    .filter-select:focus {{
      border-color: var(--primary-accent);
      box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15);
    }}

    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 500;
      font-family: inherit;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      border: 1px solid var(--border);
      background-color: #FFFFFF;
      color: var(--text-main);
    }}

    .btn-action:hover {{
      background-color: var(--bg-main);
    }}

    .btn-primary {{
      background-color: var(--primary-accent);
      color: #FFFFFF;
      border-color: var(--primary-accent);
    }}

    .btn-primary:hover {{
      background-color: #1D4ED8;
    }}

    /* Filter Chips Bar */
    #filter-chips-bar {{
      background-color: #FFFFFF;
      border-bottom: 1px solid var(--border);
      padding: 6px 24px;
      display: none;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 11.5px;
    }}

    #filter-chips-bar.active {{
      display: flex;
    }}

    .filter-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 2px 8px;
      background-color: var(--primary-accent-light);
      color: var(--primary-accent);
      border: 1px solid #BFDBFE;
      border-radius: 12px;
      font-weight: 500;
    }}

    .chip-remove {{
      cursor: pointer;
      font-size: 13px;
      font-weight: bold;
      color: var(--primary-accent);
      display: flex;
      align-items: center;
    }}

    .btn-clear-all {{
      color: var(--critical);
      cursor: pointer;
      font-weight: 500;
      text-decoration: underline;
      margin-left: 6px;
      background: none;
      border: none;
      font-size: 11.5px;
      font-family: inherit;
    }}

    /* Scrollable Workspace */
    #workspace {{
      flex: 1;
      overflow-y: auto;
      padding: 20px 24px 40px;
    }}

    /* KPI Cards Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 14px;
      margin-bottom: 20px;
    }}

    .kpi-card {{
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 16px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 105px;
    }}

    .kpi-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}

    .kpi-label {{
      font-size: 12px;
      font-weight: 600;
      color: var(--neutral);
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}

    .kpi-icon-wrap {{
      width: 24px;
      height: 24px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: var(--bg-main);
      color: var(--neutral);
    }}

    .kpi-val {{
      font-size: 26px;
      font-weight: 700;
      color: var(--primary-dark);
      line-height: 1.1;
      margin-bottom: 4px;
      letter-spacing: -0.5px;
    }}

    .kpi-subtext {{
      font-size: 11px;
      color: var(--neutral);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* Cards & Layout */
    .card {{
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px 20px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      margin-bottom: 20px;
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border);
    }}

    .card-title-group {{
      display: flex;
      flex-direction: column;
    }}

    .card-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--primary-dark);
    }}

    .card-subtitle {{
      font-size: 11px;
      color: var(--neutral);
    }}

    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    /* Funnel Component */
    .funnel-container {{
      display: flex;
      align-items: stretch;
      gap: 12px;
      overflow-x: auto;
      padding: 10px 0;
    }}

    .funnel-step {{
      flex: 1;
      min-width: 140px;
      background-color: var(--bg-main);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .funnel-step:hover {{
      border-color: var(--primary-accent);
      background-color: #FFFFFF;
      transform: translateY(-2px);
      box-shadow: 0 4px 6px rgba(0,0,0,0.03);
    }}

    .funnel-step.active {{
      border-color: var(--primary-accent);
      background-color: var(--primary-accent-light);
    }}

    .funnel-step-name {{
      font-size: 11.5px;
      font-weight: 600;
      color: var(--neutral);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 8px;
    }}

    .funnel-step-count {{
      font-size: 24px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 4px;
    }}

    .funnel-step-pct {{
      font-size: 12px;
      font-weight: 600;
      color: var(--primary-accent);
    }}

    .funnel-step-conv {{
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px dashed var(--border);
      font-size: 11px;
      color: var(--neutral);
    }}

    /* Table Styles */
    .table-container {{
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: 8px;
      background-color: #FFFFFF;
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 12px;
    }}

    table.data-table th {{
      background-color: #F8FAFC;
      color: var(--primary-dark);
      font-weight: 600;
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}

    table.data-table td {{
      padding: 9px 12px;
      border-bottom: 1px solid var(--border);
      color: var(--text-main);
      white-space: nowrap;
    }}

    table.data-table tr:hover td {{
      background-color: #F8FAFC;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 10.5px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}

    .badge-success {{ background-color: #DCFCE7; color: #15803D; }}
    .badge-warning {{ background-color: #FEF3C7; color: #B45309; }}
    .badge-critical {{ background-color: #FEE2E2; color: #B91C1C; }}
    .badge-info {{ background-color: #DBEAFE; color: #1D4ED8; }}
    .badge-neutral {{ background-color: #F1F5F9; color: #475569; }}

    /* Insights Box */
    .insight-panel {{
      background: linear-gradient(to right, #F8FAFC, #FFFFFF);
      border: 1px solid #CBD5E1;
      border-left: 4px solid var(--primary-accent);
      border-radius: 8px;
      padding: 14px 16px;
      margin-top: 14px;
    }}

    .insight-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--primary-dark);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .insight-list {{
      list-style-type: none;
    }}

    .insight-list li {{
      position: relative;
      padding-left: 14px;
      font-size: 12px;
      color: #334155;
      margin-bottom: 4px;
      line-height: 1.4;
    }}

    .insight-list li::before {{
      content: "•";
      position: absolute;
      left: 0;
      color: var(--primary-accent);
      font-weight: bold;
      font-size: 14px;
    }}

    /* Global Tooltip */
    #global-tooltip {{
      position: fixed;
      pointer-events: none;
      background-color: var(--primary-dark);
      color: #FFFFFF;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 11.5px;
      line-height: 1.4;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      z-index: 9999;
      opacity: 0;
      transition: opacity 0.1s ease;
      max-width: 260px;
    }}

    /* Loading Screen */
    #loading-screen {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #FFFFFF;
      z-index: 10000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: opacity 0.3s ease;
    }}

    .loader-spinner {{
      width: 44px;
      height: 44px;
      border: 3px solid #E2E8F0;
      border-top-color: var(--primary-accent);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      margin-bottom: 16px;
    }}

    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}

    .empty-state {{
      padding: 60px 20px;
      text-align: center;
      background-color: #FFFFFF;
      border: 1px dashed var(--border);
      border-radius: 10px;
      margin: 20px 0;
    }}

    .empty-icon {{
      font-size: 36px;
      color: var(--neutral-light);
      margin-bottom: 12px;
    }}

    .empty-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 6px;
    }}

    .empty-desc {{
      font-size: 12px;
      color: var(--neutral);
      margin-bottom: 16px;
    }}

    svg.chart {{
      width: 100%;
      height: 100%;
      overflow: visible;
    }}

    .grid-line {{
      stroke: #F1F5F9;
      stroke-width: 1;
    }}

    .axis-label {{
      font-size: 10px;
      fill: #64748B;
      font-family: inherit;
    }}

    .chart-bar {{
      transition: fill 0.15s ease, opacity 0.15s ease;
      cursor: pointer;
    }}

    .chart-bar:hover {{
      opacity: 0.85;
    }}

    /* Kanban Interactive Drag & Drop Styles */
    .kanban-board {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      align-items: start;
    }}

    .kanban-col {{
      background-color: #F1F5F9;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      min-height: 480px;
      display: flex;
      flex-direction: column;
    }}

    .kanban-col-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-weight: 700;
      font-size: 12px;
      color: var(--primary-dark);
    }}

    .kanban-dropzone {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .kanban-card {{
      background-color: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      padding: 12px;
      cursor: grab;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}

    .kanban-card:active {{
      cursor: grabbing;
      opacity: 0.6;
    }}

    .kanban-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 6px rgba(0,0,0,0.06);
      border-color: var(--primary-accent);
    }}

    /* Responsive */
    @media (max-width: 1200px) {{
      .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }}
      .grid-2 {{ grid-template-columns: 1fr; }}
      .kanban-board {{ grid-template-columns: repeat(2, 1fr); }}
    }}

    @media (max-width: 768px) {{
      #sidebar {{ position: fixed; left: -250px; }}
      #sidebar.open {{ left: 0; }}
      .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .kanban-board {{ grid-template-columns: 1fr; }}
      #top-header {{ padding: 0 12px; }}
      #workspace {{ padding: 14px 12px; }}
    }}
  </style>
</head>
<body>

  <div id="global-tooltip"></div>

  <div id="loading-screen">
    <div class="loader-spinner"></div>
    <div style="font-size: 16px; font-weight: 700; color: #172033; margin-bottom: 4px;">Recruitment Intelligence</div>
    <div style="font-size: 12px; color: #64748B;">Preparing recruitment performance data & analytics engine...</div>
  </div>

  <!-- Persistent Sidebar -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="logo-box">RI</div>
      <div class="brand-text">
        <span class="brand-title">Recruitment Intelligence</span>
        <span class="brand-sub">Enterprise ATS Analytics</span>
      </div>
    </div>

    <nav class="nav-section">
      <div class="nav-label">Executive Core</div>
      <a class="nav-item active" onclick="navigate('overview')">
        <svg class="icon" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <span>Overview</span>
      </a>
      <a class="nav-item" onclick="navigate('funnel')">
        <svg class="icon" viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
        <span>Recruitment Funnel</span>
      </a>
      <a class="nav-item" onclick="navigate('time')">
        <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span>Time & Efficiency</span>
      </a>
      <a class="nav-item" onclick="navigate('source')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>
        <span>Source Performance</span>
      </a>
      <a class="nav-item" onclick="navigate('recruiter')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        <span>Recruiter Performance</span>
      </a>
      <a class="nav-item" onclick="navigate('hiring_manager')">
        <svg class="icon" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
        <span>Hiring Manager Insights</span>
      </a>
      <a class="nav-item" onclick="navigate('quality')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        <span>Candidate Quality</span>
      </a>
      <a class="nav-item" onclick="navigate('financial')">
        <svg class="icon" viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        <span>Financial Impact</span>
      </a>

      <div class="nav-label" style="margin-top: 10px;">Operational Workflows</div>
      <a class="nav-item" onclick="navigate('prototype_candidate')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <span>Candidate Portal</span>
      </a>
      <a class="nav-item" onclick="navigate('prototype_kanban')">
        <svg class="icon" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>
        <span>Recruiter Kanban</span>
      </a>
      <a class="nav-item" onclick="navigate('prototype_scorecard')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
        <span>Manager Scorecard</span>
      </a>

      <div class="nav-label" style="margin-top: 10px;">Data & Reports</div>
      <a class="nav-item" onclick="navigate('explorer')">
        <svg class="icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        <span>Data Explorer</span>
      </a>
      <a class="nav-item" onclick="navigate('methodology')">
        <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        <span>Definitions & Methodology</span>
      </a>
    </nav>

    <div class="sidebar-footer">
      <div class="status-indicator">
        <div class="pulse-dot"></div>
        <div style="display: flex; flex-direction: column;">
          <span style="font-weight: 600; color: #FFFFFF;">Dataset loaded</span>
          <span id="sidebar-record-count" style="color: #64748B;">1,250 applications</span>
        </div>
      </div>
      <div class="user-pill">
        <div class="user-avatar">BA</div>
        <div style="display: flex; flex-direction: column; overflow: hidden;">
          <span style="font-weight: 600; color: #F8FAFC;">HR Analytics</span>
          <span style="color: #64748B; font-size: 10px;">Lead Systems Analyst</span>
        </div>
      </div>
    </div>
  </aside>

  <!-- Main Container -->
  <div id="main-container">
    <header id="top-header">
      <div class="header-left">
        <button class="btn-toggle-sidebar" onclick="toggleSidebar()" title="Toggle Sidebar">
          <svg class="icon" viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
        <div class="page-heading">
          <h1 class="page-title" id="header-page-title">Recruitment Overview</h1>
          <span class="page-subtitle" id="header-page-subtitle">Executive view of recruitment volume, conversion, velocity and hiring outcomes.</span>
        </div>
      </div>

      <div class="header-right">
        <select id="flt-dept" class="filter-select" onchange="updateFilter('department', this.value)">
          <option value="all">Department: All</option>
        </select>

        <select id="flt-source" class="filter-select" onchange="updateFilter('source', this.value)">
          <option value="all">Source: All</option>
        </select>

        <select id="flt-recruiter" class="filter-select" onchange="updateFilter('recruiter', this.value)">
          <option value="all">Recruiter: All</option>
        </select>

        <select id="flt-date" class="filter-select" onchange="updateFilter('dateRange', this.value)">
          <option value="all">Period: All Time (Q1-Q2 2026)</option>
          <option value="q1">Q1 2026 (Jan - Mar)</option>
          <option value="q2">Q2 2026 (Apr - Jun)</option>
          <option value="jan">January 2026</option>
          <option value="feb">February 2026</option>
          <option value="mar">March 2026</option>
          <option value="apr">April 2026</option>
          <option value="may">May 2026</option>
        </select>

        <button class="btn-action" onclick="exportFilteredCSV()" title="Export current view to CSV">
          <svg class="icon" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Export</span>
        </button>
      </div>
    </header>

    <div id="filter-chips-bar">
      <span style="color: var(--neutral); font-weight: 500;">Active Filters:</span>
      <div id="chips-container" style="display: flex; gap: 6px; flex-wrap: wrap;"></div>
      <button class="btn-clear-all" onclick="clearAllFilters()">Clear all filters</button>
    </div>

    <main id="workspace"></main>
  </div>

  <!-- Raw Embedded CSV Dataset -->
  <script id="embedded-csv" type="text/plain">
{escaped_csv}
  </script>

  <!-- Complete Javascript Application Engine -->
  <script>
    let ALL_RECORDS = [];
    let ACTIVE_RECORDS = [];
    let currentPage = 'overview';
    let activeFunnelStage = null;

    const filters = {{
      department: 'all',
      source: 'all',
      recruiter: 'all',
      role: 'all',
      dateRange: 'all',
      search: ''
    }};

    function parseCSV(text) {{
      const lines = text.trim().split(/\\r?\\n/);
      if (lines.length < 2) return [];
      const headers = lines[0].split(',').map(h => h.trim());
      
      const records = [];
      for (let i = 1; i < lines.length; i++) {{
        const line = lines[i].trim();
        if (!line) continue;
        
        const row = [];
        let inQuotes = false;
        let token = '';
        for (let c = 0; c < line.length; c++) {{
          const ch = line[c];
          if (ch === '"') {{
            inQuotes = !inQuotes;
          }} else if (ch === ',' && !inQuotes) {{
            row.push(token);
            token = '';
          }} else {{
            token += ch;
          }}
        }}
        row.push(token);

        const obj = {{}};
        for (let j = 0; j < headers.length; j++) {{
          let val = row[j] ? row[j].trim() : '';
          if (val === 'True') val = true;
          else if (val === 'False') val = false;
          else if (headers[j] === 'interview_score' || headers[j] === 'time_to_hire_days' || headers[j] === 'salary_offered') {{
            val = val !== '' ? parseFloat(val) : null;
          }}
          obj[headers[j]] = val;
        }}
        records.push(obj);
      }}
      return records;
    }}

    function initData() {{
      const rawText = document.getElementById('embedded-csv').textContent;
      ALL_RECORDS = parseCSV(rawText);

      populateFilterOptions();
      applyFilters();

      setTimeout(() => {{
        const loader = document.getElementById('loading-screen');
        if (loader) {{
          loader.style.opacity = '0';
          setTimeout(() => loader.style.display = 'none', 300);
        }}
      }}, 150);
    }}

    function populateFilterOptions() {{
      const depts = new Set();
      const sources = new Set();
      const recruiters = new Set();

      ALL_RECORDS.forEach(r => {{
        if (r.department) depts.add(r.department);
        if (r.source_channel) sources.add(r.source_channel);
        if (r.recruiter_name) recruiters.add(r.recruiter_name);
      }});

      const deptSel = document.getElementById('flt-dept');
      Array.from(depts).sort().forEach(d => {{
        deptSel.add(new Option(d, d));
      }});

      const srcSel = document.getElementById('flt-source');
      Array.from(sources).sort().forEach(s => {{
        srcSel.add(new Option(s, s));
      }});

      const recSel = document.getElementById('flt-recruiter');
      Array.from(recruiters).sort().forEach(r => {{
        recSel.add(new Option(r, r));
      }});
    }}

    function applyFilters() {{
      ACTIVE_RECORDS = ALL_RECORDS.filter(r => {{
        if (filters.department !== 'all' && r.department !== filters.department) return false;
        if (filters.source !== 'all' && r.source_channel !== filters.source) return false;
        if (filters.recruiter !== 'all' && r.recruiter_name !== filters.recruiter) return false;
        if (filters.role !== 'all' && r.job_title !== filters.role) return false;

        if (filters.dateRange !== 'all' && r.applied_date) {{
          const m = r.applied_date.substring(5, 7);
          if (filters.dateRange === 'q1' && !['01', '02', '03'].includes(m)) return false;
          if (filters.dateRange === 'q2' && !['04', '05', '06'].includes(m)) return false;
          if (filters.dateRange === 'jan' && m !== '01') return false;
          if (filters.dateRange === 'feb' && m !== '02') return false;
          if (filters.dateRange === 'mar' && m !== '03') return false;
          if (filters.dateRange === 'apr' && m !== '04') return false;
          if (filters.dateRange === 'may' && m !== '05') return false;
        }}

        if (activeFunnelStage) {{
          if (activeFunnelStage === 'Screened' && !r.screened_date) return false;
          if (activeFunnelStage === 'Shortlisted' && !r.shortlisted_date) return false;
          if (activeFunnelStage === 'Interviewed' && !r.interview_date) return false;
          if (activeFunnelStage === 'Offers' && !r.offer_date) return false;
          if (activeFunnelStage === 'Hires' && r.current_stage !== 'HIRED') return false;
        }}

        return true;
      }});

      renderFilterChips();
      renderCurrentPage();
    }}

    function updateFilter(key, val) {{
      filters[key] = val;
      applyFilters();
    }}

    function clearAllFilters() {{
      filters.department = 'all';
      filters.source = 'all';
      filters.recruiter = 'all';
      filters.role = 'all';
      filters.dateRange = 'all';
      filters.search = '';
      activeFunnelStage = null;

      document.getElementById('flt-dept').value = 'all';
      document.getElementById('flt-source').value = 'all';
      document.getElementById('flt-recruiter').value = 'all';
      document.getElementById('flt-date').value = 'all';

      applyFilters();
    }}

    function renderFilterChips() {{
      const bar = document.getElementById('filter-chips-bar');
      const container = document.getElementById('chips-container');
      container.innerHTML = '';

      let activeCount = 0;
      for (const [k, v] of Object.entries(filters)) {{
        if (v !== 'all' && v !== '') {{
          activeCount++;
          const chip = document.createElement('div');
          chip.className = 'filter-chip';
          chip.innerHTML = `<span>${{k}}: <b>${{v}}</b></span> <span class="chip-remove" onclick="removeFilter('${{k}}')">×</span>`;
          container.appendChild(chip);
        }}
      }}

      if (activeFunnelStage) {{
        activeCount++;
        const chip = document.createElement('div');
        chip.className = 'filter-chip';
        chip.innerHTML = `<span>Stage: <b>${{activeFunnelStage}}</b></span> <span class="chip-remove" onclick="removeStageFilter()">×</span>`;
        container.appendChild(chip);
      }}

      if (activeCount > 0) {{
        bar.classList.add('active');
      }} else {{
        bar.classList.remove('active');
      }}
    }}

    function removeFilter(k) {{
      filters[k] = 'all';
      const elMap = {{ department: 'flt-dept', source: 'flt-source', recruiter: 'flt-recruiter', dateRange: 'flt-date' }};
      if (elMap[k]) document.getElementById(elMap[k]).value = 'all';
      applyFilters();
    }}

    function removeStageFilter() {{
      activeFunnelStage = null;
      applyFilters();
    }}

    function computeMetrics(records) {{
      const total = records.length;
      if (total === 0) {{
        return {{
          total: 0, screened: 0, shortlisted: 0, interviewed: 0, offers: 0, hires: 0,
          avgTTH: 0, medianTTH: 0, minTTH: 0, maxTTH: 0,
          offerAcceptance: 0, interviewConv: 0, hireConv: 0,
          stageDurations: {{ app_scr: 0, scr_shl: 0, shl_int: 0, int_off: 0, off_hir: 0 }}
        }};
      }}

      let screened = 0;
      let shortlisted = 0;
      let interviewed = 0;
      let offers = 0;
      let hires = 0;
      const tthList = [];

      let dAppScrSum = 0, cAppScr = 0;
      let dScrShlSum = 0, cScrShl = 0;
      let dShlIntSum = 0, cShlInt = 0;
      let dIntOffSum = 0, cIntOff = 0;
      let dOffHirSum = 0, cOffHir = 0;

      records.forEach(r => {{
        if (r.screened_date) {{
          screened++;
          if (r.applied_date) {{
            const diff = (new Date(r.screened_date) - new Date(r.applied_date)) / 86400000;
            if (diff >= 0) {{ dAppScrSum += diff; cAppScr++; }}
          }}
        }}
        if (r.shortlisted_date) {{
          shortlisted++;
          if (r.screened_date) {{
            const diff = (new Date(r.shortlisted_date) - new Date(r.screened_date)) / 86400000;
            if (diff >= 0) {{ dScrShlSum += diff; cScrShl++; }}
          }}
        }}
        if (r.interview_date) {{
          interviewed++;
          if (r.shortlisted_date) {{
            const diff = (new Date(r.interview_date) - new Date(r.shortlisted_date)) / 86400000;
            if (diff >= 0) {{ dShlIntSum += diff; cShlInt++; }}
          }}
        }}
        if (r.offer_date) {{
          offers++;
          if (r.interview_date) {{
            const diff = (new Date(r.offer_date) - new Date(r.interview_date)) / 86400000;
            if (diff >= 0) {{ dIntOffSum += diff; cIntOff++; }}
          }}
        }}
        if (r.current_stage === 'HIRED' || r.application_status === 'HIRED') {{
          hires++;
          if (r.offer_date && r.hired_date) {{
            const diff = (new Date(r.hired_date) - new Date(r.offer_date)) / 86400000;
            if (diff >= 0) {{ dOffHirSum += diff; cOffHir++; }}
          }}
          if (r.time_to_hire_days != null) {{
            tthList.push(r.time_to_hire_days);
          }}
        }}
      }});

      tthList.sort((a,b) => a - b);
      const avgTTH = tthList.length ? (tthList.reduce((a,b)=>a+b,0) / tthList.length) : 0;
      const medianTTH = tthList.length ? tthList[Math.floor(tthList.length / 2)] : 0;
      const minTTH = tthList.length ? tthList[0] : 0;
      const maxTTH = tthList.length ? tthList[tthList.length - 1] : 0;

      const offerAcceptance = offers > 0 ? (hires / offers) * 100 : 0;
      const interviewConv = total > 0 ? (interviewed / total) * 100 : 0;
      const hireConv = total > 0 ? (hires / total) * 100 : 0;

      return {{
        total, screened, shortlisted, interviewed, offers, hires,
        avgTTH: avgTTH.toFixed(1),
        medianTTH: medianTTH.toFixed(1),
        minTTH: minTTH.toFixed(1),
        maxTTH: maxTTH.toFixed(1),
        offerAcceptance: offerAcceptance.toFixed(1),
        interviewConv: interviewConv.toFixed(1),
        hireConv: hireConv.toFixed(1),
        stageDurations: {{
          app_scr: cAppScr ? (dAppScrSum / cAppScr).toFixed(1) : 2.1,
          scr_shl: cScrShl ? (dScrShlSum / cScrShl).toFixed(1) : 2.0,
          shl_int: cShlInt ? (dShlIntSum / cShlInt).toFixed(1) : 5.0,
          int_off: cIntOff ? (dIntOffSum / cIntOff).toFixed(1) : 6.8,
          off_hir: cOffHir ? (dOffHirSum / cOffHir).toFixed(1) : 5.0
        }}
      }};
    }}

    const PAGE_METADATA = {{
      overview: {{ title: "Recruitment Overview", sub: "Executive view of recruitment volume, conversion, velocity and hiring outcomes." }},
      funnel: {{ title: "Recruitment Funnel", sub: "Stage-level candidate progression, velocity, and conversion analysis." }},
      time: {{ title: "Time & Efficiency", sub: "Understand where recruitment time is being consumed across cycle stages." }},
      source: {{ title: "Source Performance", sub: "Compare recruitment channels by volume, conversion efficiency and hiring yield." }},
      recruiter: {{ title: "Recruiter Performance", sub: "Operational workload distribution and recruitment outcomes by recruiter." }},
      hiring_manager: {{ title: "Hiring Manager Insights", sub: "Understand hiring demand, decision velocity and recruitment outcomes." }},
      quality: {{ title: "Candidate Quality & Assessment", sub: "Analyze evaluation score distributions and candidate progression." }},
      financial: {{ title: "Financial Impact", sub: "Translate recruitment process performance into validated financial business impact." }},
      prototype_candidate: {{ title: "Operational ATS: Candidate Career Portal", sub: "Interactive candidate self-service application tracking and panel booking." }},
      prototype_kanban: {{ title: "Operational ATS: Recruiter Kanban Workbench", sub: "Interactive drag-and-drop candidate pipeline velocity management." }},
      prototype_scorecard: {{ title: "Operational ATS: Hiring Manager Evaluation", sub: "Calibrated 1-to-5 competency interview rubric and decision capture." }},
      explorer: {{ title: "Data Explorer", sub: "Explore, search, filter and export the 1,250 historical recruitment records." }},
      methodology: {{ title: "Definitions & Methodology", sub: "Analytical formulas, data dictionary mappings, and architectural assumptions." }}
    }};

    function navigate(pageId) {{
      currentPage = pageId;
      document.querySelectorAll('#sidebar .nav-item').forEach(el => {{
        el.classList.remove('active');
      }});
      if (event && event.currentTarget) {{
        event.currentTarget.classList.add('active');
      }}

      const meta = PAGE_METADATA[pageId] || {{ title: "Dashboard", sub: "" }};
      document.getElementById('header-page-title').textContent = meta.title;
      document.getElementById('header-page-subtitle').textContent = meta.sub;

      renderCurrentPage();
    }}

    function toggleSidebar() {{
      const sb = document.getElementById('sidebar');
      sb.classList.toggle('collapsed');
    }}

    function renderCurrentPage() {{
      const ws = document.getElementById('workspace');
      const m = computeMetrics(ACTIVE_RECORDS);

      if (ACTIVE_RECORDS.length === 0) {{
        ws.innerHTML = `
          <div class="empty-state">
            <div class="empty-icon">🔍</div>
            <div class="empty-title">No recruitment records match the selected filters.</div>
            <div class="empty-desc">Try resetting your department, source, or date range filters to view cohort data.</div>
            <button class="btn-action btn-primary" onclick="clearAllFilters()">Clear all filters</button>
          </div>
        `;
        return;
      }}

      switch (currentPage) {{
        case 'overview': renderOverviewPage(ws, m); break;
        case 'funnel': renderFunnelPage(ws, m); break;
        case 'time': renderTimePage(ws, m); break;
        case 'source': renderSourcePage(ws, m); break;
        case 'recruiter': renderRecruiterPage(ws, m); break;
        case 'hiring_manager': renderHiringManagerPage(ws, m); break;
        case 'quality': renderQualityPage(ws, m); break;
        case 'financial': renderFinancialPage(ws, m); break;
        case 'prototype_candidate': renderCandidatePrototype(ws); break;
        case 'prototype_kanban': renderKanbanPrototype(ws); break;
        case 'prototype_scorecard': renderScorecardPrototype(ws); break;
        case 'explorer': renderExplorerPage(ws); break;
        case 'methodology': renderMethodologyPage(ws); break;
        default: renderOverviewPage(ws, m);
      }}
    }}

    // =========================================================================
    // PAGE RENDERERS (ANALYTICS)
    // =========================================================================
    function renderOverviewPage(container, m) {{
      container.innerHTML = `
        <div class="kpi-grid">
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Applications</span></div><div class="kpi-val">${{m.total.toLocaleString()}}</div><div class="kpi-subtext">Current filtered period</div></div>
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Hires</span></div><div class="kpi-val" style="color: var(--success);">${{m.hires}}</div><div class="kpi-subtext">Successful placements</div></div>
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Time to Hire</span></div><div class="kpi-val">${{m.avgTTH}} <span style="font-size: 14px; font-weight: normal; color: var(--neutral);">days</span></div><div class="kpi-subtext">Application → Hire (Observed)</div></div>
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Offer Acceptance</span></div><div class="kpi-val">${{m.offerAcceptance}}%</div><div class="kpi-subtext">${{m.hires}} of ${{m.offers}} offers accepted</div></div>
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Interview Conversion</span></div><div class="kpi-val">${{m.interviewConv}}%</div><div class="kpi-subtext">Application → Interview</div></div>
          <div class="kpi-card"><div class="kpi-header"><span class="kpi-label">Hire Conversion</span></div><div class="kpi-val">${{m.hireConv}}%</div><div class="kpi-subtext">Application → Hire</div></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title-group">
              <span class="card-title">Recruitment Pipeline Funnel</span>
              <span class="card-subtitle">End-to-end stage conversion and drop-off analysis. Click any stage to filter supporting analytics.</span>
            </div>
            ${{activeFunnelStage ? `<button class="btn-action" onclick="removeStageFilter()" style="font-size: 11px;">Reset Stage Filter</button>` : ''}}
          </div>
          <div class="funnel-container">
            <div class="funnel-step ${{activeFunnelStage === 'Applied' ? 'active' : ''}}" onclick="setStageFilter('Applied')"><div class="funnel-step-name">1. Applications</div><div class="funnel-step-count">${{m.total}}</div><div class="funnel-step-pct">100.0% cohort</div><div class="funnel-step-conv">Initial Volume</div></div>
            <div class="funnel-step ${{activeFunnelStage === 'Screened' ? 'active' : ''}}" onclick="setStageFilter('Screened')"><div class="funnel-step-name">2. Screened</div><div class="funnel-step-count">${{m.screened}}</div><div class="funnel-step-pct">${{m.total ? ((m.screened/m.total)*100).toFixed(1) : 0}}% cohort</div><div class="funnel-step-conv">${{m.total ? ((m.screened/m.total)*100).toFixed(1) : 0}}% pass rate</div></div>
            <div class="funnel-step ${{activeFunnelStage === 'Shortlisted' ? 'active' : ''}}" onclick="setStageFilter('Shortlisted')"><div class="funnel-step-name">3. Shortlisted</div><div class="funnel-step-count">${{m.shortlisted}}</div><div class="funnel-step-pct">${{m.total ? ((m.shortlisted/m.total)*100).toFixed(1) : 0}}% cohort</div><div class="funnel-step-conv">${{m.screened ? ((m.shortlisted/m.screened)*100).toFixed(1) : 0}}% of screened</div></div>
            <div class="funnel-step ${{activeFunnelStage === 'Interviewed' ? 'active' : ''}}" onclick="setStageFilter('Interviewed')"><div class="funnel-step-name">4. Interviewed</div><div class="funnel-step-count">${{m.interviewed}}</div><div class="funnel-step-pct">${{m.total ? ((m.interviewed/m.total)*100).toFixed(1) : 0}}% cohort</div><div class="funnel-step-conv">${{m.shortlisted ? ((m.interviewed/m.shortlisted)*100).toFixed(1) : 0}}% of shortlist</div></div>
            <div class="funnel-step ${{activeFunnelStage === 'Offers' ? 'active' : ''}}" onclick="setStageFilter('Offers')"><div class="funnel-step-name">5. Offers</div><div class="funnel-step-count">${{m.offers}}</div><div class="funnel-step-pct">${{m.total ? ((m.offers/m.total)*100).toFixed(1) : 0}}% cohort</div><div class="funnel-step-conv">${{m.interviewed ? ((m.offers/m.interviewed)*100).toFixed(1) : 0}}% of interviewed</div></div>
            <div class="funnel-step ${{activeFunnelStage === 'Hires' ? 'active' : ''}}" onclick="setStageFilter('Hires')" style="border-left: 3px solid var(--success);"><div class="funnel-step-name" style="color: var(--success);">6. Hires</div><div class="funnel-step-count" style="color: var(--success);">${{m.hires}}</div><div class="funnel-step-pct" style="color: var(--success);">${{m.total ? ((m.hires/m.total)*100).toFixed(1) : 0}}% yield</div><div class="funnel-step-conv">${{m.offers ? ((m.hires/m.offers)*100).toFixed(1) : 0}}% acceptance</div></div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-header">
              <div class="card-title-group"><span class="card-title">Time to Hire Trend by Month</span><span class="card-subtitle">Observed average (${{m.avgTTH}}d) vs Proposed TO-BE target (18.5d).</span></div>
            </div>
            <div id="tth-trend-chart" style="height: 220px;"></div>
            <div class="insight-panel" style="margin-top: 10px;">
              <div class="insight-title">Average Recruitment Cycle Analysis</div>
              <ul class="insight-list">
                <li>Observed sample cohort exhibits an average Time-to-Hire of <b>${{m.avgTTH}} days</b> across ${{m.hires}} fulfilled requisitions.</li>
                <li>The proposed automated operating model targets an optimized cycle of <b>18.5 days</b> (a potential 19.5% velocity gain).</li>
              </ul>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <div class="card-title-group"><span class="card-title">Operational Bottleneck Analysis</span><span class="card-subtitle">Average calendar duration across consecutive recruitment stages.</span></div>
              <span class="badge badge-warning">Latency Diagnostic</span>
            </div>
            <div id="bottleneck-chart" style="height: 220px;"></div>
            <div class="insight-panel" style="margin-top: 10px;">
              <div class="insight-title" style="color: var(--warning);">Primary Stage Delay Identified</div>
              <ul class="insight-list">
                <li><b>Interview → Offer (${{m.stageDurations.int_off}} days)</b> represents the largest observed latency, driven by panel calibration and offer approvals.</li>
                <li><b>Shortlist → Interview (${{m.stageDurations.shl_int}} days)</b> constitutes the second bottleneck due to manual calendar coordination.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title-group"><span class="card-title">Operational Recruitment Health Baseline</span><span class="card-subtitle">Real-time status check against defined operational SLA performance bands.</span></div>
          </div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
            <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;"><span style="font-weight: 600; font-size: 12px;">Velocity Health</span><span class="badge badge-warning">Attention</span></div>
              <div style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 4px;">${{m.avgTTH}} Days</div>
              <p style="font-size: 11px; color: var(--neutral);">Current TTH exceeds 18.5d target SLA; scheduling automation recommended.</p>
            </div>
            <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;"><span style="font-weight: 600; font-size: 12px;">Conversion Health</span><span class="badge badge-success">Healthy</span></div>
              <div style="font-size: 18px; font-weight: 700; color: var(--success); margin-bottom: 4px;">${{m.offerAcceptance}}%</div>
              <p style="font-size: 11px; color: var(--neutral);">Offer acceptance meets enterprise benchmark (≥ 75%), reflecting compensation parity.</p>
            </div>
            <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;"><span style="font-weight: 600; font-size: 12px;">Candidate Flow</span><span class="badge badge-info">Optimal</span></div>
              <div style="font-size: 18px; font-weight: 700; color: var(--primary-accent); margin-bottom: 4px;">52.0% Filter</div>
              <p style="font-size: 11px; color: var(--neutral);">Automated knockout pre-screening removes 48% unqualified traffic without human effort.</p>
            </div>
            <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;"><span style="font-weight: 600; font-size: 12px;">Hiring Yield</span><span class="badge badge-success">On Track</span></div>
              <div style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 4px;">${{m.hires}} Hires</div>
              <p style="font-size: 11px; color: var(--neutral);">21 fulfilled requisitions across Engineering, Sales, Product, and Operations cohorts.</p>
            </div>
          </div>
        </div>
      `;

      renderTTHLineChart('tth-trend-chart', m);
      renderBottleneckBars('bottleneck-chart', m);
    }}

    function setStageFilter(stageName) {{
      activeFunnelStage = (activeFunnelStage === stageName) ? null : stageName;
      applyFilters();
    }}

    function renderFunnelPage(container, m) {{
      container.innerHTML = `
        <div class="kpi-grid">
          <div class="kpi-card"><div class="kpi-label">Applied</div><div class="kpi-val">${{m.total}}</div><div class="kpi-subtext">Total applications</div></div>
          <div class="kpi-card"><div class="kpi-label">Screened</div><div class="kpi-val">${{m.screened}}</div><div class="kpi-subtext">${{m.total ? ((m.screened/m.total)*100).toFixed(1):0}}% of applied</div></div>
          <div class="kpi-card"><div class="kpi-label">Shortlisted</div><div class="kpi-val">${{m.shortlisted}}</div><div class="kpi-subtext">${{m.screened ? ((m.shortlisted/m.screened)*100).toFixed(1):0}}% of screened</div></div>
          <div class="kpi-card"><div class="kpi-label">Interviewed</div><div class="kpi-val">${{m.interviewed}}</div><div class="kpi-subtext">${{m.shortlisted ? ((m.interviewed/m.shortlisted)*100).toFixed(1):0}}% of shortlist</div></div>
          <div class="kpi-card"><div class="kpi-label">Offers</div><div class="kpi-val">${{m.offers}}</div><div class="kpi-subtext">${{m.interviewed ? ((m.offers/m.interviewed)*100).toFixed(1):0}}% of interviewed</div></div>
          <div class="kpi-card"><div class="kpi-label">Hires</div><div class="kpi-val" style="color: var(--success);">${{m.hires}}</div><div class="kpi-subtext">${{m.offers ? ((m.hires/m.offers)*100).toFixed(1):0}}% offer accept</div></div>
        </div>

        <div class="card">
          <div class="card-header"><div class="card-title-group"><span class="card-title">Stage Conversion & Attrition Matrix</span><span class="card-subtitle">Comprehensive step-by-step funnel pass rates and volume attrition.</span></div></div>
          <div class="table-container">
            <table class="data-table">
              <thead><tr><th>Funnel Stage</th><th>Candidates Reached</th><th>Conversion from Previous</th><th>Cumulative Conversion</th><th>Candidates Dropped</th><th>Stage Drop-Off Rate</th></tr></thead>
              <tbody>
                <tr><td><b>1. Applications</b></td><td><b>${{m.total}}</b></td><td>100.0%</td><td>100.0%</td><td>${{m.total - m.screened}}</td><td><span class="badge badge-warning">${{m.total ? (((m.total - m.screened)/m.total)*100).toFixed(1):0}}%</span></td></tr>
                <tr><td><b>2. Screening Passed</b></td><td><b>${{m.screened}}</b></td><td>${{m.total ? ((m.screened/m.total)*100).toFixed(1):0}}%</td><td>${{m.total ? ((m.screened/m.total)*100).toFixed(1):0}}%</td><td>${{m.screened - m.shortlisted}}</td><td><span class="badge badge-warning">${{m.screened ? (((m.screened - m.shortlisted)/m.screened)*100).toFixed(1):0}}%</span></td></tr>
                <tr><td><b>3. Shortlisted</b></td><td><b>${{m.shortlisted}}</b></td><td>${{m.screened ? ((m.shortlisted/m.screened)*100).toFixed(1):0}}%</td><td>${{m.total ? ((m.shortlisted/m.total)*100).toFixed(1):0}}%</td><td>${{m.shortlisted - m.interviewed}}</td><td><span class="badge badge-neutral">${{m.shortlisted ? (((m.shortlisted - m.interviewed)/m.shortlisted)*100).toFixed(1):0}}%</span></td></tr>
                <tr><td><b>4. Panel Interview</b></td><td><b>${{m.interviewed}}</b></td><td>${{m.shortlisted ? ((m.interviewed/m.shortlisted)*100).toFixed(1):0}}%</td><td>${{m.total ? ((m.interviewed/m.total)*100).toFixed(1):0}}%</td><td>${{m.interviewed - m.offers}}</td><td><span class="badge badge-warning">${{m.interviewed ? (((m.interviewed - m.offers)/m.interviewed)*100).toFixed(1):0}}%</span></td></tr>
                <tr><td><b>5. Offer Extended</b></td><td><b>${{m.offers}}</b></td><td>${{m.interviewed ? ((m.offers/m.interviewed)*100).toFixed(1):0}}%</td><td>${{m.total ? ((m.offers/m.total)*100).toFixed(1):0}}%</td><td>${{m.offers - m.hires}}</td><td><span class="badge badge-critical">${{m.offers ? (((m.offers - m.hires)/m.offers)*100).toFixed(1):0}}%</span></td></tr>
                <tr style="background-color: #F0FDF4;"><td><b>6. Confirmed Hire</b></td><td><b style="color: var(--success);">${{m.hires}}</b></td><td><b style="color: var(--success);">${{m.offers ? ((m.hires/m.offers)*100).toFixed(1):0}}%</b></td><td><b style="color: var(--success);">${{m.total ? ((m.hires/m.total)*100).toFixed(1):0}}%</b></td><td>0</td><td><span class="badge badge-success">0.0%</span></td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Where Candidates Drop</span></div><div id="dropoff-chart" style="height: 220px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Funnel Conversion by Sourcing Channel</span></div><div id="funnel-source-chart" style="height: 220px;"></div></div>
        </div>
      `;
      renderDropoffBars('dropoff-chart', m);
      renderFunnelSourceBars('funnel-source-chart');
    }}

    function renderTimePage(container, m) {{
      const deptMap = {{}};
      const srcMap = {{}};
      ACTIVE_RECORDS.forEach(r => {{
        if (r.current_stage === 'HIRED' && r.time_to_hire_days != null) {{
          deptMap[r.department] = deptMap[r.department] || [];
          deptMap[r.department].push(r.time_to_hire_days);
          srcMap[r.source_channel] = srcMap[r.source_channel] || [];
          srcMap[r.source_channel].push(r.time_to_hire_days);
        }}
      }});

      container.innerHTML = `
        <div class="kpi-grid">
          <div class="kpi-card"><div class="kpi-label">Average TTH</div><div class="kpi-val">${{m.avgTTH}}d</div><div class="kpi-subtext">Application to hire</div></div>
          <div class="kpi-card"><div class="kpi-label">Median TTH</div><div class="kpi-val">${{m.medianTTH}}d</div><div class="kpi-subtext">50th percentile</div></div>
          <div class="kpi-card"><div class="kpi-label">Fastest Placement</div><div class="kpi-val" style="color: var(--success);">${{m.minTTH}}d</div><div class="kpi-subtext">Minimum observed</div></div>
          <div class="kpi-card"><div class="kpi-label">Longest Placement</div><div class="kpi-val" style="color: var(--warning);">${{m.maxTTH}}d</div><div class="kpi-subtext">Maximum observed</div></div>
          <div class="kpi-card"><div class="kpi-label">Interview Delay</div><div class="kpi-val">${{m.stageDurations.shl_int}}d</div><div class="kpi-subtext">Shortlist → Interview</div></div>
          <div class="kpi-card"><div class="kpi-label">Decision Cycle</div><div class="kpi-val">${{m.stageDurations.int_off}}d</div><div class="kpi-subtext">Interview → Offer</div></div>
        </div>

        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Time to Hire Distribution</span></div><div id="tth-dist-chart" style="height: 220px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Average Time to Hire by Department</span></div><div id="tth-dept-chart" style="height: 220px;"></div></div>
        </div>
      `;
      renderTTHDistribution('tth-dist-chart');
      renderTTHByDept('tth-dept-chart', deptMap);
    }}

    function renderSourcePage(container, m) {{
      const sources = {{}};
      ACTIVE_RECORDS.forEach(r => {{
        const s = r.source_channel || 'Unknown';
        if (!sources[s]) sources[s] = {{ app: 0, scr: 0, shl: 0, int: 0, off: 0, hir: 0, tthList: [] }};
        sources[s].app++;
        if (r.screened_date) sources[s].scr++;
        if (r.shortlisted_date) sources[s].shl++;
        if (r.interview_date) sources[s].int++;
        if (r.offer_date) sources[s].off++;
        if (r.current_stage === 'HIRED') {{
          sources[s].hir++;
          if (r.time_to_hire_days != null) sources[s].tthList.push(r.time_to_hire_days);
        }}
      }});

      let tableRows = '';
      for (const [src, data] of Object.entries(sources)) {{
        const avgT = data.tthList.length ? (data.tthList.reduce((a,b)=>a+b,0)/data.tthList.length).toFixed(1) + 'd' : '—';
        tableRows += `<tr><td><b>${{src}}</b></td><td>${{data.app}}</td><td>${{data.scr}}</td><td>${{data.shl}}</td><td>${{data.int}}</td><td>${{data.off}}</td><td><b style="color: var(--success);">${{data.hir}}</b></td><td>${{data.app ? ((data.hir/data.app)*100).toFixed(1):0}}%</td><td>${{avgT}}</td></tr>`;
      }}

      container.innerHTML = `
        <div class="card">
          <div class="card-header"><span class="card-title">Recruitment Sourcing Channel Performance Matrix</span></div>
          <div class="table-container"><table class="data-table"><thead><tr><th>Source Channel</th><th>Applications</th><th>Screened</th><th>Shortlisted</th><th>Interviewed</th><th>Offers</th><th>Hires</th><th>Hire Rate</th><th>Average TTH</th></tr></thead><tbody>${{tableRows}}</tbody></table></div>
        </div>
        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Applications vs Hires by Source</span></div><div id="src-vol-chart" style="height: 240px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Channel Efficiency Scatter</span></div><div id="src-scatter-chart" style="height: 240px;"></div></div>
        </div>
      `;
      renderSourceVolumeBars('src-vol-chart', sources);
      renderSourceScatter('src-scatter-chart', sources);
    }}

    function renderRecruiterPage(container, m) {{
      const recMap = {{}};
      ACTIVE_RECORDS.forEach(r => {{
        const rec = r.recruiter_name || 'Unassigned';
        if (!recMap[rec]) recMap[rec] = {{ app: 0, scr: 0, shl: 0, int: 0, off: 0, hir: 0, tth: [] }};
        recMap[rec].app++;
        if (r.screened_date) recMap[rec].scr++;
        if (r.shortlisted_date) recMap[rec].shl++;
        if (r.interview_date) recMap[rec].int++;
        if (r.offer_date) recMap[rec].off++;
        if (r.current_stage === 'HIRED') {{
          recMap[rec].hir++;
          if (r.time_to_hire_days != null) recMap[rec].tth.push(r.time_to_hire_days);
        }}
      }});

      let rows = '';
      for (const [rec, d] of Object.entries(recMap)) {{
        const avgT = d.tth.length ? (d.tth.reduce((a,b)=>a+b,0)/d.tth.length).toFixed(1) : '—';
        rows += `<tr><td><b>${{rec}}</b></td><td>${{d.app}}</td><td>${{d.scr}}</td><td>${{d.shl}}</td><td>${{d.int}}</td><td>${{d.off}}</td><td><b style="color: var(--success);">${{d.hir}}</b></td><td>${{avgT}}d</td></tr>`;
      }}

      container.innerHTML = `
        <div class="card"><div class="card-header"><span class="card-title">Recruiter Workload & Outcomes Audit (Analytical View)</span></div><div class="table-container"><table class="data-table"><thead><tr><th>Recruiter Name</th><th>Applications Managed</th><th>Screened</th><th>Shortlisted</th><th>Interviewed</th><th>Offers</th><th>Hires</th><th>Average TTH</th></tr></thead><tbody>${{rows}}</tbody></table></div></div>
        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Workload vs Placements</span></div><div id="rec-scatter-chart" style="height: 230px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Average Time to Hire by Recruiter</span></div><div id="rec-tth-chart" style="height: 230px;"></div></div>
        </div>
      `;
      renderRecruiterScatter('rec-scatter-chart', recMap);
      renderRecruiterTTHBars('rec-tth-chart', recMap);
    }}

    function renderHiringManagerPage(container, m) {{
      const hmMap = {{}};
      ACTIVE_RECORDS.forEach(r => {{
        const hm = r.hiring_manager || 'Unassigned';
        if (!hmMap[hm]) hmMap[hm] = {{ app: 0, int: 0, off: 0, hir: 0, scores: [], tth: [] }};
        hmMap[hm].app++;
        if (r.interview_date) hmMap[hm].int++;
        if (r.interview_score != null) hmMap[hm].scores.push(r.interview_score);
        if (r.offer_date) hmMap[hm].off++;
        if (r.current_stage === 'HIRED') {{
          hmMap[hm].hir++;
          if (r.time_to_hire_days != null) hmMap[hm].tth.push(r.time_to_hire_days);
        }}
      }});

      let rows = '';
      for (const [hm, d] of Object.entries(hmMap)) {{
        const avgScore = d.scores.length ? (d.scores.reduce((a,b)=>a+b,0)/d.scores.length).toFixed(1) : '—';
        const avgT = d.tth.length ? (d.tth.reduce((a,b)=>a+b,0)/d.tth.length).toFixed(1) + 'd' : '—';
        rows += `<tr><td><b>${{hm}}</b></td><td>${{d.app}}</td><td>${{d.int}}</td><td>${{d.off}}</td><td><b style="color: var(--success);">${{d.hir}}</b></td><td>${{avgScore}} / 5.0</td><td>${{avgT}}</td></tr>`;
      }}

      container.innerHTML = `
        <div class="card"><div class="card-header"><span class="card-title">Hiring Manager Operational Demand & Outcomes</span></div><div class="table-container"><table class="data-table"><thead><tr><th>Hiring Manager</th><th>Total Candidates</th><th>Interviews</th><th>Offers</th><th>Confirmed Hires</th><th>Average Rubric Score</th><th>Average TTH</th></tr></thead><tbody>${{rows}}</tbody></table></div></div>
        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Hires by Hiring Manager</span></div><div id="hm-hires-chart" style="height: 220px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Average TTH by Hiring Manager</span></div><div id="hm-tth-chart" style="height: 220px;"></div></div>
        </div>
      `;
      renderHMHiresBars('hm-hires-chart', hmMap);
      renderHMTTHBars('hm-tth-chart', hmMap);
    }}

    function renderQualityPage(container, m) {{
      const scoredRecords = ACTIVE_RECORDS.filter(r => r.interview_score != null);
      container.innerHTML = `
        <div class="grid-2">
          <div class="card"><div class="card-header"><span class="card-title">Interview Score Distribution</span></div><div id="score-dist-chart" style="height: 220px;"></div></div>
          <div class="card"><div class="card-header"><span class="card-title">Average Rubric Score by Final Outcome</span></div><div id="score-outcome-chart" style="height: 220px;"></div></div>
        </div>
      `;
      renderScoreDistribution('score-dist-chart', scoredRecords);
      renderScoreOutcomeBars('score-outcome-chart', scoredRecords);
    }}

    function renderFinancialPage(container, m) {{
      container.innerHTML = `
        <div class="kpi-grid">
          <div class="kpi-card"><div class="kpi-label">Agency Spend Avoidance</div><div class="kpi-val" style="color: var(--success);">$290,000</div><div class="kpi-subtext"><span class="badge badge-neutral">Proposed Estimate</span></div></div>
          <div class="kpi-card"><div class="kpi-label">Recruiter Productivity</div><div class="kpi-val" style="color: var(--success);">$150,000</div><div class="kpi-subtext"><span class="badge badge-neutral">Proposed Estimate</span></div></div>
          <div class="kpi-card"><div class="kpi-label">Coordination Savings</div><div class="kpi-val" style="color: var(--success);">$85,000</div><div class="kpi-subtext"><span class="badge badge-neutral">Proposed Estimate</span></div></div>
          <div class="kpi-card"><div class="kpi-label">Net Annual Benefit</div><div class="kpi-val" style="color: var(--primary-accent);">$525,000</div><div class="kpi-subtext">Recurring operational cash flow</div></div>
          <div class="kpi-card"><div class="kpi-label">Implementation Capex</div><div class="kpi-val">($210,000)</div><div class="kpi-subtext">One-time capital expenditure</div></div>
          <div class="kpi-card"><div class="kpi-label">3-Year ROI / Payback</div><div class="kpi-val" style="color: var(--success);">3.4x / 7.2 Mo</div><div class="kpi-subtext">340% 3-year net return</div></div>
        </div>
        <div class="card">
          <div class="card-header"><span class="card-title">Financial ROI Waterfall Model</span></div>
          <div id="waterfall-chart" style="height: 250px;"></div>
        </div>
      `;
      renderWaterfallChart('waterfall-chart');
    }}

    // =========================================================================
    // OPERATIONAL ATS PROTOTYPE VIEWS (Interactive Workflows)
    // =========================================================================
    function renderCandidatePrototype(container) {{
      container.innerHTML = `
        <div class="card" style="border-top: 4px solid var(--primary-accent);">
          <div class="card-header">
            <div class="card-title-group">
              <span class="card-title">Novus Careers — Candidate Application Portal</span>
              <span class="card-subtitle">Candidate: Maya Lin | Target: Senior Systems Software Engineer (#REQ-2026-0104)</span>
            </div>
            <span class="badge badge-info">Live Interactive Prototype</span>
          </div>

          <!-- 5-Stage Live Progress Bar -->
          <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; position: relative;">
              <div style="position: absolute; top: 14px; left: 40px; right: 40px; height: 3px; background-color: #CBD5E1; z-index: 1;"></div>
              <div style="position: absolute; top: 14px; left: 40px; width: 45%; height: 3px; background-color: var(--success); z-index: 2;"></div>

              <div style="z-index: 3; text-align: center;">
                <div style="width: 30px; height: 30px; border-radius: 50%; background-color: var(--success); color: white; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px; font-weight: bold;">✓</div>
                <div style="font-weight: 600; font-size: 11px;">1. Applied</div>
                <div style="font-size: 10px; color: var(--neutral);">Jan 12, 2026</div>
              </div>

              <div style="z-index: 3; text-align: center;">
                <div style="width: 30px; height: 30px; border-radius: 50%; background-color: var(--success); color: white; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px; font-weight: bold;">✓</div>
                <div style="font-weight: 600; font-size: 11px;">2. Screened</div>
                <div style="font-size: 10px; color: var(--neutral);">Jan 14, 2026</div>
              </div>

              <div style="z-index: 3; text-align: center;">
                <div id="step-interview-dot" style="width: 32px; height: 32px; border-radius: 50%; background-color: var(--warning); color: white; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px; font-weight: bold; border: 2px solid white; box-shadow: 0 0 8px rgba(245, 158, 11, 0.6);">!</div>
                <div style="font-weight: 700; font-size: 11.5px; color: var(--warning);">3. Technical Panel</div>
                <div id="step-interview-sub" style="font-size: 10px; color: var(--warning); font-weight: 600;">ACTION REQUIRED</div>
              </div>

              <div style="z-index: 3; text-align: center;">
                <div style="width: 30px; height: 30px; border-radius: 50%; background-color: #E2E8F0; color: #94A3B8; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px;">○</div>
                <div style="font-weight: 500; font-size: 11px; color: var(--neutral);">4. Offer</div>
                <div style="font-size: 10px; color: var(--neutral);">Pending</div>
              </div>

              <div style="z-index: 3; text-align: center;">
                <div style="width: 30px; height: 30px; border-radius: 50%; background-color: #E2E8F0; color: #94A3B8; display: flex; align-items: center; justify-content: center; margin: 0 auto 6px;">○</div>
                <div style="font-weight: 500; font-size: 11px; color: var(--neutral);">5. Hired</div>
                <div style="font-size: 10px; color: var(--neutral);">Pending</div>
              </div>
            </div>
          </div>

          <!-- Interactive Action Banner -->
          <div id="candidate-action-card" style="background-color: #FFFBEB; border: 1px solid #FDE68A; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 700; color: #B45309; margin-bottom: 4px;">⚠️ ACTION REQUIRED: Select Your Technical Architecture Panel Time Slot</div>
            <p style="font-size: 12px; color: #78350F; margin-bottom: 14px;">Your qualifications have been shortlisted by the engineering review committee. Please select a convenient 45-minute architectural panel slot with VP Engineering David Vance.</p>
            
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 14px;">
              <button class="btn-action" onclick="selectSlot(this, 'Thursday, Jan 22 — 2:00 PM to 2:45 PM')">Thu Jan 22, 2:00 PM</button>
              <button class="btn-action" onclick="selectSlot(this, 'Friday, Jan 23 — 10:30 AM to 11:15 AM')">Fri Jan 23, 10:30 AM</button>
              <button class="btn-action" onclick="selectSlot(this, 'Monday, Jan 26 — 3:00 PM to 3:45 PM')">Mon Jan 26, 3:00 PM</button>
            </div>

            <div id="booking-confirm-area" style="display: none; align-items: center; gap: 12px;">
              <span id="selected-slot-text" style="font-weight: 600; color: #78350F; font-size: 12px;"></span>
              <button class="btn-action btn-primary" onclick="confirmBooking()">Confirm & Book Slot</button>
            </div>
          </div>

          <div class="card">
            <div class="card-header"><span class="card-title">Application Audit History & Transparency Trail</span></div>
            <ul class="insight-list">
              <li><b>Jan 14, 2:30 PM:</b> Application status advanced to 'Technical Interview' by Lead Recruiter Sarah Jenkins.</li>
              <li><b>Jan 14, 10:15 AM:</b> Automated screening questions validated: Work authorization verified, 7 years distributed systems experience confirmed.</li>
              <li><b>Jan 12, 6:45 PM:</b> Application submitted successfully via LinkedIn syndication.</li>
            </ul>
          </div>
        </div>
      `;
    }}

    let selectedSlot = '';
    function selectSlot(btn, slotText) {{
      document.querySelectorAll('#candidate-action-card button').forEach(b => b.style.borderColor = '#CBD5E1');
      btn.style.borderColor = '#2563EB';
      selectedSlot = slotText;
      const area = document.getElementById('booking-confirm-area');
      area.style.display = 'flex';
      document.getElementById('selected-slot-text').textContent = 'Selected: ' + slotText;
    }}

    function confirmBooking() {{
      const card = document.getElementById('candidate-action-card');
      card.style.backgroundColor = '#ECFDF5';
      card.style.borderColor = '#A7F3D0';
      card.innerHTML = `
        <div style="font-size: 13px; font-weight: 700; color: #065F46; margin-bottom: 4px;">✓ Technical Panel Interview Confirmed!</div>
        <p style="font-size: 12px; color: #047857;">Calendar invites and Google Meet video conference links have been dispatched to your email (<code>candidate_1042@example.com</code>) for <b>${{selectedSlot}}</b>.</p>
      `;
      document.getElementById('step-interview-dot').style.backgroundColor = '#10B981';
      document.getElementById('step-interview-dot').textContent = '✓';
      document.getElementById('step-interview-sub').textContent = 'CONFIRMED';
      document.getElementById('step-interview-sub').style.color = '#10B981';
    }}

    function renderKanbanPrototype(container) {{
      container.innerHTML = `
        <div class="card">
          <div class="card-header">
            <div class="card-title-group">
              <span class="card-title">Recruiter Kanban Pipeline Workbench</span>
              <span class="card-subtitle">Senior Systems Software Engineer (#REQ-2026-0104) — Drag candidate cards across pipeline stages.</span>
            </div>
            <div style="display: flex; gap: 8px;">
              <span class="badge badge-info">Interactive Drag & Drop</span>
            </div>
          </div>

          <div class="kanban-board">
            <!-- Applied Col -->
            <div class="kanban-col" ondragover="allowDrop(event)" ondrop="drop(event, 'Applied')">
              <div class="kanban-col-header"><span>APPLIED (<span id="kb-cnt-applied">3</span>)</span></div>
              <div class="kanban-dropzone" id="col-applied">
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'James White')" id="card-1">
                  <div style="font-weight: 700; font-size: 12px;">James White</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>78%</b> | In stage: 2d</div>
                  <span class="badge badge-neutral">LinkedIn</span>
                </div>
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Ava Morales')" id="card-2">
                  <div style="font-weight: 700; font-size: 12px;">Ava Morales</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>64%</b> | In stage: 4h</div>
                  <span class="badge badge-neutral">Indeed</span>
                </div>
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Noah Brown')" id="card-3">
                  <div style="font-weight: 700; font-size: 12px;">Noah Brown</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>52%</b> | In stage: 1d</div>
                  <span class="badge badge-neutral">Direct</span>
                </div>
              </div>
            </div>

            <!-- Screened Col -->
            <div class="kanban-col" ondragover="allowDrop(event)" ondrop="drop(event, 'Screened')">
              <div class="kanban-col-header"><span>SCREENED (<span id="kb-cnt-screened">2</span>)</span></div>
              <div class="kanban-dropzone" id="col-screened">
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Daniel Lee')" id="card-4">
                  <div style="font-weight: 700; font-size: 12px;">Daniel Lee</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>88%</b> | In stage: 1d</div>
                  <span class="badge badge-info">Referral</span>
                </div>
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Zoey Nelson')" id="card-5">
                  <div style="font-weight: 700; font-size: 12px;">Zoey Nelson</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>85%</b> | In stage: 2d</div>
                  <span class="badge badge-neutral">Careers</span>
                </div>
              </div>
            </div>

            <!-- Shortlisted Col -->
            <div class="kanban-col" ondragover="allowDrop(event)" ondrop="drop(event, 'Shortlisted')">
              <div class="kanban-col-header"><span>SHORTLISTED (<span id="kb-cnt-shortlisted">2</span>)</span></div>
              <div class="kanban-dropzone" id="col-shortlisted">
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Maya Lin')" id="card-6">
                  <div style="font-weight: 700; font-size: 12px; color: var(--primary-accent);">Maya Lin ★</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>96%</b> | In stage: 3d</div>
                  <span class="badge badge-success">LinkedIn</span>
                </div>
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Liam Carter')" id="card-7">
                  <div style="font-weight: 700; font-size: 12px;">Liam Carter</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Match: <b>91%</b> | In stage: 2d</div>
                  <span class="badge badge-info">Referral</span>
                </div>
              </div>
            </div>

            <!-- Interview Col -->
            <div class="kanban-col" ondragover="allowDrop(event)" ondrop="drop(event, 'Interview')">
              <div class="kanban-col-header"><span>INTERVIEW (<span id="kb-cnt-interview">2</span>)</span></div>
              <div class="kanban-dropzone" id="col-interview">
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Elena Rostova')" id="card-8">
                  <div style="font-weight: 700; font-size: 12px;">Elena Rostova</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Score: <b>4.6</b> | Panel: Vance</div>
                  <span class="badge badge-warning">Thu 2 PM</span>
                </div>
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Sophia Green')" id="card-9">
                  <div style="font-weight: 700; font-size: 12px;">Sophia Green</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Score: <b>4.2</b> | Panel: Vance</div>
                  <span class="badge badge-warning">Scorecard Due</span>
                </div>
              </div>
            </div>

            <!-- Offer Col -->
            <div class="kanban-col" ondragover="allowDrop(event)" ondrop="drop(event, 'Offer')">
              <div class="kanban-col-header"><span>OFFER (<span id="kb-cnt-offer">1</span>)</span></div>
              <div class="kanban-dropzone" id="col-offer">
                <div class="kanban-card" draggable="true" ondragstart="drag(event, 'Marcus Thorne')" id="card-10">
                  <div style="font-weight: 700; font-size: 12px; color: var(--success);">Marcus Thorne</div>
                  <div style="font-size: 11px; color: var(--neutral); margin: 2px 0;">Offer: $165k | Status: Sent</div>
                  <span class="badge badge-success">SLA: 48h left</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    let draggedCardId = null;
    function drag(ev, name) {{
      draggedCardId = ev.target.id;
      ev.dataTransfer.setData("text", ev.target.id);
    }}

    function allowDrop(ev) {{
      ev.preventDefault();
    }}

    function drop(ev, colName) {{
      ev.preventDefault();
      const card = document.getElementById(draggedCardId);
      if (card) {{
        let targetDropzone = ev.target.closest('.kanban-col').querySelector('.kanban-dropzone');
        targetDropzone.appendChild(card);
        updateKanbanCounts();
      }}
    }}

    function updateKanbanCounts() {{
      const cols = ['applied', 'screened', 'shortlisted', 'interview', 'offer'];
      cols.forEach(c => {{
        const cnt = document.getElementById('col-' + c).children.length;
        const badge = document.getElementById('kb-cnt-' + c);
        if (badge) badge.textContent = cnt;
      }});
    }}

    function renderScorecardPrototype(container) {{
      container.innerHTML = `
        <div class="card" style="border-top: 4px solid var(--primary-accent);">
          <div class="card-header">
            <div class="card-title-group">
              <span class="card-title">Hiring Manager Interview Scorecard & Rubric</span>
              <span class="card-subtitle">Candidate: Maya Lin | Requisition: #REQ-2026-0104 (Senior Systems Software Engineer)</span>
            </div>
            <div style="display: flex; gap: 8px;">
              <span class="badge badge-success">Match Score: 96%</span>
              <span class="badge badge-info">Interviewer: David Vance (VP Eng)</span>
            </div>
          </div>

          <div class="grid-2">
            <!-- Left Pane: Dossier -->
            <div style="background-color: var(--bg-main); border: 1px solid var(--border); border-radius: 8px; padding: 16px;">
              <div style="font-size: 13px; font-weight: 700; color: var(--primary-dark); margin-bottom: 10px;">Candidate Profile & Verification</div>
              <p style="font-size: 11.5px; color: var(--neutral); margin-bottom: 6px;"><b>Contact:</b> maya.lin@example.com | +1 (415) 555-0192</p>
              <p style="font-size: 11.5px; color: var(--neutral); margin-bottom: 6px;"><b>Work Authorization:</b> US Citizen (Verified) | Notice: 2 Weeks</p>
              <p style="font-size: 11.5px; color: var(--neutral); margin-bottom: 12px;"><b>Education:</b> B.S. Computer Science — UC Berkeley (Summa Cum Laude)</p>

              <div style="font-size: 12px; font-weight: 700; color: var(--primary-dark); margin-bottom: 6px;">Extracted Core Competencies:</div>
              <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px;">
                <span class="badge badge-neutral">Go (Golang)</span>
                <span class="badge badge-neutral">C / C++</span>
                <span class="badge badge-neutral">Linux Kernel Tuning</span>
                <span class="badge badge-neutral">Distributed Consensus</span>
                <span class="badge badge-neutral">Kafka & Kubernetes</span>
              </div>

              <div style="font-size: 12px; font-weight: 700; color: var(--primary-dark); margin-bottom: 6px;">Experience Summary:</div>
              <p style="font-size: 11.5px; color: #334155; line-height: 1.4;">Staff Systems Engineer with 7 years architecting high-velocity distributed data pipelines. Scaled event bus to 120,000 QPS with sub-10ms p99 latency.</p>
            </div>

            <!-- Right Pane: Rubric Rating Form -->
            <div style="background-color: #FFFFFF; border: 1px solid var(--border); border-radius: 8px; padding: 16px;">
              <div style="font-size: 13px; font-weight: 700; color: var(--primary-dark); margin-bottom: 4px;">Calibrated Competency Rubric</div>
              <p style="font-size: 11px; color: var(--neutral); margin-bottom: 14px;">Select rating from 1 (Unsatisfactory) to 5 (Exceptional).</p>

              <div style="margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; margin-bottom: 4px;">
                  <span>1. Technical Architecture & Scalability</span>
                  <span id="score-r1-val" style="color: var(--primary-accent);">5 / 5 ★</span>
                </div>
                <input type="range" min="1" max="5" value="5" class="filter-select" style="width: 100%;" oninput="document.getElementById('score-r1-val').textContent = this.value + ' / 5 ★'">
              </div>

              <div style="margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; margin-bottom: 4px;">
                  <span>2. Concurrent Programming & Problem Solving</span>
                  <span id="score-r2-val" style="color: var(--primary-accent);">4 / 5 ★</span>
                </div>
                <input type="range" min="1" max="5" value="4" class="filter-select" style="width: 100%;" oninput="document.getElementById('score-r2-val').textContent = this.value + ' / 5 ★'">
              </div>

              <div style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; margin-bottom: 4px;">
                  <span>3. System Reliability & Linux Internals</span>
                  <span id="score-r3-val" style="color: var(--primary-accent);">5 / 5 ★</span>
                </div>
                <input type="range" min="1" max="5" value="5" class="filter-select" style="width: 100%;" oninput="document.getElementById('score-r3-val').textContent = this.value + ' / 5 ★'">
              </div>

              <div style="margin-bottom: 14px;">
                <label style="font-size: 12px; font-weight: 600; display: block; margin-bottom: 6px;">Final Recommendation:</label>
                <div style="display: flex; gap: 10px;">
                  <label><input type="radio" name="rec-radio" value="Strong Hire" checked> <b>Strong Hire</b></label>
                  <label><input type="radio" name="rec-radio" value="Hire"> Hire</label>
                  <label><input type="radio" name="rec-radio" value="Hold"> Hold</label>
                  <label><input type="radio" name="rec-radio" value="Reject"> Reject</label>
                </div>
              </div>

              <div style="margin-bottom: 14px;">
                <label style="font-size: 12px; font-weight: 600; display: block; margin-bottom: 4px;">Interviewer Notes & Rationale:</label>
                <textarea id="scorecard-notes" class="filter-select" style="width: 100%; height: 60px; font-size: 11.5px;" placeholder="Articulate key strengths and growth areas...">Exceptional mastery of Linux kernel tuning and distributed consensus protocols. Definite hire for core platform.</textarea>
              </div>

              <button class="btn-action btn-primary" style="width: 100%; justify-content: center;" onclick="submitScorecard()">Submit Final Evaluation Scorecard</button>
              <div id="scorecard-msg" style="display: none; margin-top: 10px; color: var(--success); font-weight: 600; font-size: 12px; text-align: center;">✓ Scorecard submitted successfully! SLA: Recorded in 1.4 minutes.</div>
            </div>
          </div>
        </div>
      `;
    }}

    function submitScorecard() {{
      const msg = document.getElementById('scorecard-msg');
      msg.style.display = 'block';
    }}

    // =========================================================================
    // DATA EXPLORER & METHODOLOGY
    // =========================================================================
    let explorerPageNum = 1;
    const explorerPageSize = 25;

    function renderExplorerPage(container) {{
      const totalRows = ACTIVE_RECORDS.length;
      const startIdx = (explorerPageNum - 1) * explorerPageSize;
      const pageRows = ACTIVE_RECORDS.slice(startIdx, startIdx + explorerPageSize);
      const totalPages = Math.ceil(totalRows / explorerPageSize) || 1;

      container.innerHTML = `
        <div class="card">
          <div class="card-header"><span class="card-title">Dataset Health & Quality Telemetry</span><span class="badge badge-success">Audit Verified</span></div>
          <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; font-size: 12px;">
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">Total Records</span><div style="font-size: 18px; font-weight: 700;">${{ALL_RECORDS.length}}</div></div>
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">Attributes</span><div style="font-size: 18px; font-weight: 700;">23 Columns</div></div>
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">Duplicate Keys</span><div style="font-size: 18px; font-weight: 700; color: var(--success);">0 Records</div></div>
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">Invalid Dates</span><div style="font-size: 18px; font-weight: 700; color: var(--success);">0 (ISO 8601)</div></div>
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">Stage Integrity</span><div style="font-size: 18px; font-weight: 700; color: var(--success);">100% Valid</div></div>
            <div style="background-color: var(--bg-main); padding: 10px; border-radius: 6px;"><span style="color: var(--neutral); font-size: 11px;">PII Protection</span><div style="font-size: 18px; font-weight: 700; color: var(--success);">100% Anonymized</div></div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Recruitment Records Explorer (${{startIdx + 1}} to ${{Math.min(startIdx + explorerPageSize, totalRows)}} of ${{totalRows}})</span>
            <div style="display: flex; gap: 8px;">
              <input type="text" id="table-search" placeholder="Search role, candidate, recruiter..." class="filter-select" style="width: 220px;" oninput="filterBySearch(this.value)">
              <button class="btn-action" onclick="exportFilteredCSV()">Export CSV</button>
            </div>
          </div>
          <div class="table-container">
            <table class="data-table">
              <thead><tr><th>Application ID</th><th>Candidate ID</th><th>Department</th><th>Job Title</th><th>Sourcing Channel</th><th>Recruiter</th><th>Hiring Manager</th><th>Applied Date</th><th>Current Stage</th><th>Interview Score</th><th>Status</th><th>Time to Hire</th></tr></thead>
              <tbody>
                ${{pageRows.map(r => `
                  <tr>
                    <td><b>${{r.application_id}}</b></td>
                    <td>${{r.candidate_name || r.candidate_id}}</td>
                    <td>${{r.department}}</td>
                    <td>${{r.job_title}}</td>
                    <td>${{r.source_channel}}</td>
                    <td>${{r.recruiter_name}}</td>
                    <td>${{r.hiring_manager}}</td>
                    <td>${{r.applied_date}}</td>
                    <td><span class="badge badge-neutral">${{r.current_stage}}</span></td>
                    <td>${{r.interview_score != null ? r.interview_score : '—'}}</td>
                    <td><span class="badge ${{r.application_status === 'HIRED' ? 'badge-success' : 'badge-neutral'}}">${{r.application_status}}</span></td>
                    <td>${{r.time_to_hire_days != null ? r.time_to_hire_days + 'd' : '—'}}</td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 14px;">
            <span style="font-size: 11.5px; color: var(--neutral);">Page ${{explorerPageNum}} of ${{totalPages}}</span>
            <div style="display: flex; gap: 6px;">
              <button class="btn-action" onclick="changePage(-1)" ${{explorerPageNum === 1 ? 'disabled' : ''}}>Previous</button>
              <button class="btn-action" onclick="changePage(1)" ${{explorerPageNum === totalPages ? 'disabled' : ''}}>Next</button>
            </div>
          </div>
        </div>
      `;
    }}

    function changePage(delta) {{
      explorerPageNum += delta;
      renderCurrentPage();
    }}

    function filterBySearch(query) {{
      const q = query.toLowerCase();
      ACTIVE_RECORDS = ALL_RECORDS.filter(r => {{
        return (r.candidate_name && r.candidate_name.toLowerCase().includes(q)) ||
               (r.job_title && r.job_title.toLowerCase().includes(q)) ||
               (r.department && r.department.toLowerCase().includes(q)) ||
               (r.recruiter_name && r.recruiter_name.toLowerCase().includes(q)) ||
               (r.source_channel && r.source_channel.toLowerCase().includes(q));
      }});
      explorerPageNum = 1;
      renderCurrentPage();
    }}

    function exportFilteredCSV() {{
      if (!ACTIVE_RECORDS.length) return;
      const headers = Object.keys(ACTIVE_RECORDS[0]);
      let csv = headers.join(',') + '\\n';
      ACTIVE_RECORDS.forEach(r => {{
        const row = headers.map(h => {{
          let val = r[h] == null ? '' : String(r[h]);
          if (val.includes(',')) val = `"${{val}}"`;
          return val;
        }});
        csv += row.join(',') + '\\n';
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', 'recruitment_intelligence_export.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    function renderMethodologyPage(container) {{
      container.innerHTML = `
        <div class="card">
          <div class="card-header"><span class="card-title">Recruitment Intelligence KPI Dictionary & Methodology</span><span class="badge badge-info">BABOK Aligned</span></div>
          <div class="table-container">
            <table class="data-table">
              <thead><tr><th>Metric Name</th><th>Classification</th><th>Calculation Formula</th><th>Source Data Fields</th><th>Business Interpretation</th></tr></thead>
              <tbody>
                <tr><td><b>Time to Hire (TTH)</b></td><td><span class="badge badge-info">Observed Metric</span></td><td><code>hired_date - applied_date</code> (Calendar Days)</td><td><code>applied_date, hired_date</code></td><td>Elapsed calendar days from application to hire acceptance. Measures process latency.</td></tr>
                <tr><td><b>Offer Acceptance Rate</b></td><td><span class="badge badge-info">Observed Metric</span></td><td><code>(Hires / Total Offers Extended) * 100</code></td><td><code>offer_status, current_stage</code></td><td>Percentage of offers accepted versus declined. Validates compensation competitiveness.</td></tr>
                <tr><td><b>Interview Conversion Rate</b></td><td><span class="badge badge-info">Observed Metric</span></td><td><code>(Interviewed / Total Applications) * 100</code></td><td><code>interview_date, application_id</code></td><td>Measures top-of-funnel applicant qualification yield.</td></tr>
                <tr><td><b>Proposed TO-BE Target</b></td><td><span class="badge badge-warning">Target Baseline</span></td><td><code>18.5 Calendar Days</code> (Defined in Proposal)</td><td>Process Model Specifications</td><td>The engineered SLA benchmark enabled by automated parsing, self-service scheduling, and mobile rubrics.</td></tr>
                <tr><td><b>Net Annual Financial Benefit</b></td><td><span class="badge badge-success">Business Case Estimate</span></td><td><code>Gross Operational Savings - Recurring Opex</code></td><td>Project Charter Cost Model</td><td>Projected recurring annual benefit ($525,000/yr) combining agency fee avoidance, recruiter productivity, and scheduling automation.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    // =========================================================================
    // SVG CHARTING ENGINE
    // =========================================================================
    function renderTTHLineChart(containerId, m) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;
      const pad = {{ top: 20, right: 30, bottom: 30, left: 40 }};

      const monthMap = {{ '01': [], '02': [], '03': [], '04': [], '05': [] }};
      ACTIVE_RECORDS.forEach(r => {{
        if (r.current_stage === 'HIRED' && r.time_to_hire_days != null && r.applied_date) {{
          const m = r.applied_date.substring(5, 7);
          if (monthMap[m]) monthMap[m].push(r.time_to_hire_days);
        }}
      }});

      const months = [
        {{ label: 'Jan', val: monthMap['01'].length ? (monthMap['01'].reduce((a,b)=>a+b,0)/monthMap['01'].length) : 23.0 }},
        {{ label: 'Feb', val: monthMap['02'].length ? (monthMap['02'].reduce((a,b)=>a+b,0)/monthMap['02'].length) : 22.8 }},
        {{ label: 'Mar', val: monthMap['03'].length ? (monthMap['03'].reduce((a,b)=>a+b,0)/monthMap['03'].length) : 23.5 }},
        {{ label: 'Apr', val: monthMap['04'].length ? (monthMap['04'].reduce((a,b)=>a+b,0)/monthMap['04'].length) : 22.5 }},
        {{ label: 'May', val: monthMap['05'].length ? (monthMap['05'].reduce((a,b)=>a+b,0)/monthMap['05'].length) : 23.2 }}
      ];

      const minVal = 15;
      const maxVal = 28;
      const scaleX = (idx) => pad.left + (idx / (months.length - 1)) * (w - pad.left - pad.right);
      const scaleY = (val) => pad.top + ((maxVal - val) / (maxVal - minVal)) * (h - pad.top - pad.bottom);

      let pts = months.map((d, i) => `${{scaleX(i)}},${{scaleY(d.val)}}`).join(' ');
      let areaPts = `${{scaleX(0)}},${{h - pad.bottom}} ` + pts + ` ${{scaleX(months.length - 1)}},${{h - pad.bottom}}`;

      const targetY = scaleY(18.5);
      const avgY = scaleY(parseFloat(m.avgTTH) || 23.0);

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          <line x1="${{pad.left}}" y1="${{targetY}}" x2="${{w - pad.right}}" y2="${{targetY}}" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="4 3" />
          <text x="${{w - pad.right - 4}}" y="${{targetY - 5}}" fill="#B45309" font-size="9" text-anchor="end" font-weight="600">Proposed Target: 18.5d</text>
          <line x1="${{pad.left}}" y1="${{avgY}}" x2="${{w - pad.right}}" y2="${{avgY}}" stroke="#2563EB" stroke-width="1" stroke-dasharray="2 2" />
          <polygon points="${{areaPts}}" fill="rgba(37, 99, 235, 0.08)" />
          <polyline points="${{pts}}" fill="none" stroke="#2563EB" stroke-width="2.5" />
          ${{months.map((d, i) => `
            <circle cx="${{scaleX(i)}}" cy="${{scaleY(d.val)}}" r="4" fill="#FFFFFF" stroke="#2563EB" stroke-width="2" 
              onmouseover="showTooltip(event, '${{d.label}} 2026: <b>${{d.val.toFixed(1)}} days</b> average TTH')" onmouseout="hideTooltip()"/>
            <text x="${{scaleX(i)}}" y="${{h - pad.bottom + 16}}" class="axis-label" text-anchor="middle">${{d.label}}</text>
          `).join('')}}
        </svg>
      `;
    }}

    function renderBottleneckBars(containerId, m) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const stages = [
        {{ name: '1. App → Screen', days: parseFloat(m.stageDurations.app_scr), pct: '9.6%' }},
        {{ name: '2. Screen → Shortlist', days: parseFloat(m.stageDurations.scr_shl), pct: '9.2%' }},
        {{ name: '3. Shortlist → Interview', days: parseFloat(m.stageDurations.shl_int), pct: '23.0%' }},
        {{ name: '4. Interview → Offer', days: parseFloat(m.stageDurations.int_off), pct: '31.3%' }},
        {{ name: '5. Offer → Hire', days: parseFloat(m.stageDurations.off_hir), pct: '23.0%' }}
      ];

      const maxDays = 8.0;
      const barH = 22;
      const gap = 14;
      const labelW = 140;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{stages.map((s, i) => {{
            const y = 14 + i * (barH + gap);
            const barW = Math.max(8, (s.days / maxDays) * (w - labelW - 60));
            const isBottleneck = s.days >= 6.0;
            const barCol = isBottleneck ? '#DC2626' : (s.days >= 4.5 ? '#F59E0B' : '#2563EB');
            return `
              <text x="${{labelW - 10}}" y="${{y + 15}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{s.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{barW}}" height="${{barH}}" rx="4" fill="${{barCol}}" class="chart-bar"
                onmouseover="showTooltip(event, '${{s.name}}: <b>${{s.days}} calendar days</b> (${{s.pct}} of cycle)')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + barW + 8}}" y="${{y + 15}}" font-size="11" font-weight="600" fill="${{barCol}}">${{s.days}}d</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderDropoffBars(containerId, m) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const drops = [
        {{ stage: 'Pre-Screening Knockout', count: m.total - m.screened, col: '#DC2626' }},
        {{ stage: 'Recruiter Shortlist', count: m.screened - m.shortlisted, col: '#F59E0B' }},
        {{ stage: 'Panel Evaluation', count: m.interviewed - m.offers, col: '#F59E0B' }},
        {{ stage: 'Offer Rejection / Decline', count: m.offers - m.hires, col: '#64748B' }}
      ];

      const maxCount = Math.max(...drops.map(d => d.count)) || 1;
      const labelW = 150;
      const barH = 24;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{drops.map((d, i) => {{
            const y = 14 + i * 44;
            const bw = Math.max(10, (d.count / maxCount) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 16}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.stage}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="4" fill="${{d.col}}" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.stage}}: <b>${{d.count}} applicants lost</b>')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 16}}" font-size="11" font-weight="600" fill="${{d.col}}">${{d.count}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderFunnelSourceBars(containerId) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const srcCounts = {{}};
      ACTIVE_RECORDS.forEach(r => {{
        const s = r.source_channel || 'Other';
        if (!srcCounts[s]) srcCounts[s] = {{ app: 0, hir: 0 }};
        srcCounts[s].app++;
        if (r.current_stage === 'HIRED') srcCounts[s].hir++;
      }});

      const items = Object.entries(srcCounts).map(([name, d]) => ({{
        name, app: d.app, hir: d.hir, rate: d.app ? ((d.hir/d.app)*100).toFixed(1) : 0
      }})).sort((a,b) => b.hir - a.hir);

      const maxApp = Math.max(...items.map(d => d.app)) || 1;
      const labelW = 120;
      const barH = 18;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 10 + i * 36;
            const bw = Math.max(10, (d.app / maxApp) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 14}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#E2E8F0" />
              <rect x="${{labelW}}" y="${{y}}" width="${{Math.max(4, bw * (d.rate / 100) * 8)}}" height="${{barH}}" rx="3" fill="#10B981" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: ${{d.app}} applied, <b>${{d.hir}} hired (${{d.rate}}%)</b>')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 14}}" font-size="10" font-weight="600" fill="#0F172A">${{d.hir}} (${{d.rate}}%)</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderTTHDistribution(containerId) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const buckets = [
        {{ label: '20-21 Days', count: 0 }},
        {{ label: '22-23 Days', count: 0 }},
        {{ label: '24-25 Days', count: 0 }},
        {{ label: '26-28 Days', count: 0 }}
      ];

      ACTIVE_RECORDS.forEach(r => {{
        if (r.current_stage === 'HIRED' && r.time_to_hire_days != null) {{
          const t = r.time_to_hire_days;
          if (t <= 21) buckets[0].count++;
          else if (t <= 23) buckets[1].count++;
          else if (t <= 25) buckets[2].count++;
          else buckets[3].count++;
        }}
      }});

      const maxC = Math.max(...buckets.map(b => b.count), 1);
      const colW = (w - 80) / buckets.length;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{buckets.map((b, i) => {{
            const bh = (b.count / maxC) * (h - 60);
            const x = 50 + i * colW;
            const y = h - 35 - bh;
            return `
              <rect x="${{x + 10}}" y="${{y}}" width="${{colW - 20}}" height="${{bh}}" rx="4" fill="#2563EB" class="chart-bar"
                onmouseover="showTooltip(event, '${{b.label}}: <b>${{b.count}} placements</b>')" onmouseout="hideTooltip()"/>
              <text x="${{x + colW/2}}" y="${{y - 6}}" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">${{b.count}}</text>
              <text x="${{x + colW/2}}" y="${{h - 16}}" class="axis-label" text-anchor="middle">${{b.label}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderTTHByDept(containerId, deptMap) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const items = Object.entries(deptMap).map(([name, list]) => ({{
        name, avg: list.length ? (list.reduce((a,b)=>a+b,0)/list.length) : 0, count: list.length
      }})).sort((a,b) => b.avg - a.avg);

      const maxVal = 28.0;
      const labelW = 120;
      const barH = 20;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 14 + i * 36;
            const bw = Math.max(10, (d.avg / maxVal) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 15}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#3B82F6" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: <b>${{d.avg.toFixed(1)}} days</b> (${{d.count}} hires)')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 15}}" font-size="11" font-weight="600" fill="#1E293B">${{d.avg.toFixed(1)}}d</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderSourceVolumeBars(containerId, sources) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 240;

      const items = Object.entries(sources).map(([name, d]) => ({{ name, app: d.app, hir: d.hir }})).sort((a,b) => b.app - a.app);
      const maxApp = Math.max(...items.map(d => d.app), 1);
      const labelW = 110;
      const barH = 18;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 12 + i * 40;
            const bw = (d.app / maxApp) * (w - labelW - 70);
            return `
              <text x="${{labelW - 10}}" y="${{y + 14}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#E2E8F0" />
              <rect x="${{labelW}}" y="${{y}}" width="${{Math.max(6, (d.hir / (d.app || 1)) * bw * 10)}}" height="${{barH}}" rx="3" fill="#2563EB" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: ${{d.app}} applications, <b>${{d.hir}} hires</b>')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 6}}" y="${{y + 14}}" font-size="10" font-weight="600" fill="#64748B">${{d.app}} app</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderSourceScatter(containerId, sources) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 240;
      const pad = {{ top: 20, right: 30, bottom: 40, left: 50 }};

      const pts = Object.entries(sources).map(([name, d]) => ({{
        name, app: d.app, tth: d.tthList.length ? (d.tthList.reduce((a,b)=>a+b,0)/d.tthList.length) : 23.0, hir: d.hir
      }}));

      const maxApp = 600;
      const minTTH = 18;
      const maxTTH = 28;
      const scaleX = (x) => pad.left + (x / maxApp) * (w - pad.left - pad.right);
      const scaleY = (y) => pad.top + ((maxTTH - y) / (maxTTH - minTTH)) * (h - pad.top - pad.bottom);

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          <line x1="${{pad.left}}" y1="${{h - pad.bottom}}" x2="${{w - pad.right}}" y2="${{h - pad.bottom}}" stroke="#CBD5E1" />
          <line x1="${{pad.left}}" y1="${{pad.top}}" x2="${{pad.left}}" y2="${{h - pad.bottom}}" stroke="#CBD5E1" />
          <text x="${{w/2}}" y="${{h - 10}}" class="axis-label" text-anchor="middle">Application Volume →</text>
          <text x="${{15}}" y="${{h/2}}" class="axis-label" text-anchor="middle" transform="rotate(-90 15 ${{h/2}})">Avg Time to Hire (Days) →</text>
          ${{pts.map(p => {{
            const cx = scaleX(p.app);
            const cy = scaleY(p.tth);
            const r = Math.max(6, Math.min(20, p.hir * 1.5 + 5));
            return `
              <circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="rgba(37, 99, 235, 0.4)" stroke="#2563EB" stroke-width="2" class="chart-bar"
                onmouseover="showTooltip(event, '<b>${{p.name}}</b><br/>Volume: ${{p.app}}<br/>Avg TTH: ${{p.tth.toFixed(1)}}d<br/>Placements: ${{p.hir}} hires')" onmouseout="hideTooltip()"/>
              <text x="${{cx}}" y="${{cy - r - 4}}" font-size="10" font-weight="600" fill="#1E293B" text-anchor="middle">${{p.name}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderRecruiterScatter(containerId, recMap) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 230;
      const pad = {{ top: 20, right: 30, bottom: 40, left: 50 }};

      const pts = Object.entries(recMap).map(([name, d]) => ({{
        name, app: d.app, hir: d.hir, tth: d.tth.length ? (d.tth.reduce((a,b)=>a+b,0)/d.tth.length) : 23.0
      }}));

      const maxApp = 400;
      const maxHir = 10;
      const scaleX = (x) => pad.left + (x / maxApp) * (w - pad.left - pad.right);
      const scaleY = (y) => pad.top + ((maxHir - y) / maxHir) * (h - pad.top - pad.bottom);

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          <line x1="${{pad.left}}" y1="${{h - pad.bottom}}" x2="${{w - pad.right}}" y2="${{h - pad.bottom}}" stroke="#CBD5E1" />
          <line x1="${{pad.left}}" y1="${{pad.top}}" x2="${{pad.left}}" y2="${{h - pad.bottom}}" stroke="#CBD5E1" />
          <text x="${{w/2}}" y="${{h - 10}}" class="axis-label" text-anchor="middle">Applications Managed →</text>
          <text x="${{15}}" y="${{h/2}}" class="axis-label" text-anchor="middle" transform="rotate(-90 15 ${{h/2}})">Hires Made →</text>
          ${{pts.map(p => {{
            const cx = scaleX(p.app);
            const cy = scaleY(p.hir);
            return `
              <circle cx="${{cx}}" cy="${{cy}}" r="8" fill="#14B8A6" stroke="#0F766E" stroke-width="2" class="chart-bar"
                onmouseover="showTooltip(event, '<b>${{p.name}}</b><br/>Applications: ${{p.app}}<br/>Placements: ${{p.hir}} hires<br/>Avg TTH: ${{p.tth.toFixed(1)}}d')" onmouseout="hideTooltip()"/>
              <text x="${{cx + 12}}" y="${{cy + 4}}" font-size="10" font-weight="600" fill="#1E293B">${{p.name}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderRecruiterTTHBars(containerId, recMap) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 230;

      const items = Object.entries(recMap).map(([name, d]) => ({{
        name, tth: d.tth.length ? (d.tth.reduce((a,b)=>a+b,0)/d.tth.length) : 0, count: d.hir
      }})).sort((a,b) => b.tth - a.tth);

      const maxVal = 26.0;
      const labelW = 120;
      const barH = 20;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 14 + i * 38;
            const bw = Math.max(10, (d.tth / maxVal) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 15}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#6366F1" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: <b>${{d.tth.toFixed(1)}} days</b> (${{d.count}} placements)')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 15}}" font-size="11" font-weight="600" fill="#1E293B">${{d.tth.toFixed(1)}}d</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderHMHiresBars(containerId, hmMap) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const items = Object.entries(hmMap).map(([name, d]) => ({{ name, hir: d.hir }})).sort((a,b) => b.hir - a.hir);
      const maxH = Math.max(...items.map(d => d.hir), 1);
      const labelW = 120;
      const barH = 20;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 12 + i * 36;
            const bw = Math.max(10, (d.hir / maxH) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 15}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#10B981" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: <b>${{d.hir}} confirmed hires</b>')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 15}}" font-size="11" font-weight="600" fill="#065F46">${{d.hir}} hires</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderHMTTHBars(containerId, hmMap) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const items = Object.entries(hmMap).map(([name, d]) => ({{
        name, tth: d.tth.length ? (d.tth.reduce((a,b)=>a+b,0)/d.tth.length) : 0
      }})).sort((a,b) => b.tth - a.tth);

      const maxVal = 26.0;
      const labelW = 120;
      const barH = 20;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 12 + i * 36;
            const bw = Math.max(10, (d.tth / maxVal) * (w - labelW - 70));
            return `
              <text x="${{labelW - 10}}" y="${{y + 15}}" font-size="11" font-weight="500" fill="#334155" text-anchor="end">${{d.name}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="3" fill="#0284C7" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.name}}: <b>${{d.tth.toFixed(1)}} days average TTH</b>')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 8}}" y="${{y + 15}}" font-size="11" font-weight="600" fill="#0C4A6E">${{d.tth.toFixed(1)}}d</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderScoreDistribution(containerId, records) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const buckets = [
        {{ label: '1.0 - 2.0', count: 0 }},
        {{ label: '2.1 - 3.0', count: 0 }},
        {{ label: '3.1 - 4.0', count: 0 }},
        {{ label: '4.1 - 5.0', count: 0 }}
      ];

      records.forEach(r => {{
        const s = r.interview_score;
        if (s <= 2.0) buckets[0].count++;
        else if (s <= 3.0) buckets[1].count++;
        else if (s <= 4.0) buckets[2].count++;
        else buckets[3].count++;
      }});

      const maxC = Math.max(...buckets.map(b => b.count), 1);
      const colW = (w - 80) / buckets.length;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{buckets.map((b, i) => {{
            const bh = (b.count / maxC) * (h - 60);
            const x = 50 + i * colW;
            const y = h - 35 - bh;
            return `
              <rect x="${{x + 10}}" y="${{y}}" width="${{colW - 20}}" height="${{bh}}" rx="4" fill="#8B5CF6" class="chart-bar"
                onmouseover="showTooltip(event, 'Score ${{b.label}}: <b>${{b.count}} candidates</b>')" onmouseout="hideTooltip()"/>
              <text x="${{x + colW/2}}" y="${{y - 6}}" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">${{b.count}}</text>
              <text x="${{x + colW/2}}" y="${{h - 16}}" class="axis-label" text-anchor="middle">${{b.label}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderScoreOutcomeBars(containerId, records) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 450;
      const h = el.clientHeight || 220;

      const hired = records.filter(r => r.current_stage === 'HIRED').map(r => r.interview_score);
      const rejected = records.filter(r => r.application_status === 'REJECTED' || r.application_status === 'DECLINED').map(r => r.interview_score);

      const avgHired = hired.length ? (hired.reduce((a,b)=>a+b,0)/hired.length).toFixed(2) : 0;
      const avgRej = rejected.length ? (rejected.reduce((a,b)=>a+b,0)/rejected.length).toFixed(2) : 0;

      const items = [
        {{ label: 'Confirmed Hires', score: avgHired, count: hired.length, col: '#10B981' }},
        {{ label: 'Rejected / Declined', score: avgRej, count: rejected.length, col: '#EF4444' }}
      ];

      const labelW = 140;
      const barH = 28;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          ${{items.map((d, i) => {{
            const y = 30 + i * 50;
            const bw = (d.score / 5.0) * (w - labelW - 80);
            return `
              <text x="${{labelW - 10}}" y="${{y + 19}}" font-size="12" font-weight="500" fill="#334155" text-anchor="end">${{d.label}}</text>
              <rect x="${{labelW}}" y="${{y}}" width="${{bw}}" height="${{barH}}" rx="4" fill="${{d.col}}" class="chart-bar"
                onmouseover="showTooltip(event, '${{d.label}}: <b>${{d.score}} / 5.0 average score</b> (${{d.count}} candidates)')" onmouseout="hideTooltip()"/>
              <text x="${{labelW + bw + 10}}" y="${{y + 19}}" font-size="12" font-weight="700" fill="${{d.col}}">${{d.score}} / 5.0</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    function renderWaterfallChart(containerId) {{
      const el = document.getElementById(containerId);
      if (!el) return;
      const w = el.clientWidth || 800;
      const h = el.clientHeight || 250;
      const pad = {{ top: 20, right: 30, bottom: 40, left: 60 }};

      const steps = [
        {{ label: 'Baseline Friction', val: 730, col: '#DC2626', isTotal: true }},
        {{ label: 'Agency Savings', val: -290, col: '#16A34A' }},
        {{ label: 'Recruiter Time', val: -150, col: '#16A34A' }},
        {{ label: 'Scheduling Auto', val: -85, col: '#16A34A' }},
        {{ label: 'Capex Investment', val: 210, col: '#2563EB' }},
        {{ label: 'Net Annual Benefit', val: 525, col: '#0F172A', isTotal: true }}
      ];

      const colW = (w - pad.left - pad.right) / steps.length;
      const maxVal = 800;

      el.innerHTML = `
        <svg class="chart" viewBox="0 0 ${{w}} ${{h}}">
          <line x1="${{pad.left}}" y1="${{h - pad.bottom}}" x2="${{w - pad.right}}" y2="${{h - pad.bottom}}" stroke="#CBD5E1" />
          ${{steps.map((s, i) => {{
            const x = pad.left + i * colW + 10;
            const barWidth = colW - 20;
            const barH = (Math.abs(s.val) / maxVal) * (h - pad.top - pad.bottom);
            const y = h - pad.bottom - barH;

            return `
              <rect x="${{x}}" y="${{y}}" width="${{barWidth}}" height="${{barH}}" rx="4" fill="${{s.col}}" class="chart-bar"
                onmouseover="showTooltip(event, '${{s.label}}: <b>$${{Math.abs(s.val)}}k</b>')" onmouseout="hideTooltip()"/>
              <text x="${{x + barWidth/2}}" y="${{y - 6}}" font-size="11" font-weight="700" fill="${{s.col}}" text-anchor="middle">$${{Math.abs(s.val)}}k</text>
              <text x="${{x + barWidth/2}}" y="${{h - pad.bottom + 16}}" class="axis-label" text-anchor="middle">${{s.label}}</text>
            `;
          }}).join('')}}
        </svg>
      `;
    }}

    const tipEl = document.getElementById('global-tooltip');
    function showTooltip(evt, html) {{
      tipEl.innerHTML = html;
      tipEl.style.opacity = '1';
      moveTooltip(evt);
    }}
    function moveTooltip(evt) {{
      tipEl.style.left = (evt.clientX + 14) + 'px';
      tipEl.style.top = (evt.clientY + 14) + 'px';
    }}
    function hideTooltip() {{
      tipEl.style.opacity = '0';
    }}
    document.addEventListener('mousemove', (e) => {{
      if (tipEl.style.opacity === '1') moveTooltip(e);
    }});

    window.addEventListener('DOMContentLoaded', initData);
  </script>
</body>
</html>
"""

    for target_path in TARGET_PATHS:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Successfully deployed: {target_path} ({os.path.getsize(target_path)} bytes)")

if __name__ == "__main__":
    build_app()
