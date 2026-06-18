#!/usr/bin/env bash
# S2 Playground prep — free comp, gin lane, no tournament/rebuy spend.
#
# Validates locally first (caller should run gates). Then:
#   ./scripts/s2_playground_prep_apply.sh
#   ./scripts/s2_playground_prep_apply.sh cmq57o53r0bhw18g23qkydb08
#
# Switches main lobby to Playground S2; clears kill switch; disables eval-panel
# tight gate so gin lane can fire. Parallel S2 service optional (starts if unit exists).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${S2_PLAYGROUND_COMP:-cmq57o53r0bhw18g23qkydb08}}"
EXPORT_SLUG="${S2_EXPORT_SLUG:-s2-playground-live}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s2p.${GIT_SHA}.playground-gin}"

echo "==> S2 playground prep: comp=${COMP} export=${EXPORT_SLUG} version=${AGENT_VERSION}"

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
AGENT_VERSION="${AGENT_VERSION}"

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "S2 playground gin prep" || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

# Main lobby → Playground S2 (S1 tournament dead / no rebuy)
set_kv ARENA_LOBBY_COMPETITION_ID "\${COMP}"
set_kv S2_PLAYGROUND_COMP "\${COMP}"
set_kv S1_TOURNAMENT_COMP "cmq6l1gnq0lkz60y9i9d9eca1"
set_kv CEMINI_HL_PRIMARY_COMP "\${COMP}"
set_kv AGENT_VERSION "\${AGENT_VERSION}"
set_kv CEMINI_LOBBY_LABEL "Playground_S2_prep"
set_kv CEMINI_LOBBY_ROLE "s2_playground_prep"

# Playground posture — width + gin, not tournament survival
set_kv CEMINI_TOURNAMENT_MODE 0
set_kv CEMINI_EVAL_PANEL_GATE 0
set_kv CEMINI_EVAL_PANEL_BB100_FLOOR -25
set_kv CEMINI_KO_SURVIVAL 0
set_kv CEMINI_STAGGER_LOCKS 0
set_kv CEMINI_PACE_PHASE volume
set_kv CEMINI_JOIN_RETRY_S 15
set_kv CEMINI_IN_QUEUE_RETRY_S 30
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 15
set_kv CEMINI_QUAL_BUFFER_CHIPS 0
set_kv CEMINI_LEAD_BUFFER_CHIPS 0
set_kv CEMINI_PRIZE_CUTOFF_RANK 20
set_kv CEMINI_QUAL_CUTOFF_RANK 20

# Gin lane (run gin_style_gate.py locally before apply)
set_kv CEMINI_GIN_STYLE 1
set_kv CEMINI_GIN_STYLE_PREFLOP 1
set_kv CEMINI_GIN_STYLE_POSTFLOP 1
set_kv CEMINI_GIN_STYLE_GATE 1
set_kv CEMINI_GIN_V008 1
set_kv CEMINI_COLD_START_NO_STEAL 0

# Exploits — lighter than full nemesis-tight tournament stack
set_kv CEMINI_S1B_EXPLOIT 1
set_kv CEMINI_S1B_MIN_STACK_BB 50
set_kv CEMINI_NEMESIS_EXPLOIT 1
set_kv CEMINI_NEMESIS_TIGHT 0
set_kv CEMINI_NEMESIS_HANDLES "hunterguy102,thaddius,v_16,0xJeff_ai"
set_kv CEMINI_ISO_PASSIVE_LP 1
set_kv CEMINI_SEAT_MATRIX_V2 1

# Jackpots off — focus on style validation
set_kv JACKPOT_ROYAL_ENABLED 0
set_kv JACKPOT_ROYAL_SHOWDOWN 0
set_kv JACKPOT_27_HUNT_ENABLED 0
set_kv JACKPOT_27_AGGRESSIVE 0

set_kv CEMINI_PLAYGROUND_TIMESERIES 1

grep -E '^(ARENA_LOBBY|CEMINI_GIN|CEMINI_TOURNAMENT|CEMINI_EVAL|AGENT_VERSION)=' .env

mkdir -p "\${EXPORT_DIR}"
if [[ ! -f "\${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "\${EXPORT_DIR}/crawl_state.json"
fi

if [[ -f /etc/systemd/system/cemini-devfun-poker-export-crawl.service ]]; then
  sed -i "s|Environment=CEMINI_EXPORT_DIR=.*|Environment=CEMINI_EXPORT_DIR=\${EXPORT_DIR}|" \
    /etc/systemd/system/cemini-devfun-poker-export-crawl.service 2>/dev/null || true
fi

systemctl daemon-reload
# Main lobby owns this comp — stop parallel S3 unit (same agent, 1-table limit).
if systemctl is-active cemini-devfun-poker-lobby-s3.service 2>/dev/null | grep -q active; then
  echo "==> Stop parallel S3 lobby (main owns comp \${COMP})"
  systemctl stop cemini-devfun-poker-lobby-s3.service || true
fi
systemctl restart cemini-devfun-poker-lobby.service
if systemctl list-unit-files cemini-devfun-poker-lobby-s2.service --no-legend 2>/dev/null | grep -q enabled; then
  sed -i "s|--competition-id .*|--competition-id \${COMP}|" \
    /etc/systemd/system/cemini-devfun-poker-lobby-s2.service 2>/dev/null || true
  systemctl restart cemini-devfun-poker-lobby-s2.service || true
fi
systemctl enable cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl start cemini-devfun-poker-export-crawl.service 2>/dev/null || true

sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
REMOTE

echo ""
echo "✓ S2 playground prep live on ${HOST}"
echo "  Logs: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
echo "  Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
echo "  Target after ≥50h: VPIP 18–25%, PFR 8–15% (Arena export)"
