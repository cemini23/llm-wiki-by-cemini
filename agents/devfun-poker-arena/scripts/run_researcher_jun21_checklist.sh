#!/usr/bin/env bash
# K123 Jun 21 closed-beta checklist — automated gates (gambling-wiki brief).
#
# Usage:
#   ./scripts/run_researcher_jun21_checklist.sh           # full local gate
#   ./scripts/run_researcher_jun21_checklist.sh --ci      # faster pytest + 200h gate
#   ./scripts/run_researcher_jun21_checklist.sh --smoke   # trajectory smoke only
set -euo pipefail
cd "$(dirname "$0")/.."

CI=0
SMOKE=0
GATE_HANDS=500
while [[ $# -gt 0 ]]; do
  case "$1" in
    --ci) CI=1; GATE_HANDS=200; shift ;;
    --smoke) SMOKE=1; shift ;;
    --hands) GATE_HANDS="${2:-500}"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

export CEMINI_TABLE_FORMAT=hu
export CEMINI_GIN_STYLE=1
export CEMINI_GIN_STYLE_PREFLOP=1
export CEMINI_GIN_STYLE_POSTFLOP=1
export CEMINI_GIN_V008=1
export CEMINI_S1B_EXPLOIT=1
export CEMINI_RESEARCHER_MODE=1
export CEMINI_MAFP_CHART=1

echo "==> K123 Jun 21 checklist (gate_hands=${GATE_HANDS})"

if [[ "$SMOKE" == "1" ]]; then
  TRAJ="reports/researcher-round/jun21-smoke/selfplay_trajectory.jsonl"
  mkdir -p reports/researcher-round/jun21-smoke
  uv run python examples/selfplay.py \
    --agent examples/cemini_decide.py \
    --hands 50 --players 2 --opponent lag --seed 42 \
    --trajectory-out "$TRAJ"
  ./scripts/export_researcher_trajectory.sh --selfplay "$TRAJ" \
    --out-dir reports/researcher-round/jun21-smoke
  uv run python examples/researcher_trajectory_summary.py \
    --selfplay "$TRAJ" \
    --out-dir reports/researcher-round/jun21-smoke
  # K125: optional probabilistic trajectory-bound smoke.
  if [[ -f scripts/calibrate_trajectory_bounds.py && -f examples/trajectory_bound_report.py ]]; then
    bash scripts/run_trajectory_bound_calibration.sh
  else
    echo "==> K125 trajectory-bound smoke skipped (tools not present)"
  fi
  echo "CHECKLIST SMOKE OK"
  exit 0
fi

echo "==> pytest (HU + MAFP + trajectory bound + selfplay card format)"
if [[ "$CI" == "1" ]]; then
  uv run pytest tests/test_hu_regression.py \
    tests/test_mafp_chart_refinement.py \
    tests/test_cemini_trajectory_bound_integration.py \
    tests/test_trajectory_bound.py \
    tests/test_selfplay_card_format.py \
    tests/test_cemini_preflop_guards.py -q --tb=line
else
  uv run pytest tests/test_hu_regression.py \
    tests/test_mafp_chart_refinement.py \
    tests/test_cemini_trajectory_bound_integration.py \
    tests/test_trajectory_bound.py \
    tests/test_selfplay_card_format.py \
    tests/test_cemini_regression.py -q --tb=line
fi

if [[ ! -f research/mafp_hu_chart.json ]]; then
  echo "==> MAFP HU chart missing — offline refinement (quick)"
  bash scripts/run_mafp_chart_refinement.sh
fi

echo "==> pick researcher competition (advisory)"
uv run python examples/pick_researcher_competition.py || true

echo "==> HU sandbox gate (${GATE_HANDS} hands)"
CEMINI_TABLE_FORMAT=hu bash scripts/run_hu_sandbox_gate.sh --hands "$GATE_HANDS"

echo "==> trajectory + axis_summary smoke (80h)"
TRAJ="reports/researcher-round/jun21-checklist/selfplay_trajectory.jsonl"
mkdir -p reports/researcher-round/jun21-checklist
uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands 80 --players 2 --opponent mixed --seed 42 \
  --training-hud --trajectory-out "$TRAJ"
./scripts/export_researcher_trajectory.sh --selfplay "$TRAJ" \
  --out-dir reports/researcher-round/jun21-checklist
uv run python examples/researcher_trajectory_summary.py \
  --selfplay "$TRAJ" \
  --out-dir reports/researcher-round/jun21-checklist --gate

echo ""
echo "K123 JUN21 CHECKLIST GATE OK"
echo "  Next: pin ARENA_RESEARCHER_COMP_ID when API lists comp → researcher_jun21_beta_apply.sh"
