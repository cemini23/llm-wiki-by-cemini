#!/usr/bin/env bash
# run_macro_charts_email_poller.sh — Gmail → inbox drop for Macro Charts cousin forwards.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$HOME/Library/Logs/cemini-macro-charts-email.log"
mkdir -p "$(dirname "$LOG")"

# LaunchAgent PATH is /usr/bin:/bin → system 3.9. Prefer pyenv 3.12+.
PYTHON="${CEMINI_PYTHON:-}"
if [[ -z "$PYTHON" ]]; then
  for candidate in \
    "$HOME/.pyenv/versions/3.12.5/bin/python3" \
    "$HOME/.pyenv/shims/python3.12" \
    "$(command -v python3.12 || true)" \
    "$(command -v python3 || true)"; do
    if [[ -n "$candidate" && -x "$candidate" ]]; then
      PYTHON="$candidate"
      break
    fi
  done
fi
[[ -n "${PYTHON:-}" ]] || PYTHON=python3

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_email_poller start ($PYTHON)"
  "$PYTHON" "$ROOT/scripts/macro_charts_email_poller.py" "$@"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_email_poller done"
} >> "$LOG" 2>&1
