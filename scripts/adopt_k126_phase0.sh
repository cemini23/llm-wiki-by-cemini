#!/usr/bin/env bash
# K126 Phase-0 — links.docx tool eval (146 URLs) + arXiv 2606.20495
set -euo pipefail

echo "K126 Phase-0 audits"
echo "==================="

echo "Continuum robots (2606.20495):"
echo "  No code repo — REFERENCE castle-sim pathfinding steal only"

echo ""
echo "Tool eval license spot-check (Adopt / Steal-from cluster):"
gh api repos/nvidia/skills --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — nvidia/skills)"
gh api repos/mattpocock/skills --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — mattpocock/skills)"
gh api repos/NousResearch/hermes-agent --jq '{license:.license.spdx_id,stars:.stargazers_count,pushed:.pushed_at}' 2>/dev/null || echo "(gh unavailable — hermes-agent)"
gh api repos/alchaincyf/nuwa-skill --jq '{license:.license.spdx_id,stars:.stargazers_count}' 2>/dev/null || echo "(gh unavailable — nuwa-skill)"

echo ""
echo "Verdicts (2026-06-22):"
echo "  arxiv-2606.20495 (continuum robots)     REFERENCE — AHP+GA path diversity → castle-sim"
echo "  links.docx (146 URLs)                 deep-read — table format collapsed; tiers from Tier: field"
echo "  nvidia/skills                         CONDITIONAL-GO — Apache-2.0 AND CC-BY-4.0 (NOT MIT as docx claimed)"
echo "  mattpocock/skills                     ADOPT — MIT confirmed"
echo "  NousResearch/hermes-agent             STEAL-FROM — MIT; runtime too heavy for prod"
echo "  ClarusC64 NFL coherence suite (×10)   STEAL-FROM — MIT HF cards; clean-room in CeminiDFS"
echo "  kuhn-poker / Spiral-Kuhn SFT          REFERENCE — NO LICENSE on HF; no training"
echo ""
echo "Briefs:"
echo "  ../projects/CeminiDFS/briefs/2026-06-22_k126-nfl-coherence-risk-steal.md"
echo "  ../projects/castle-sim/briefs/2026-06-22_k126-continuum-robot-path-planning-steal.md"
echo "  agents/devfun-poker-arena/briefs/2026-06-22_k126-kuhn-poker-sft-reference.md"
echo "  ../projects/Cemini claude code CCC/briefs/2026-06-22_k126-nvidia-mattpocock-skills-adopt.md"
