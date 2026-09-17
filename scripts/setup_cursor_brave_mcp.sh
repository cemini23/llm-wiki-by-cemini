#!/usr/bin/env bash
# Wire Brave Search MCP into ~/.cursor/mcp.json without embedding the API key.
# GUI Cursor does not inherit ~/.zshrc, so ${env:BRAVE_API_KEY} was empty and
# the server exited with "A Brave API key is required".
#
# Auth source (same pattern as Exa): ~/.cemini/brave-api-key (chmod 600)
# Wrapper: ~/.local/bin/mcp-brave  (copy of scripts/mcp_brave.sh)
#
# Usage:
#   bash scripts/setup_cursor_brave_mcp.sh
#   bash scripts/setup_cursor_brave_mcp.sh --from-cursor-history
#   bash scripts/setup_cursor_brave_mcp.sh --from-env
#
# Never prints the key. Never writes BSA literals into mcp.json.
set -euo pipefail

KEY_FILE="${HOME}/.cemini/brave-api-key"
MCP_FILE="${HOME}/.cursor/mcp.json"
WRAPPER_DST="${HOME}/.local/bin/mcp-brave"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WRAPPER_SRC="${SCRIPT_DIR}/mcp_brave.sh"
FROM_HISTORY=0
FROM_ENV=0

for arg in "$@"; do
  case "$arg" in
    --from-cursor-history) FROM_HISTORY=1 ;;
    --from-env) FROM_ENV=1 ;;
    -h|--help)
      sed -n '2,16p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 1
      ;;
  esac
done

mkdir -p "${HOME}/.cemini" "${HOME}/.local/bin" "${HOME}/.cursor"
chmod 700 "${HOME}/.cemini"

recover_from_history() {
  python3 << 'PY'
import json, os, re, stat, sys
from pathlib import Path

hist = Path.home() / "Library/Application Support/Cursor/User/History/3f1544d7"
entries_path = hist / "entries.json"
if not entries_path.exists():
    # locate mcp.json history dir
    root = Path.home() / "Library/Application Support/Cursor/User/History"
    hist = None
    if root.exists():
        for d in root.iterdir():
            ep = d / "entries.json"
            if not ep.exists():
                continue
            try:
                meta = json.loads(ep.read_text())
            except Exception:
                continue
            if meta.get("resource") == "file:///Users/claudiobarone/.cursor/mcp.json":
                hist = d
                entries_path = ep
                break
    if hist is None:
        print("NO_HISTORY", file=sys.stderr)
        sys.exit(2)

entries = json.loads(entries_path.read_text())
pat = re.compile(r"^BSA[A-Za-z0-9_-]{10,}$")
key = None
source = None
for e in reversed(entries.get("entries", [])):
    p = hist / e["id"]
    if not p.exists():
        continue
    try:
        data = json.loads(p.read_text())
    except Exception:
        continue
    raw = (
        data.get("mcpServers", {})
        .get("brave-search", {})
        .get("env", {})
        .get("BRAVE_API_KEY")
    )
    if not isinstance(raw, str):
        continue
    raw = raw.strip()
    if raw.startswith("${") or not pat.match(raw):
        continue
    key = raw
    source = e["id"]
    break

if not key:
    print("NO_RECOVERABLE_KEY", file=sys.stderr)
    sys.exit(2)

dest = Path.home() / ".cemini" / "brave-api-key"
dest.write_text(key + "\n")
os.chmod(dest, stat.S_IRUSR | stat.S_IWUSR)
print(f"recovered key file from Cursor history {source} (not printed)")
PY
}

if [[ "${FROM_ENV}" -eq 1 ]]; then
  if [[ -z "${BRAVE_API_KEY:-}" ]]; then
    echo "setup_cursor_brave_mcp: --from-env requires BRAVE_API_KEY in this shell" >&2
    exit 1
  fi
  printf '%s\n' "${BRAVE_API_KEY}" > "${KEY_FILE}"
  chmod 600 "${KEY_FILE}"
  echo "Wrote ${KEY_FILE} from env (chmod 600)"
elif [[ "${FROM_HISTORY}" -eq 1 ]] || [[ ! -r "${KEY_FILE}" ]]; then
  recover_from_history
fi

if [[ ! -r "${KEY_FILE}" ]]; then
  echo "setup_cursor_brave_mcp: missing ${KEY_FILE}" >&2
  echo "Write the Brave Search API key to that file (chmod 600), then re-run." >&2
  exit 1
fi

if [[ ! -f "${WRAPPER_SRC}" ]]; then
  echo "setup_cursor_brave_mcp: missing ${WRAPPER_SRC}" >&2
  exit 1
fi
install -m 755 "${WRAPPER_SRC}" "${WRAPPER_DST}"
echo "Installed ${WRAPPER_DST}"

export MCP_FILE WRAPPER_DST KEY_FILE
python3 << 'PY'
import json
import os
from pathlib import Path

mcp_path = Path(os.environ["MCP_FILE"])
wrapper = os.environ["WRAPPER_DST"]
key_file = os.environ["KEY_FILE"]
data = {"mcpServers": {}}
if mcp_path.exists():
    data = json.loads(mcp_path.read_text())

servers = data.setdefault("mcpServers", {})
servers["brave-search"] = {
    "type": "stdio",
    "command": wrapper,
    "args": [],
    "env": {
        "BRAVE_API_KEY_FILE": key_file,
    },
    "disabled": False,
}
text = json.dumps(data, indent=2) + "\n"
if "BSA" in text:
    raise SystemExit("refusing to write mcp.json: BSA literal detected")
mcp_path.write_text(text)
print(f"Updated {mcp_path} — brave-search uses wrapper + BRAVE_API_KEY_FILE (no embedded key)")
PY

cat <<EOF

Brave MCP is wired for GUI Cursor (no shell env required).
  key file: ${KEY_FILE}
  wrapper:  ${WRAPPER_DST}

Reload: Settings → MCP → brave-search → Retry
  or Developer: Reload Window

Rotate later: paste a new key into ${KEY_FILE} (chmod 600), then Retry MCP.
EOF
