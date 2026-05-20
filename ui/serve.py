#!/usr/bin/env python3
"""
Cemini AI chat UI — local HTTP server + proxy to the gateway.

Topology:
    browser  ->  http://127.0.0.1:9000/                  (this server)
                            |
                            |  /chat, /health proxied to
                            v
                 http://127.0.0.1:8088/...               (SSH tunnel)
                            |
                            v
                 cemini-egress-fi:8088 (gateway)

Run:
    ssh -fN -L 8288:127.0.0.1:8088 cemini-egress-fi      # in another terminal
    python3 ui/serve.py
    open http://127.0.0.1:9000/                          # browser

Local port 8288 was chosen because 8088 is commonly used by another tunnel to
cemini-librarian (stash MCP). Override with CEMINI_AI_GATEWAY_PORT if needed.

The proxy exists because the gateway has no CORS middleware; serving the HTML
from the same origin as the API avoids a server-side change.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

UI_DIR = Path(__file__).resolve().parent
INDEX_HTML = UI_DIR / "index.html"

GATEWAY_PORT = int(os.environ.get("CEMINI_AI_GATEWAY_PORT", "8288"))
GATEWAY_URL = f"http://127.0.0.1:{GATEWAY_PORT}"
LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = int(os.environ.get("CEMINI_AI_UI_PORT", "9000"))

CHAT_TIMEOUT_S = 60   # gateway p50 ~3s, p99 ~12s; pad for slow conductor turns
HEALTH_TIMEOUT_S = 5


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write(f"[{self.log_date_time_string()}] {fmt % args}\n")

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _proxy(self, method: str, path: str, body: bytes | None, timeout: float) -> None:
        url = f"{GATEWAY_URL}{path}"
        headers = {"Content-Type": "application/json"} if body else {}
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                upstream_body = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", resp.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(upstream_body)))
                self.end_headers()
                self.wfile.write(upstream_body)
        except urllib.error.HTTPError as e:
            upstream_body = e.read() or b'{"error":"upstream HTTP error"}'
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(upstream_body)))
            self.end_headers()
            self.wfile.write(upstream_body)
        except (urllib.error.URLError, ConnectionRefusedError, TimeoutError) as e:
            self._send_json(
                502,
                {
                    "error": "gateway_unreachable",
                    "detail": str(e),
                    "hint": f"Is the SSH tunnel up? `ssh -fN -L {GATEWAY_PORT}:127.0.0.1:8088 cemini-egress-fi`",
                },
            )

    def do_GET(self) -> None:
        if self.path == "/" or self.path == "/index.html":
            try:
                html = INDEX_HTML.read_bytes()
            except FileNotFoundError:
                self._send_json(500, {"error": "index.html not found", "expected": str(INDEX_HTML)})
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return

        if self.path == "/health":
            self._proxy("GET", "/health", None, HEALTH_TIMEOUT_S)
            return

        self._send_json(404, {"error": "not_found", "path": self.path})

    def do_POST(self) -> None:
        if self.path != "/chat":
            self._send_json(404, {"error": "not_found", "path": self.path})
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        self._proxy("POST", "/chat", body, CHAT_TIMEOUT_S)


def main() -> None:
    if not INDEX_HTML.exists():
        sys.stderr.write(f"warning: {INDEX_HTML} not found — GET / will 500 until it exists\n")
    server = ThreadingHTTPServer((LISTEN_HOST, LISTEN_PORT), Handler)
    url = f"http://{LISTEN_HOST}:{LISTEN_PORT}/"
    sys.stderr.write(f"Cemini AI UI serving at {url}\n")
    sys.stderr.write(f"Proxying /chat + /health -> {GATEWAY_URL}\n")
    sys.stderr.write("Reminder: SSH tunnel must be open:\n")
    sys.stderr.write(f"  ssh -fN -L {GATEWAY_PORT}:127.0.0.1:8088 cemini-egress-fi\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.stderr.write("\nshutting down\n")
        server.server_close()


if __name__ == "__main__":
    main()
