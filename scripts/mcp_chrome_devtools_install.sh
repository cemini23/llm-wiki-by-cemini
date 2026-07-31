#!/usr/bin/env bash
# Pin chrome-devtools-mcp into gitignored .local/mcp-bins (no npx -y at runtime).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/.local/mcp-bins"
VER="${1:-1.6.0}"
mkdir -p "$BIN"
cd "$BIN"
if [[ ! -f package.json ]]; then
  npm init -y >/dev/null
fi
npm install --no-fund --no-audit "chrome-devtools-mcp@${VER}"
echo "OK: $BIN/node_modules/.bin/chrome-devtools-mcp @${VER}"
