#!/usr/bin/env bash
# K128 Phase-0 — 3 arXiv + Metaplan tool eval docx
set -euo pipefail

echo "K128 Phase-0 audits"
echo "==================="

echo "arXiv cluster (no code repos — REFERENCE steals):"
echo "  2606.23032 IPO Finance Agent     REFERENCE → automated rubric eval pattern (wiki-only)"
echo "  2606.23070 CL-AMM dynamic fees   REFERENCE → pm-kalshi LP toxicity gate brief"
echo "  2606.24019 Square-root law AAPL  REFERENCE → pm-kalshi CLOB √Q/V sizing brief"

echo ""
echo "Tool eval license spot-check:"
gh api repos/blueburncz/BBMOD --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — BBMOD)"
gh api repos/fovane/yuspec-gamedev-ai --jq '{license:.license.spdx_id,stars:.stargazers_count}' 2>/dev/null || echo "(gh unavailable — yuspec)"
gh api repos/Setfive/fanduel-api --jq '{license:.license.spdx_id,stars:.stargazers_count}' 2>/dev/null || echo "(gh unavailable — fanduel-api)"
gh api repos/DimaKudosh/pydfs-lineup-optimizer --jq '{license:.license.spdx_id,stars:.stargazers_count}' 2>/dev/null || echo "(gh unavailable — pydfs)"

echo ""
echo "Verdicts (2026-06-24):"
echo "  arxiv-2606.23032 (IPO Finance Agent)     REFERENCE — rubric evaluator-optimizer; no prod brief"
echo "  arxiv-2606.23070 (CL-AMM LVR)            REFERENCE — dynamic fee / toxicity steal → pm brief"
echo "  arxiv-2606.24019 (SRL AAPL)              REFERENCE — √Q/V clip sizing → pm brief"
echo "  Tool Eval Metaplan (81 URLs)               1 Adopt BBMOD MIT (game-dev only); NO-GO castle-sim Godot"
echo "                                            4 Steal-from; 3 Defer LongShu MLX; CeminiDFS duplicates → Reference-only"
echo ""
echo "Briefs:"
echo "  briefs/pm-2026-06-24_k128-cl-amm-lvr-dynamic-fees-steal.md"
echo "  briefs/pm-2026-06-24_k128-square-root-law-clob-sizing.md"
echo "  @game-dev-wiki/briefs/2026-06-24_k128-bbmod-gamemaker-3d-reference.md (cross-wiki)"
