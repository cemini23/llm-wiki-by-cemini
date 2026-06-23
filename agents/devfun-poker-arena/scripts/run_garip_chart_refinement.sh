#!/usr/bin/env bash
# K127 GARIP chart refinement — CI smoke (dry-run, no chart write).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export CEMINI_HL_REPORTS_DIR="${CEMINI_HL_REPORTS_DIR:-$ROOT/reports/hl-loop}"

uv run python examples/garip_chart_refinement.py \
  --max-rounds 2 \
  --aggregate-hands 40 \
  --garip-alpha 0.3 \
  --no-deploy-log

echo "GARIP smoke OK"
