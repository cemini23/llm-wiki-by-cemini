#!/usr/bin/env bash
# One-time / refresh: wire official GitHub MCP into ~/.cursor/mcp.json (global).
# Token: GITHUB_PERSONAL_ACCESS_TOKEN, ~/.cemini/github-pat, or `gh auth token`.
set -euo pipefail

PAT_FILE="${HOME}/.cemini/github-pat"
MCP_FILE="${HOME}/.cursor/mcp.json"

resolve_token() {
  if [[ -n "${GITHUB_PERSONAL_ACCESS_TOKEN:-}" ]]; then
    printf '%s' "${GITHUB_PERSONAL_ACCESS_TOKEN}"
    return
  fi
  if [[ -f "${PAT_FILE}" ]]; then
    tr -d '[:space:]' < "${PAT_FILE}"
    return
  fi
  if command -v gh >/dev/null 2>&1; then
    gh auth token
    return
  fi
  echo "setup_cursor_github_mcp: need GITHUB_PERSONAL_ACCESS_TOKEN, ${PAT_FILE}, or gh auth login" >&2
  exit 1
}

mkdir -p "${HOME}/.cemini" "${HOME}/.cursor"
TOKEN="$(resolve_token)"
if [[ ! -f "${PAT_FILE}" ]]; then
  printf '%s' "${TOKEN}" > "${PAT_FILE}"
  chmod 600 "${PAT_FILE}"
fi

export MCP_FILE TOKEN
python3 << PY
import json
import os
from pathlib import Path

mcp_path = Path(os.environ["MCP_FILE"])
token = os.environ["TOKEN"]
data = {"mcpServers": {}}
if mcp_path.exists():
    data = json.loads(mcp_path.read_text())
data.setdefault("mcpServers", {})["github"] = {
    "url": "https://api.githubcopilot.com/mcp/",
    "headers": {"Authorization": f"Bearer {token}"},
}
mcp_path.write_text(json.dumps(data, indent=2) + "\n")
print(f"Updated {mcp_path} — github MCP (remote HTTP)")
PY

echo "Reload Cursor: Settings → MCP → github → Retry, or Developer: Reload Window"
