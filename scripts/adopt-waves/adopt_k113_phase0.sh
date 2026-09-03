#!/usr/bin/env bash
# K113 Phase-0 — Hermes workspace + SkillClaw + AI-Research-SKILLs + wondelai/skills
set -euo pipefail
AUDIT="${TMPDIR:-/tmp}/k113-phase0-audit"
mkdir -p "$AUDIT"
cd "$AUDIT"

echo "K113 Phase-0 audits (laptop clone smoke)"
echo "========================================"

clone_smoke() {
  local repo="$1"
  local dir="${repo##*/}"
  if [[ ! -d "$dir/.git" ]]; then
    git clone --depth 1 "https://github.com/${repo}.git" "$dir"
  fi
  echo "OK clone: $repo"
}

for r in outsourc-e/hermes-workspace AMAP-ML/SkillClaw Orchestra-Research/AI-Research-SKILLs wondelai/skills; do
  clone_smoke "$r"
done

echo ""
echo "Verdicts (2026-06-12):"
echo "  hermes-workspace     CONDITIONAL-GO — laptop GUI; MIT; 5652★"
echo "  SkillClaw            CONDITIONAL-GO — Hermes skill evolution proxy; MIT; 1880★"
echo "  AI-Research-SKILLs   CONDITIONAL-GO — skill library; skill_audit before use; MIT; 9613★"
echo "  wondelai/skills      CONDITIONAL-GO — SEO/CCC plugin trial; MIT; 1300★"
echo "  all-agentic-arch     Steal-from only — pattern extraction"
echo "  CloddsBot            Steal-from reaffirmed — MIT; WC module 4 reference"
echo ""
echo "Laptop trial 2026-06-12:"
echo "  SkillClaw pip install + --help     PASS"
echo "  SkillClaw doctor hermes            BLOCKER (skillclaw setup; no Hermes)"
echo "  hermes-workspace npm dry-run       PASS (hermes-agent not installed)"
echo "  AI-Research-SKILLs SKILL.md count  98"
echo "Report: .local/reports/k113-laptop-trial-2026-06-12.md"
echo "Done. See wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md"
