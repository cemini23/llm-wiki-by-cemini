#!/usr/bin/env bash
# S1 tournament–first HL cycle — patches deploy from primary comp only.
#
# 1. Multi-comp snapshot (+ export primary hands with chip_delta)
# 2. Analyze S1 tournament (not S2)
# 3. Tournament-posture eval smoke (500h default)
# 4. Optional deploy: --deploy (requires S1 hand gate + regression)
#
# Usage:
#   ./scripts/run_s1_tournament_hl_cycle.sh
#   ./scripts/run_s1_tournament_hl_cycle.sh --deploy
#   EVAL_PANEL_SMOKE_HANDS=300 ./scripts/run_s1_tournament_hl_cycle.sh
set -euo pipefail
cd "$(dirname "$0")/.."

DEPLOY=0
for arg in "$@"; do
  case "$arg" in
    --deploy) DEPLOY=1 ;;
  esac
done

HANDS="${EVAL_PANEL_SMOKE_HANDS:-500}"
MIN_DEPLOY_HANDS="${CEMINI_S1_MIN_DEPLOY_HANDS:-80}"

echo "==> [1/4] Multi-comp oracle (S1 primary + S2 intel)"
uv run python examples/multi_comp_registry.py discover
uv run python examples/multi_comp_registry.py snapshot --export

PRIMARY="$(uv run python -c "from multi_comp_registry import primary_competition_id; print(primary_competition_id())")"
if [[ -z "${PRIMARY}" ]]; then
  echo "ERROR: No S1 tournament competition_id." >&2
  echo "  Set S1_TOURNAMENT_COMP=cmp... or wait for bracket + discover" >&2
  exit 2
fi
echo "    S1 primary comp: ${PRIMARY}"

export CEMINI_HL_PRIMARY_COMP="${PRIMARY}"

echo "==> [2/4] Analyze S1 tournament only (--match ${PRIMARY})"
mkdir -p reports/analyze reports/hl-loop
uv run python examples/analyze.py \
  --match "${PRIMARY}" \
  --top "${HL_ANALYZE_TOP:-15}" \
  --out reports/hl-loop/latest_analyze.txt
cp -f reports/hl-loop/latest_analyze.txt reports/analyze/latest_analyze_s1_tournament.txt

echo "==> [3/4] Deploy gate (S1 hands only; S2 does not authorize deploy)"
if uv run python examples/multi_comp_registry.py deploy-gate --min-hands "${MIN_DEPLOY_HANDS}"; then
  echo "    Gate: OK for patch consideration"
else
  echo "    Gate: WARN — low S1 volume; use analyze + smoke only until hands grow"
fi

echo "==> [4/4] Tournament posture smoke (${HANDS} hands)"
EVAL_PANEL_SMOKE_HANDS="${HANDS}" bash scripts/run_eval_panel_smoke.sh

if [[ "${DEPLOY}" -eq 1 ]]; then
  echo "==> Deploy (S1-gated, fast preflight)"
  uv run python examples/multi_comp_registry.py deploy-gate --min-hands "${MIN_DEPLOY_HANDS}"
  CEMINI_SKIP_COMP_CHECK=1 ./examples/cemini_hl_loop.sh \
    --deploy-fast \
    --match "${PRIMARY}" \
    --round tournament-s1
else
  echo ""
  echo "Next: patch cemini_decide.py from reports/hl-loop/latest_analyze.txt"
  echo "      then: ./scripts/run_s1_tournament_hl_cycle.sh --deploy"
fi
