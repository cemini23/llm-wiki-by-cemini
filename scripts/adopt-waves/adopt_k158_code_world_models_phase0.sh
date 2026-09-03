#!/usr/bin/env bash
# adopt_k158_code_world_models_phase0.sh — Phase-0 for K158 CWM play-adequacy (2026-07-17)
set -euo pipefail
gh api repos/JaviMaligno/code-world-models --jq '"\(.full_name) | license=\(.license.spdx_id // "NOASSERTION") | \(.size)KB | \(.stargazers_count)★ | pushed \(.pushed_at[0:10])"'
echo "LICENSE file: missing"
echo "Local copy: CCC + gambling raw-sources/foss-evals/code-world-models (~4.8MB)"
echo "Verdict: CONDITIONAL-GO — play-adequacy methodology Adopt; code WATCH until SPDX"
echo "Briefs:"
echo "  gambling-wiki/briefs/2026-07-17_k158-play-adequacy-cwm-steals.md"
echo "  OSINT agents/devfun-poker-arena/briefs/2026-07-17_k158-play-adequacy-gate-steal.md"
echo "  CCC briefs/2026-07-17_k158-play-adequacy-world-model-eval-prod.md → scp prod"
