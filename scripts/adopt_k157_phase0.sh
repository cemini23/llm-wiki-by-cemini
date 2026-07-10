#!/usr/bin/env bash
# adopt_k157_phase0.sh — Phase-0 metadata for K157 ingest (2026-07-10)
set -euo pipefail
repos=(
  davila7/claude-code-templates
  sickn33/agentic-awesome-skills
  mattprusak/autoresearch-genealogy
  PeWu/topola-viewer
  liberu-genealogy/genealogy-laravel
  oven-sh/bun
  autonomous-ai/autonomous-computer
  fisharebest/webtrees
  zeux/meshoptimizer
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Integrate: agentic-awesome-skills (MIT) → TipDrop/David; autoresearch-genealogy (MIT) → family sprint"
echo "Extract: claude-code-templates (MIT) → TipDrop subagent/CI steal; topola-viewer (Apache-2.0); liberu php-dna (MIT)"
echo "Integrate (API): Muse Spark 1.1 → xsp orchestration spike brief (commercial ToS)"
echo "Watch: bun (NOASSERTION SPDX — stability); autonomous-computer (MIT); webtrees (GPL-3.0)"
echo "Context: meshoptimizer (MIT) — 3d-printing/game-dev reference only"
echo "Briefs:"
echo "  ../projects/tipdrop-workspace-kit/briefs/2026-07-10_k157-claude-code-templates-steal-david.md"
echo "  ../projects/tipdrop-workspace-kit/briefs/2026-07-10_k157-agentic-awesome-skills-david.md"
echo "  briefs/xsp-2026-07-10_k157-muse-spark-orchestration-eval.md → scp prod"
echo "  ~/Desktop/family/research/2026-07-10_k157-autoresearch-genealogy-integrate.md (private)"
