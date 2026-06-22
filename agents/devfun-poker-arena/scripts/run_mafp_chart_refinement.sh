#!/usr/bin/env bash
# K124 MAFP offline fictitious-play chart refinement (pre Jun 21 Researcher beta).
#
# Runs stance aggregation (rock/maniac/lag) + best-response chart updates,
# writes research/mafp_hu_chart.json, logs mafp_round=N to deploys.jsonl.
#
# Usage:
#   ./scripts/run_mafp_chart_refinement.sh
#   ./scripts/run_mafp_chart_refinement.sh --robustness --hands 150
set -euo pipefail
cd "$(dirname "$0")/.."

ROBUSTNESS=0
HANDS=150
EXTRA_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --robustness)
      ROBUSTNESS=1
      shift
      ;;
    --hands)
      HANDS="${2:-150}"
      shift 2
      ;;
    *)
      EXTRA_ARGS+=("$1")
      shift
      ;;
  esac
done

export CEMINI_TABLE_FORMAT=hu
export CEMINI_GIN_STYLE=1
export CEMINI_S1B_EXPLOIT=1
export CEMINI_RESEARCHER_MODE=1

CMD=(uv run python examples/mafp_chart_refinement.py
  --aggregate-hands 80
  --max-rounds 5
  --seed 42)

if [[ "$ROBUSTNESS" == "1" ]]; then
  CMD+=(--robustness --hands "$HANDS")
fi
if [[ ${#EXTRA_ARGS[@]} -gt 0 ]]; then
  CMD+=("${EXTRA_ARGS[@]}")
fi

echo "==> MAFP chart refinement (HU, offline)"
"${CMD[@]}"

echo "==> HU regression smoke after MAFP overlay"
uv run pytest tests/test_hu_regression.py -q --tb=line

echo "MAFP refinement complete — chart: research/mafp_hu_chart.json"
