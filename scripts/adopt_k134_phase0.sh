#!/usr/bin/env bash
# K134 Phase-0 — GitHub eval docx (20 URLs) + arXiv 2606.26294 (RQGM reference)
set -euo pipefail

echo "K134 Phase-0 audits"
echo "==================="

echo "Adopt / Steal license spot-check:"
for repo in vercel-labs/deepsec mattpocock/skills DeusData/codebase-memory-mcp Panniantong/Agent-Reach ZhuLinsen/daily_stock_analysis mukul975/Anthropic-Cybersecurity-Skills vibheksoni/stealth-browser-mcp; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at,issues:.open_issues_count}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-29):"
echo "  Adopt GO (2): vercel-labs/deepsec Apache-2.0 · mukul975/Anthropic-Cybersecurity-Skills Apache-2.0"
echo "  CONDITIONAL-GO (2): DeusData/codebase-memory-mcp MIT (binary trust) · Panniantong/Agent-Reach MIT (ToS/cookies)"
echo "  Steal-from (2): ZhuLinsen/daily_stock_analysis MIT (xsp GHA patterns) · vibheksoni/stealth-browser-mcp MIT (browser overlap)"
echo "  Reaffirm Adopt: mattpocock/skills MIT (K126 entity)"
echo "  REFERENCE paper: arXiv 2606.26294 RQGM — no code install"
echo "  Reject aggregated (6): FluidVoice GPL · SimpleX AGPL · OpenMontage AGPL · Metabase AGPL · system-design-101 CC-BY-NC · …"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-29_k134-rqgm-co-evolving-evaluator-steal.md"
echo "  briefs/ccc-2026-06-29_k134-codebase-memory-mcp-adopt.md"
echo "  briefs/osint-2026-06-29_k134-agent-reach-conditional.md"
echo "  briefs/cybersec-2026-06-29_k134-deepsec-adopt.md"
echo "  briefs/xsp-2026-06-29_k134-daily-stock-analysis-steal.md"
