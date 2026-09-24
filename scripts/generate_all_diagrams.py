"""
Generates all 7 required diagram images with exact naming into diagrams/
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

dst_dir = r'C:\Users\namra\.gemini\antigravity\scratch\recruitment-ats-business-analysis\diagrams'
os.makedirs(dst_dir, exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Arial', 'DejaVu Sans', 'Helvetica'

# -------------------------------------------------------------
# 1. diagrams/as-is-process.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=200)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

lanes = ['CANDIDATE', 'RECRUITER (HR)', 'HIRING MANAGER', 'INBOXES & SILOS']
lane_colors = ['#f1f5f9', '#ffffff', '#f1f5f9', '#fee2e2']
y_lanes = [3, 2, 1, 0]

for y, name, col in zip(y_lanes, lanes, lane_colors):
    rect = patches.Rectangle((0, y), 12, 1, facecolor=col, edgecolor='#cbd5e1', linewidth=1)
    ax.add_patch(rect)
    ax.text(0.15, y + 0.5, name, va='center', ha='left', fontsize=9.5, fontweight='bold', color='#334155')

def draw_node(x, y, text, color='#2563eb', text_col='#ffffff', width=1.4, height=0.6, is_red=False):
    fill = '#ef4444' if is_red else color
    box = patches.FancyBboxPatch((x, y - height/2), width, height, boxstyle='round,pad=0.08',
                                 facecolor=fill, edgecolor='#0f172a', linewidth=0.8)
    ax.add_patch(box)
    ax.text(x + width/2, y, text, ha='center', va='center', fontsize=7.5, fontweight='bold', color=text_col)

def draw_arrow(x1, y1, x2, y2, red=False):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='#ef4444' if red else '#64748b'))

draw_node(1.5, 3.5, 'Finds Job on\nJob Board', '#3b82f6')
draw_node(3.3, 3.5, 'Emails Resume\n(PDF Attachment)', '#3b82f6')
draw_node(5.2, 3.5, 'Waits in\nBlack Hole', '#94a3b8')
draw_node(7.0, 3.5, 'Phone Screen\nInterview', '#3b82f6')
draw_node(8.8, 3.5, 'Attends Panel\nInterview', '#3b82f6')
draw_node(10.3, 3.5, 'Signs Paper\nOffer Scan', '#10b981')

draw_node(1.5, 2.5, 'Receives Requisition\nvia Email (7d lag)', '#f59e0b', is_red=True)
draw_node(3.3, 2.5, 'Manual Copy-Paste\nto 4 Job Boards', '#f59e0b')
draw_node(5.2, 2.5, 'Downloads CVs into\nExcel Tracker', '#f59e0b', is_red=True)
draw_node(7.0, 2.5, 'Emails Hiring Mgr\nfor Review (5d lag)', '#f59e0b', is_red=True)
draw_node(8.8, 2.5, '6.8 Emails to\nSchedule Panel', '#f59e0b', is_red=True)
draw_node(10.3, 2.5, 'Drafts Offer in\nWord Document', '#f59e0b')

draw_node(1.5, 1.5, 'Drafts Need in\nWord Doc', '#6366f1')
draw_node(5.2, 1.5, 'Inbox Cluttered with\nUnscreened CVs', '#6366f1', is_red=True)
draw_node(8.8, 1.5, 'Unstructured Notes\non Notepad', '#6366f1', is_red=True)
draw_node(10.3, 1.5, 'Verbal Offer\nApproval', '#6366f1')

draw_node(3.3, 0.5, 'jobs@ Outlook\nInbox', '#dc2626')
draw_node(5.2, 0.5, '8 Local Recruiter\nExcel Spreadsheets', '#dc2626')
draw_node(8.8, 0.5, 'Personal Inboxes &\nPaper Folders', '#dc2626')

draw_arrow(2.2, 1.5, 2.2, 2.2, True)
draw_arrow(2.9, 3.5, 3.3, 3.5)
draw_arrow(4.0, 3.5, 4.0, 0.8)
draw_arrow(4.0, 0.8, 5.2, 2.5, True)
draw_arrow(6.6, 2.5, 7.0, 3.5)
draw_arrow(7.7, 3.5, 8.8, 2.5, True)
draw_arrow(9.5, 2.5, 9.5, 1.8)
draw_arrow(9.5, 1.8, 9.5, 3.2)
draw_arrow(9.5, 3.8, 10.3, 2.5)

ax.set_xlim(0, 12)
ax.set_ylim(-0.2, 4.2)
ax.axis('off')
ax.set_title('CURRENT STATE (AS-IS) RECRUITMENT SWIMLANE PROCESS MAP\nCycle Time: 46.5 Calendar Days (93.0% Non-Value-Add Waiting Latency)',
             fontsize=12, fontweight='bold', color='#991b1b', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'as-is-process.png'))
plt.close()

# -------------------------------------------------------------
# 2. diagrams/to-be-process.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 8), dpi=200)
ax.set_facecolor('#f0fdf4')
fig.patch.set_facecolor('#ffffff')

lanes_tb = ['CANDIDATE', 'RECRUITER (HR)', 'HIRING MANAGER', 'ATS AUTOMATION ENGINE', 'ENTERPRISE CORE HRIS']
lane_cols_tb = ['#ffffff', '#f8fafc', '#ffffff', '#eff6ff', '#ecfdf5']
y_lanes_tb = [4, 3, 2, 1, 0]

for y, name, col in zip(y_lanes_tb, lanes_tb, lane_cols_tb):
    rect = patches.Rectangle((0, y), 12, 1, facecolor=col, edgecolor='#94a3b8', linewidth=0.8)
    ax.add_patch(rect)
    ax.text(0.15, y + 0.5, name, va='center', ha='left', fontsize=9, fontweight='bold', color='#1e293b')

draw_node(1.2, 2.5, 'Submits Digital\nRequisition', '#4f46e5')
draw_node(2.8, 1.5, 'Rule BR-01: Auto-Routes\nApproval (24h SLA)', '#0284c7')
draw_node(2.8, 3.5, '1-Click Approve &\nPublish', '#3b82f6')
draw_node(4.4, 1.5, 'Rule BR-02: 1-Click\nJob Board Syndication', '#0284c7')
draw_node(4.4, 4.5, 'Applies Online &\nTakes Knockout Qs', '#10b981')
draw_node(6.0, 1.5, 'Smart Parser &\nDisqualification Buffer', '#0284c7')
draw_node(6.0, 3.5, 'Kanban Triage &\nShortlisting', '#3b82f6')
draw_node(7.6, 4.5, 'Self-Service Calendar\nSlot Selection', '#10b981')
draw_node(7.6, 1.5, 'Rule BR-03: Real-Time\nMS 365 Calendar Sync', '#0284c7')
draw_node(9.0, 2.5, 'Interviews & Submits\nDigital Scorecard', '#4f46e5')
draw_node(9.0, 1.5, 'Rule BR-04: Consolidates\nRubric Scores', '#0284c7')
draw_node(10.5, 4.5, 'Reviews & E-Signs\nFormal Offer Letter', '#10b981')
draw_node(10.5, 1.5, 'Rule BR-05: Generates\nOffer PDF Contract', '#0284c7')
draw_node(10.5, 0.5, 'Rule BR-06: REST API\nPush to Workday HRIS', '#059669')

draw_arrow(1.9, 2.5, 2.8, 1.8)
draw_arrow(2.8, 1.8, 2.8, 3.2)
draw_arrow(3.5, 3.5, 4.4, 1.8)
draw_arrow(4.4, 1.8, 4.4, 4.2)
draw_arrow(5.1, 4.5, 6.0, 1.8)
draw_arrow(6.0, 1.8, 6.0, 3.2)
draw_arrow(6.7, 3.5, 7.6, 4.2)
draw_arrow(7.6, 4.2, 7.6, 1.8)
draw_arrow(8.3, 1.5, 9.0, 2.2)
draw_arrow(9.0, 2.2, 9.0, 1.8)
draw_arrow(9.7, 1.5, 10.5, 1.8)
draw_arrow(10.5, 1.8, 10.5, 4.2)
draw_arrow(11.2, 4.5, 11.2, 1.2)
draw_arrow(11.2, 1.2, 11.2, 0.8)

ax.set_xlim(0, 12)
ax.set_ylim(-0.2, 5.2)
ax.axis('off')
ax.set_title('FUTURE STATE (TO-BE) RE-ENGINEERED RECRUITMENT WORKFLOW\nCycle Time: 18.5 Calendar Days (-60.2% Reduction | 38.5% Active Efficiency)',
             fontsize=12, fontweight='bold', color='#065f46', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'to-be-process.png'))
plt.close()

# -------------------------------------------------------------
# 3. diagrams/use-case-diagram.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
ax.set_facecolor('#ffffff')

# Boundary box
sys_box = patches.FancyBboxPatch((2.6, 0.4), 6.8, 6.8, boxstyle='round,pad=0.1', facecolor='#f8fafc', edgecolor='#3b82f6', linewidth=1.5)
ax.add_patch(sys_box)
ax.text(6.0, 7.0, 'Recruitment ATS System Boundary', ha='center', fontsize=11, fontweight='bold', color='#1e3a8a')

# Actors
def draw_actor(x, y, name):
    circle = patches.Circle((x, y + 0.3), 0.22, facecolor='#ffffff', edgecolor='#0f172a', linewidth=1.5)
    ax.add_patch(circle)
    ax.plot([x, x], [y + 0.08, y - 0.25], color='#0f172a', lw=1.5)
    ax.plot([x - 0.2, x + 0.2], [y, y], color='#0f172a', lw=1.5)
    ax.plot([x, x - 0.18], [y - 0.25, y - 0.55], color='#0f172a', lw=1.5)
    ax.plot([x, x + 0.18], [y - 0.25, y - 0.55], color='#0f172a', lw=1.5)
    ax.text(x, y - 0.75, name, ha='center', fontsize=8.5, fontweight='bold', color='#1e293b')

draw_actor(1.2, 5.2, 'Candidate')
draw_actor(1.2, 1.8, 'Recruiter')
draw_actor(10.8, 5.2, 'Hiring Manager')
draw_actor(10.8, 1.8, 'System Admin')

# Use case ovals
ucs = [
    (4.2, 6.2, 'Apply Online &\nTake Knockout Qs'),
    (7.5, 6.2, 'Submit Job\nRequisition'),
    (4.2, 4.8, 'Book Interview\nSlot'),
    (7.5, 4.8, 'Submit Digital\nScorecard'),
    (4.2, 3.4, 'Triage Kanban\nPipeline'),
    (7.5, 3.4, 'Review Candidate\nDossier'),
    (4.2, 2.0, 'One-Click Job\nSyndication'),
    (7.5, 2.0, 'Audit Logs &\nGDPR Erasure'),
    (5.8, 1.0, 'Review & E-Sign\nOffer Letter')
]

for ux, uy, utext in ucs:
    oval = patches.Ellipse((ux, uy), 2.2, 0.8, facecolor='#ffffff', edgecolor='#2563eb', linewidth=1.2)
    ax.add_patch(oval)
    ax.text(ux, uy, utext, ha='center', va='center', fontsize=7.2, fontweight='semibold', color='#0f172a')

# Actor association lines
lines = [
    (1.4, 5.2, 3.1, 6.2),
    (1.4, 5.2, 3.1, 4.8),
    (1.4, 5.2, 4.8, 1.0),
    (1.4, 1.8, 3.1, 3.4),
    (1.4, 1.8, 3.1, 2.0),
    (10.6, 5.2, 8.6, 6.2),
    (10.6, 5.2, 8.6, 4.8),
    (10.6, 5.2, 8.6, 3.4),
    (10.6, 1.8, 8.6, 2.0)
]
for x1, y1, x2, y2 in lines:
    ax.plot([x1, x2], [y1, y2], color='#64748b', lw=1.0)

ax.set_xlim(0, 12)
ax.set_ylim(0, 7.6)
ax.axis('off')
ax.set_title('OMG UML 2.5 USE CASE ARCHITECTURE DIAGRAM', fontsize=12, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'use-case-diagram.png'))
plt.close()

# -------------------------------------------------------------
# 4. diagrams/erd.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

def draw_table_card(x, y, title, pks, fks, attrs, w=2.4, h=1.8, col='#1e293b'):
    header_h = 0.35
    box = patches.FancyBboxPatch((x, y - h), w, h, boxstyle='round,pad=0.04', facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1)
    ax.add_patch(box)
    header = patches.Rectangle((x, y - header_h), w, header_h, facecolor=col, edgecolor=col)
    ax.add_patch(header)
    ax.text(x + w/2, y - header_h/2, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#ffffff')
    lines = [f'PK: {p}' for p in pks] + [f'FK: {f}' for f in fks] + attrs[:3]
    text_content = '\n'.join(lines)
    ax.text(x + 0.1, y - header_h - 0.15, text_content, va='top', ha='left', fontsize=7, color='#334155', fontfamily='monospace')

draw_table_card(0.5, 6.5, 'USERS', ['user_id'], ['role_id', 'dept_id'], ['sso_id', 'email', 'status'], col='#2563eb')
draw_table_card(3.5, 6.5, 'JOB_REQUISITIONS', ['requisition_id'], ['hiring_mgr_id', 'dept_id'], ['job_title', 'min_salary', 'status'], col='#2563eb')
draw_table_card(6.5, 6.5, 'JOB_POSTINGS', ['posting_id'], ['requisition_id'], ['portal_channel', 'posting_status'], col='#3b82f6')
draw_table_card(9.5, 6.5, 'DEPARTMENTS', ['department_id'], ['dept_head_id'], ['dept_name', 'cost_center'], col='#64748b')

draw_table_card(0.5, 4.0, 'CANDIDATES', ['candidate_id'], [], ['email (UK)', 'phone', 'gdpr_consent'], col='#059669')
draw_table_card(3.5, 4.0, 'RESUMES', ['resume_id'], ['candidate_id'], ['file_s3_uri', 'parsed_skills'], col='#059669')
draw_table_card(6.5, 4.0, 'APPLICATIONS (HUB)', ['application_id'], ['candidate_id', 'requisition_id'], ['current_stage', 'fit_score', 'applied_at'], col='#d97706')

draw_table_card(0.5, 1.8, 'INTERVIEWS', ['interview_id'], ['application_id'], ['interview_stage', 'meeting_link'], col='#7c3aed')
draw_table_card(3.5, 1.8, 'INTERVIEW_PANEL', ['panel_id'], ['interview_id', 'interviewer_id'], ['panel_role'], col='#7c3aed')
draw_table_card(6.5, 1.8, 'SCORECARDS', ['scorecard_id'], ['panel_id'], ['technical_score', 'overall_score', 'recommendation'], col='#7c3aed')
draw_table_card(9.5, 1.8, 'OFFERS', ['offer_id'], ['application_id'], ['base_salary', 'signature_hash', 'status'], col='#dc2626')

ax.set_xlim(0, 12.5)
ax.set_ylim(-0.3, 7.2)
ax.axis('off')
ax.set_title('ENTITY-RELATIONSHIP DIAGRAM (3RD NORMAL FORM RELATIONAL SCHEMA)', fontsize=12, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'erd.png'))
plt.close()

# -------------------------------------------------------------
# 5. diagrams/c4-context.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
ax.set_facecolor('#ffffff')

core = patches.FancyBboxPatch((3.8, 2.6), 3.4, 2.0, boxstyle='round,pad=0.1', facecolor='#1e40af', edgecolor='#172554', linewidth=1.5)
ax.add_patch(core)
ax.text(5.5, 3.8, 'Novus Enterprise ATS\n[Software System]', ha='center', va='center', fontsize=10, fontweight='bold', color='#ffffff')
ax.text(5.5, 3.1, 'Centralized recruitment,\npipeline triage, scorecards,\nand offer management.', ha='center', va='center', fontsize=7.5, color='#bfdbfe')

def draw_c4_ext(x, y, title, desc, col='#475569'):
    b = patches.FancyBboxPatch((x, y), 2.2, 1.2, boxstyle='round,pad=0.08', facecolor=col, edgecolor='#1e293b', linewidth=1)
    ax.add_patch(b)
    ax.text(x + 1.1, y + 0.8, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#ffffff')
    ax.text(x + 1.1, y + 0.4, desc, ha='center', va='center', fontsize=6.8, color='#e2e8f0')

# Users on left
draw_c4_ext(0.6, 4.4, 'Candidate\n[Person]', 'Applies & books slots', '#0f766e')
draw_c4_ext(0.6, 2.8, 'Corporate Recruiter\n[Person]', 'Triages & schedules', '#0f766e')
draw_c4_ext(0.6, 1.2, 'Hiring Manager\n[Person]', 'Evaluates & decides', '#0f766e')

# External systems on right
draw_c4_ext(8.2, 4.4, 'Azure AD / Okta\n[External IAM]', 'SSO authentication', '#334155')
draw_c4_ext(8.2, 2.8, 'Microsoft 365\n[Graph API]', 'Calendar synchronization', '#334155')
draw_c4_ext(8.2, 1.2, 'Workday HRIS\n[Core HR Platform]', 'New-hire onboarding API', '#334155')

# Connecting lines
for y in [5.0, 3.4, 1.8]:
    ax.plot([2.8, 3.8], [y, 3.6], color='#94a3b8', lw=1.2, linestyle='--')
    ax.plot([7.2, 8.2], [3.6, y], color='#94a3b8', lw=1.2, linestyle='--')

ax.set_xlim(0, 11)
ax.set_ylim(0.5, 6.5)
ax.axis('off')
ax.set_title('C4 ARCHITECTURE MODEL: LEVEL 1 SYSTEM CONTEXT DIAGRAM', fontsize=12, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'c4-context.png'))
plt.close()

# -------------------------------------------------------------
# 6. diagrams/c4-container.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

layers = [
    ('PRESENTATION TIER (Next.js / React Web & Mobile)', 5.2, 1.3, '#eff6ff', '#bfdbfe'),
    ('SECURITY & API GATEWAY LAYER (WAF, Kong API Gateway, TLS 1.3)', 3.6, 1.1, '#f1f5f9', '#cbd5e1'),
    ('APPLICATION MICROSERVICES TIER (8 Domain Services + Workers)', 1.8, 1.4, '#faf5ff', '#e9d5ff'),
    ('DATA & STORAGE TIER (PostgreSQL 15 Cluster, Redis, AWS S3)', 0.2, 1.2, '#f0fdf4', '#bbf7d0')
]

for name, y, h, bg, border in layers:
    box = patches.FancyBboxPatch((0.5, y), 11.0, h, boxstyle='round,pad=0.05', facecolor=bg, edgecolor=border, linewidth=1.2)
    ax.add_patch(box)
    ax.text(0.7, y + h - 0.22, name, fontsize=8.5, fontweight='bold', color='#334155')

draw_node(1.2, 5.7, 'Candidate Portal\n(Next.js Mobile-First)', '#2563eb', width=2.4)
draw_node(4.2, 5.7, 'Staff Workstation\n(React SPA Kanban)', '#2563eb', width=2.4)
draw_node(7.2, 5.7, 'Mobile Scorecard\n(PWA Responsive)', '#2563eb', width=2.4)

draw_node(1.2, 4.0, 'Cloudflare WAF\nDDoS & Rate Limit', '#475569', width=2.4)
draw_node(4.2, 4.0, 'Kong API Gateway\nJWT & Route Table', '#475569', width=2.4)
draw_node(7.2, 4.0, 'Azure AD / Okta SSO\nSAML 2.0 Auth', '#475569', width=2.4)

draw_node(1.0, 2.3, 'Requisition\nService', '#7c3aed', width=1.6)
draw_node(2.8, 2.3, 'Ingestion &\nParser', '#7c3aed', width=1.6)
draw_node(4.6, 2.3, 'Pipeline\nEngine', '#7c3aed', width=1.6)
draw_node(6.4, 2.3, 'Calendar\nScheduler', '#7c3aed', width=1.6)
draw_node(8.2, 2.3, 'Scorecard &\nOffer', '#7c3aed', width=1.6)

draw_node(1.2, 0.6, 'PostgreSQL 15\n(Primary Encrypted)', '#059669', width=2.4)
draw_node(4.2, 0.6, 'Read Replica\n(Dedicated Power BI)', '#059669', width=2.4)
draw_node(7.2, 0.6, 'Redis Cluster &\nAWS S3 Vault', '#059669', width=2.4)

ax.set_xlim(0, 12)
ax.set_ylim(-0.1, 7.0)
ax.axis('off')
ax.set_title('C4 ARCHITECTURE MODEL: LEVEL 2 CONTAINER ARCHITECTURE', fontsize=12, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'c4-container.png'))
plt.close()

# -------------------------------------------------------------
# 7. diagrams/integration-architecture.png
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6.5), dpi=200)
ax.set_facecolor('#ffffff')

# Lifelines
actors = ['Candidate\nPortal', 'ATS Core\nBackend', 'MS Graph API\n(Calendar)', 'Workday Core HRIS\n(REST API)']
x_actors = [1.5, 4.2, 6.9, 9.5]

for name, x in zip(actors, x_actors):
    box = patches.FancyBboxPatch((x - 0.9, 5.4), 1.8, 0.6, boxstyle='round,pad=0.05', facecolor='#1e293b', edgecolor='#0f172a')
    ax.add_patch(box)
    ax.text(x, 5.7, name, ha='center', va='center', fontsize=8, fontweight='bold', color='#ffffff')
    ax.plot([x, x], [5.3, 0.4], color='#cbd5e1', lw=1.2, linestyle='--')

def draw_msg(y, x1, x2, text, num, color='#2563eb'):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', lw=1.4, color=color))
    ax.text((x1 + x2)/2, y + 0.12, f'{num}. {text}', ha='center', fontsize=7.5, fontweight='bold', color='#1e293b')

draw_msg(4.6, 1.5, 4.2, 'Accepts Offer & Signs Digitally', '1')
draw_msg(3.9, 4.2, 6.9, 'Release Interview Calendar Holds', '2')
draw_msg(3.3, 6.9, 4.2, '200 OK (Holds Released)', '3', '#059669')
draw_msg(2.6, 4.2, 9.5, 'POST /api/v1/employees/onboarding-intake', '4', '#d97706')
draw_msg(1.9, 9.5, 4.2, '201 Created { employee_id: "EMP-94021" }', '5', '#059669')
draw_msg(1.2, 4.2, 1.5, 'Status: HIRED & Onboarding Package Ready', '6', '#10b981')

ax.set_xlim(0, 11)
ax.set_ylim(0.2, 6.2)
ax.axis('off')
ax.set_title('INTEGRATION ARCHITECTURE & CORE HRIS HANDOVER SEQUENCE', fontsize=12, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig(os.path.join(dst_dir, 'integration-architecture.png'))
plt.close()

print('All 7 diagrams generated successfully in diagrams/')

