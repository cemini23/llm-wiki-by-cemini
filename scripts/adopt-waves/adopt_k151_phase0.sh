#!/usr/bin/env bash
# adopt_k151_phase0.sh — Phase-0 metadata for K151 ingest (2026-07-09)
set -euo pipefail
repos=(
  unclecode/crawl4ai
  huxingyi/autoremesher
  kyutai-labs/pocket-tts
  wavetermdev/waveterm
  muratcankoylan/Agent-Skills-for-Context-Engineering
  Nitrode-Research/GameEngineBench
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at)"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Integrate: crawl4ai (Apache-2.0, reaffirm Wave 5.1) → OSINT ingest + MCP"
echo "Extract: autoremesher (MIT) → castle-sim mesh pipeline"
echo "Watch: pocket-tts (MIT) → castle-sim NPC audio; waveterm (Apache-2.0) → TipDrop/David ops"
echo "Reaffirm: Agent-Skills-for-Context-Engineering (MIT) — K149 overlap"
echo "Context: GameEngineBench repo (NOASSERTION) — cite paper + Nitrode-Research/GitHub"
