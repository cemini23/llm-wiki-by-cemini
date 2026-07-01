#!/usr/bin/env bash
# K138 Phase-0 — GitHub eval docx (20 URLs) + arXiv spot-check repos
set -euo pipefail

echo "K138 Phase-0 audits"
echo "==================="

for repo in cwendt94/espn-api BenBrostoff/draftfast PENEEEEE732/AI_pokergame api-evangelist/sportsbook-api personal-coding/Live-Sports-Arbitrage-Bet-Finder google-research/football jokecamp/FootballData PodeCaradox/CastleSimWeb statsbomb/open-data; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-07-01):"
echo "  Adopt (1): cwendt94/espn-api MIT"
echo "  CONDITIONAL-GO (1): BenBrostoff/draftfast — no LICENSE file on gh"
echo "  Steal-from (3): AI_pokergame MIT (docx corrected) · sportsbook-api · Live-Sports-Arbitrage"
echo "  Reference-only (2): jokecamp/FootballData MIT · PodeCaradox/CastleSimWeb"
echo "  Defer (1): google-research/football Apache-2.0 TF1.15 debt"
echo "  Reject (8+): statsbomb NC UA · legacy R DFS scrapers · dead poker UIs · …"
echo "  arXiv: 2606.29457 deal games · 2606.31675 PM settlement manipulation — REFERENCE briefs"
echo ""
echo "Briefs:"
echo "  briefs/2026-07-01_k138-pm-settlement-manipulation-guard-prod.md"
echo "  agents/devfun-poker-arena/briefs/2026-07-01_k138-deal-games-ppo-solver-steal.md"
echo "  agents/devfun-poker-arena/briefs/2026-07-01_k138-ai-pokergame-opponent-steal.md"
echo "  ../projects/CeminiDFS/briefs/2026-07-01_k138-espn-api-fetch-adopt.md"
echo "  ../projects/CeminiDFS/briefs/2026-07-01_k138-draftfast-optimizer-conditional.md"
echo "  ../projects/Game Dev wiki/briefs/2026-07-01_k138-castlesimweb-wgpu-reference.md"
