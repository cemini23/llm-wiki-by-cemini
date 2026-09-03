#!/usr/bin/env bash
# K136 Phase-0 — 3 arXiv inbox (theory-only; no adoptable repos)
set -euo pipefail

echo "K136 Phase-0 audits"
echo "==================="

for id in 2606.28308 2606.29169 2606.30092; do
  echo "arXiv $id: no public implementation repo found at ingest (2026-06-30)"
done

echo ""
echo "Verdicts (2026-06-30):"
echo "  REFERENCE (3): Nash solver selection · PED · HRL-IM/CBS StarCraft"
echo "  Adopt: none"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-30_k136-nash-solver-fp-ped-steal.md"
echo "  ../projects/Game Dev wiki/briefs/2026-06-30_k136-hrl-influence-map-micromanagement-steal.md"
