#!/usr/bin/env bash
# adopt_k163_phase0.sh — Phase-0 for K163 ingest (2026-07-14)
set -euo pipefail
repos=(
  Dicklesworthstone/destructive_command_guard
  Nutlope/hallmark
  chenyme/grok2api
  OpenCut-app/OpenCut
  penpot/penpot
  Shubhamsaboo/awesome-llm-apps
  HenryNdubuaku/maths-cs-ai-compendium
  Kappaemme-git/codex-first-customer-finder-skill
  WillNigri/Agentic-Tool-Optimization
  AIEraDev/Clypra
  Raphire/Win11Debloat
  par274/sharpemu
)
echo "K163 Phase-0 license check"
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "CONDITIONAL-GO: destructive_command_guard — MIT+OpenAI/Anthropic rider (NOASSERTION on GitHub); fail-open; local shell hook OK"
echo "Adopt: hallmark (MIT) — npx skills add nutlope/hallmark"
echo "Integrate TipDrop: codex-first-customer-finder-skill (MIT) — GDPR gate"
echo "Extract: maths-cs-ai-compendium (Apache-2.0); awesome-llm-apps patterns only (Apache-2.0)"
echo "Watch: OpenCut, penpot, Agentic-Tool-Optimization, grok2api (cookie/ToS)"
echo "Pass: Win11Debloat, Clypra, sharpemu GPL-2.0, PHP analyzer cluster"
echo "REFERENCE: arXiv 2607.08199 DR-AS — no install"
echo "David ComfyUI/Fish-Speech: none"
echo "Briefs: pm×2 + xsp (**scp prod**); TipDrop/David×2; poker; CCC; cybersec; gambling; CeminiDFS"
