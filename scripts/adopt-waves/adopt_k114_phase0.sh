#!/usr/bin/env bash
# K114 Phase-0 — federation wave eval repos (SciConBench, PerspectiveGap, GraphAnything)
set -euo pipefail
AUDIT="${TMPDIR:-/tmp}/k114-phase0-audit"
mkdir -p "$AUDIT"
cd "$AUDIT"

echo "K114 Phase-0 audits (clone smoke)"
echo "================================="

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "$dir/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "$dir"
  fi
  echo "OK clone: $repo"
  gh api "repos/${repo}" --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || true
}

for r in hayoungjungg/SciConBench WhymustIhaveaname/PerspectiveGap InternScience/GraphAnything; do
  clone_smoke "$r"
done

echo ""
echo "Verdicts (2026-06-13):"
echo "  SciConBench       REFERENCE — MIT; 5★; clean-room eval harness; laptop smoke only"
echo "  PerspectiveGap    REFERENCE — MIT; 2★; orchestration prompt benchmark; periodic eval"
echo "  GraphAnything     CONDITIONAL-GO — MIT; 8★; markdown-vault preset vs kb-server gap test"
echo ""
echo "No prod install without operator GO + skill_audit on brief."
