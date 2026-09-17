#!/usr/bin/env bash
# GitHub MCP (stdio) — loads token from env, ~/.cemini/github-pat, or `gh auth token`.
# Used by global Cursor MCP so GUI apps do not depend on shell-exported GITHUB_TOKEN.
# Never print the token.
set -euo pipefail

PAT_FILE="${GITHUB_PAT_FILE:-${HOME}/.cemini/github-pat}"
BIN="${GITHUB_MCP_BIN:-${HOME}/.local/bin/github-mcp-server}"

if [[ -z "${GITHUB_PERSONAL_ACCESS_TOKEN:-}" ]]; then
  if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    GITHUB_PERSONAL_ACCESS_TOKEN="${GITHUB_TOKEN}"
  elif [[ -r "${PAT_FILE}" ]]; then
    GITHUB_PERSONAL_ACCESS_TOKEN="$(tr -d '[:space:]' < "${PAT_FILE}")"
  elif command -v gh >/dev/null 2>&1; then
    GITHUB_PERSONAL_ACCESS_TOKEN="$(gh auth token 2>/dev/null || true)"
  fi
fi

if [[ -z "${GITHUB_PERSONAL_ACCESS_TOKEN:-}" ]]; then
  echo "mcp_github: set GITHUB_PERSONAL_ACCESS_TOKEN / GITHUB_TOKEN," >&2
  echo "mcp_github: write token to ${PAT_FILE}, or run: gh auth login" >&2
  exit 1
fi

export GITHUB_PERSONAL_ACCESS_TOKEN
export GITHUB_TOKEN="${GITHUB_TOKEN:-${GITHUB_PERSONAL_ACCESS_TOKEN}}"

if [[ ! -x "${BIN}" ]]; then
  echo "mcp_github: missing ${BIN} — run scripts/setup_cursor_github_mcp.sh" >&2
  exit 1
fi

exec "${BIN}" stdio "$@"
