#!/usr/bin/env bash
# Wire official GitHub MCP into ~/.cursor/mcp.json using env refs only.
# NEVER embeds a token into mcp.json. Operator loads token via shell/env.
#
# Usage:
#   bash scripts/setup_cursor_github_mcp.sh
#   bash scripts/setup_cursor_github_mcp.sh --write-pat-file   # optional: save gh token to ~/.cemini/github-pat
#
# Then (each shell / Cursor launch):
#   export GITHUB_TOKEN="$(gh auth token)"
# See: reports/audit/cursor-config-2026-08-01/OPERATOR_ENV_ROTATE.md
set -euo pipefail

PAT_FILE="${HOME}/.cemini/github-pat"
MCP_FILE="${HOME}/.cursor/mcp.json"
WRITE_PAT_FILE=0

for arg in "$@"; do
  case "$arg" in
    --write-pat-file) WRITE_PAT_FILE=1 ;;
    -h|--help)
      sed -n '2,14p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg (try --write-pat-file)" >&2
      exit 1
      ;;
  esac
done

mkdir -p "${HOME}/.cemini" "${HOME}/.cursor"

if [[ "${WRITE_PAT_FILE}" -eq 1 ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "setup_cursor_github_mcp: --write-pat-file requires gh CLI" >&2
    exit 1
  fi
  # Write PAT file only when explicitly requested; never print the token.
  gh auth token > "${PAT_FILE}"
  chmod 600 "${PAT_FILE}"
  echo "Wrote ${PAT_FILE} (chmod 600). Prefer env over this file for Cursor MCP."
fi

export MCP_FILE
python3 << 'PY'
import json
import os
from pathlib import Path

mcp_path = Path(os.environ["MCP_FILE"])
data = {"mcpServers": {}}
if mcp_path.exists():
    data = json.loads(mcp_path.read_text())

# Env-ref only — Cursor expands ${env:GITHUB_TOKEN} at MCP start.
# Operator: export GITHUB_TOKEN="$(gh auth token)" before launching Cursor.
data.setdefault("mcpServers", {})["github"] = {
    "url": "https://api.githubcopilot.com/mcp/",
    "headers": {"Authorization": "Bearer ${env:GITHUB_TOKEN}"},
}
mcp_path.write_text(json.dumps(data, indent=2) + "\n")
print(f"Updated {mcp_path} — github MCP uses Bearer ${{env:GITHUB_TOKEN}} (no embedded token)")
PY

cat <<'EOF'

Next (do not paste tokens into mcp.json):
  export GITHUB_TOKEN="$(gh auth token)"
  # Optional refresh: gh auth refresh -h github.com -s gist,read:org,repo,workflow
  # Persist for GUI Cursor: add export to ~/.zshrc, then launch Cursor from that shell
  #   OR: launchctl setenv GITHUB_TOKEN "$(gh auth token)"  (session only)

Reload Cursor: Settings → MCP → github → Retry, or Developer: Reload Window
Full steps: reports/audit/cursor-config-2026-08-01/OPERATOR_ENV_ROTATE.md
EOF
