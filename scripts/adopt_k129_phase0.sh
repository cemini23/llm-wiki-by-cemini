#!/usr/bin/env bash
# K129 Phase-0 — 12 arXiv + 37-URL tool eval docx
set -euo pipefail

echo "K129 Phase-0 audits"
echo "==================="

echo "arXiv cluster (REFERENCE steals — no code repos):"
echo "  2606.23995 EMAgnet              → poker-arena brief (parameter EMA magnet)"
echo "  2606.21975 IRumAI               → poker + gambling-wiki imperfect-info card steal"
echo "  2606.20960 SETE/M-SETE          → wiki-only game-theory (poker equilibrium cluster)"
echo "  2606.23525 SelfCompact          → CCC harness compaction rubric steal"
echo "  2606.22488 SCOPE                → castle-sim symbolic planning steal"
echo "  2606.22757 C-ORCA*              → castle-sim proactive deadlock steal"
echo "  2606.21008 Metanym              → game-dev LLM benchmark reference"
echo "  2606.20785 Fara-1.5             → browser-agent training reference"
echo "  2606.21841 False Summit         → agent harness failure taxonomy"
echo "  2606.21867 ForEx               → verifier / Lean4 eval reference"
echo "  2606.21967 Moral Geometry       → wiki-only Nash-Kantian"
echo "  2606.24386 Line Planning        → wiki-only (weak Cemini hook)"

echo ""
echo "Tool eval license spot-check (gh api):"
for repo in cobusgreyling/loop-engineering kunchenguid/no-mistakes headroomlabs-ai/headroom zanwei/design-dna anthropics/financial-services zhaoxuya520/reverse-skill microsoft/fara; do
  gh api "repos/$repo" --jq '{repo:"'"$repo"'",license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — $repo)"
done

echo ""
echo "Verdicts (2026-06-25):"
echo "  Adopt (6): loop-engineering MIT · no-mistakes MIT · headroom Apache-2.0"
echo "             design-dna MIT · financial-services Apache-2.0 · reverse-skill MIT"
echo "  Steal-from (6): executor · gchq/sleeper · dtsong/sleeper-api-wrapper · sleeper-mini"
echo "                  fantasy-football-wrapped · template-repo"
echo "  Reject/UNAVAILABLE: aggregated on eval source page — no stub farm"
echo ""
echo "Briefs:"
echo "  agents/devfun-poker-arena/briefs/2026-06-25_k129-emagnet-ema-self-play-steal.md"
echo "  agents/devfun-poker-arena/briefs/2026-06-25_k129-irumai-imperfect-info-card-steal.md"
echo "  ../projects/castle-sim/briefs/2026-06-25_k129-scope-corca-planning-steal.md"
echo "  briefs/ccc-2026-06-25_k129-harness-loop-headroom-no-mistakes.md"
echo "  ../projects/CeminiDFS/briefs/2026-06-25_k129-sleeper-api-reference.md"
echo "  cross-wiki: gambling IRumAI · cybersec reverse-skill · image-gen design-dna"
