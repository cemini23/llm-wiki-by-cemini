"""Conductor MCP server — exposes conductor_query tool to Claude Code.

Minimal JSON-RPC MCP implementation. No extra dependencies — just stdio.
Configure in Claude Code settings or .mcp.json to invoke.

Usage: python3 conductor/mcp_server.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any

SERVER_NAME = "conductor"
SERVER_VERSION = "0.1.1"

TOOLS = [
    {
        "name": "conductor_query",
        "description": "Route a financial/research question through Cemini Conductor — "
                       "the multi-model orchestrator. Classifies the query into taxonomy "
                       "(ticker_lookup, macro_analysis, quantitative_methods, etc.), "
                       "selects the best model (deepseek-chat vs deepseek-reasoner), "
                       "and returns the answer with routing metadata. Use this for any "
                       "analyst-style question about tickers, markets, options, macro "
                       "conditions, or quantitative methods.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The analyst question to route through Conductor"
                }
            },
            "required": ["query"]
        }
    }
]

SSH_HOST = "cemini-librarian"
CONDUCTOR_CMD = (
    "cd /opt/cemini && "
    "PYTHONPATH=/opt/cemini /opt/cemini/.venv/bin/python "
    "-m conductor.cli --routing-log /opt/cemini/logs/routing.jsonl --query"
)


def _call_conductor(query: str) -> dict[str, Any]:
    """Route a query through Conductor on the librarian via SSH."""
    cmd = f'ssh {SSH_HOST} \'{CONDUCTOR_CMD} "{query}"\' '
    try:
        result = subprocess.run(
            ["ssh", SSH_HOST, f"{CONDUCTOR_CMD} {_shell_quote(query)}"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return {"error": f"SSH failed (rc={result.returncode})", "stderr": result.stderr[:500]}
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        return {"error": "Conductor query timed out after 60s"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse Conductor response: {e}", "raw": result.stdout[:500] if 'result' in dir() else ""}
    except Exception as e:
        return {"error": str(e)}


def _shell_quote(s: str) -> str:
    """Minimal shell quoting."""
    escaped = s.replace("\\", "\\\\").replace('"', '\\"').replace("$", "\\$").replace("`", "\\`")
    return f'"{escaped}"'


def _send(response: dict[str, Any]) -> None:
    """Write a JSON-RPC response to stdout."""
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()


def _handle_request(req: dict[str, Any]) -> None:
    rid = req.get("id")
    method = req.get("method", "")

    if method == "initialize":
        _send({
            "jsonrpc": "2.0", "id": rid,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION}
            }
        })
    elif method == "notifications/initialized":
        pass  # no response for notifications
    elif method == "tools/list":
        _send({"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}})
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        if tool_name == "conductor_query":
            query_text = arguments.get("query", "").strip()
            if not query_text:
                _send({"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": "Error: missing 'query' argument"}]}})
                return
            result = _call_conductor(query_text)
            if "error" in result:
                text = f"Conductor error: {result['error']}"
            else:
                text = json.dumps(result, indent=2)
            _send({"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": text}]}})
        else:
            _send({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}})
    else:
        _send({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"Unknown method: {method}"}})


def main() -> None:
    """Run MCP server on stdio."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            _handle_request(req)
        except json.JSONDecodeError:
            _send({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}})
        except Exception as exc:
            _send({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(exc)}})


if __name__ == "__main__":
    main()
