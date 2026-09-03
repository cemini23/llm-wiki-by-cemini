#!/usr/bin/env bash
# K143 Phase-0 — runtime / Fable harness batch
set -euo pipefail

echo "K143 Phase-0 audits"
echo "==================="

repos=(
  breferrari/obsidian-mind
  headroomlabs-ai/headroom
  open-free-llm-api/awesome-freellm-apis
  cheahjs/free-llm-api-resources
  asgeirtj/system_prompts_leaks
  VoidLight00/deo-harness
  Supereldecoder/claude-opus48-context-packer
  keirsalterego/jailbreak-fable
  Rylaa/fable5-orchestrator
  nagarjuna-msr/fable-god-mode
  kpab/claude-fable-5-skills
)

for repo in "${repos[@]}"; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at,open_issues:.open_issues_count,archived:.archived}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-07-04):"
echo "  Adopt reaffirmed (1): headroomlabs-ai/headroom Apache-2.0 — optional OSINT/CCC context compression; no prod path."
echo "  Steal-from (1 promoted): breferrari/obsidian-mind MIT — vault-manifest/QMD/hook-test patterns; no TipDrop/David install brief."
echo "  Reference/aggregate: free LLM API indexes + Fable harness repos; keep in source page unless CCC opens a concrete integration."
echo "  Reject/unavailable: generic primers, unavailable repos, broad GodMode-style packages without safe Cemini surface."
echo ""
echo "Brief routing: no cemini-prod scp; no David/TipDrop adoption brief from this batch."
