#!/usr/bin/env bash
# librarian_healthcheck.sh
#
# LSA Phase 6a: laptop-side cron health probe of cemini-librarian.
# Runs every 5 minutes; logs success/failure with timestamp.
# Foundation for the Phase 6c Grafana/Prometheus/Loki integration brief
# (until that brief executes server-side, this gives us LOCAL alerting).
#
# Usage:
#   - Manual:  ./scripts/librarian_healthcheck.sh
#   - Cron:    */5 * * * * /Users/claudiobarone/Desktop/OSINT\ WORKSPACE/scripts/librarian_healthcheck.sh
#
# Exit codes:
#   0 — both kb-server + node_exporter healthy
#   1 — kb-server unreachable / wrong response
#   2 — node_exporter unreachable / wrong response
#   3 — both unreachable

set -uo pipefail

LIBRARIAN_HOST="cemini-librarian"
LOGFILE="$HOME/Library/Logs/cemini-librarian-health.log"

mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOGFILE"
}

# kb-server probe — any 2xx OR 401 means "server is up + responding"
# (401 = auth required on /api/v1/* routes; valid health signal)
kb_status=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$LIBRARIAN_HOST" \
  "curl -s -m 3 -o /dev/null -w '%{http_code}' http://10.0.0.2:3838/api/v1/health" 2>/dev/null)
kb_ok=0
case "$kb_status" in
  2*|401) kb_ok=1 ;;
esac

# node_exporter probe — should always return 200 with text/plain Prometheus output
ne_status=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$LIBRARIAN_HOST" \
  "curl -s -m 3 -o /dev/null -w '%{http_code}' http://10.0.0.2:9100/metrics" 2>/dev/null)
ne_ok=0
[[ "$ne_status" == "200" ]] && ne_ok=1

# Also pull a few key system metrics to log (CPU load, mem available, disk free root)
metrics=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$LIBRARIAN_HOST" \
  "curl -s -m 3 http://10.0.0.2:9100/metrics" 2>/dev/null | \
  awk '
    /^node_load1 / {load1=$2}
    /^node_memory_MemAvailable_bytes / {mem_avail_gb=$2/1024/1024/1024}
    /^node_filesystem_avail_bytes.*mountpoint="\/"/ {disk_avail_gb=$2/1024/1024/1024}
    END {printf "load1=%.2f mem_avail=%.1fGB disk_avail=%.1fGB", load1, mem_avail_gb, disk_avail_gb}
  ' 2>/dev/null)

# Log result
if [[ $kb_ok -eq 1 && $ne_ok -eq 1 ]]; then
  log "OK kb-server($kb_status) node_exporter($ne_status) $metrics"
  exit 0
elif [[ $kb_ok -eq 0 && $ne_ok -eq 0 ]]; then
  log "ERROR both unreachable: kb=$kb_status ne=$ne_status"
  exit 3
elif [[ $kb_ok -eq 0 ]]; then
  log "ERROR kb-server unreachable: kb=$kb_status (ne=$ne_status OK)"
  exit 1
else
  log "ERROR node_exporter unreachable: ne=$ne_status (kb=$kb_status OK)"
  exit 2
fi
