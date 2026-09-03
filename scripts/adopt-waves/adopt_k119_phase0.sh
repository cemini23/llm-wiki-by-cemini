#!/usr/bin/env bash
# K119 Phase-0 — Tier-2 sweep ingest (3 arXiv)
set -euo pipefail

echo "K119 Phase-0 audits"
echo "==================="

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "/tmp/k119-${dir}/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "/tmp/k119-${dir}"
  fi
  gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || true
}

clone_smoke opensquilla/claw-swe-bench

echo ""
echo "Verdicts (2026-06-16):"
echo "  arxiv-2606.12344 (Claw-SWE-Bench)     CONDITIONAL-GO — MIT; laptop Lite-80 smoke only"
echo "  arxiv-2606.06324 (HarnessFix)         REFERENCE — no public repo; steal HTIR/operator discipline"
echo "  arxiv-2606.08228 (PRFS)               REFERENCE — Zenodo dataset; methodology for filter audits"
echo ""
echo "See wiki/sources/ and briefs/2026-06-16_k119-*.md"
