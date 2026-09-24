import os
import re

html_path = "interactive_ats_portal.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

print("File size:", len(text), "bytes")

# Find all navigation onclick targets
nav_targets = re.findall(r"navigate\('([^']+)'\)", text)
print("Navigation targets found:", sorted(list(set(nav_targets))))

# Verify rendering functions
render_funcs = re.findall(r"function (render[A-Za-z]+)\(", text)
print("Render functions found:", sorted(list(set(render_funcs))))

# Check embedded data
has_embedded_csv = 'id="embedded-csv"' in text
row_count = len(re.findall(r'APP-2026-\d+', text))
print(f"Has embedded CSV: {has_embedded_csv} | Records count: {row_count}")

# Check key capabilities
capabilities = [
    ("Kanban Drag & Drop", "dragstart" in text and "dragover" in text and "drop" in text),
    ("Manager Scorecard Rubric", "setScore" in text or "rating" in text or "submitScorecard" in text),
    ("Candidate Self-Service Booking", "bookInterview" in text or "confirmBooking" in text or "booking-modal" in text or "renderCandidatePrototype" in text),
    ("Data Explorer Search & Pagination", "renderExplorerPage" in text and "exportFilteredCSV" in text),
    ("Filter Engine", "applyFilters" in text and "filter-chip" in text),
    ("SVG Charting Engines", "renderTTHTrendChart" in text and "renderBottleneckChart" in text and "renderFunnelBySource" in text),
    ("Financial Waterfall & ROI", "renderFinancialPage" in text and "waterfall" in text.lower())
]

for name, status in capabilities:
    print(f"[{'PASS' if status else 'FAIL'}] {name}")
