#!/usr/bin/env bash
# verify_wiki_sync.sh — post-sync librarian freshness check (K84 workflow adoption).
#
# Compares local OSINT wiki HEAD commit time against librarian index mtime and
# kb-server health. Called at end of sync_wiki_to_librarian.sh and on demand.
#
# Usage:
#   ./scripts/verify_wiki_sync.sh
#
# Exit codes:
#   0 — librarian reachable; wiki tree present; index fresh within threshold
#   1 — ssh/rsync path failure
#   2 — index older than threshold (stale sync)
#   3 — kb-server health check failed

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LIBRARIAN_HOST="${CEMINI_LIBRARIAN_HOST:-cemini-librarian}"
REMOTE_WIKI="/opt/cemini-wiki/wiki"
LOGFILE="${HOME}/Library/Logs/cemini-wiki-sync.log"
STALE_MINUTES="${CEMINI_WIKI_STALE_MINUTES:-180}"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] verify: $*" | tee -a "$LOGFILE"
}

local_head=$(git -C "$ROOT" log -1 --format='%H %ci' -- wiki/ 2>/dev/null || echo "unknown")
remote_stat=$(ssh -o ConnectTimeout=8 -o BatchMode=yes "$LIBRARIAN_HOST" \
  "stat -c '%Y %y' ${REMOTE_WIKI}/index.md 2>/dev/null || stat -f '%m %Sm' ${REMOTE_WIKI}/index.md" 2>/dev/null) || {
  log "ERROR: cannot stat ${REMOTE_WIKI}/index.md on $LIBRARIAN_HOST"
  exit 1
}

remote_epoch=$(echo "$remote_stat" | awk '{print $1}')
now_epoch=$(date +%s)
age_min=$(( (now_epoch - remote_epoch) / 60 ))

kb_status=$(ssh -o ConnectTimeout=8 -o BatchMode=yes "$LIBRARIAN_HOST" \
  "curl -s -m 5 -o /dev/null -w '%{http_code}' http://127.0.0.1:3838/api/v1/health" 2>/dev/null || echo "000")

kb_ok=0
case "$kb_status" in
  2*|401) kb_ok=1 ;;
esac

if [[ $kb_ok -eq 0 ]]; then
  log "ERROR kb-server health=$kb_status local_head=($local_head) remote_index_age=${age_min}m"
  exit 3
fi

if [[ $age_min -gt $STALE_MINUTES ]]; then
  log "WARN stale remote index (${age_min}m > ${STALE_MINUTES}m threshold) local_head=($local_head)"
  exit 2
fi

log "OK remote_index_age=${age_min}m kb=$kb_status local_head=($local_head)"
exit 0
