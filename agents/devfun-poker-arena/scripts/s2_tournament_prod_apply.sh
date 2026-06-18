#!/usr/bin/env bash
# Tournament S2 posture — free entry from Playground S2 qual; placement EV + archetype exploits.
#
# Usage:
#   ./scripts/s2_tournament_prod_apply.sh
#   ./scripts/s2_tournament_prod_apply.sh cmqggiv9k37am11ydmppz466e
#   TOURNAMENT_COMP=cmq... ./scripts/s2_tournament_prod_apply.sh
#
# Run gates locally first:
#   uv run python scripts/regression_gate.py
#   uv run python scripts/gin_style_gate.py
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${TOURNAMENT_COMP:-cmqggiv9k37am11ydmppz466e}}"
OLD_PLAYGROUND="${OLD_PLAYGROUND_COMP:-cmq57o53r0bhw18g23qkydb08}"
EXPORT_SLUG="${S2_TOURNAMENT_EXPORT_SLUG:-s2-tournament-live}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s2t.${GIT_SHA}.tournament-s2}"

echo "==> Tournament S2 prod apply: comp=${COMP} agent_version=${AGENT_VERSION}"

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
OLD="${OLD_PLAYGROUND}"
EXPORT_SLUG="${EXPORT_SLUG}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/\${EXPORT_SLUG}"
AGENT_VERSION="${AGENT_VERSION}"

echo "==> Drain ended playground tables (optional)"
./venv/bin/python scripts/playground_drain_competition.py "\${OLD}" || true

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "Tournament S2 enter" || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "\${COMP}"
set_kv S2_TOURNAMENT_COMP "\${COMP}"
set_kv S1_TOURNAMENT_COMP "cmq6l1gnq0lkz60y9i9d9eca1"
set_kv S2_PLAYGROUND_COMP "\${OLD}"
set_kv CEMINI_HL_PRIMARY_COMP "\${COMP}"
set_kv CEMINI_TOURNAMENT_SEASON 2
set_kv AGENT_VERSION "\${AGENT_VERSION}"
set_kv CEMINI_LOBBY_LABEL "Tournament_S2"
set_kv CEMINI_LOBBY_ROLE "s2_tournament"

# Tournament = placement EV; gin width without eval-panel gate (S2 audit consensus).
set_kv CEMINI_TOURNAMENT_MODE 1
set_kv CEMINI_EVAL_PANEL_GATE 0
set_kv CEMINI_EVAL_PANEL_BB100_FLOOR -25
set_kv CEMINI_PRIZE_CUTOFF_RANK 10
set_kv CEMINI_QUAL_CUTOFF_RANK 10
set_kv CEMINI_STAGGER_LOCKS 0
set_kv CEMINI_QUAL_BUFFER_CHIPS 999999
set_kv CEMINI_LEAD_BUFFER_CHIPS 999999
set_kv CEMINI_PACE_PHASE ""
set_kv CEMINI_KO_SURVIVAL 1
set_kv CEMINI_KO_SURVIVAL_HANDS 60
set_kv CEMINI_KO_SURVIVAL_MIN_STACK 600
set_kv CEMINI_SURVIVAL_STACK_CHIPS 300
set_kv JACKPOT_27_HUNT_ENABLED 0
set_kv JACKPOT_27_AGGRESSIVE 0
set_kv JACKPOT_ROYAL_ENABLED 0
set_kv JACKPOT_ROYAL_SHOWDOWN 0

# Gin lane (validated locally via gin_style_gate.py)
set_kv CEMINI_GIN_STYLE 1
set_kv CEMINI_GIN_STYLE_PREFLOP 1
set_kv CEMINI_GIN_STYLE_POSTFLOP 1
set_kv CEMINI_GIN_STYLE_GATE 1
set_kv CEMINI_GIN_V008 1
set_kv CEMINI_COLD_START_NO_STEAL 0

# Exploit stack — archetype over blanket nemesis-tight (S1 tournament mistake).
set_kv CEMINI_S1B_EXPLOIT 1
set_kv CEMINI_S1B_MIN_STACK_BB 80
set_kv CEMINI_NEMESIS_EXPLOIT 1
set_kv CEMINI_NEMESIS_TIGHT 0
set_kv CEMINI_NEMESIS_ARCHETYPE 1
set_kv CEMINI_NEMESIS_PREMIUM_NIT 1
set_kv CEMINI_NEMESIS_WIDE_PASSIVE 1
set_kv CEMINI_NEMESIS_LINEAR_AGGRO 1
set_kv CEMINI_NEMESIS_PHOENIX_CLUSTER 1
set_kv CEMINI_ISO_PASSIVE_LP 1
set_kv CEMINI_SEAT_MATRIX_V2 1
# Empty → nemesis_seed.py defaults (S1/S2 export handles + holonomic-/phoenix- prefixes)
set_kv CEMINI_NEMESIS_HANDLES ""
set_kv CEMINI_NEMESIS_PREFIXES "v12_,phoenix-rises-nrkdhd,phoenix-nrkdhd,phoenix-,holonomic-"

