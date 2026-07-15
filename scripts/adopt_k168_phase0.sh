#!/usr/bin/env bash
# adopt_k168_phase0.sh — Phase-0 for K168 tool-eval (2026-07-15)
set -euo pipefail
echo "K168 Phase-0"
for repo in PrismML-Eng/Bonsai-demo middyjs/middy nodejs/undici stoplightio/prism espanso/espanso fastify/fastify strawberry-graphql/strawberry; do
  gh api "repos/$repo" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | size_kb=\(.size)"' 2>/dev/null || true
done
echo "---"
echo "Integrate: middy (MIT TipDrop); espanso (GPL-3 personal family-tree)"
echo "Extract: Bonsai-demo (Apache xsp patterns); undici (MIT xsp); prism (Apache TipDrop)"
echo "Watch: fastify; strawberry"
echo "Local clones <500MB: Bonsai + prism (+ optional middy). No ComfyUI. No YimMenu."
echo "Briefs: xsp (**scp**); TipDrop/David; CCC; cybersec; family private; poker no-fit"
