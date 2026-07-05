#!/usr/bin/env bash
# adopt_k146_phase0.sh — Phase-0 metadata for K146 ingest (2026-07-05)
set -euo pipefail
repos=(
  Leonxlnx/taste-skill
  gastownhall/gastown
  brightdata/brightdata-mcp
  bytebase/dbhub
  firecrawl/firecrawl-mcp-server
  CoplayDev/unity-mcp
  tavily-ai/tavily-mcp
  ihor-sokoliuk/mcp-searxng
  sunriseapps/imagesorcery-mcp
  huggingface/hf-mcp-server
  snyk/studio-mcp
  ChromeDevTools/chrome-devtools-mcp
  oraios/serena
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at) | archived=\(.archived)"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Brief targets:"
echo "  tipdrop-workspace-kit/briefs/2026-07-05_k146-gastown-agent-handoff-adopt.md"
echo "  tipdrop-workspace-kit/briefs/2026-07-05_k146-taste-skill-ui-adopt.md"
echo "  tipdrop-workspace-kit/briefs/2026-07-05_k146-marketing-loops-steal.md"
echo "  ../projects/CeminiDFS/briefs/2026-07-05_k146-fetch-mcp-stack-adopt.md"
echo "  ../projects/Game Dev wiki/briefs/2026-07-05_k146-unity-mcp-adopt.md"
echo "  agents/devfun-poker-arena/briefs/2026-07-05_k146-substrate-steerability-steal.md"
