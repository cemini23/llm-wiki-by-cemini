#!/usr/bin/env bash
# run_substack_rss_poller.sh — finance Substack RSS feeds → inbox drop.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$HOME/Library/Logs/cemini-substack-rss.log"
mkdir -p "$(dirname "$LOG")"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] substack_rss_poller start"
  python3 "$ROOT/scripts/substack_rss_poller.py" "$@"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] substack_rss_poller done"
} >> "$LOG" 2>&1
