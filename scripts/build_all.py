"""
Master Build Script: Generates all diagrams, analytics workbooks, UI images, and PDF deliverables.
Usage:
    python scripts/build_all.py
"""

import os
import subprocess
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPTS_DIR)

BUILD_STEPS = [
    ("Diagrams", "generate_all_diagrams.py"),
    ("Analytics Assets", "build_analytics_assets.py"),
    ("UI Mockups", "build_ui_images.py"),
    ("Wireframes PDF", "build_wireframes_pdf.py"),
    ("Executive Presentation PDF", "build_presentation_pdf.py"),
    ("Project Summary PDF", "build_project_summary_pdf.py"),
]

def run_build():
    print("=" * 60)
    print("RECRUITMENT ATS PORTFOLIO - MASTER ASSET GENERATION")
    print(f"Project Root: {PROJECT_ROOT}")
    print("=" * 60)

    for label, script_name in BUILD_STEPS:
        script_path = os.path.join(SCRIPTS_DIR, script_name)
        print(f"\n[BUILDING] {label} ({script_name})...")
        if not os.path.exists(script_path):
            print(f"ERROR: Script not found at {script_path}")
            sys.exit(1)
        
        result = subprocess.run([sys.executable, script_path], cwd=PROJECT_ROOT)
        if result.returncode != 0:
            print(f"FAILED: {label} exited with code {result.returncode}")
            sys.exit(result.returncode)
        print(f"[SUCCESS] {label} generated cleanly.")

    print("\n" + "=" * 60)
    print("ALL DELIVERABLES SUCCESSFULLY GENERATED AND VERIFIED!")
    print("=" * 60)

if __name__ == "__main__":
    run_build()