set_kv CEMINI_JOIN_RETRY_S 25
set_kv CEMINI_CHASE_JOIN_RETRY_S 10
set_kv CEMINI_IN_QUEUE_RETRY_S 60
set_kv CEMINI_EXPORT_DIR "reports/exports/\${EXPORT_SLUG}"
set_kv CEMINI_FIELD_EXPORT_HUD 1
set_kv CEMINI_FIELD_EXPORT_DIR "reports/exports/\${EXPORT_SLUG}"
set_kv CEMINI_FIELD_EXPORT_HUD_TTL_S 3600
set_kv CEMINI_FIELD_EXPORT_MIN_LIVE_SAMPLE 8
set_kv CEMINI_PLAYGROUND_TIMESERIES 0

if grep -q '^CEMINI_DUAL_LOBBY_COMP=' .env 2>/dev/null; then
  sed -i.bak '/^CEMINI_DUAL_LOBBY_COMP=/d' .env
fi

grep -E '^(ARENA_LOBBY|S2_TOURNAMENT|CEMINI_HL_PRIMARY|AGENT_VERSION|CEMINI_TOURNAMENT|CEMINI_EVAL|CEMINI_NEMESIS_TIGHT|CEMINI_GIN_STYLE)=' .env

mkdir -p "\${EXPORT_DIR}"
if [[ ! -f "\${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "\${EXPORT_DIR}/crawl_state.json"
fi

if [[ -f /etc/systemd/system/cemini-devfun-poker-export-crawl.service ]]; then
  sed -i "s|Environment=CEMINI_EXPORT_DIR=.*|Environment=CEMINI_EXPORT_DIR=\${EXPORT_DIR}|" \
    /etc/systemd/system/cemini-devfun-poker-export-crawl.service 2>/dev/null || true
fi

./venv/bin/python - <<PY
import json
from pathlib import Path
comp = "${COMP}"
old = "${OLD_PLAYGROUND}"
export_slug = "${EXPORT_SLUG}"
path = Path("reports/hl-loop/multi_comp_config.json")
cfg = {}
if path.is_file():
    cfg = json.loads(path.read_text())
cfg.setdefault("schema", "devfun.multi_comp_config.v1")
cfg["lobby_competition_id"] = comp
cfg["primary"] = {
    "role": "s2_tournament",
    "label": "Tournament S2",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": f"reports/exports/{export_slug}",
    "season": 2,
}
cfg["secondary"] = [{
    "role": "s2_playground",
    "label": "Playground S2 (ended)",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/s2-audit-pack",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
print(f"multi_comp_config updated primary={comp}")
PY

systemctl daemon-reload
systemctl restart cemini-devfun-poker-lobby.service
systemctl enable cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl start cemini-devfun-poker-export-crawl.service 2>/dev/null || true

if [[ -f deploy/cemini-tournament-priority.service ]]; then
  cp -f deploy/cemini-tournament-priority.service deploy/cemini-tournament-priority.timer \
    /etc/systemd/system/
  systemctl daemon-reload
  systemctl enable cemini-tournament-priority.timer
  systemctl start cemini-tournament-priority.timer
  CEMINI_TOURNAMENT_PRIORITY_LOCAL=1 ./scripts/tournament_priority_guard.sh || true
fi

sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
REMOTE

uv run python - <<PY
import json
from pathlib import Path
comp = "${COMP}"
old = "${OLD_PLAYGROUND}"
export_slug = "${EXPORT_SLUG}"
path = Path("reports/hl-loop/multi_comp_config.json")
cfg = json.loads(path.read_text()) if path.is_file() else {}
cfg["lobby_competition_id"] = comp
cfg["primary"] = {
    "role": "s2_tournament",
    "label": "Tournament S2",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": f"reports/exports/{export_slug}",
    "season": 2,
}
cfg["secondary"] = [{
    "role": "s2_playground",
    "label": "Playground S2 (ended)",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/s2-audit-pack",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
PY

echo "==> Tournament S2 lobby restarted on ${COMP}"
echo "  Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
echo "  HL: patches only after ≥50 tournament hands + analyze (no fold-only rounds)"
