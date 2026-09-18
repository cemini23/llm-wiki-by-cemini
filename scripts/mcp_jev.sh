#!/usr/bin/env bash
# jev-mcp (stdio) — TypeSafe Jev judgment tools from the K263 REFERENCE clone.
# Operator GO 2026-09-18. Loads TYPESAFE_API_KEY from env or ~/.cemini/typesafe-api-key.
# Never npx github:. Never commit keys.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/.local/adopts/jev-mcp/dist/index.js"

if [[ -z "${TYPESAFE_API_KEY:-}" ]] && [[ -f "${HOME}/.cemini/typesafe-api-key" ]]; then
  TYPESAFE_API_KEY="$(tr -d '[:space:]' < "${HOME}/.cemini/typesafe-api-key")"
  export TYPESAFE_API_KEY
fi

if [[ -z "${TYPESAFE_API_KEY:-}" ]]; then
  echo "mcp_jev: set TYPESAFE_API_KEY or write key to ~/.cemini/typesafe-api-key" >&2
  exit 1
fi

if [[ ! -f "$BIN" ]]; then
  echo "mcp_jev: missing $BIN — npm ci && npm run build in .local/adopts/jev-mcp" >&2
  exit 1
fi

exec node "$BIN"
