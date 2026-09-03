#!/usr/bin/env bash
# K132 Phase-0 — Tool Evaluation and Routing Plan.docx + 2 arXiv
set -euo pipefail

echo "K132 Phase-0 audits"
echo "==================="

echo "Adopt / Steal license spot-check:"
for repo in garrytan/gbrain colbymchenry/codegraph thedotmack/claude-mem screenpipe/screenpipe getzep/graphiti kunchenguid/no-mistakes NousResearch/hermes-agent NVIDIA/NemoClaw farion1231/cc-switch firecrawl/firecrawl; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-27):"
echo "  Adopt (2 new stubs): graphiti Apache-2.0 · no-mistakes MIT (K129 reaffirmed)"
echo "  CONFIRMED existing: codegraph MIT · claude-mem Apache-2.0"
echo "  CONDITIONAL-GO: screenpipe NOASSERTION — manual LICENSE read before install"
echo "  Re-eval spike: gbrain MIT — entity RETIRED 2026-05-18; pattern steal only"
echo "  Steal-from: hermes-agent curator · NemoClaw Apache-2.0 · cc-switch MIT"
echo "  Reject: firecrawl AGPL-3.0 · facebook/hermes keyword collision · Hermes Desktop/WebUI aggregated"
echo ""
echo "Briefs:"
echo "  briefs/ccc-2026-06-27_k132-hermes-curator-skill-prune-steal.md"
echo "  briefs/ccc-2026-06-27_k132-gbrain-hybrid-search-spike.md"
echo "  briefs/ccc-2026-06-27_k132-graphiti-temporal-kg-spike.md"
