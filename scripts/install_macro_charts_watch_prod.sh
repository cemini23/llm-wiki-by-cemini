#!/usr/bin/env bash
# Install Macro Charts watch timer on cemini-prod (24/7, alert-only).
#
# Expects pack at /opt/cemini/macro-charts-watch/ with:
#   macro_charts_watch.py
#   macro-charts-watch.yaml
#   run_macro_charts_watch_check.sh
#   systemd/*.service + *.timer
#
# Env:
#   UNUSUAL_WHALES_API_KEY via /opt/tipdrop-scanner/.env (read by script)
#   DISCORD_WEBHOOK_URL via /opt/cemini/.env (EnvironmentFile)
#
# Usage (on prod):
#   bash /opt/cemini/macro-charts-watch/install_macro_charts_watch_prod.sh
#   bash /opt/cemini/macro-charts-watch/install_macro_charts_watch_prod.sh --uninstall

set -euo pipefail

ROOT="/opt/cemini/macro-charts-watch"
LABEL="cemini-macro-charts-watch"
UNIT_DIR="/etc/systemd/system"

if [[ "${1:-}" == "--uninstall" ]]; then
  systemctl disable --now "${LABEL}.timer" 2>/dev/null || true
  rm -f "${UNIT_DIR}/${LABEL}.service" "${UNIT_DIR}/${LABEL}.timer"
  systemctl daemon-reload
  echo "Removed ${LABEL}"
  exit 0
fi

if [[ ! -f "$ROOT/macro_charts_watch.py" ]]; then
  echo "ERROR: missing $ROOT/macro_charts_watch.py — scp pack first" >&2
  exit 1
fi

mkdir -p /opt/cemini/logs /opt/cemini/state
chmod 755 "$ROOT/run_macro_charts_watch_check.sh"

install -m 644 "$ROOT/systemd/${LABEL}.service" "${UNIT_DIR}/${LABEL}.service"
install -m 644 "$ROOT/systemd/${LABEL}.timer" "${UNIT_DIR}/${LABEL}.timer"
systemctl daemon-reload
systemctl enable --now "${LABEL}.timer"
systemctl start "${LABEL}.service" || true

echo "Installed ${LABEL}.timer"
systemctl list-timers "${LABEL}.timer" --no-pager || true
echo "Manual: bash $ROOT/run_macro_charts_watch_check.sh --dry-run"
echo "Logs:   /opt/cemini/logs/macro-charts-watch.log"
echo "State:  /opt/cemini/state/macro-charts-watches.json"
