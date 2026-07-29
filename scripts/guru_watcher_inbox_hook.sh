#!/usr/bin/env bash
# OSINT hook: Macro Charts inbox drop → GuruWatcher ingest + prod reconcile.
set -euo pipefail

OSINT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GW="${GURU_WATCHER_ROOT:-$HOME/Projects/GuruWatcher}"
INBOX="$OSINT_ROOT/research to be indexed"
LOG="${HOME}/Library/Logs/cemini-guru-watcher-sync.log"

mkdir -p "$(dirname "$LOG")"

if [[ ! -f "$GW/scripts/sync_from_osint_inbox.sh" ]]; then
  echo "[$(date '+%F %T')] GuruWatcher missing at $GW — skip" | tee -a "$LOG"
  exit 0
fi

shopt -s nullglob
files=("$INBOX"/macro-charts-paid-forward-* "$INBOX"/macro-charts-rss-*)
if [[ ${#files[@]} -eq 0 ]]; then
  exit 0
fi

{
  echo "==== $(date -u +%Y-%m-%dT%H:%M:%SZ) ===="
  OSINT_ROOT="$OSINT_ROOT" OSINT_INBOX="$INBOX" \
    bash "$GW/scripts/sync_from_osint_inbox.sh"
} >>"$LOG" 2>&1 || {
  echo "[$(date '+%F %T')] sync failed — see $LOG" >&2
  exit 0
}
