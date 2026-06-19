#!/usr/bin/env bash
# Researcher Track memory ablation.
#
# Runs paired local selfplay bundles with identical seed/opponents while
# toggling CEMINI_SESSION_MEMORY on vs off. The wrapper mirrors the lobby path:
# it builds cemini research_context, injects session_villain_memory, updates
# memory after each hero action, then writes paired trajectory bundles plus an
# axis delta summary (memory_on - memory_off) under reports/researcher-round/.
#
# Table format:
#   CEMINI_TABLE_FORMAT=hu (default for Researcher prep) → 2-max, tight opponent
#   CEMINI_TABLE_FORMAT=6max → 6-max mixed (legacy)
#
# Usage:
#   ./scripts/run_researcher_memory_ablation.sh
#   CEMINI_TABLE_FORMAT=6max ./scripts/run_researcher_memory_ablation.sh
set -euo pipefail
cd "$(dirname "$0")/.."

TABLE_FORMAT="${CEMINI_TABLE_FORMAT:-hu}"
case "$TABLE_FORMAT" in
  hu|heads-up|headsup|2max|2-max)
    HANDS=150
    PLAYERS=2
    OPPONENT=tight
    ;;
  6max|6-max)
    HANDS=150
    PLAYERS=6
    OPPONENT=mixed
    ;;
  *)
    echo "ERROR: CEMINI_TABLE_FORMAT must be hu or 6max" >&2
    exit 2
    ;;
esac

SEED=42
TS=$(date -u +%Y%m%dT%H%M%SZ)
BUNDLE_DIR="reports/researcher-round/ablation-${TABLE_FORMAT}-${TS}"
ON_DIR="${BUNDLE_DIR}/memory-on"
OFF_DIR="${BUNDLE_DIR}/memory-off"
ON_TRAJ="${ON_DIR}/selfplay_trajectory.jsonl"
OFF_TRAJ="${OFF_DIR}/selfplay_trajectory.jsonl"

mkdir -p "$ON_DIR" "$OFF_DIR"

run_wrapped_selfplay() {
  local memory_flag="$1"
  local traj_file="$2"
  local label="$3"
  echo "==> ${label} (CEMINI_SESSION_MEMORY=${memory_flag}, ${PLAYERS}-max, ${OPPONENT})"
  CEMINI_SESSION_MEMORY="$memory_flag" \
  CEMINI_TABLE_FORMAT="$TABLE_FORMAT" \
  CEMINI_GIN_STYLE=1 \
  CEMINI_GIN_STYLE_PREFLOP=1 \
  CEMINI_GIN_STYLE_POSTFLOP=1 \
  CEMINI_GIN_V008=1 \
  CEMINI_S1B_EXPLOIT=1 \
  CEMINI_RESEARCHER_MODE=1 \
    uv run python - "$traj_file" "$HANDS" "$PLAYERS" "$SEED" "$OPPONENT" <<'PY'
from pathlib import Path
import sys

root = Path.cwd()
examples = root / "examples"
if str(examples) not in sys.path:
    sys.path.insert(0, str(examples))

import cemini_decide  # noqa: E402
import selfplay  # noqa: E402
from session_memory import exploit_from_memory, update_session_memory, villain_memory_for_table  # noqa: E402

traj_path = Path(sys.argv[1])
hands = int(sys.argv[2])
players = int(sys.argv[3])
seed = int(sys.argv[4])
opponent = sys.argv[5]
state: dict = {}

def wrapped_decide(table: dict, deadline_s: float = 10.0) -> dict:
    ctx = cemini_decide.retrieve_solver_context(table)
    villain_mem = villain_memory_for_table(state, table)
    if villain_mem.get("villains"):
        ctx["session_villain_memory"] = villain_mem
        mem_margins = exploit_from_memory(villain_mem)
        if mem_margins:
            hud = ctx.setdefault("opponent_hud", {})
            base = hud.get("margins") or {}
            hud["margins"] = {
                **base,
                **{key: base.get(key, 0.0) + delta for key, delta in mem_margins.items()},
            }
    action = cemini_decide.decide(table, deadline_s=deadline_s, research_context=ctx)
    update_session_memory(state, table)
    return action

stats = selfplay.run_selfplay(
    decide_fn=wrapped_decide,
    n_hands=hands,
    opponent_label=opponent,
    n_players=players,
    starting_stack=200,
    small_blind=1,
    big_blind=2,
    seed=seed,
    trajectory_out=traj_path,
)
print(
    "[memory-ablation] "
    f"hands={stats['hands']} players={stats['players']} "
    f"net={stats['net_chips']:+d} bb100={stats['bb_per_100']:+.2f} "
    f"trajectory={stats.get('trajectory_path')}"
)
PY
}

run_wrapped_selfplay 1 "$ON_TRAJ" "Memory ON selfplay"
run_wrapped_selfplay 0 "$OFF_TRAJ" "Memory OFF selfplay"

echo "==> Axis summaries"
uv run python examples/researcher_trajectory_summary.py --selfplay "$ON_TRAJ" --out-dir "$ON_DIR"
uv run python examples/researcher_trajectory_summary.py --selfplay "$OFF_TRAJ" --out-dir "$OFF_DIR"

echo "==> Axis delta summary (memory_on - memory_off)"
uv run python - "$ON_DIR/axis_summary.json" "$OFF_DIR/axis_summary.json" "$BUNDLE_DIR/axis_delta_summary.json" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

on_path = Path(sys.argv[1])
off_path = Path(sys.argv[2])
out_path = Path(sys.argv[3])
on = json.loads(on_path.read_text(encoding="utf-8"))
off = json.loads(off_path.read_text(encoding="utf-8"))
on_self = on.get("selfplay") or {}
off_self = off.get("selfplay") or {}
on_axes = on_self.get("axes") or {}
off_axes = off_self.get("axes") or {}

metrics = (
    "net_chips",
    "bb_per_100",
    "vpip_proxy",
    "pfr_proxy",
)
axis_keys = (
    "M4_vpip_delta_post_bad_beat",
    "M7_mean_action_entropy",
    "M8_hallucination_rate",
    "M8_hole_leak_rate",
    "M9_btn_minus_utg_vpip",
)

delta = {
    "memory_on_bundle": str(on_path.parent),
    "memory_off_bundle": str(off_path.parent),
    "metric_delta": {},
    "axis_delta": {},
}

for key in metrics:
    delta["metric_delta"][key] = round(
        float(on_self.get(key) or 0.0) - float(off_self.get(key) or 0.0),
        4,
    )
for key in axis_keys:
    delta["axis_delta"][key] = round(
        float(on_axes.get(key) or 0.0) - float(off_axes.get(key) or 0.0),
        4,
    )

out_path.write_text(json.dumps(delta, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"  memory_on : {on_path.parent}")
print(f"  memory_off: {off_path.parent}")
for key, value in delta["metric_delta"].items():
    print(f"  metric {key}: {value:+.4f}")
for key, value in delta["axis_delta"].items():
    print(f"  axis   {key}: {value:+.4f}")
print(f"  wrote delta → {out_path}")
PY

echo ""
echo "RESEARCHER MEMORY ABLATION OK — bundle: ${BUNDLE_DIR}"
echo "Table format: ${TABLE_FORMAT} (${PLAYERS}-max, opponent=${OPPONENT})"
