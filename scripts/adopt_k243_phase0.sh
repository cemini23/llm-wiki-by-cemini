#!/usr/bin/env bash
# OSINT K243 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# License: .local/reports/license-k243-2026-08-20.md
# Dual-ID: OSINT K243 = this inbox (20 Aug 2026); do not collapse onto
# ACEM / CCC K243 (agentic cost estimation vocabulary in
# cemin-phase1-policy-wires.mdc). Resolve by file+wiki / arXiv / brief path.
# 0 new runtime Integrate GO. Never trust eval docx SPDX.
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone() {
  local slug="$1" dest="$2"
  if [ -d "$dest/.git" ]; then echo "HAVE $dest"; du -sh "$dest"; return; fi
  echo "CLONE $slug -> $dest"
  git clone --depth 1 "https://github.com/${slug}.git" "$dest"
  du -sh "$dest"
}

# Extract clones (license-corrected from license-k243-2026-08-20.md)
clone QuentinFuxa/WhisperLiveKit WhisperLiveKit        # Apache-2.0 STT; not HTR; no Barone audio
clone General-Legal/legal-templates legal-templates    # CC0-1.0; HITL lawyer review
clone CopilotKit/openbot openbot                        # MIT CEL pre-action; no CopilotKit cloud
clone 514-labs/dnsglobe dnsglobe                        # MIT
clone m1ckc3s/nullframe nullframe                       # MIT
clone ErezShahaf/Lore Lore                              # MIT Atto narrative schemas; no living-person vitals
clone mahlernim/google-timeline-visualizer google-timeline-visualizer  # MIT Atto maps; no Barone coords
clone santifer/career-ops career-ops                    # MIT GW Playwright/claim ingest
clone Tencent/AI-Infra-Guard AI-Infra-Guard             # Apache-2.0 cyber lab REFERENCE
clone spade-rl/spade spade                              # MIT poker Arena REFERENCE

echo "=== SKIP (documented, license-k243-2026-08-20.md) ==="
echo "ai-memory — MIT HAVE from K242 .local/adopts/ai-memory; skip re-clone"
echo "MoneyPrinterTurbo — MIT SIZE-SKIP ~536MB (image-gen/SEO brief only)"
echo "vstorm-co/full-stack-ai-agent-template — MIT SIZE-SKIP ~255MB + Stripe HITL"
echo "dory / picosnitch — GPL-3.0 Extract-only, no clone"
echo "openwolf / Clone-Wars / OpenViking / plane — AGPL-3.0 no clone"
echo "OpenOutreach / modular / braindump-butler / copilot-discord-bot — NOASSERTION/null, no clone"
echo "SemaPLC / Eureka — NOASSERTION/null SPDX, no clone (CCC OOD wont_wire / policy only)"
echo "Do not copy any skill into ~/.cursor/skills (misevolution HITL)"
echo "=== DONE ==="

NEW=(WhisperLiveKit legal-templates openbot dnsglobe nullframe Lore google-timeline-visualizer career-ops AI-Infra-Guard spade)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d"
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1
