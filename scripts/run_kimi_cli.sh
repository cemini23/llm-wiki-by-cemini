#!/usr/bin/env bash
# Thin wrapper — requires Moonshot login (operator: kimi + /login or API key).
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
if ! command -v kimi >/dev/null 2>&1; then
  echo "kimi not installed. Run: bash scripts/adopt_k173_local.sh" >&2
  exit 1
fi
exec kimi "$@"
