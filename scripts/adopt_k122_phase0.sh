#!/usr/bin/env bash
# K122 Phase-0 — daily digest full ingest (5 inbox: 4 arXiv + one-pager)
set -euo pipefail

echo "K122 Phase-0 audits"
echo "==================="

gh_api() {
  gh api "$1" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable)"
}

echo "MoVerse (Orange-3DV-Team/MoVerse):"
gh_api repos/Orange-3DV-Team/MoVerse

echo ""
echo "dev.fun starter kit (existing steal-from):"
gh_api repos/devfun-org/poker-arena-starter-kit

echo ""
echo "Verdicts (2026-06-18):"
echo "  arxiv-2606.13093 (EFGSAS / SI-CFR)     REFERENCE — no repo; game-theory catalog"
echo "  arxiv-2606.13376 (MoVerse)              REFERENCE — GitHub no LICENSE; weights gated"
echo "  arxiv-2606.13815 (Poker Arena / Raeth)  STEAL-FROM — axis defs + memory ablation; product at poker.raeth.ai"
echo "  arxiv-2606.13840 (MAEAD survey)         REFERENCE — survey only"
echo "  poker-arena-onepager.pdf                INGESTED — operator collateral (LIKELY dup of existing source page)"
echo ""
echo "See wiki/sources/ and agents/devfun-poker-arena/briefs/2026-06-18_k122-*.md"
