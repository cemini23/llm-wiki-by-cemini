#!/usr/bin/env bash
# adopt_k147_phase0.sh — Phase-0 metadata for K147 ingest (2026-07-06)
set -euo pipefail
repos=(
  Arthur742Ramos/repo-bootcamp
  BurntSushi/ripgrep
  HoppouAI/OctoBrowser
  ivproduced/SYSAdmin-CoPilot
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at)"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Brief: ../projects/tipdrop-workspace-kit/briefs/2026-07-06_k147-repo-bootcamp-m4-adopt.md"
