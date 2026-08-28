#!/usr/bin/env bash
# OSINT K248 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K248 = 28 Aug 2026 inbox (8 arXiv + 17 newsletters + eval docx).
# 0 new runtime Integrate GO. Never trust eval docx SPDX — verify via gh api.
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

# Eval Extract REFERENCE (Atto / CCC / image-gen briefs)
clone bilawalsidhu/gods-eye-view gods-eye-view
clone abi/screenshot-to-code screenshot-to-code
clone Merit-Systems/OpenInstinct OpenInstinct
clone segfault42/heliosgen heliosgen
clone tashfeenahmed/freellmapi freellmapi

echo "=== SKIP (documented) ==="
echo "calesthio/OpenMontage — AGPL-3.0; Extract out-of-process only; no clone (76MB)"
echo "ServiceNow/StarHarness — K247 shelf; arXiv 27311 is follow-on paper not re-clone"
echo "DietrichGebert/ponytail / laude-institute/headlong / marc-shade/world-intel-mcp — K247 shelf"
echo "NationalSecurityAgency/ghidra — cyber REFERENCE; operator install separate"
echo "marin-community/marin — Watch OOD TPU"
echo "google/googletest — test harness vocab only"
echo "RedEvoAgent 2608.27439 — no public SPDX repo; policy K324 Cybersec-primary"
echo "2608.25995 sympatric speciation — biology OOD stub"
echo "=== DONE ==="

NEW=(gods-eye-view screenshot-to-code OpenInstinct heliosgen freellmapi)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d" 2>/dev/null || true
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1 || true
