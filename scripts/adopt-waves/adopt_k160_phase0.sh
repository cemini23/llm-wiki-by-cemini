#!/usr/bin/env bash
# adopt_k160_phase0.sh — Phase-0 metadata for K160 ingest (2026-07-12)
set -euo pipefail
repos=(
  mira-wm/mira
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Watch: mira-wm/mira (Apache-2.0) — MP world model shelf; castle-sim design-pattern steal only"
echo "REFERENCE: RCT-AD 2607.04689 — autonomous driving; wiki-only"
echo "Deep-read archive: 2607.05352, 2607.06008, 2607.06166, 2607.06854 (prior K151/K155 pages)"
echo "Genealogy: Abruzzo Diaspora docx → private family/research/ + wiki methodology"
echo "Briefs:"
echo "  briefs/pm-2026-07-12_k160-proper-betting-conviction-layer-steal.md → scp prod"
echo "  agents/devfun-poker-arena/briefs/2026-07-12_k160-lightweight-yardstick-deep-read-steal.md"
echo "  ../projects/castle-sim/briefs/2026-07-12_k160-mira-mp-attribution-steal.md"
echo "  ~/Desktop/family/research/2026-07-12_k160-abruzzo-barone-diaspora-sprint.md (private)"
echo "David/TipDrop: none"
