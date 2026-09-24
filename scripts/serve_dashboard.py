"""
Launch a local HTTP server and open the Recruitment Intelligence Dashboard in the browser.
Usage:
    python scripts/serve_dashboard.py
"""

import http.server
import os
import socketserver
import webbrowser
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080

def start_server():
    os.chdir(PROJECT_ROOT)
    handler = http.server.SimpleHTTPRequestHandler
    
    # Try port 8080 or find next available port
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), handler) as httpd:
                url = f"http://localhost:{port}/analytics/recruitment-intelligence-dashboard.html"
                print("=" * 65)
                print("RECRUITMENT INTELLIGENCE - ENTERPRISE ATS ANALYTICS DASHBOARD")
                print("=" * 65)
                print(f"Serving dashboard at: {url}")
                print("Press Ctrl+C to stop the server.")
                print("=" * 65)
                webbrowser.open(url)
                httpd.serve_forever()
                break
        except OSError:
            port += 1

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nDashboard server stopped.")
        sys.exit(0)
