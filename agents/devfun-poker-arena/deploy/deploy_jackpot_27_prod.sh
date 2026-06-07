#!/usr/bin/env bash
# Deploy jackpot-27 satellite to cemini-prod — does NOT restart prod qualification lobby.
set -euo pipefail

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
SERVICE="jackpot-27-lobby.service"
CREDS_LOCAL="${JACKPOT_27_CREDS_FILE:-.arena-credentials.jackpot-probe}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "==> Jackpot-27 deploy → ${HOST} (service: ${SERVICE})"
echo "    Prod lobby (cemini-devfun-poker-lobby.service) is NOT restarted."

if [[ ! -f "${AGENT_DIR}/${CREDS_LOCAL}" ]]; then
  echo "ERROR: missing ${CREDS_LOCAL} — run ./scripts/jackpot_27_register.sh first" >&2
  exit 1
fi

rsync -avz \
  --exclude '.venv/' --exclude 'venv/' --exclude '.git/' \
  --exclude '__pycache__/' --exclude '.arena-credentials' \
  --exclude '.arena-poker-state' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

scp -q "${AGENT_DIR}/${CREDS_LOCAL}" "${HOST}:${REMOTE_DIR}/${CREDS_LOCAL}"

ssh "${HOST}" bash -s <<'REMOTE'
set -euo pipefail
REMOTE_DIR="/opt/devfun-poker-arena"
chmod 600 "${REMOTE_DIR}/.arena-credentials.jackpot-probe"
mkdir -p "${REMOTE_DIR}/reports/jackpot-27"
install -m 644 "${REMOTE_DIR}/deploy/jackpot-27-lobby.service" \
  /etc/systemd/system/jackpot-27-lobby.service
systemctl daemon-reload
systemctl enable jackpot-27-lobby.service
systemctl restart jackpot-27-lobby.service
sleep 2
systemctl --no-pager status jackpot-27-lobby.service || true
REMOTE

echo ""
echo "✓ Jackpot satellite live (hunt OFF until JACKPOT_27_HUNT_ENABLED=1 on S2). Logs:"
echo "  ssh ${HOST} journalctl -u ${SERVICE} -f"
echo "  ssh ${HOST} tail -f ${REMOTE_DIR}/reports/jackpot-27/dealt.jsonl"
