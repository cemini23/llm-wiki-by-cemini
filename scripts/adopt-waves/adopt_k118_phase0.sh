#!/usr/bin/env bash
# K118 Phase-0 — daily digest full ingest (4 arXiv)
set -euo pipefail
AUDIT="${TMPDIR:-/tmp}/k118-phase0-audit"
mkdir -p "$AUDIT"
cd "$AUDIT"

echo "K118 Phase-0 audits"
echo "==================="

check_repo() {
  local repo="$1"
  if gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null; then
    echo "OK metadata: $repo"
  else
    echo "MISSING: $repo (404 or private — paper-only REFERENCE)"
  fi
}

# OrchRM — cited in 2606.13598; not published at ingest time
check_repo Wang-ML-Lab/OrchRM

echo ""
echo "Verdicts (2026-06-16):"
echo "  arxiv-2606.11798 (DPG time-inconsistent equilibrium)  REFERENCE — no public code; control-theory framing only"
echo "  arxiv-2606.11869 (Agents All the Way Down)          REFERENCE — methodology paper; steal P4/P5 patterns"
echo "  arxiv-2606.13598 (Orch-RM)                          REFERENCE — repo 404; re-audit when Wang-ML-Lab/OrchRM lands"
echo "  arxiv-2606.13822 (tokenized FI admissibility)       REFERENCE — empirical measurement; no code install"
echo ""
echo "No prod installs. See wiki/sources/ and briefs/2026-06-16_k118-*.md"
