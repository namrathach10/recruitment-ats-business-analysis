import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.join(PROJECT_ROOT, "ui-ux")
os.makedirs(base_dir, exist_ok=True)

# -------------------------------------------------------------------------
# 1. Candidate Portal Mockup
# -------------------------------------------------------------------------
def create_candidate_portal():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 90)
    ax.axis("off")
    fig.patch.set_facecolor("#f1f5f9")

    # Top Navigation Bar
    nav = patches.Rectangle((0, 82), 140, 8, facecolor="#0f172a", edgecolor="none")
    ax.add_patch(nav)
    ax.text(6, 85.5, "NOVUS CAREERS", fontsize=15, fontweight="bold", color="#ffffff", va="center")
    ax.text(28, 85.5, "Search Jobs", fontsize=10, color="#94a3b8", va="center")
    ax.text(42, 85.5, "My Applications", fontsize=10, fontweight="bold", color="#38bdf8", va="center")
    ax.text(60, 85.5, "Company Culture", fontsize=10, color="#94a3b8", va="center")
    
    # User Profile Pill on right
    user_pill = patches.FancyBboxPatch((110, 83.5), 24, 5, boxstyle="round,pad=0.5", facecolor="#1e293b", edgecolor="#334155")
    ax.add_patch(user_pill)
    ax.text(122, 86, "Maya Lin | Profile", fontsize=10, color="#f8fafc", ha="center", va="center")

    # Breadcrumb & Page Heading
    ax.text(8, 77.5, "Home  >  Candidate Dashboard  >  Application #APP-2026-1042", fontsize=9, color="#64748b")
    ax.text(8, 74, "Application Tracking & Next Steps", fontsize=18, fontweight="bold", color="#0f172a")

    # Main Card
    main_card = patches.FancyBboxPatch((8, 14), 124, 56, boxstyle="round,pad=1.2", facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.5)
    ax.add_patch(main_card)

    # Job Header in Main Card
    ax.text(12, 65.5, "Senior Systems Software Engineer", fontsize=15, fontweight="bold", color="#1e293b")
    ax.text(12, 62.5, "Department: Core Infrastructure   |   Location: San Francisco, CA (Hybrid)   |   Requisition: #REQ-2026-0104", fontsize=10, color="#64748b")

    # Status Progress Bar Container
    prog_bg = patches.FancyBboxPatch((12, 47), 116, 12, boxstyle="round,pad=0.6", facecolor="#f8fafc", edgecolor="#e2e8f0")
    ax.add_patch(prog_bg)

    # Stages line
    ax.plot([25, 115], [53, 53], color="#cbd5e1", linewidth=3, zorder=2)
    ax.plot([25, 70], [53, 53], color="#10b981", linewidth=3.5, zorder=3)

    stages = [
        (25, "1. Applied", "Jan 12", True, "#10b981"),
        (47.5, "2. Screened", "Jan 14", True, "#10b981"),
        (70, "3. Interview", "ACTION REQ.", True, "#f59e0b"),
        (92.5, "4. Offer", "Pending", False, "#94a3b8"),
        (115, "5. Hired", "Pending", False, "#94a3b8")
    ]

    for x, label, sub, done, col in stages:
        if col == "#f59e0b":
            circ = plt.Circle((x, 53), 2.2, facecolor="#f59e0b", edgecolor="#ffffff", linewidth=2, zorder=4)
            ax.add_patch(circ)
            ax.text(x, 53, "!", color="white", fontsize=11, fontweight="bold", ha="center", va="center", zorder=5)
        elif done:
            circ = plt.Circle((x, 53), 2.0, facecolor="#10b981", edgecolor="#ffffff", linewidth=2, zorder=4)
            ax.add_patch(circ)
            ax.text(x, 53, "v", color="white", fontsize=9, fontweight="bold", ha="center", va="center", zorder=5)
        else:
            circ = plt.Circle((x, 53), 1.8, facecolor="#e2e8f0", edgecolor="#94a3b8", linewidth=1.5, zorder=4)
            ax.add_patch(circ)
        ax.text(x, 49, label, fontsize=9, fontweight="bold", color="#1e293b", ha="center")
        ax.text(x, 46.8, sub, fontsize=8, color="#64748b", ha="center")

    # Action Callout Banner (Yellow/Amber box)
    action_box = patches.FancyBboxPatch((12, 31), 116, 12, boxstyle="round,pad=0.8", facecolor="#fffbeb", edgecolor="#fde68a", linewidth=1.5)
    ax.add_patch(action_box)
    ax.text(15, 39.5, "ACTION REQUIRED: Schedule Your Technical Panel Interview", fontsize=12, fontweight="bold", color="#b45309")
    ax.text(15, 36, "Your technical qualifications have been shortlisted by the engineering review committee.\nPlease choose a convenient 45-minute architectural panel slot with Engineering Director David Vance.", fontsize=9, color="#78350f")

    # Button 1: Book slot
    btn_book = patches.FancyBboxPatch((86, 33), 22, 5, boxstyle="round,pad=0.4", facecolor="#2563eb", edgecolor="none")
    ax.add_patch(btn_book)
    ax.text(97, 35.5, "Choose Time Slot", fontsize=9.5, fontweight="bold", color="#ffffff", ha="center", va="center")

    # Button 2: Contact Recruiter
    btn_msg = patches.FancyBboxPatch((109.5, 33), 16, 5, boxstyle="round,pad=0.4", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(btn_msg)
    ax.text(117.5, 35.5, "Contact Recruiter", fontsize=8.5, color="#334155", ha="center", va="center")

    # Activity History section
    ax.text(12, 27, "Application History & Audit Trail", fontsize=11, fontweight="bold", color="#1e293b")
    ax.text(12, 23.5, "- Jan 14, 2026 - 02:30 PM: Application status advanced to 'Technical Interview' by Recruiter Sarah Jenkins.", fontsize=8.5, color="#475569")
    ax.text(12, 20.8, "- Jan 14, 2026 - 10:15 AM: Automated screening questions verified: Work authorization confirmed; 7 yrs experience validated.", fontsize=8.5, color="#475569")
    ax.text(12, 18.1, "- Jan 12, 2026 - 06:45 PM: Application submitted successfully via LinkedIn Job Syndication.", fontsize=8.5, color="#475569")

    # Footer note
    ax.text(8, 9, "Novus HR Systems  |  Applicant Privacy Statement  |  GDPR/CCPA Data Protection Rights  |  Encrypted 256-bit AES", fontsize=8, color="#94a3b8")

    out_path = os.path.join(base_dir, "candidate-portal.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_path)

# -------------------------------------------------------------------------
# 2. Recruiter Dashboard Kanban Mockup
# -------------------------------------------------------------------------
def create_recruiter_dashboard():
    fig, ax = plt.subplots(figsize=(15, 9.5), dpi=150)
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 95)
    ax.axis("off")
    fig.patch.set_facecolor("#f8fafc")

    # Top Navigation Bar
    nav = patches.Rectangle((0, 87), 150, 8, facecolor="#0f172a", edgecolor="none")
    ax.add_patch(nav)
    ax.text(6, 91, "NOVUS ATS WORKBENCH", fontsize=15, fontweight="bold", color="#ffffff", va="center")
    ax.text(38, 91, "Requisitions", fontsize=10, color="#94a3b8", va="center")
    ax.text(52, 91, "Candidates", fontsize=10, color="#94a3b8", va="center")
    ax.text(65, 91, "Pipelines", fontsize=10, fontweight="bold", color="#38bdf8", va="center")
    ax.text(78, 91, "Analytics", fontsize=10, color="#94a3b8", va="center")

    user_pill = patches.FancyBboxPatch((116, 88.5), 28, 5, boxstyle="round,pad=0.5", facecolor="#1e293b", edgecolor="#334155")
    ax.add_patch(user_pill)
    ax.text(130, 91, "Sarah Jenkins (Lead Recruiter)", fontsize=9, color="#f8fafc", ha="center", va="center")

    # Title & Filter Bar
    ax.text(6, 82.5, "Requisition: Senior Systems Software Engineer (#REQ-2026-0104)", fontsize=14, fontweight="bold", color="#0f172a")
    ax.text(6, 79.5, "Department: Core Infrastructure   |   Hiring Manager: David Vance   |   Target Openings: 1   |   SLA Target: 25 Days", fontsize=9, color="#64748b")

    # Filter Controls
    search_bar = patches.FancyBboxPatch((78, 80), 22, 4.5, boxstyle="round,pad=0.3", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(search_bar)
    ax.text(80, 82.2, "Search candidate...", fontsize=8.5, color="#94a3b8", va="center")

    flt_src = patches.FancyBboxPatch((102, 80), 18, 4.5, boxstyle="round,pad=0.3", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(flt_src)
    ax.text(111, 82.2, "Source: All [v]", fontsize=8.5, color="#334155", ha="center", va="center")

    flt_score = patches.FancyBboxPatch((122, 80), 14, 4.5, boxstyle="round,pad=0.3", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(flt_score)
    ax.text(129, 82.2, "Score: 80%+ [v]", fontsize=8.5, color="#334155", ha="center", va="center")

    btn_bulk = patches.FancyBboxPatch((138, 80), 9, 4.5, boxstyle="round,pad=0.3", facecolor="#2563eb", edgecolor="none")
    ax.add_patch(btn_bulk)
    ax.text(142.5, 82.2, "+ Add", fontsize=8.5, fontweight="bold", color="#ffffff", ha="center", va="center")

    # Kanban Columns
    columns = [
        ("APPLIED", "42 Candidates", 6, "#64748b", [
            ("James White", "Match: 78%", "In stage: 2d", "Source: LinkedIn", "#f1f5f9"),
            ("Ava Morales", "Match: 64%", "In stage: 4h", "Source: Indeed", "#f1f5f9"),
            ("Noah Brown", "Match: 52%", "In stage: 1d", "Source: Direct", "#f1f5f9")
        ]),
        ("SCREENED", "18 Candidates", 35, "#3b82f6", [
            ("Daniel Lee", "Match: 88%", "In stage: 1d", "Source: Referral", "#eff6ff"),
            ("Zoey Nelson", "Match: 85%", "In stage: 2d", "Source: Careers", "#eff6ff")
        ]),
        ("SHORTLISTED", "8 Candidates", 64, "#8b5cf6", [
            ("Maya Lin", "Match: 96%", "In stage: 3d", "Source: LinkedIn", "#f5f3ff"),
            ("Liam Carter", "Match: 91%", "In stage: 2d", "Source: Referral", "#f5f3ff")
        ]),
        ("INTERVIEW", "4 Candidates", 93, "#f59e0b", [
            ("Elena Rostova", "Match: 92%", "Panel: Vance", "Next: Thu 2 PM", "#fffbeb"),
            ("Sophia Green", "Match: 89%", "Panel: Vance", "Scorecard Due", "#fffbeb")
        ]),
        ("OFFER", "1 Candidate", 122, "#10b981", [
            ("Marcus Thorne", "Offer: $165k Base", "Status: Sent", "SLA: 48h left", "#ecfdf5")
        ])
    ]

    for title, count, x, col, cards in columns:
        # Col Header background
        col_hdr = patches.FancyBboxPatch((x, 71), 26, 6, boxstyle="round,pad=0.3", facecolor=col, edgecolor="none")
        ax.add_patch(col_hdr)
        ax.text(x + 2, 74.8, title, fontsize=9.5, fontweight="bold", color="#ffffff")
        ax.text(x + 2, 72.3, count, fontsize=8, color="#e2e8f0")

        # Col Body Background
        col_body = patches.FancyBboxPatch((x, 6), 26, 64, boxstyle="round,pad=0.4", facecolor="#f1f5f9", edgecolor="#e2e8f0")
        ax.add_patch(col_body)

        # Cards
        y_card = 60
        for name, score, time_info, src, card_bg in cards:
            card = patches.FancyBboxPatch((x + 1.2, y_card), 23.6, 8.5, boxstyle="round,pad=0.4", facecolor=card_bg, edgecolor="#cbd5e1", linewidth=1)
            ax.add_patch(card)
            
            # Name & match badge
            ax.text(x + 2.5, y_card + 6.2, name, fontsize=9, fontweight="bold", color="#0f172a")
            badge = patches.FancyBboxPatch((x + 16, y_card + 5.2), 7.5, 2.5, boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#94a3b8")
            ax.add_patch(badge)
            ax.text(x + 19.7, y_card + 6.4, score, fontsize=7.5, fontweight="bold", color="#1e293b", ha="center", va="center")

            ax.text(x + 2.5, y_card + 3.2, time_info, fontsize=8, color="#64748b")
            ax.text(x + 2.5, y_card + 1.2, src, fontsize=7.5, color="#94a3b8")

            y_card -= 10.5

    out_path = os.path.join(base_dir, "recruiter-dashboard.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_path)

# -------------------------------------------------------------------------
# 3. Hiring Manager Scorecard Mockup
# -------------------------------------------------------------------------
def create_hiring_manager_view():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 90)
    ax.axis("off")
    fig.patch.set_facecolor("#f8fafc")

    # Header Bar
    nav = patches.Rectangle((0, 83), 140, 7, facecolor="#0f172a", edgecolor="none")
    ax.add_patch(nav)
    ax.text(6, 86.5, "NOVUS ATS  |  HIRING MANAGER WORKBENCH", fontsize=14, fontweight="bold", color="#ffffff", va="center")
    ax.text(120, 86.5, "David Vance (VP Eng)", fontsize=9, color="#94a3b8", va="center")

    # Candidate Summary Banner
    banner = patches.FancyBboxPatch((6, 69), 128, 11, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(banner)
    ax.text(10, 76.5, "Candidate: Maya Lin", fontsize=13, fontweight="bold", color="#0f172a")
    ax.text(10, 73.5, "Requisition: Senior Systems Software Engineer (#REQ-2026-0104)   |   Stage: Technical Panel Review", fontsize=9, color="#64748b")
    ax.text(10, 70.8, "Application Date: Jan 12, 2026   |   Current Status: Evaluation Pending   |   Target SLA: < 24 Hours", fontsize=8.5, color="#94a3b8")

    # Quick metrics right side of banner
    m_box1 = patches.FancyBboxPatch((98, 70.5), 16, 8, boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor="#bfdbfe")
    ax.add_patch(m_box1)
    ax.text(106, 75.5, "96%", fontsize=13, fontweight="bold", color="#1d4ed8", ha="center")
    ax.text(106, 72.2, "Match Score", fontsize=7.5, color="#1e40af", ha="center")

    m_box2 = patches.FancyBboxPatch((116, 70.5), 16, 8, boxstyle="round,pad=0.3", facecolor="#ecfdf5", edgecolor="#a7f3d0")
    ax.add_patch(m_box2)
    ax.text(124, 75.5, "4.6 / 5.0", fontsize=12, fontweight="bold", color="#047857", ha="center")
    ax.text(124, 72.2, "Panel Rating", fontsize=7.5, color="#065f46", ha="center")

    # Left Column: Candidate Dossier (width 58)
    left_card = patches.FancyBboxPatch((6, 8), 58, 58, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(left_card)
    ax.text(9, 62.5, "CANDIDATE DOSSIER & PROFILE", fontsize=10.5, fontweight="bold", color="#1e293b")
    
    # Resume Details
    ax.text(9, 58.5, "Contact & Verification:", fontsize=9, fontweight="bold", color="#475569")
    ax.text(9, 56, "Email: maya.lin@example.com   |   Phone: +1 (415) 555-0192", fontsize=8, color="#64748b")
    ax.text(9, 53.5, "Work Authorization: US Citizen (Verified)   |   Notice: 2 Weeks", fontsize=8, color="#64748b")

    ax.text(9, 49.5, "Technical Competencies (Extracted):", fontsize=9, fontweight="bold", color="#475569")
    skills = ["Go (Golang)", "C / C++", "Linux Internals", "Distributed Consensus", "Kafka", "Docker & K8s"]
    x_s = 9
    for s in skills:
        spill = patches.FancyBboxPatch((x_s, 45.8), len(s)*1.3 + 2, 2.8, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor="#cbd5e1")
        ax.add_patch(spill)
        ax.text(x_s + (len(s)*1.3+2)/2, 47.2, s, fontsize=7.5, color="#334155", ha="center", va="center")
        x_s += len(s)*1.3 + 3.2
        if x_s > 50:
            x_s = 9

    ax.text(9, 42.5, "Experience Summary:", fontsize=9, fontweight="bold", color="#475569")
    ax.text(9, 39.5, "- Staff Systems Engineer @ High-Scale FinTech (4 yrs)", fontsize=8, color="#334155")
    ax.text(12, 37.2, "Architected high-throughput matching engine handling 120k QPS.", fontsize=7.5, color="#64748b")
    ax.text(9, 34.5, "- Senior Infrastructure Software Engineer @ CloudTech (3 yrs)", fontsize=8, color="#334155")
    ax.text(12, 32.2, "Designed custom eBPF networking telemetry and reduced p99 by 40%.", fontsize=7.5, color="#64748b")

    ax.text(9, 28.5, "Education & Credentials:", fontsize=9, fontweight="bold", color="#475569")
    ax.text(9, 26, "B.S. in Computer Science - UC Berkeley (Summa Cum Laude)", fontsize=8, color="#334155")
    ax.text(9, 23.5, "AWS Certified Solutions Architect - Professional", fontsize=8, color="#334155")

    btn_view_pdf = patches.FancyBboxPatch((9, 12), 26, 4.5, boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#94a3b8")
    ax.add_patch(btn_view_pdf)
    ax.text(22, 14.2, "[PDF] View Full Original Resume", fontsize=8, color="#1e293b", ha="center", va="center")

    # Right Column: Standardized Evaluation Rubric (width 68)
    right_card = patches.FancyBboxPatch((68, 8), 66, 58, boxstyle="round,pad=0.8", facecolor="#ffffff", edgecolor="#cbd5e1")
    ax.add_patch(right_card)
    ax.text(71, 62.5, "STRUCTURED INTERVIEW SCORECARD", fontsize=10.5, fontweight="bold", color="#1e293b")
    ax.text(71, 59.8, "Calibrated Competency Rubric (1 = Unsatisfactory, 5 = Exceptional)", fontsize=8, color="#64748b")

    rubrics = [
        ("1. Technical Architecture & Scalability", "Rating: 5.0 / 5.0 (Exceptional)", 54),
        ("2. Concurrent Programming & Problem Solving", "Rating: 4.5 / 5.0 (Strong Hire)", 46.5),
        ("3. System Reliability & Linux Internals", "Rating: 5.0 / 5.0 (Exceptional)", 39),
        ("4. Collaboration, Culture & Engineering Mentorship", "Rating: 4.0 / 5.0 (Competent)", 31.5)
    ]

    for r_title, r_score, y_pos in rubrics:
        ax.text(71, y_pos + 4, r_title, fontsize=8.5, fontweight="bold", color="#1e293b")
        ax.text(71, y_pos + 1.8, r_score, fontsize=8, color="#059669")
        # Star visualization bar
        prog_r = patches.FancyBboxPatch((105, y_pos + 1.5), 26, 2.5, boxstyle="round,pad=0.2", facecolor="#e2e8f0", edgecolor="none")
        ax.add_patch(prog_r)
        prog_fill = patches.FancyBboxPatch((105, y_pos + 1.5), 24, 2.5, boxstyle="round,pad=0.2", facecolor="#10b981", edgecolor="none")
        ax.add_patch(prog_fill)

    # Decision Recommendation
    ax.text(71, 28, "Final Recommendation:", fontsize=9, fontweight="bold", color="#1e293b")
    recs = [("Strong Hire", True), ("Hire", False), ("Hold", False), ("Reject", False)]
    x_rec = 71
    for label, selected in recs:
        radio_col = "#2563eb" if selected else "#94a3b8"
        bg_col = "#eff6ff" if selected else "#f8fafc"
        r_box = patches.FancyBboxPatch((x_rec, 23.5), 14, 3.5, boxstyle="round,pad=0.2", facecolor=bg_col, edgecolor=radio_col, linewidth=1.5 if selected else 1)
        ax.add_patch(r_box)
        ax.text(x_rec + 7, 25.2, label, fontsize=7.5, fontweight="bold" if selected else "normal", color="#1e293b", ha="center", va="center")
        x_rec += 15.5

    # Evaluation Notes
    ax.text(71, 20.5, "Evaluation Notes & Rationale:", fontsize=8.5, fontweight="bold", color="#1e293b")
    ax.text(71, 17.5, "\"Maya displayed world-class mastery of distributed systems and memory profiling.\nArticulated nuanced trade-offs in consensus engines. Exemplary technical fit.\"", fontsize=7.5, style="italic", color="#475569")

    # Action Buttons
    btn_submit = patches.FancyBboxPatch((71, 10.5), 32, 4.5, boxstyle="round,pad=0.3", facecolor="#10b981", edgecolor="none")
    ax.add_patch(btn_submit)
    ax.text(87, 12.7, "Submit Evaluation & Advance", fontsize=8.5, fontweight="bold", color="#ffffff", ha="center", va="center")

    btn_sync = patches.FancyBboxPatch((105, 10.5), 26, 4.5, boxstyle="round,pad=0.3", facecolor="#f1f5f9", edgecolor="#cbd5e1")
    ax.add_patch(btn_sync)
    ax.text(118, 12.7, "Request Panel Sync", fontsize=8, color="#334155", ha="center", va="center")

    out_path = os.path.join(base_dir, "hiring-manager.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Saved", out_path)

if __name__ == "__main__":
    create_candidate_portal()
    create_recruiter_dashboard()
    create_hiring_manager_view()
