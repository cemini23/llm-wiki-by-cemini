#!/usr/bin/env bash
# K127 Phase-0 — 3 arXiv + 2 tool eval docx
set -euo pipefail

echo "K127 Phase-0 audits"
echo "==================="

echo "arXiv cluster (no code repos — REFERENCE steals):"
echo "  2606.21013 Agentic Time Machine  REFERENCE → pm-kalshi offline eval harness"
echo "  2606.22688 GARIP                 REFERENCE → poker running-average magnet"
echo "  2606.23449 AOHP                  CONDITIONAL-GO → CCC secure interfaces (AOSP study only)"

echo ""
echo "Tool eval license spot-check:"
gh api repos/sportsdataverse/sportsdataverse-py --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — sportsdataverse-py)"
gh api repos/aohp-os/aohp --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — aohp-os/aohp)"

echo ""
echo "Verdicts (2026-06-23):"
echo "  arxiv-2606.21013 (Agentic TM)           REFERENCE — leakage-filter replay + multi-agent forecast decomposition"
echo "  arxiv-2606.22688 (GARIP)                REFERENCE — running-average magnet vs R-NaD snapshot"
echo "  arxiv-2606.23449 (AOHP)                 CONDITIONAL-GO — Apache-2.0; mobile AOSP, architecture study only"
echo "  Cemini Tool Evaluation Plan (62 URLs)     1 Adopt (sportsdataverse-py MIT), 42 Reject, 16 Reference-only"
echo "  Hugging Face Model Evals (74 URLs)        52 UNAVAILABLE, 18 Reject, 1 Adopt (balatro cards → image-gen), 1 Steal-from (Poker_LORA)"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-23_k127-garip-running-average-self-play-steal.md"
echo "  briefs/pm-2026-06-23_k127-agentic-time-machine-polymarket-eval.md"
echo "  ../projects/CeminiDFS/briefs/2026-06-23_k127-sportsdataverse-py-adopt.md"
echo "  ../projects/Cemini claude code CCC/briefs/2026-06-23_k127-aohp-secure-agent-interfaces-reference.md"
