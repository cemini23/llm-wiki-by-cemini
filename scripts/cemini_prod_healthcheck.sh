#!/usr/bin/env bash
# cemin_prod_healthcheck.sh
#
# Laptop-side cron health probe of cemini-prod (Hetzner production trading stack).
# Runs at 5 AM daily; logs success/failure with timestamp.
#
# Usage:
#   - Manual:  ./scripts/cemini_prod_healthcheck.sh
#   - Cron:    0 5 * * * /Users/claudiobarone/Desktop/OSINT\ WORKSPACE/scripts/cemini_prod_healthcheck.sh
#
# Exit codes:
#   0 — claude-code-router + docker both healthy
#   1 — claude-code-router not active
#   2 — docker not active
#   3 — both not active
#   4 — SSH unreachable

set -uo pipefail

PROD_HOST="cemini-prod"
LOGFILE="$HOME/Library/Logs/cemini-prod-health.log"

mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOGFILE"
}

# --- SSH connectivity check ---
if ! ssh -o ConnectTimeout=5 -o BatchMode=yes "$PROD_HOST" "echo ok" &>/dev/null; then
  log "ERROR SSH unreachable"
  exit 4
fi

# --- service checks ---
ccr_status=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$PROD_HOST" \
  "systemctl is-active claude-code-router.service" 2>/dev/null)
ccr_ok=0
[[ "$ccr_status" == "active" ]] && ccr_ok=1

docker_status=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$PROD_HOST" \
  "systemctl is-active docker.service" 2>/dev/null)
docker_ok=0
[[ "$docker_status" == "active" ]] && docker_ok=1

# --- system metrics ---
metrics=$(ssh -o ConnectTimeout=5 -o BatchMode=yes "$PROD_HOST" \
  "uptime | awk -F'load average:' '{gsub(/^ +| +\$/,\"\",\$2); print \"load=\"\$2}' 2>/dev/null;
   free -m | awk '/^Mem:/ {printf \" mem_avail=%dMB\", \$7}';
   df -h / | awk 'NR==2 {printf \" disk_avail=%s\", \$4}'" 2>/dev/null | tr -d '\n')

# --- log result ---
if [[ $ccr_ok -eq 1 && $docker_ok -eq 1 ]]; then
  log "OK ccr=active docker=active$metrics"
  exit 0
elif [[ $ccr_ok -eq 0 && $docker_ok -eq 0 ]]; then
  log "ERROR both down: ccr=$ccr_status docker=$docker_status$metrics"
  exit 3
elif [[ $ccr_ok -eq 0 ]]; then
  log "ERROR claude-code-router down: ccr=$ccr_status (docker=$docker_status OK)$metrics"
  exit 1
else
  log "ERROR docker down: docker=$docker_status (ccr=$ccr_status OK)$metrics"
  exit 2
fi
