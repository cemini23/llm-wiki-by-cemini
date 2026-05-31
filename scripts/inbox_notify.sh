#!/usr/bin/env bash
# inbox_notify.sh — run preingest_check when files land in the ingest drop zone (Phase 2).
#
# Invoked by LaunchAgent (WatchPaths) or manually after dropping sources.
# Updates today's daily sweep inbox section + optional macOS notification.
#
# Usage:
#   ./scripts/inbox_notify.sh
#   bash scripts/install_workflow_launchagents.sh   # one-time LaunchAgent install

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INBOX="$ROOT/research to be indexed"
LOGFILE="$HOME/Library/Logs/cemini-inbox-watch.log"
TODAY=$(date +%Y-%m-%d)
SWEEP="$ROOT/wiki/sweeps/${TODAY}-daily.md"

mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGFILE"
}

notify_macos() {
  local title="$1"
  local message="$2"
  if [[ "$(uname -s)" == "Darwin" ]] && command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"${message}\" with title \"${title}\"" 2>/dev/null || true
  fi
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

# Phase 2: mirror inbox state into today's daily sweep
if python3 "$ROOT/scripts/append_inbox_to_daily_sweep.py" >> "$LOGFILE" 2>&1; then
  log "appended inbox section to ${SWEEP}"
else
  log "WARN: append_inbox_to_daily_sweep failed"
fi

# Auto license spot-check on tool-eval drops (K84 workflow)
while IFS= read -r f; do
  base=$(basename "$f")
  if echo "$base" | grep -Eiq 'tool.?eval|evaluation|wiki.?fit'; then
    log "tool-eval detected: $base — running post_tool_eval_license.sh"
    bash "$ROOT/scripts/post_tool_eval_license.sh" "$f" >> "$LOGFILE" 2>&1 || true
    notify_macos "Cemini inbox" "Tool eval dropped — license spot-check saved to .local/reports/"
  fi
done < <(find "$INBOX" -maxdepth 1 -type f ! -name '.*')

notify_macos "Cemini inbox" "${count} file(s) in research to be indexed — see ${SWEEP##*/}"

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
