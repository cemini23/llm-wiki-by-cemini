#!/usr/bin/env bash
# K125 Phase-0 — daily digest full ingest (2 arXiv + tool eval docx)
set -euo pipefail

echo "K125 Phase-0 audits"
echo "==================="

echo "Probabilistic verification (2606.20510):"
echo "  No public repo at ingest — REFERENCE pattern steal only"

echo "RNG-Bench (2606.19338):"
echo "  No public repo at ingest — REFERENCE Memory Gap rubric"

echo ""
echo "Tool eval license spot-check (NFL/DFS batch):"
gh api repos/bbenbenek/nfl-fantasy-football --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"
gh api repos/hvpkod/NFL-Data --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"
gh api repos/danmorse314/nfl-stuff --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"
gh api repos/thiagocavalheiro/polymarket-sports-trading-bot --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"

echo ""
echo "Verdicts (2026-06-21):"
echo "  arxiv-2606.20510 (probabilistic verification)  REFERENCE — Google; trajectory risk bound steal"
echo "  arxiv-2606.19338 (RNG-Bench)                  REFERENCE — Memory Gap diagnostic; no repo"
echo "  github-nfl-repo-eval docx                     REFERENCE — nflverse confirmed; danmorse314 clean-room only"
echo "  thiagocavalheiro/polymarket-sports-trading-bot REJECT — null license"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-21_k125-probabilistic-verifier-trajectory-steal.md"
echo "  ../projects/castle-sim/briefs/2026-06-21_k125-rng-bench-memory-gap-playtest.md"
echo "  ../projects/CeminiDFS/briefs/2026-06-21_k125-nfl-repo-eval-epa-cleanroom.md"
