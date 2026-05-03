"""Conductor HTTP API — lightweight server for inter-service queries.

Exposes /api/v1/query so any agent (Cemini LangGraph nodes, Claude Code MCP,
production analyst services) can route through Conductor via HTTP.

Run: PYTHONPATH=/opt/cemini python -m conductor.server --port 3840
"""

from __future__ import annotations

import json
import logging
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger("conductor.server")

_CONFIG_PATH: str = ""
_ORCHESTRATOR: Any = None


def _get_config_path(args_config: str = "") -> str:
    global _CONFIG_PATH
    if not _CONFIG_PATH:
        _CONFIG_PATH = args_config or os.path.join(os.path.dirname(__file__), "config.yaml")
    return _CONFIG_PATH


def _get_orchestrator():
    global _ORCHESTRATOR
    if _ORCHESTRATOR is not None:
        return _ORCHESTRATOR
    from conductor.orchestrator import Conductor

    _ORCHESTRATOR = Conductor(_get_config_path())
    return _ORCHESTRATOR


class QueryHandler(BaseHTTPRequestHandler):
    """Minimal HTTP handler — no framework dependency, fits in tight memory budget."""

    def log_message(self, fmt: str, *args: Any) -> None:
        logger.info("HTTP %s", fmt % args)

    def do_POST(self) -> None:
        if self.path not in ("/api/v1/query", "/api/v1/query/"):
            self._send_json(404, {"error": "not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length) if length else b"{}"
            payload = json.loads(body)
            query_text = payload.get("query", "").strip()
            if not query_text:
                self._send_json(400, {"error": "missing 'query' field"})
                return

            conductor = _get_orchestrator()
            response = conductor.route(query_text)

            self._send_json(200, {
                "query": query_text,
                "taxonomy": {
                    "name": response.routing.taxonomy.name if response.routing.taxonomy else "unknown",
                    "confidence": response.routing.taxonomy.confidence if response.routing.taxonomy else 0.0,
                },
                "model": response.routing.selected_model,
                "cascade_path": response.routing.cascade_path,
                "outcome": response.routing.outcome,
                "cost_estimate": response.routing.cost_estimate,
                "latency_ms": response.routing.latency_ms,
                "content": response.content,
                "tool_calls": response.routing.tool_calls,
                "sources": response.sources,
            })
        except Exception as exc:
            logger.exception("query error: %s", exc)
            self._send_json(500, {"error": str(exc)})

    def do_GET(self) -> None:
        if self.path in ("/api/v1/health", "/api/v1/health/"):
            self._send_json(200, {"status": "ok", "service": "conductor"})
        else:
            self._send_json(404, {"error": "not found"})

    def _send_json(self, status: int, data: dict[str, Any]) -> None:
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Conductor HTTP API server")
    parser.add_argument("--port", type=int, default=3840, help="Listen port (default: 3840)")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: 127.0.0.1)")
    parser.add_argument("--config", default="", help="Path to config.yaml")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(message)s")

    # Pre-load config path and orchestrator so the first query isn't slow
    if args.config:
        _get_config_path(args.config)
    orchestrator = _get_orchestrator()
    logger.info("Conductor server: orchestrator loaded and ready")

    server = HTTPServer((args.host, args.port), QueryHandler)
    logger.info("Conductor HTTP API listening on %s:%d", args.host, args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("shutting down")
        server.shutdown()


if __name__ == "__main__":
    main()
