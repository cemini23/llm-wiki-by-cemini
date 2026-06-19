#!/usr/bin/env bash
# K123 Phase-0 — daily digest full ingest (1 arXiv)
set -euo pipefail

echo "K123 Phase-0 audits"
echo "==================="

echo "VERITAS project page:"
curl -fsSL -o /dev/null -w "veritas-improvement.github.io HTTP %{http_code}\n" \
  https://veritas-improvement.github.io/ 2>/dev/null || echo "(fetch failed)"

echo "ScholarQuest (pty12345/ScholarQuest):"
gh api repos/pty12345/ScholarQuest --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"

echo ""
echo "Verdicts (2026-06-19):"
echo "  arxiv-2606.18247 (VERITAS)     REFERENCE — no public GitHub repo; steal generator-verifier for poker decide()"
echo "  arxiv-2606.20235 (ScholarQuest) CONDITIONAL-GO — GitHub no LICENSE; eval steal for daily digest"
echo ""
echo "See wiki/sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md"
echo "Brief: agents/devfun-poker-arena/briefs/2026-06-18_k123-verifier-inference-steering.md"
