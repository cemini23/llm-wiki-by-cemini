#!/usr/bin/env bash
# 150-hand eval-panel self-play smoke — compare vs pre-lane-gate baseline (−26.67).
set -euo pipefail
cd "$(dirname "$0")/.."

HANDS="${EVAL_PANEL_SMOKE_HANDS:-150}"
BASELINE="${EVAL_PANEL_SMOKE_BASELINE:--26.67}"
SEED="${EVAL_PANEL_SMOKE_SEED:-42}"

echo "==> Eval panel smoke: ${HANDS} hands vs rock (eval_panel_mode=ON)"
echo "    Baseline bb/100: ${BASELINE}"

uv run python examples/eval_panel_gate.py \
  --hands "${HANDS}" \
  --seed "${SEED}" \
  --baseline "${BASELINE}" \
  --write-metrics

echo "==> Tournament posture smoke (no eval_panel — lane-gate OFF)"
uv run python examples/eval_panel_gate.py \
  --hands "${HANDS}" \
  --seed "${SEED}" \
  --baseline "${BASELINE}" \
  --tournament-posture \
  --write-metrics

echo "==> Metrics: reports/hl-loop/preflight_metrics.json"
