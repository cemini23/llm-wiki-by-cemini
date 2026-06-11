#!/usr/bin/env bash
# Tournament S1 posture — prize-pool focus, 5 rebuys (S1 playground win perk).
#
# Usage (when Tournament S1 competition ID is live in list-active):
#   TOURNAMENT_COMP=cmpXXXXXXXX ./scripts/s1_tournament_prod_apply.sh
#   ./scripts/s1_tournament_prod_apply.sh cmpXXXXXXXX
#
# Does NOT rsync code — run deploy_to_cemini_prod.sh or hl_loop --deploy-fast first.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${TOURNAMENT_COMP:-}}"
OLD_PLAYGROUND="${OLD_PLAYGROUND_COMP:-cmq57o53r0bhw18g23qkydb08}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s1t.${GIT_SHA}.tournament-s1}"

if [[ -z "${COMP}" ]]; then
  echo "Tournament competition ID required." >&2
  echo "  ./scripts/s1_tournament_prod_apply.sh <TOURNAMENT_COMP_ID>" >&2
  echo "  or: TOURNAMENT_COMP=cmp... ./scripts/s1_tournament_prod_apply.sh" >&2
  echo "" >&2
  echo "Discover when bracket opens:" >&2
  echo "  uv run python -c \"from examples.arena_monitor import _fetch_active_competitions; ...\"" >&2
  exit 2
fi

echo "==> Tournament S1 prod apply: comp=${COMP} agent_version=${AGENT_VERSION}"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
COMP="${COMP}"
OLD="${OLD_PLAYGROUND}"
AGENT_VERSION="${AGENT_VERSION}"

echo "==> Drain playground tables (optional — frees lobby focus)"
./venv/bin/python scripts/playground_drain_competition.py "\${OLD}" || true

echo "==> Clear kill switch"
./venv/bin/python examples/arena_kill_switch.py clear --reason "Tournament S1 enter" || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "\${COMP}"
set_kv S1_TOURNAMENT_COMP "\${COMP}"
set_kv CEMINI_HL_PRIMARY_COMP "\${COMP}"
set_kv S2_PLAYGROUND_COMP "\${OLD}"
set_kv AGENT_VERSION "\${AGENT_VERSION}"
# Tournament = placement EV; not eval-panel self-play gate or jackpot volume chase.
set_kv CEMINI_EVAL_PANEL_GATE 0
set_kv CEMINI_TOURNAMENT_MODE 1
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
set_kv CEMINI_S1B_EXPLOIT 1
set_kv CEMINI_S1B_MIN_STACK_BB 80
set_kv CEMINI_NEMESIS_EXPLOIT 1
set_kv CEMINI_NEMESIS_TIGHT 1
set_kv CEMINI_JOIN_RETRY_S 25
set_kv CEMINI_IN_QUEUE_RETRY_S 60
# Single-table API: S1-only lobby until tournament ends (~Jun 14–15).
if grep -q '^CEMINI_DUAL_LOBBY_COMP=' .env 2>/dev/null; then
  sed -i.bak '/^CEMINI_DUAL_LOBBY_COMP=/d' .env
fi

grep -E '^(ARENA_LOBBY|S1_TOURNAMENT|CEMINI_HL_PRIMARY|S2_PLAYGROUND|AGENT_VERSION|CEMINI_EVAL|CEMINI_TOURNAMENT|CEMINI_STAGGER|CEMINI_QUAL_BUFFER|CEMINI_LEAD_BUFFER|CEMINI_PACE|CEMINI_KO|CEMINI_SURVIVAL|JACKPOT|CEMINI_S1B|CEMINI_NEMESIS_TIGHT)=' .env

./venv/bin/python - <<PY
import json
from pathlib import Path
comp = "${COMP}"
old = "${OLD_PLAYGROUND}"
path = Path("reports/hl-loop/multi_comp_config.json")
cfg = {}
if path.is_file():
    cfg = json.loads(path.read_text())
cfg.setdefault("schema", "devfun.multi_comp_config.v1")
cfg["lobby_competition_id"] = comp
cfg["primary"] = {
    "role": "s1_tournament",
    "label": "Tournament S1",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": "reports/exports/s1-tournament-live",
}
cfg["secondary"] = [{
    "role": "s2_playground",
    "label": "Playground S2",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/s2-playground-live",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
print(f"multi_comp_config updated primary={comp}")
PY

systemctl restart cemini-devfun-poker-lobby.service
sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
REMOTE

# Laptop oracle config (same primary comp)
uv run python - <<PY
import json, os
from pathlib import Path
comp = "${COMP}"
old = "${OLD_PLAYGROUND}"
path = Path("reports/hl-loop/multi_comp_config.json")
cfg = json.loads(path.read_text()) if path.is_file() else {}
cfg["lobby_competition_id"] = comp
cfg.setdefault("primary", {})
cfg["primary"].update({
    "role": "s1_tournament",
    "label": "Tournament S1",
    "competition_id": comp,
    "priority": 1,
    "drives_deploy": True,
    "export_dir": "reports/exports/s1-tournament-live",
})
cfg["secondary"] = [{
    "role": "s2_playground",
    "label": "Playground S2",
    "competition_id": old,
    "priority": 2,
    "drives_deploy": False,
    "export_dir": "reports/exports/s2-playground-live",
}]
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(cfg, indent=2) + "\n")
PY

echo "==> Tournament S1 lobby restarted on ${COMP}"
echo "==> HL primary: CEMINI_HL_PRIMARY_COMP=${COMP} (S2 intel only in oracle)"
