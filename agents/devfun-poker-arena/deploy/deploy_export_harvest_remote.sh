#!/usr/bin/env bash
# Deploy read-only tournament export worker (one shard) to librarian or egress-fi.
# Uses prod Arena API key (read-only harvest). Does NOT touch prod lobby.
#
# Usage:
#   ./deploy/deploy_export_harvest_remote.sh --host cemini-librarian --shard-index 1
set -euo pipefail

HOST=""
SHARD_INDEX=""
LABEL=""
REMOTE_DIR="${HARVEST_REMOTE_DIR:-/opt/devfun-poker-arena-harvest}"
PROD_HOST="${CEMINI_PROD_HOST:-cemini-prod}"
PROD_DIR="${CEMINI_PROD_HARVEST_DIR:-/opt/devfun-poker-arena}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host) HOST="$2"; shift 2 ;;
    --shard-index) SHARD_INDEX="$2"; shift 2 ;;
    --label) LABEL="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "${HOST}" || -z "${SHARD_INDEX}" ]]; then
  echo "Usage: $0 --host HOST --shard-index N [--label name]" >&2
  exit 1
fi
LABEL="${LABEL:-${HOST}}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "==> Harvest worker shard ${SHARD_INDEX}/3 → ${HOST}:${REMOTE_DIR}"

rsync -avz \
  --exclude '.venv/' --exclude 'venv/' --exclude 'venv-pokerskill/' \
  --exclude '.git/' --exclude '__pycache__/' --exclude '.pytest_cache/' \
  --exclude '.arena-credentials' --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' --exclude '.env' --exclude 'reports/' \
  --exclude 'private/' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

# Pull Arena env fragment from prod (API key + competition id)
ENV_BLOCK="$(ssh "${PROD_HOST}" "grep -E '^(ARENA_API_KEY|ARENA_API_BASE|S1_TOURNAMENT_COMP|ARENA_LOBBY_COMPETITION_ID)=' ${PROD_DIR}/.env 2>/dev/null || true")"

ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
REMOTE_DIR="${REMOTE_DIR}"
SHARD_INDEX="${SHARD_INDEX}"
LABEL="${LABEL}"
PY="\$(command -v python3.12 || command -v python3.11 || command -v python3)"

mkdir -p "\${REMOTE_DIR}/reports/exports/s1-tournament-live"

if [[ ! -x "\${REMOTE_DIR}/venv/bin/python" ]]; then
  "\${PY}" -m venv "\${REMOTE_DIR}/venv"
fi
"\${REMOTE_DIR}/venv/bin/pip" install -q --upgrade pip
"\${REMOTE_DIR}/venv/bin/pip" install -q httpx python-dotenv treys pokerkit

cat > "\${REMOTE_DIR}/.env.harvest" <<'ENVEOF'
${ENV_BLOCK}
CEMINI_EXPORT_SHARD_INDEX=${SHARD_INDEX}
CEMINI_EXPORT_SHARD_COUNT=3
CEMINI_EXPORT_DIR=reports/exports/s1-tournament-live
CEMINI_EXPORT_TOP_AGENTS=200
CEMINI_EXPORT_STATS_TOP=200
CEMINI_EXPORT_REPLAYS_TOP=50
CEMINI_EXPORT_CRAWL_BATCH=120
ENVEOF

chmod 600 "\${REMOTE_DIR}/.env.harvest"

cat > /etc/systemd/system/cemini-export-harvest-worker.service <<UNIT
[Unit]
Description=Cemini Arena harvest worker (shard ${SHARD_INDEX}/3) ${LABEL}
After=network-online.target

[Service]
Type=oneshot
User=root
Group=root
WorkingDirectory=${REMOTE_DIR}
Environment=PYTHONUNBUFFERED=1
EnvironmentFile=${REMOTE_DIR}/.env.harvest
ExecStart=/bin/bash ${REMOTE_DIR}/scripts/run_export_harvest_worker.sh
UMask=0077

[Install]
WantedBy=multi-user.target
UNIT

cat > /etc/systemd/system/cemini-export-harvest-worker.timer <<TIMER
[Unit]
Description=Arena harvest worker shard ${SHARD_INDEX} (staggered)

[Timer]
OnBootSec=25min
OnCalendar=*-*-* *:$((${SHARD_INDEX} * 20)):00
Persistent=true

[Install]
WantedBy=timers.target
TIMER

systemctl daemon-reload
systemctl enable cemini-export-harvest-worker.timer
systemctl start cemini-export-harvest-worker.timer
echo "Timer: cemini-export-harvest-worker.timer (shard ${SHARD_INDEX})"
REMOTE

echo "✓ ${HOST} shard ${SHARD_INDEX} ready"
