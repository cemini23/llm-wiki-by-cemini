#!/usr/bin/env bash
# inbox_notify.sh — run preingest_check when files land in the ingest drop zone (K84 adoption).
#
# Invoked by LaunchAgent (WatchPaths) or manually after dropping sources.
# Logs to ~/Library/Logs/cemini-inbox-watch.log; prints summary to stdout.
#
# Usage:
#   ./scripts/inbox_notify.sh
#   bash scripts/install_workflow_launchagents.sh   # one-time LaunchAgent install

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INBOX="$ROOT/research to be indexed"
LOGFILE="$HOME/Library/Logs/cemini-inbox-watch.log"

mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGFILE"
}

if [[ ! -d "$INBOX" ]]; then
  log "ERROR: inbox missing at $INBOX"
  exit 1
fi

count=$(find "$INBOX" -maxdepth 1 -type f ! -name '.*' 2>/dev/null | wc -l | tr -d ' ')
if [[ "$count" -eq 0 ]]; then
  log "inbox empty — nothing to triage"
  exit 0
fi

log "inbox has $count file(s) — running preingest_check"
report=$(python3 "$ROOT/scripts/preingest_check.py" 2>&1) || true
echo "$report" >> "$LOGFILE"
echo "$report"

# Optional webhook (set in env or ~/.cemini/inbox-webhook.url)
WEBHOOK_FILE="$HOME/.cemini/inbox-webhook.url"
if [[ -f "$WEBHOOK_FILE" ]]; then
  url=$(tr -d '[:space:]' < "$WEBHOOK_FILE")
  if [[ -n "$url" ]]; then
    payload=$(python3 -c "import json,sys; print(json.dumps({'text': sys.stdin.read()[:3500]}))" <<< "$report")
    curl -sS -X POST -H 'Content-Type: application/json' -d "$payload" "$url" >> "$LOGFILE" 2>&1 || \
      log "webhook POST failed"
  fi
fi

exit 0
