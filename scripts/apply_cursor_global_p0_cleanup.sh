#!/usr/bin/env bash
# Apply P0/P1 GLOBAL Cursor cleanup that agents cannot write under TCC-locked ~/.cursor.
# Run from Terminal.app (not Cursor agent sandbox) after closing other Cursor windows if needed.
#
# Safe: never prints secrets; converts Brave/GitHub literals → ${env:…}; disables cold MCP;
# deletes tipdrop-route-outsource.mdc twin.
#
# Usage:
#   bash scripts/apply_cursor_global_p0_cleanup.sh
#   bash scripts/apply_cursor_global_p0_cleanup.sh --dry-run
set -euo pipefail

DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1

RULES="${HOME}/.cursor/rules"
MCP="${HOME}/.cursor/mcp.json"
TIPDROP="${RULES}/tipdrop-route-outsource.mdc"

echo "== Cursor global P0 cleanup =="
echo "MCP: ${MCP}"
echo "Rules: ${RULES}"

if [[ ! -f "${MCP}" ]]; then
  echo "ERROR: missing ${MCP}" >&2
  exit 1
fi

# 1) Delete tipdrop twin (keep cemini-route-outsource.mdc only)
if [[ -f "${TIPDROP}" ]]; then
  if [[ "${DRY}" -eq 1 ]]; then
    echo "[dry-run] would rm ${TIPDROP}"
  else
    rm -f "${TIPDROP}"
    echo "Deleted ${TIPDROP}"
  fi
else
  echo "OK tipdrop already absent"
fi

# 2) Redact secrets + disable cold MCP in global mcp.json
export MCP DRY
python3 << 'PY'
import json
import os
import re
import sys
from pathlib import Path

mcp_path = Path(os.environ["MCP"])
dry = os.environ.get("DRY") == "1"
data = json.loads(mcp_path.read_text())
servers = data.setdefault("mcpServers", {})

# Brave → env ref + disabled until operator exports key
if "brave-search" in servers:
    env = servers["brave-search"].setdefault("env", {})
    env["BRAVE_API_KEY"] = "${env:BRAVE_API_KEY}"
    servers["brave-search"]["disabled"] = True

# GitHub → env ref (no embedded Bearer)
if "github" in servers:
    headers = servers["github"].setdefault("headers", {})
    headers["Authorization"] = "Bearer ${env:GITHUB_TOKEN}"

# Cold / heavy MCP off
for name in (
    "playwright",
    "cloudflare",
    "cloudflare-docs",
    "cloudflare-bindings",
    "cloudflare-builds",
    "cloudflare-observability",
    "stash",
    "stripe",
    "codebase-memory-mcp",
    "brave-search",
):
    if name in servers:
        servers[name]["disabled"] = True

text = json.dumps(data, indent=2) + "\n"

# Fail closed if any credential-like literal remains
bad = []
for pat, label in (
    (r"\bgho_[A-Za-z0-9_]+", "gho_"),
    (r"\bghp_[A-Za-z0-9_]+", "ghp_"),
    (r"\bgithub_pat_[A-Za-z0-9_]+", "github_pat_"),
    (r"\bBSA[A-Za-z0-9_-]{10,}", "BSA"),
):
    for m in re.finditer(pat, text):
        # allow only inside comments? none — any match is fail
        bad.append(label)

if bad:
    print("ERROR: scanner still sees credential patterns:", sorted(set(bad)), file=sys.stderr)
    sys.exit(2)

if dry:
    print("[dry-run] would write mcp.json (keys only):", sorted(servers.keys()))
    for k, v in servers.items():
        print(f"  {k}: disabled={v.get('disabled', False)}")
else:
    mcp_path.write_text(text)
    print(f"Updated {mcp_path}")
    for k, v in servers.items():
        print(f"  {k}: disabled={v.get('disabled', False)}")
PY

echo ""
echo "Done. Next:"
echo "  export GITHUB_TOKEN=\"\$(gh auth token)\""
echo "  # Brave: rotate key in dashboard, then export BRAVE_API_KEY=... and set brave-search disabled:false"
echo "  Reload Cursor window"
echo "  See: reports/audit/cursor-config-2026-08-01/OPERATOR_ENV_ROTATE.md"
