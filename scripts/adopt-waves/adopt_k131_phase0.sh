#!/usr/bin/env bash
# K131 Phase-0 — 5 arXiv inbox (ToolBench-X repo only)
set -euo pipefail

echo "K131 Phase-0 audits"
echo "==================="

echo "ToolBench-X repo check:"
gh api repos/Foreverskyou/ToolBench-X \
  --jq '{repo:"Foreverskyou/ToolBench-X",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' \
  2>/dev/null || echo "(gh unavailable — Foreverskyou/ToolBench-X)"

echo ""
echo "Verdicts (2026-06-26):"
echo "  REFERENCE (1): ToolBench-X — NO LICENSE; steal hazard taxonomy only"
echo "  Wiki-only (4): 2606.23913 RLVF · 2606.24099 co-occurrence · 2606.24434 theme-park · 2606.24443 Relaxed NFL (paper steal → poker brief)"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-26_k131-relaxed-nfl-verifier-steal.md"
echo "  briefs/ccc-2026-06-26_k131-toolbench-x-hazard-recovery.md"
