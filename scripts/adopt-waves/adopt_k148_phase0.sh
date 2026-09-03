#!/usr/bin/env bash
# adopt_k148_phase0.sh — Phase-0 metadata for K148 ingest (2026-07-07)
set -euo pipefail
repos=(
  tradingview/lightweight-charts
  ccxt/ccxt
  hyperliquid-dex/hyperliquid-python-sdk
  iOfficeAI/OfficeCLI
  bradautomates/claude-video
  AhmedOsman101/commit-sage-cli
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at)"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Briefs: TipDrop lightweight-charts; xsp ccxt+HL SDK; poker claude-video"
