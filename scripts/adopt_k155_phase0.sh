#!/usr/bin/env bash
# adopt_k155_phase0.sh — Phase-0 for K155 IdeaGene-Bench (2026-07-14)
set -euo pipefail
gh api repos/VisionXLab/IdeasHaveGenomes --jq '"\(.full_name) | license=\(.license.spdx_id // "NOASSERTION") | \(.size)KB | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"'
echo "LICENSE file: TBD (README ## License)"
echo "Local copy: CCC + gambling raw-sources/foss-evals/IdeasHaveGenomes (~26MB)"
echo "Verdict: CONDITIONAL-GO — methodology Adopt; code WATCH until SPDX"
echo "Briefs:"
echo "  gambling-wiki/briefs/2026-07-14_k155-ideagene-lineage-steals.md"
echo "  OSINT agents/devfun-poker-arena/briefs/2026-07-14_k155-ideagene-patch-lineage-steal.md"
echo "  CCC briefs/2026-07-14_k155-ideagene-lineage-eval-prod.md → scp prod"
