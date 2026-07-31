#!/usr/bin/env bash
# Tournament S10 posture — free entry from Playground S10 top-20 qual.
# DO NOT run until Tournament S10 is Active (or use wait_tournament_s10_and_apply.sh).
#
# Usage:
#   CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh <tournament-s10-comp-id>
#   TOURNAMENT_COMP=cms... CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh
#
# Safety: refuses without CONFIRM=1 and an explicit competition id.
# Discover: ./scripts/list_arena_competitions.sh | grep -i 'Tournament S10'
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${TOURNAMENT_COMP:-}}"
OLD_PLAYGROUND="${OLD_PLAYGROUND_COMP:-cms0bwufmf3n8kyykdpxi6d2i}"
EXPORT_SLUG="${S10_TOURNAMENT_EXPORT_SLUG:-s10-tournament-live}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s10t.${GIT_SHA}.tournament-s10}"

if [[ -z "${COMP}" ]]; then
  echo "ERROR: pass Tournament S10 competition id (not live yet as of prep)." >&2
  echo "  ./scripts/list_arena_competitions.sh" >&2
  echo "  CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh <comp-id>" >&2
  exit 1
fi
if [[ "${CONFIRM:-}" != "1" ]]; then
  echo "ERROR: refusing lobby swap without CONFIRM=1" >&2
  echo "  (Playground S10 must keep running until T10 starts.)" >&2
  echo "  CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh ${COMP}" >&2
  exit 1
fi

echo "==> Tournament S10 prod apply: comp=${COMP} agent_version=${AGENT_VERSION}"
echo "    draining playground ${OLD_PLAYGROUND}"

bash "${AGENT_DIR}/scripts/rsync_poker_arena_code.sh"

ssh -q "${HOST}" bash -s -- "${COMP}" "${OLD_PLAYGROUND}" "${EXPORT_SLUG}" "${AGENT_VERSION}" "${REMOTE_DIR}" <<'REMOTE'
set -euo pipefail
COMP="$1"
OLD="$2"
EXPORT_SLUG="$3"
AGENT_VERSION="$4"
REMOTE_DIR="$5"
cd "${REMOTE_DIR}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/${EXPORT_SLUG}"

echo "==> Drain playground tables (best-effort)"
./venv/bin/python scripts/playground_drain_competition.py "${OLD}" 2>/dev/null || true

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "Tournament S10 enter" 2>/dev/null || true

