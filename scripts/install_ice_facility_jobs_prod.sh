#!/usr/bin/env bash
# Stage and schedule ICE turnkey intel monitors on cemini-prod.
#
# Usage:
#   bash scripts/install_ice_facility_jobs_prod.sh
#   bash scripts/sync_ice_detention_cache_to_prod.sh   # after laptop fetch (ICE blocks prod IP)

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROD_HOST="${PROD_HOST:-cemini-prod}"
REMOTE_ROOT="/opt/cemini/intel/ice-facility-jobs"
LOG_PATH="/opt/cemini/logs/ice-facility-jobs.log"
SERVICE="cemini-ice-facility-jobs.service"
TIMER="cemini-ice-facility-jobs.timer"

ssh "$PROD_HOST" "mkdir -p '$REMOTE_ROOT'/scripts '$REMOTE_ROOT'/config/theses/ice-turnkey \
  '$REMOTE_ROOT'/.local/reports/ice-facility-jobs \
  '$REMOTE_ROOT'/.local/reports/ice-detention-stats \
  '$REMOTE_ROOT'/.local/ice-jobs-daily \
  '$REMOTE_ROOT'/.local/ice-detention-stats \
  /opt/cemini/logs"

scp \
  "$ROOT/scripts/__init__.py" \
  "$ROOT/scripts/cemini_discord_notify.py" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp -r \
  "$ROOT/scripts/intel" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp \
  "$ROOT/scripts/run_ice_turnkey_monitors.sh" \
  "$ROOT/scripts/run_ice_facility_jobs_monitor.sh" \
  "$ROOT/scripts/run_ice_detention_stats_monitor.sh" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp -r \
  "$ROOT/config/theses/ice-turnkey" \
  "$PROD_HOST:$REMOTE_ROOT/config/theses/"

ssh "$PROD_HOST" "chmod +x '$REMOTE_ROOT/scripts/'*.sh"

ssh "$PROD_HOST" "cat > /etc/systemd/system/$SERVICE" <<EOF
[Unit]
Description=ICE turnkey intel monitors (detention stats + facility jobs) + Discord alerts
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=root
WorkingDirectory=$REMOTE_ROOT
Environment=PYTHONUNBUFFERED=1
Environment=PYTHONPATH=$REMOTE_ROOT
EnvironmentFile=-/opt/cemini/.env
ExecStart=/bin/bash -c "cd $REMOTE_ROOT && bash scripts/run_ice_turnkey_monitors.sh --notify >> $LOG_PATH 2>&1"
UMask=0077

[Install]
WantedBy=multi-user.target
EOF

ssh "$PROD_HOST" "cat > /etc/systemd/system/$TIMER" <<EOF
[Unit]
Description=Run ICE turnkey intel monitors every 4 hours

[Timer]
OnBootSec=12min
OnUnitActiveSec=4h
Persistent=true

[Install]
WantedBy=timers.target
EOF

ssh "$PROD_HOST" "systemctl daemon-reload && systemctl enable --now '$TIMER'"

echo "Installed $SERVICE / $TIMER on $PROD_HOST"
echo "  Root:  $REMOTE_ROOT"
echo "  Log:   $LOG_PATH"
echo "  Sync:  bash scripts/sync_ice_detention_cache_to_prod.sh  (ICE.gov blocks prod IP)"
echo "  Check: ssh $PROD_HOST 'systemctl status $TIMER --no-pager'"
