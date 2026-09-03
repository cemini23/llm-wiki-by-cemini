#!/usr/bin/env bash
# OSINT K247 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K247 = 26 Aug 2026 inbox (8 arXiv + eval docx + 5 newsletters).
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

# arXiv GO REFERENCE (CCC K313/K314 policy_wired)
clone ServiceNow/StarHarness StarHarness
clone Gen-Verse/Recuris Recuris

# Eval Extract/Integrate — REFERENCE shelf only (Atto/GuruWatcher briefs)
clone tobi/walgit walgit
clone tt-a1i/archify archify
clone DietrichGebert/ponytail ponytail
clone ConardLi/garden-skills garden-skills
clone laude-institute/headlong headlong
clone marc-shade/world-intel-mcp world-intel-mcp

# browser-use — size gate (~check before clone)
if [ ! -d browser-use/.git ]; then
  SZ=$(gh api repos/browser-use/browser-use -q .size 2>/dev/null || echo 999999)
  if [ "${SZ:-999999}" -lt 50000 ]; then
    clone browser-use/browser-use browser-use
  else
    echo "SKIP browser-use size=${SZ}KB — README/docs only"
  fi
else
  echo "HAVE browser-use"; du -sh browser-use
fi

echo "=== SKIP (documented) ==="
echo "AgriciDaniel/claude-obsidian — source page exists; eval URL duplicate"
echo "b-nnett/grok-bot-0.18-reconstructed — Pass tier"
echo "ln-dev7/circle — Pass tier"
echo "freestylefly/awesome-gpt-image-2 — Extract prompt catalog; no clone (NOT FOUND license in eval)"
echo "basecamp/omarchy — Context only"
echo "marin-community/marin — Watch; TPU cluster OOD"
echo "ADScanPro/Claude-AD — Watch; AD lab"
echo "portbuster1337/Atlas — Watch; cyber scope"
echo "0xor0ne/awesome-list — Context catalog"
echo "=== DONE ==="

NEW=(StarHarness Recuris walgit archify ponytail garden-skills headlong world-intel-mcp)
[ -d browser-use/.git ] && NEW+=(browser-use)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d" 2>/dev/null || true
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1 || true