set_kv() {
  local key="$1" val="$2"
  if grep -q "^${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^${key}=.*|${key}=${val}|" .env
  else
    echo "${key}=${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "${COMP}"
set_kv S10_TOURNAMENT_COMP "${COMP}"
set_kv S10_PLAYGROUND_COMP "${OLD}"
set_kv CEMINI_HL_PRIMARY_COMP "${COMP}"
set_kv CEMINI_TOURNAMENT_SEASON 10
set_kv AGENT_VERSION "${AGENT_VERSION}"
set_kv CEMINI_LOBBY_LABEL "Tournament_S10"
set_kv CEMINI_LOBBY_ROLE "s10_tournament"
set_kv CEMINI_PRIMARY "lobby"
set_kv CEMINI_PRIMARY_TRACK "tournament"

# Exit Researcher / Playground chip-qual posture
set_kv CEMINI_RESEARCHER_MODE 0
set_kv CEMINI_SANDBOX_PVP_SUBMIT_ONLY 0
set_kv CEMINI_TABLE_FORMAT "auto"
set_kv CEMINI_MAFP_CHART 0
set_kv CEMINI_SOLVER_V3 0
set_kv CEMINI_SOLVER_HARD 0
set_kv CEMINI_TRAJECTORY_BOUND 0
set_kv CEMINI_VERIFIER_BON 0
set_kv CEMINI_EVAL_CRUSH 0
set_kv CEMINI_ARENA_PROFILE ""
set_kv CEMINI_PLACEMENT_CHASE 1

set_kv CEMINI_TOURNAMENT_MODE 1
set_kv CEMINI_EVAL_PANEL_GATE 0
set_kv CEMINI_EVAL_PANEL_MODE 0
set_kv CEMINI_EVAL_PANEL_BB100_FLOOR -25
# Money-zone protect at top-3; climb widen when behind (2026-07-31)
set_kv CEMINI_PRIZE_CUTOFF_RANK 3
set_kv CEMINI_QUAL_CUTOFF_RANK 25
set_kv CEMINI_STAGGER_LOCKS 0
# 999999 disables chip-qual protect (wrong metric in KO)
set_kv CEMINI_QUAL_BUFFER_CHIPS 999999
set_kv CEMINI_LEAD_BUFFER_CHIPS 999999
set_kv CEMINI_PACE_PHASE ""
set_kv CEMINI_KO_SURVIVAL 0
set_kv CEMINI_KO_SURVIVAL_HANDS 0
set_kv CEMINI_KO_SURVIVAL_MIN_STACK 600
set_kv CEMINI_SURVIVAL_STACK_CHIPS 200
set_kv CEMINI_S1B_MIN_STACK_BB 25
set_kv JACKPOT_27_HUNT_ENABLED 0
set_kv JACKPOT_27_AGGRESSIVE 0
set_kv JACKPOT_ROYAL_ENABLED 0
set_kv JACKPOT_ROYAL_SHOWDOWN 0

# Climb: gin ON — field VPIP~0.26 winners; 79% fold was bleeding blinds
set_kv CEMINI_GIN_STYLE 1
set_kv CEMINI_GIN_STYLE_PREFLOP 1
set_kv CEMINI_GIN_STYLE_POSTFLOP 1
set_kv CEMINI_GIN_STYLE_GATE 1
set_kv CEMINI_GIN_V008 1
set_kv CEMINI_GIN_V2_EXPLOITS 1
set_kv CEMINI_COLD_START_NO_STEAL 0
set_kv CEMINI_NUTS_DETECT 1
set_kv CEMINI_SANITIZE_OUTPUT 1

set_kv CEMINI_S1B_EXPLOIT 1
set_kv CEMINI_NEMESIS_EXPLOIT 1
set_kv CEMINI_NEMESIS_TIGHT 0
set_kv CEMINI_NEMESIS_ARCHETYPE 1
set_kv CEMINI_NEMESIS_PREMIUM_NIT 1
set_kv CEMINI_NEMESIS_WIDE_PASSIVE 1
set_kv CEMINI_NEMESIS_LINEAR_AGGRO 1
set_kv CEMINI_NEMESIS_PHOENIX_CLUSTER 1
set_kv CEMINI_ISO_PASSIVE_LP 1
set_kv CEMINI_SEAT_MATRIX_V2 1
# Intel 2026-07-30: T9/T8 winners + S10 leaders + early T10
set_kv CEMINI_NEMESIS_HANDLES "halloran,royal_79f44c,reaper,vigilate,okonkwo,whalealert,nineteenshot,sam_whale,lodestar,joseph,cosmometrics,batu_sabar,StartupBros,page,kav_grind,alex_nft,reichelligahh,flattened_v2,si_nekat,mako_shark,sky_top,stu_ungar,crimson_range,blacksite,kuma_zero,ronin,clurit,highroller,onyxfang"
set_kv CEMINI_NEMESIS_PREFIXES "batu_,flattened_,kuma_,royal_,phoenix-,holonomic-,v12_,grok,si_,mako_,xiishii_"

set_kv CEMINI_JOIN_RETRY_S 12
set_kv CEMINI_CHASE_JOIN_RETRY_S 8
set_kv CEMINI_IN_QUEUE_RETRY_S 25
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 15
set_kv CEMINI_EXPORT_DIR "reports/exports/${EXPORT_SLUG}"
set_kv CEMINI_FIELD_EXPORT_HUD 1
set_kv CEMINI_FIELD_EXPORT_DIR "reports/exports/${EXPORT_SLUG}"
set_kv CEMINI_FIELD_EXPORT_HUD_TTL_S 3600
set_kv CEMINI_FIELD_EXPORT_MIN_LIVE_SAMPLE 8
set_kv CEMINI_PLAYGROUND_TIMESERIES 0
set_kv CEMINI_HL_AUTO_ANALYST 0
set_kv ARENA_NO_AUTO_REGISTER 1

grep -E '^(ARENA_LOBBY|S10_TOURNAMENT|CEMINI_HL_PRIMARY|AGENT_VERSION|CEMINI_TOURNAMENT|CEMINI_LOBBY_ROLE|CEMINI_GIN_STYLE|CEMINI_KO_SURVIVAL|CEMINI_NEMESIS_HANDLES)=' .env

mkdir -p "${EXPORT_DIR}"
if [[ ! -f "${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "${EXPORT_DIR}/crawl_state.json"
fi

./venv/bin/python - <<PY
import json
from pathlib import Path
comp = "${COMP}"
old = "${OLD}"
export_slug = "${EXPORT_SLUG}"
path = Path("reports/hl-loop/multi_comp_config.json")
cfg = json.loads(path.read_text()) if path.is_file() else {}
cfg.setdefault("schema", "devfun.multi_comp_config.v1")
cfg["lobby_competition_id"] = comp
cfg["primary"] = {
    "role": "s10_tournament",
    "label": "Tournament S10",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": f"reports/exports/{export_slug}",
    "season": 10,
}
cfg["secondary"] = [{
    "role": "s10_playground",
    "label": "Playground S10",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/playground-s10-live",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
print(f"multi_comp_config updated primary={comp}")
PY

systemctl daemon-reload
systemctl restart cemini-devfun-poker-lobby.service
systemctl enable cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl start cemini-devfun-poker-export-crawl.service 2>/dev/null || true
sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
# Cap journal dump so SSH remote does not hang waiting on pager/pipe
timeout 15 journalctl -u cemini-devfun-poker-lobby.service -n 20 --no-pager || true
REMOTE

# Mirror multi_comp on laptop
uv run python - <<PY
import json
from pathlib import Path
comp = "${COMP}"
old = "${OLD_PLAYGROUND}"
export_slug = "${EXPORT_SLUG}"
path = Path("${AGENT_DIR}/reports/hl-loop/multi_comp_config.json")
cfg = json.loads(path.read_text()) if path.is_file() else {}
cfg["lobby_competition_id"] = comp
cfg["primary"] = {
    "role": "s10_tournament",
    "label": "Tournament S10",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": f"reports/exports/{export_slug}",
    "season": 10,
}
cfg["secondary"] = [{
    "role": "s10_playground",
    "label": "Playground S10",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/playground-s10-live",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
print("laptop multi_comp_config updated")
PY

echo "==> Tournament S10 lobby restarted on ${COMP}"
echo "  Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
