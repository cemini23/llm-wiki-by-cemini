#!/usr/bin/env bash
# K136 P1 — FP->PED spike on 3-player Kuhn (offline, reference-only literacy).
#   ./scripts/run_kuhn3p_ped_spike.sh
#   ./scripts/run_kuhn3p_ped_spike.sh --deck-size 6 --budget 400
set -euo pipefail
cd "$(dirname "$0")/.."

DECK=4
BUDGET=200
EXTRA_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --deck-size) DECK="${2:-4}"; shift 2 ;;
    --budget)    BUDGET="${2:-200}"; shift 2 ;;
    *) EXTRA_ARGS+=("$1"); shift ;;
  esac
done

echo "==> kuhn3p solver unit suite"
uv run pytest tests/test_kuhn3p_solver.py -q

echo "==> FP->PED vs CFR equal-budget spike (deck=${DECK}, budget=${BUDGET})"
CMD=(uv run python examples/kuhn3p_solver.py --deck-size "$DECK" --budget "$BUDGET" --seed 42)
[[ ${#EXTRA_ARGS[@]} -gt 0 ]] && CMD+=("${EXTRA_ARGS[@]}")
"${CMD[@]}"

echo "Spike complete — report: research/kuhn3p_ped_spike.json"
