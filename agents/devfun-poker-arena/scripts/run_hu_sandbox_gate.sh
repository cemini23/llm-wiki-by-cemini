#!/usr/bin/env bash
# HU sandbox pre-submit gate — researcher track / Poker Agent Challenge.
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

echo "==> HU regression spots"
uv run pytest tests/test_hu_regression.py -q --tb=line

echo "==> HU selfplay gate (${HANDS} hands, cemini_decide vs tight)"
CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 \
  uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands "$HANDS" \
  --opponent tight \
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
echo "HU SANDBOX GATE OK — bundle: ${BUNDLE_DIR}"
echo "Confirm with pokerkit run / BenchFlow before Jun 21 submit"
