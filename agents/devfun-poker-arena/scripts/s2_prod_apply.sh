#!/usr/bin/env bash
# Apply S2 prod posture: s1b exploit, main-bot jackpot, drain old comp, no probe.
#
# Usage:
#   ./scripts/s2_prod_apply.sh
#   OLD_COMPS="cmpy2qy65002ud9ej6b7jjq0l" ./scripts/s2_prod_apply.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${S2_COMPETITION_ID:-cmq57o53r0bhw18g23qkydb08}"
EXPORT_SLUG="${S2_EXPORT_SLUG:-playground-s2-live}"
OLD_COMPS="${OLD_COMPS:-cmpy2qy65002ud9ej6b7jjq0l}"

echo "==> S2 prod apply: comp=${COMP} export=${EXPORT_SLUG}"

rsync -avz \
  --exclude '.venv/' --exclude 'venv/' --exclude '.git/' \
  --exclude '__pycache__/' --exclude '.env' --exclude '.env.*' \
  --exclude '.arena-credentials' --exclude '.arena-poker-state' \
  --exclude '.arena-credentials.jackpot*' --exclude 'reports/' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
COMP="${COMP}"
EXPORT_SLUG="${EXPORT_SLUG}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/\${EXPORT_SLUG}"
OLD_COMPS="${OLD_COMPS}"

echo "==> Probe lane OFF (never run parallel jackpot bot)"
systemctl stop jackpot-27-lobby.service 2>/dev/null || true
systemctl disable jackpot-27-lobby.service 2>/dev/null || true
systemctl reset-failed jackpot-27-lobby.service 2>/dev/null || true
if [[ -f .arena-credentials.jackpot-probe ]]; then
  mv -f .arena-credentials.jackpot-probe .arena-credentials.jackpot-probe.disabled
  echo "    moved jackpot-probe creds aside"
fi

echo "==> Drain old competition tables"
for old in \${OLD_COMPS}; do
  ./venv/bin/python scripts/playground_drain_competition.py "\${old}" || true
done

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "S2 prod apply" || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "\${COMP}"
set_kv CEMINI_S1B_EXPLOIT 1
set_kv CEMINI_S1B_MIN_STACK_BB 60
set_kv CEMINI_NEMESIS_EXPLOIT 1
set_kv CEMINI_NEMESIS_HANDLES "hunterguy102,thaddius,v_16,0xJeff_ai,range_ledger,arjun_c,rvkkv1,long_ngu_poker,damon"
set_kv CEMINI_NEMESIS_TIGHT 1
set_kv JACKPOT_ROYAL_ENABLED 1
set_kv JACKPOT_ROYAL_SHOWDOWN 1
set_kv JACKPOT_27_HUNT_ENABLED 0
set_kv JACKPOT_27_PHASE climb
set_kv JACKPOT_27_AGGRESSIVE 1
set_kv JACKPOT_27_MAX_ATTEMPTS 10
set_kv JACKPOT_27_POSITIONS "CO,BTN,SB,BB"
set_kv JACKPOT_27_MAX_VILLAINS 3
set_kv JACKPOT_27_COMPETITION_ID "\${COMP}"
set_kv JACKPOT_27_COMPETITION_ONLY 1
set_kv JACKPOT_27_INSTANCE cemini_wiki_poker
set_kv CEMINI_PLAYGROUND_TIMESERIES 1
set_kv CEMINI_PACE_PHASE volume
set_kv CEMINI_JOIN_RETRY_S 20
set_kv CEMINI_IN_QUEUE_RETRY_S 45
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 30

grep -E '^(ARENA_LOBBY|CEMINI_S1B|CEMINI_NEMESIS|JACKPOT|CEMINI_PLAYGROUND|CEMINI_PACE|CEMINI_JOIN|CEMINI_IN_QUEUE)=' .env

mkdir -p "\${EXPORT_DIR}"
if [[ ! -f "\${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "\${EXPORT_DIR}/crawl_state.json"
fi

sed -i "s|Environment=CEMINI_EXPORT_DIR=.*|Environment=CEMINI_EXPORT_DIR=\${EXPORT_DIR}|" \
  /etc/systemd/system/cemini-devfun-poker-export-crawl.service 2>/dev/null || true
if ! grep -q CEMINI_EXPORT_DIR /etc/systemd/system/cemini-devfun-poker-export-crawl.service 2>/dev/null; then
  install -m 644 deploy/cemini-devfun-poker-export-crawl.service /etc/systemd/system/
  sed -i "s|playground-s1-live|\${EXPORT_SLUG}|g" /etc/systemd/system/cemini-devfun-poker-export-crawl.service
fi

systemctl daemon-reload
systemctl enable cemini-devfun-poker-export-crawl.timer
systemctl restart cemini-devfun-poker-lobby.service
systemctl start cemini-devfun-poker-export-crawl.service || true

sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
systemctl is-enabled jackpot-27-lobby.service 2>&1 || echo "jackpot probe: not enabled"
REMOTE

echo ""
echo "✓ S2 prod apply complete."
echo "  Lobby: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
echo "  Timeseries: ssh ${HOST} tail -f ${REMOTE_DIR}/reports/hl-loop/playground_timeseries.jsonl"
echo "  Export: ssh ${HOST} ls ${REMOTE_DIR}/reports/exports/${EXPORT_SLUG}/"
