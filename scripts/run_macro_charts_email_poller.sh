#!/usr/bin/env bash
# run_macro_charts_email_poller.sh — Gmail → inbox drop for Macro Charts cousin forwards.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$HOME/Library/Logs/cemini-macro-charts-email.log"
mkdir -p "$(dirname "$LOG")"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_email_poller start"
  python3 "$ROOT/scripts/macro_charts_email_poller.py" "$@"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_email_poller done"
} >> "$LOG" 2>&1
