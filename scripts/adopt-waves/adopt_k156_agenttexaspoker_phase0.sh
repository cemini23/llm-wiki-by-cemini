#!/usr/bin/env bash
# adopt_k156_agenttexaspoker_phase0.sh — Phase-0 for K156 AgentTexasPoker (2026-07-15)
set -euo pipefail
gh api repos/XuankunRong/AgentTexasPoker --jq '"\(.full_name) | license=\(.license.spdx_id // "NOASSERTION") | \(.size)KB | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"'
echo "LICENSE file: missing"
echo "Local copy: CCC + gambling raw-sources/foss-evals/AgentTexasPoker (~688KB)"
echo "Verdict: CONDITIONAL-GO — VPIP/PFR risk assay Adopt; code WATCH until SPDX"
echo "HF dataset XuankunRong/AgentTexasPoker — size-check before download"
echo "Briefs:"
echo "  gambling-wiki/briefs/2026-07-15_k156-risk-sensitive-llm-poker-steals.md"
echo "  OSINT agents/devfun-poker-arena/briefs/2026-07-15_k156-agenttexaspoker-risk-spectrum-steal.md"
echo "  CCC briefs/2026-07-15_k156-llm-risk-behaviour-audit-prod.md → scp prod"
