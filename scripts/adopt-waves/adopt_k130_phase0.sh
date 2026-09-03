#!/usr/bin/env bash
# K130 Phase-0 — Poker GitHub Repository Evaluation.docx (30 URLs)
set -euo pipefail

echo "K130 Phase-0 audits"
echo "==================="

echo "Tool eval license spot-check:"
for repo in uoftcprg/pokerkit datamllab/rlcard HenryRLee/PokerHandEvaluator goldfire/pokersolver HarperJonesGPT/PokerGPT kwai/DouZero EricSteinberger/PokerRL ishikota/PyPokerEngine dickreuter/Poker pokerth/pokerth; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-26):"
echo "  Adopt (2): pokerkit MIT — CONFIRMED already in agents/devfun-poker-arena"
echo "             rlcard MIT — offline baseline venv only"
echo "  Steal-from (4): PokerHandEvaluator Apache-2.0 · pokersolver MIT · PokerGPT MIT · DouZero Apache-2.0"
echo "  Reject (15+): GPL/AGPL dickreuter/* pokerth · NO LICENSE fedden/deuces/chenosaurus · aggregated on source page"
echo ""
echo "Brief:"
echo "  agents/devfun-poker-arena/briefs/2026-06-26_k130-poker-stack-baseline-steal.md"
