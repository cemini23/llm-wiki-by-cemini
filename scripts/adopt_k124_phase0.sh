#!/usr/bin/env bash
# K124 Phase-0 — daily digest full ingest (4 arXiv)
set -euo pipefail

echo "K124 Phase-0 audits"
echo "==================="

echo "Trainee-to-Trainer (LARK-AI-Lab/Trainee-to-Trainer):"
gh api repos/LARK-AI-Lab/Trainee-to-Trainer --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"

echo "Qwen-RobotNav (QwenLM/Qwen-RobotNav):"
gh api repos/QwenLM/Qwen-RobotNav --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(404 or gh unavailable)"

echo ""
echo "Verdicts (2026-06-20):"
echo "  arxiv-2606.16139 (team zero-sum)  REFERENCE — PPAD theory; no repo"
echo "  arxiv-2606.17682 (Trainee-to-Trainer) CONDITIONAL-GO — NOASSERTION license; env-engineer pattern steal"
echo "  arxiv-2606.18112 (Qwen-RobotNav)  REFERENCE — repo 404; memory-interface steal for castle-sim"
echo "  arxiv-2606.19308 (MAFP)           REFERENCE — no repo; fictitious-play steal for poker offline charts"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-20_k124-mafp-fictitious-play-steal.md"
echo "  ../projects/castle-sim/briefs/2026-06-20_k124-robotnav-playtest-memory-steal.md"
