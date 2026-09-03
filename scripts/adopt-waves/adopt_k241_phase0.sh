#!/usr/bin/env bash
# K241 Phase-0 — budget <500MB new clones (shallow). License: .local/reports/license-k241-2026-08-18.md
# Dual-ID: OSINT K241 = this inbox (18 Aug 2026); do not collapse onto CCC K241.
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

# Extract REFERENCE (this batch) — license-corrected
clone google/sam sam
clone llm-as-a-verifier/llm-as-a-verifier llm-as-a-verifier
clone cathrynlavery/diagram-design diagram-design
clone blacklanternsecurity/bbot bbot   # AGPL-3.0 Extract-only — do not vendor into Atto
clone sherlock-project/sherlock sherlock
clone ninoseki/mitaka mitaka

echo "=== SKIP (documented, license-k241-2026-08-18) ==="
echo "PageLM / multica / usertour — NOASSERTION, no clone"
echo "ssh-ai-chat — AGPL Watch, no clone"
echo "codex-plusplus — MIT archived Context, no clone"
echo "DeepSeek-V4-J-Space / movfuscator / GHunt — NOASSERTION, no clone"
echo "PrivFu — BSD-3 Context-no-clone (token-steal PoC)"
echo "HTB cheatsheets — null SPDX, Context only"
echo "traceway — SIZE-SKIP ~514MB (>500)"
echo "redditsfinder — MIT stale 2022, pattern-only, no clone"
echo "LinkScope_Client — AGPL catalog, no clone"
echo "CyberChef already entities/tools/cyberchef.md K149 Context — do not re-tier Integrate"
echo "Do not copy diagram-design into ~/.cursor/skills (misevolution HITL)"
echo "=== DONE ==="

NEW=(sam llm-as-a-verifier diagram-design bbot sherlock mitaka)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d"
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1
