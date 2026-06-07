#!/usr/bin/env bash
# Deploy one jackpot-27 probe instance to librarian, egress-fi, or any SSH host.
# Does NOT touch prod qualification lobby (cemini-prod).
#
# Usage:
#   ./scripts/jackpot_probe_fleet_register.sh   # once, local
#   ./deploy/deploy_jackpot_probe_remote.sh \
#     --host cemini-librarian --instance lib-a \
#     --creds .arena-credentials.jackpot-lib-a
#
# Env overrides:
#   JACKPOT_27_COMPETITION_ID  (default empty — set only for S2 / non-qual comp)
#   JACKPOT_27_JOIN_ENABLED    (default 0 — anti-cheat: no lobby join until enabled)
#   JACKPOT_27_HUNT_ENABLED    (default 0 — passive data until S2)
set -euo pipefail

HOST=""
INSTANCE=""
CREDS_LOCAL=""
REMOTE_DIR="${JACKPOT_REMOTE_DIR:-/opt/devfun-poker-arena-jackpot}"
COMPETITION_ID="${JACKPOT_27_COMPETITION_ID:-}"
HUNT_ENABLED="${JACKPOT_27_HUNT_ENABLED:-0}"
JOIN_ENABLED="${JACKPOT_27_JOIN_ENABLED:-0}"
MAX_ATTEMPTS="${JACKPOT_27_MAX_ATTEMPTS:-5}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host) HOST="$2"; shift 2 ;;
    --instance) INSTANCE="$2"; shift 2 ;;
    --creds) CREDS_LOCAL="$2"; shift 2 ;;
    --competition-id) COMPETITION_ID="$2"; shift 2 ;;
    --hunt) HUNT_ENABLED=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "${HOST}" || -z "${INSTANCE}" || -z "${CREDS_LOCAL}" ]]; then
  echo "Usage: $0 --host HOST --instance NAME --creds LOCAL_CREDS_FILE [--competition-id ID] [--hunt]" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
CREDS_PATH="${AGENT_DIR}/${CREDS_LOCAL}"

if [[ ! -f "${CREDS_PATH}" ]]; then
  echo "ERROR: missing ${CREDS_PATH} — register first (jackpot_probe_fleet_register.sh)" >&2
  exit 1
fi

HANDLE="$(python3 -c "import json; d=json.load(open('${CREDS_PATH}')); print(d.get('handle') or '')")"
AGENT_ID="$(python3 -c "import json; print(json.load(open('${CREDS_PATH}'))['agentId'])")"

echo "==> Jackpot probe ${INSTANCE} → ${HOST}:${REMOTE_DIR}"
echo "    agentId=${AGENT_ID} handle=${HANDLE:-?} hunt=${HUNT_ENABLED}"

rsync -avz \
  --exclude '.venv/' --exclude 'venv/' --exclude 'venv-pokerskill/' \
  --exclude '.git/' --exclude '__pycache__/' --exclude '.pytest_cache/' \
  --exclude '.arena-credentials' --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' --exclude '.env' --exclude 'reports/' \
  --exclude 'private/' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

REMOTE_CREDS="${REMOTE_DIR}/creds/${INSTANCE}.json"
INSTANCE_ENV="${REMOTE_DIR}/instances/${INSTANCE}.env"

ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
REMOTE_DIR="${REMOTE_DIR}"
INSTANCE="${INSTANCE}"
PY="\$(command -v python3.12 || command -v python3.11 || command -v python3)"
mkdir -p "\${REMOTE_DIR}/creds" "\${REMOTE_DIR}/instances" "\${REMOTE_DIR}/reports/jackpot-27/\${INSTANCE}"

if [[ ! -x "\${REMOTE_DIR}/venv/bin/python" ]]; then
  echo "Creating venv with \${PY}..."
  "\${PY}" -m venv "\${REMOTE_DIR}/venv"
fi
"\${REMOTE_DIR}/venv/bin/pip" install -q --upgrade pip
"\${REMOTE_DIR}/venv/bin/pip" install -q httpx python-dotenv treys pokerkit

install -m 644 "\${REMOTE_DIR}/deploy/jackpot-27-probe@.service" \
  /etc/systemd/system/jackpot-27-probe@.service
systemctl daemon-reload
REMOTE

scp -q "${CREDS_PATH}" "${HOST}:${REMOTE_CREDS}"
ssh "${HOST}" "chmod 600 '${REMOTE_CREDS}'"

ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
cat > "${INSTANCE_ENV}" <<ENV
ARENA_API_BASE=https://arena.dev.fun/api/arena
ARENA_CREDENTIALS_FILE=${REMOTE_CREDS}
JACKPOT_27_COMPETITION_ID=${COMPETITION_ID}
JACKPOT_27_INSTANCE=${INSTANCE}
JACKPOT_27_JOIN_ENABLED=${JOIN_ENABLED}
JACKPOT_27_HUNT_ENABLED=${HUNT_ENABLED}
JACKPOT_27_MAX_ATTEMPTS=${MAX_ATTEMPTS}
JACKPOT_27_HANDLE=${HANDLE:-arena_probe_${INSTANCE}}
JACKPOT_27_NAME=Table Probe ${INSTANCE}
JACKPOT_27_QUOTE=fold and observe
ENV
chmod 600 "${INSTANCE_ENV}"
systemctl enable "jackpot-27-probe@${INSTANCE}.service"
systemctl restart "jackpot-27-probe@${INSTANCE}.service"
sleep 2
systemctl --no-pager status "jackpot-27-probe@${INSTANCE}.service" || true
REMOTE

echo ""
echo "✓ Probe ${INSTANCE} on ${HOST}"
echo "  journalctl -u jackpot-27-probe@${INSTANCE}.service -f"
echo "  tail -f ${REMOTE_DIR}/reports/jackpot-27/${INSTANCE}/dealt.jsonl"
