#!/usr/bin/env bash
# K136 P0 — solver provenance stamp + guarded diff demo (offline).
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Provenance unit suite"
uv run pytest tests/test_solver_provenance.py -q

echo "==> Print provenance on existing charts (if present)"
for f in research/mafp_hu_chart.json research/preflop.json; do
  [[ -f "$f" ]] && uv run python examples/solver_provenance.py print "$f" || true
done

echo "==> Guarded diff demo (same file -> diffable, exit 0)"
uv run python examples/solver_provenance.py diff research/mafp_hu_chart.json research/mafp_hu_chart.json || true

echo "K136 P0 provenance checks complete."
