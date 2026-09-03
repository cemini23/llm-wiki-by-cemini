#!/usr/bin/env bash
# adopt_k159_phase0.sh — Phase-0 metadata for K159 ingest (2026-07-11)
set -euo pipefail
repos=(
  DannyMac180/fable-advisor
  JustVugg/colibri
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Integrate: fable-advisor (MIT) → xsp prod brief + CCC + CeminiDFS cost pattern"
echo "Watch: colibri (Apache-2.0) — offline MoE; SSD wear / latency blockers"
echo "Pass: 17 SSG repos (Jekyll, Hugo, Next.js, Pelican AGPL, archived Slate, …)"
echo "Genealogy: Ricerca Sellia docx → private family/research/ + wiki methodology only"
echo "Briefs:"
echo "  briefs/xsp-2026-07-11_k159-fable-advisor-orchestration-steal.md → scp prod"
echo "  briefs/ccc-2026-07-11_k159-fable-advisor-orchestration-steal.md"
echo "  ../projects/CeminiDFS/briefs/2026-07-11_k159-fable-advisor-pipeline-cost-steal.md"
echo "  ~/Desktop/family/research/2026-07-11_k159-sellia-costantino-passante-sprint.md (private)"
echo "Local adopt: bash scripts/adopt_k159_local.sh"
