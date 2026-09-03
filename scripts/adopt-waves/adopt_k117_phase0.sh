#!/usr/bin/env bash
# K117 Phase-0 — daily digest full ingest (2 arXiv; SciConBench backlog close-out)
set -euo pipefail
AUDIT="${TMPDIR:-/tmp}/k117-phase0-audit"
mkdir -p "$AUDIT"
cd "$AUDIT"

echo "K117 Phase-0 audits"
echo "==================="

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "$dir/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "$dir"
  fi
  echo "OK clone: $repo"
  gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || true
}

# SciConBench — K114 backlog; laptop smoke only
clone_smoke hayoungjungg/SciConBench

echo ""
echo "Verdicts (2026-06-15):"
echo "  arxiv-2606.09055 (particle partial-obs control)  REFERENCE — no public code; steal problem framing only"
echo "  arxiv-2606.09478 (regime vol + return pred)      REFERENCE — methodology for equity backtest diagnostics"
echo "  SciConBench                                     REFERENCE — MIT; clean-room eval harness; laptop smoke"
echo ""
echo "No prod installs. See wiki/sources/ and briefs/2026-06-15_k117-*.md"
