#!/usr/bin/env bash
# Stage and schedule gov-asset-rerate intel monitors on cemini-prod (24/7).
#
# Lanes: EDGAR full-text (edgar_fulltext.py) + USASpending procurement
# (procurement.py) + Federal Register DoD/DOE (fedreg.py). Runs every 4h via
# systemd timer, alerts to Discord (webhook from /opt/cemini/.env).
#
# Usage:
#   bash scripts/install_gov_asset_monitors_prod.sh
#   ssh cemini-prod 'systemctl status cemini-gov-asset-monitors.timer --no-pager'
#   ssh cemini-prod 'systemctl start cemini-gov-asset-monitors.service'   # run now

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROD_HOST="${PROD_HOST:-cemini-prod}"
REMOTE_ROOT="/opt/cemini/intel/gov-asset-rerate"
LOG_PATH="/opt/cemini/logs/gov-asset-monitors.log"
SERVICE="cemini-gov-asset-monitors.service"
TIMER="cemini-gov-asset-monitors.timer"

ssh "$PROD_HOST" "mkdir -p '$REMOTE_ROOT'/scripts '$REMOTE_ROOT'/config/theses \
  '$REMOTE_ROOT'/.local/reports/gov-asset-edgar \
  '$REMOTE_ROOT'/.local/reports/gov-asset-procurement \
  '$REMOTE_ROOT'/.local/reports/gov-asset-fedreg \
  /opt/cemini/logs"

scp \
  "$ROOT/scripts/__init__.py" \
  "$ROOT/scripts/cemini_discord_notify.py" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp -r \
  "$ROOT/scripts/intel" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp \
  "$ROOT/scripts/run_gov_asset_monitors.sh" \
  "$ROOT/scripts/run_gov_asset_edgar_monitor.sh" \
  "$ROOT/scripts/run_gov_asset_procurement_monitor.sh" \
  "$ROOT/scripts/run_gov_asset_fedreg_monitor.sh" \
  "$PROD_HOST:$REMOTE_ROOT/scripts/"

scp -r \
  "$ROOT/config/theses/gov-asset-rerate" \
  "$PROD_HOST:$REMOTE_ROOT/config/theses/"

ssh "$PROD_HOST" "chmod +x '$REMOTE_ROOT/scripts/'*.sh"

ssh "$PROD_HOST" "cat > /etc/systemd/system/$SERVICE" <<EOF
[Unit]
Description=Gov single-buyer asset-rerating intel monitors (EDGAR + USASpending + Federal Register) + Discord alerts
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=root
WorkingDirectory=$REMOTE_ROOT
Environment=PYTHONUNBUFFERED=1
Environment=PYTHONPATH=$REMOTE_ROOT
Environment=CEMINI_THESIS_ID=gov-asset-rerate
EnvironmentFile=-/opt/cemini/.env
ExecStart=/bin/bash -c "cd $REMOTE_ROOT && bash scripts/run_gov_asset_monitors.sh --notify >> $LOG_PATH 2>&1"
UMask=0077

[Install]
WantedBy=multi-user.target
EOF

ssh "$PROD_HOST" "cat > /etc/systemd/system/$TIMER" <<EOF
[Unit]
Description=Run gov-asset-rerate intel monitors every 4 hours

[Timer]
OnBootSec=15min
OnUnitActiveSec=4h
Persistent=true

[Install]
WantedBy=timers.target
EOF

ssh "$PROD_HOST" "systemctl daemon-reload && systemctl enable --now '$TIMER'"

echo "Installed $SERVICE / $TIMER on $PROD_HOST"
echo "  Root:  $REMOTE_ROOT"
echo "  Log:   $LOG_PATH"
echo "  Now:   ssh $PROD_HOST 'systemctl start $SERVICE'"
echo "  Check: ssh $PROD_HOST 'systemctl status $TIMER --no-pager'"
