#!/usr/bin/env bash
# K120 Phase-0 — daily digest full ingest (2 arXiv)
set -euo pipefail

echo "K120 Phase-0 audits"
echo "==================="

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "/tmp/k120-${dir}/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "/tmp/k120-${dir}"
  fi
  gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || true
}

echo "Ensemble RL reproduction package:"
clone_smoke ZheliXiong/Ensemble-RL-through-Classifier-Models

echo ""
echo "TradeMaster data dependency (existing K60 steal-from):"
gh api repos/TradeMaster-NTU/TradeMaster --jq '{license:.license.spdx_id,stars:.stargazers_count}' 2>/dev/null || true

echo ""
echo "Verdicts (2026-06-17):"
echo "  arxiv-2502.17518 (Ensemble RL + classifiers)  CONDITIONAL-GO — MIT repro repo; laptop DJ30 smoke only"
echo "  arxiv-2606.12612 (HPO theory)                REFERENCE — no repo; GRS/optimality-map steal for Riskfolio ladder"
echo ""
echo "See wiki/sources/ and briefs/2026-06-17_k120-*.md"
