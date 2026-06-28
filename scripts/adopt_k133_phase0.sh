#!/usr/bin/env bash
# K133 Phase-0 — 3 tool-eval docx + Karpathy field notes PNG
set -euo pipefail

echo "K133 Phase-0 audits"
echo "==================="

echo "Adopt / Steal license spot-check:"
for repo in phields/unusualwhales-mcp unusual-whales/unusual-whales-official-mcp AdoNunes/DiscordAlertsTrader danwagnerco/mcp-server-unusualwhales icharm/StockTips lijx10/uwb-localization; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-28):"
echo "  Adopt: phields/unusualwhales-mcp MIT — TipDrop MCP eval"
echo "  Reference: unusual-whales/unusual-whales-official-mcp MIT — vendor canonical MCP"
echo "  Steal-from: AdoNunes/DiscordAlertsTrader BSD-3-Clause — parse patterns only"
echo "  Reference-only: danwagnerco/mcp-server-unusualwhales (no LICENSE on gh)"
echo "  Reject: airnub/unusualwhales-api-client · icharm/StockTips · Ramzi-Sah self-bot · lijx10/uwb-localization (wrong domain)"
echo "  UNAVAILABLE: 33 dead DiscordMonitor/tipdrop/UW fork URLs — aggregated on source pages"
echo ""
echo "Briefs:"
echo "  tipdrop-workspace-kit/briefs/2026-06-28_k133-unusualwhales-mcp-adopt.md"
echo "  tipdrop-workspace-kit/briefs/2026-06-28_k133-discord-alerts-trader-steal.md"
echo "  tipdrop-workspace-kit/briefs/2026-06-28_k133-form4-sp500-crossref-steal.md"
echo "  briefs/ccc-2026-06-28_k133-openclaw-dm-pairing-cybersec-steal.md"
echo "  briefs/game-dev-2026-06-28_k133-uwb-ekf-pathfinding-reference.md"
