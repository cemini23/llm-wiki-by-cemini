#!/usr/bin/env bash
# run_macro_charts_rss_poller.sh — Macro Charts free RSS → inbox drop.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$HOME/Library/Logs/cemini-macro-charts-rss.log"
mkdir -p "$(dirname "$LOG")"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_rss_poller start"
  python3 "$ROOT/scripts/macro_charts_rss_poller.py" "$@"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] macro_charts_rss_poller done"
} >> "$LOG" 2>&1
