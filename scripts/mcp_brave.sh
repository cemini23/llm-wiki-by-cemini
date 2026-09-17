#!/usr/bin/env bash
# Brave Search MCP (stdio) — loads API key from env or ~/.cemini/brave-api-key.
# Used by global Cursor MCP so GUI apps do not depend on shell-exported BRAVE_API_KEY.
# Never print the key.
set -euo pipefail

KEY_FILE="${BRAVE_API_KEY_FILE:-${HOME}/.cemini/brave-api-key}"
PKG="${BRAVE_MCP_PACKAGE:-@brave/brave-search-mcp-server@2.1.0}"

if [[ -z "${BRAVE_API_KEY:-}" ]] && [[ -r "${KEY_FILE}" ]]; then
  BRAVE_API_KEY="$(tr -d '[:space:]' < "${KEY_FILE}")"
  export BRAVE_API_KEY
fi

if [[ -z "${BRAVE_API_KEY:-}" ]]; then
  echo "mcp_brave: set BRAVE_API_KEY or write key to ${KEY_FILE}" >&2
  echo "mcp_brave: Brave dashboard → https://api-dashboard.search.brave.com/" >&2
  exit 1
fi

export BRAVE_API_KEY_FILE="${KEY_FILE}"
exec npx -y "${PKG}" "$@"
