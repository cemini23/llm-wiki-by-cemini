#!/usr/bin/env bash
# KO tournament freeze apply — free ticket only (no MON entry / no rebuy).
# Do NOT copy s10 climb (gin / polar / TABLE_FORMAT=auto). T12 busted that pack.
#
# Usage:
#   CONFIRM=1 ./scripts/tournament_freeze_prod_apply.sh <tournament-comp-id>
#   SEASON=13 OLD_PLAYGROUND_COMP=cms... CONFIRM=1 ./scripts/tournament_freeze_prod_apply.sh cms...
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${TOURNAMENT_COMP:-}}"
SEASON="${SEASON:-13}"
OLD_PLAYGROUND="${OLD_PLAYGROUND_COMP:-cmsrglcro33ttvijti3slinjh}"
EXPORT_SLUG="${TOURNAMENT_EXPORT_SLUG:-s${SEASON}-tournament-live}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s${SEASON}t.${GIT_SHA}.freeze}"

if [[ -z "${COMP}" ]]; then
  echo "ERROR: pass Tournament competition id." >&2
  echo "  CONFIRM=1 SEASON=13 ./scripts/tournament_freeze_prod_apply.sh <comp-id>" >&2
  exit 1
fi
if [[ "${CONFIRM:-}" != "1" ]]; then
  echo "ERROR: refusing lobby swap without CONFIRM=1" >&2
  echo "  CONFIRM=1 SEASON=${SEASON} ./scripts/tournament_freeze_prod_apply.sh ${COMP}" >&2
  exit 1
fi

echo "==> Tournament S${SEASON} freeze apply: comp=${COMP} agent_version=${AGENT_VERSION}"
echo "    draining playground ${OLD_PLAYGROUND}"

bash "${AGENT_DIR}/scripts/rsync_poker_arena_code.sh"

ssh -q "${HOST}" bash -s -- "${COMP}" "${OLD_PLAYGROUND}" "${EXPORT_SLUG}" "${AGENT_VERSION}" "${REMOTE_DIR}" "${SEASON}" <<'REMOTE'
set -euo pipefail
COMP="$1"
OLD="$2"
EXPORT_SLUG="$3"
AGENT_VERSION="$4"
REMOTE_DIR="$5"
SEASON="$6"
cd "${REMOTE_DIR}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/${EXPORT_SLUG}"

echo "==> Drain playground tables (best-effort)"
./venv/bin/python scripts/playground_drain_competition.py "${OLD}" 2>/dev/null || true

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "Tournament S${SEASON} freeze enter" 2>/dev/null || true

