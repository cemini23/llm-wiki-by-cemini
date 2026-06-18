#!/usr/bin/env bash
# Researcher Round pre-submit gate — 6-max regression + selfplay + trajectory.
#
#   ./scripts/run_hu_sandbox_gate.sh
#   ./scripts/run_hu_sandbox_gate.sh --hands 500
set -euo pipefail
cd "$(dirname "$0")/.."

HANDS=200
if [[ "${1:-}" == "--hands" ]]; then
  HANDS="${2:-200}"
fi

TS=$(date -u +%Y%m%dT%H%M%SZ)
BUNDLE_DIR="reports/researcher-round/gate-${TS}"
TRAJ_FILE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
mkdir -p "$BUNDLE_DIR"

echo "==> 6-max regression (full + HU smoke)"
uv run pytest tests/test_cemini_regression.py tests/test_hu_regression.py -q --tb=line

echo "==> 6-max selfplay gate (${HANDS} hands, cemini_decide vs tight)"
CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 \
  uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands "$HANDS" \
  --players 6 \
  --opponent mixed \
  --seed 42 \
  --trajectory-out "$TRAJ_FILE"

echo "==> Trajectory + axis summary"
./scripts/export_researcher_trajectory.sh \
  --selfplay "$TRAJ_FILE" \
  --out-dir "$BUNDLE_DIR"

if [[ -n "${ARENA_RESEARCHER_COMP_ID:-}" ]]; then
  echo "==> Arena trajectory pull (ARENA_RESEARCHER_COMP_ID)"
  ./scripts/export_researcher_trajectory.sh \
    --competition-id "$ARENA_RESEARCHER_COMP_ID" \
    --out-dir "${BUNDLE_DIR}/arena"
  uv run python examples/researcher_trajectory_summary.py \
    --selfplay "$TRAJ_FILE" \
    --export-dir "${BUNDLE_DIR}/arena/arena-export" \
    --out-dir "$BUNDLE_DIR"
fi

echo ""
echo "RESEARCHER SANDBOX GATE OK — bundle: ${BUNDLE_DIR}"
echo "Arena submit: pokerkit run --max-hands 50 (smoke) then pokerkit run (500h default)"
echo "Full match length assumed same as Eval S5 until Researcher skill contradicts."
