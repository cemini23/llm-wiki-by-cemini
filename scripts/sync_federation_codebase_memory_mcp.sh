#!/usr/bin/env bash
# Merge codebase-memory-mcp (K134 CONDITIONAL-GO) into federation workspace .cursor/mcp.json
# Also merges into ~/.cursor/mcp.json (global). Creates project mcp.json when missing.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="${CODEBASE_MEMORY_MCP_BIN:-$HOME/.local/bin/codebase-memory-mcp}"

WORKSPACES=(
  "${ROOT}"
  "/Users/claudiobarone/Projects/Cemini claude code CCC"
  "/Users/claudiobarone/Projects/OSINT WORKSPACE"
  "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
  "/Users/claudiobarone/Projects/Gambling wiki"
  "/Users/claudiobarone/Projects/Game Dev wiki"
  "/Users/claudiobarone/Desktop/projects/Game Dev wiki"
  "/Users/claudiobarone/Projects/Cybersecurity wiki"
  "/Users/claudiobarone/Projects/Image gen"
  "/Users/claudiobarone/Projects/SEO:GEO B&M Business"
  "/Users/claudiobarone/Projects/3D printing"
  "/Users/claudiobarone/Projects/CeminiSuite"
  "/Users/claudiobarone/Projects/cemini-federation-hub"
  "/Users/claudiobarone/Projects/castle-sim"
  "/Users/claudiobarone/Projects/CeminiDFS"
  "/Users/claudiobarone/Projects/world-cup-bot"
  "/Users/claudiobarone/Projects/wc-ticket-monitor"
  "/Users/claudiobarone/Projects/wc-r16-ticket-monitor"
  "/Users/claudiobarone/Projects/agent-toolkit-demo"
)

if [[ ! -x "${BIN}" ]]; then
  echo "Missing binary: ${BIN}" >&2
  echo "Install: curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config" >&2
  exit 1
fi

python3 - "${BIN}" "${HOME}/.cursor/mcp.json" "create-if-missing" "${WORKSPACES[@]}" <<'PY'
import json
import sys
from pathlib import Path

bin_path = sys.argv[1]
global_mcp = Path(sys.argv[2])
mode_create = sys.argv[3] == "create-if-missing"
workspaces = sys.argv[4:]
entry = {
    "type": "stdio",
    "disabled": False,
    "command": bin_path,
    "args": [],
    "env": {},
}
key = "codebase-memory-mcp"

def merge_file(mcp_path: Path, *, create: bool) -> str:
    if not mcp_path.is_file():
        if not create:
            return "skip-missing"
        mcp_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"mcpServers": {}}
    else:
        try:
            data = json.loads(mcp_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            return f"fail-json:{e}"
    servers = data.setdefault("mcpServers", {})
    if key in servers and servers[key].get("command") == bin_path:
        return "already"
    servers[key] = dict(entry)
    mcp_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return "merged"

ok = 0
skip = 0
fail = 0

g = merge_file(global_mcp, create=True)
if g.startswith("fail"):
    print(f"  FAIL global {global_mcp}: {g}", file=sys.stderr)
    fail += 1
elif g == "already":
    print(f"  OK   already global {global_mcp}")
    ok += 1
else:
    print(f"  OK   {g} global {global_mcp}")
    ok += 1

for ws in workspaces:
    p = Path(ws)
    if not p.is_dir():
        print(f"  SKIP missing {ws}")
        skip += 1
        continue
    mcp_path = p / ".cursor" / "mcp.json"
    result = merge_file(mcp_path, create=mode_create)
    if result.startswith("fail"):
        print(f"  FAIL {mcp_path}: {result}", file=sys.stderr)
        fail += 1
    elif result == "skip-missing":
        print(f"  SKIP no .cursor/mcp.json {ws}")
        skip += 1
    elif result == "already":
        print(f"  OK   already {ws}")
        ok += 1
    else:
        print(f"  OK   {result} {ws}")
        ok += 1

print("")
if fail:
    print(f"Merged/verified {ok}; skipped {skip}; failed {fail}", file=sys.stderr)
    raise SystemExit(1)
print(f"Merged/verified {ok} target(s); skipped {skip}.")
PY

echo "Binary: ${BIN} ($("${BIN}" --version 2>/dev/null || echo unknown))"