set_kv() {
  local key="$1" val="$2"
  if grep -q "^${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^${key}=.*|${key}=${val}|" .env
  else
    echo "${key}=${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "${COMP}"
set_kv "S${SEASON}_TOURNAMENT_COMP" "${COMP}"
set_kv "S${SEASON}_PLAYGROUND_COMP" "${OLD}"
set_kv CEMINI_HL_PRIMARY_COMP "${COMP}"
set_kv CEMINI_TOURNAMENT_SEASON "${SEASON}"
set_kv AGENT_VERSION "${AGENT_VERSION}"
set_kv CEMINI_LOBBY_LABEL "Tournament_S${SEASON}"
set_kv CEMINI_LOBBY_ROLE "s${SEASON}_tournament"
set_kv CEMINI_PRIMARY "lobby"
set_kv CEMINI_PRIMARY_TRACK "tournament"

set_kv CEMINI_RESEARCHER_MODE 0
set_kv CEMINI_SANDBOX_PVP_SUBMIT_ONLY 0
set_kv CEMINI_TABLE_FORMAT "6max"
set_kv CEMINI_TAG_WIDEN 0
set_kv CEMINI_TAG_BLIND_DEFEND 0
set_kv CEMINI_MAFP_CHART 0
set_kv CEMINI_SOLVER_V3 0
set_kv CEMINI_SOLVER_HARD 0
set_kv CEMINI_TRAJECTORY_BOUND 0
set_kv CEMINI_VERIFIER_BON 0
set_kv CEMINI_EVAL_CRUSH 0
set_kv CEMINI_ARENA_PROFILE ""
set_kv CEMINI_PLACEMENT_CHASE 0
set_kv CEMINI_TOURNAMENT_3BET 0
set_kv CEMINI_TOURNAMENT_3BET_POLAR 0
set_kv CEMINI_FLAT_DOMINATE 0
set_kv CEMINI_STOP_WIN_MULT 0

set_kv CEMINI_TOURNAMENT_MODE 1
set_kv CEMINI_EVAL_PANEL_GATE 0
set_kv CEMINI_EVAL_PANEL_MODE 0
set_kv CEMINI_PRIZE_CUTOFF_RANK 3
set_kv CEMINI_QUAL_CUTOFF_RANK 25
set_kv CEMINI_STAGGER_LOCKS 0
set_kv CEMINI_QUAL_BUFFER_CHIPS 999999
set_kv CEMINI_LEAD_BUFFER_CHIPS 999999
set_kv CEMINI_PLACEMENT_PROTECT_BUFFER_PCT 0.35
set_kv CEMINI_PACE_PHASE ""
set_kv CEMINI_KO_SURVIVAL 1
set_kv CEMINI_KO_SURVIVAL_HANDS 60
set_kv CEMINI_KO_SURVIVAL_MIN_STACK 250
set_kv CEMINI_SURVIVAL_STACK_CHIPS 400
set_kv CEMINI_S1B_MIN_STACK_BB 60
set_kv CEMINI_SHORT_STACK_BB 20
set_kv CEMINI_SHORT_STACK_JAM_BB 8
set_kv CEMINI_NEMESIS_TIGHT 1
set_kv CEMINI_NAMED_NEMESIS_TIGHT 1
set_kv CEMINI_COLD_START_NO_STEAL 1
set_kv JACKPOT_27_HUNT_ENABLED 0
set_kv JACKPOT_ROYAL_ENABLED 0
set_kv JACKPOT_ROYAL_SHOWDOWN 0

set_kv CEMINI_GIN_KILL 1
set_kv CEMINI_GIN_STYLE 0
set_kv CEMINI_GIN_STYLE_PREFLOP 0
set_kv CEMINI_GIN_STYLE_POSTFLOP 0
set_kv CEMINI_GIN_STYLE_GATE 0
set_kv CEMINI_GIN_V008 0
set_kv CEMINI_GIN_V2_EXPLOITS 0
set_kv CEMINI_MAX_REBUYS 0
set_kv CEMINI_REBUY_MAX_MON 0
set_kv CEMINI_REFUSE_ENTRY_FEE 1
set_kv CEMINI_SANITIZE_OUTPUT 1
set_kv CEMINI_JOIN_RETRY_S 25
set_kv CEMINI_IN_QUEUE_RETRY_S 60
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 30
set_kv CEMINI_EXPORT_DIR "reports/exports/${EXPORT_SLUG}"
set_kv CEMINI_FIELD_EXPORT_DIR "reports/exports/${EXPORT_SLUG}"
set_kv CEMINI_PREFLOP_LOG 1
set_kv CEMINI_PREFLOP_LOG_PATH "reports/exports/${EXPORT_SLUG}/preflop_decisions.jsonl"
set_kv CEMINI_PLAYGROUND_TIMESERIES 0
set_kv ARENA_NO_AUTO_REGISTER 1

grep -E "^(ARENA_LOBBY|S${SEASON}_TOURNAMENT|CEMINI_HL_PRIMARY|AGENT_VERSION|CEMINI_TOURNAMENT_MODE|CEMINI_LOBBY_ROLE|CEMINI_GIN_KILL|CEMINI_MAX_REBUYS|CEMINI_REFUSE_ENTRY_FEE|CEMINI_TAG_WIDEN|CEMINI_TABLE_FORMAT)=" .env

mkdir -p "${EXPORT_DIR}"
if [[ ! -f "${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "${EXPORT_DIR}/crawl_state.json"
fi

systemctl daemon-reload
systemctl restart cemini-devfun-poker-lobby.service
sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
timeout 15 journalctl -u cemini-devfun-poker-lobby.service -n 25 --no-pager || true
REMOTE

echo "==> Freeze apply complete. Confirm free join (no 402 pay) in journal."
echo "    If entry fee refused: stay parked — do not pay MON."
