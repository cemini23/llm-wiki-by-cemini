#!/usr/bin/env bash
# OSINT K242 Phase-0 — budget <500MB new clones (shallow).
# License: .local/reports/license-k242-2026-08-19.md
# Dual-ID: OSINT K242 = this inbox (19 Aug 2026); do not collapse onto
# Trajectory Sentinel / CCC K242 (wiki/concepts/agent-harness-verification-bottleneck.md).
# 0 new runtime Integrate GO. Never trust eval docx SPDX.
set -euo pipefail
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

# Extract / Extract-only / Extract REFERENCE (license-corrected)
clone ibrahimqureshae/mdflux mdflux
clone arxhr007/Aliens_eye Aliens_eye
clone BetterWright/betterwright betterwright
clone ConardLi/easy-agent easy-agent
clone Lakr233/vphone-cli vphone-cli
clone akitaonrails/ai-memory ai-memory
clone guillaumemeyer/watermarks-remover watermarks-remover
clone SquidSec/BloodBash BloodBash   # MIT Extract-only — authorized SharpHound JSON; no PoC

echo "=== SKIP (documented, license-k242-2026-08-19) ==="
echo "deepteam — Apache-2.0 already wiki/entities/tools/deepteam.md (K32 Defer → Extract REFERENCE); skip clone"
echo "omlx — Apache-2.0 already wiki/entities/tools/omlx.md K182 wont_wire; skip clone"
echo "PureMac — MIT Pass, no clone"
echo "headway — Apache-2.0 Context (50–100GB tiles), no clone"
echo "App-Store-Connect-CLI — MIT Watch ~86MB, no iOS SKU, no clone"
echo "autonomous-computer — MIT SIZE-SKIP ~350MB"
echo "cua — MIT SIZE-SKIP ~313MB; optional ultralytics AGPL isolate; Extract pattern only"
echo "text-to-cad — MIT Context 3D, no clone (~135MB); brief preferred"
echo "botdirectory.ai — MIT Context SEO, no clone"
echo "unbound-dashboard — Apache-2.0 Context, no clone"
echo "J-Space-Cognition-Suite — Apache-2.0 Context (abliterated family), no clone"
echo "rybbit — AGPL-3.0 Watch, no clone (~410MB). Do not vendor into Atto"
echo "KrillinAI — GPL-3.0 Watch, no clone"
echo "repowise — AGPL-3.0 Context, no clone"
echo "WireTapper / H.I.V.E / herdrm / treg / EasyCopy / munder-difflin — NOASSERTION, no clone"
echo "PrivFu — BSD-3 Context-no-clone (token-steal PoC)"
echo "elasticsearch — Pass SIZE-SKIP dual non-OSI"
echo "Qwen uncensored MLX — Watch, no HF weights"
echo "aceternity — commercial UI Context, skip Image-gen local wire"
echo "pwneye — camera-hack Context listed-only, no exploit"
echo "Do not copy any skill into ~/.cursor/skills (misevolution HITL)"
echo "=== DONE ==="

NEW=(mdflux Aliens_eye betterwright easy-agent vphone-cli ai-memory watermarks-remover BloodBash)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d"
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1
