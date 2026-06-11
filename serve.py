#!/usr/bin/env python3
import http.server, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, fmt, *args):
        pass  # silence per-request logs

print(f"FWC 2026 tracker running at http://localhost:{PORT}  (Ctrl+C to stop)")
http.server.HTTPServer(("", PORT), Handler).serve_forever()
