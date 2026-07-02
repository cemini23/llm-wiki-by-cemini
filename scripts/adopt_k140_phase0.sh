#!/usr/bin/env bash
# K140 Phase-0 — 3 arXiv inbox (theory/survey; no adoptable repos at ingest)
set -euo pipefail

echo "K140 Phase-0 audits"
echo "==================="

for id in 2606.30040 2607.00065 2607.00527; do
  echo "arXiv $id: no SPDX adoptable implementation repo verified at ingest (2026-07-02)"
done

echo "Optional demo (REFERENCE): dronectr.tudelft.nl pathfinder — Zou/Borst 2025; license unverified"
echo "AI-native corpus: 53 games listed in paper; no single canonical GitHub org"

echo ""
echo "Verdicts (2026-07-02):"
echo "  REFERENCE (3): Kalshi CPI belief distributions · Zeta* any-angle planning · AI-native G/N taxonomy"
echo "  Adopt: none"
echo ""
echo "Briefs:"
echo "  briefs/pm-2026-07-02_k140-kalshi-cpi-tail-belief-steal-prod.md"
echo "  ../projects/Game Dev wiki/briefs/2026-07-02_k140-zeta-any-angle-path-planning-steal.md"
echo "  ../projects/Game Dev wiki/briefs/2026-07-02_k140-ai-native-games-gn-taxonomy-steal.md"
echo "  agents/devfun-poker-arena/briefs/2026-07-02_k140-mechanical-invariants-rubric-steal.md"
