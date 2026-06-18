#!/usr/bin/env bash
# HU sandbox pre-submit gate — researcher track / Poker Agent Challenge.
#
# Fast local check before BenchFlow sandbox submit (no Arena network).
#   ./scripts/run_hu_sandbox_gate.sh
#   ./scripts/run_hu_sandbox_gate.sh --hands 500
set -euo pipefail
cd "$(dirname "$0")/.."

HANDS="${1:-200}"
if [[ "${1:-}" == "--hands" ]]; then
  HANDS="${2:-200}"
fi

echo "==> HU selfplay gate (${HANDS} hands, cemini_decide vs tight-passive)"
CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 \
  uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands "$HANDS" \
  --opponent tight \
  --seed 42

echo ""
echo "HU SANDBOX GATE OK — confirm with pokerkit run / BenchFlow before Jun 21 submit"
