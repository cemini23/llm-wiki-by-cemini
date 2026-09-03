#!/usr/bin/env bash
# K240 Phase-0 — budget <500MB new clones (shallow). License: .local/reports/license-k240-2026-08-17.md
# Dual-ID: OSINT K240 = this inbox; CCC K240 = MixedComplementarityProblems.jl robotics (old).
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

# Extract REFERENCE (this batch)
clone emeraldpay/dshackle dshackle
clone Anionex/dsh-vision-toolkit dsh-vision-toolkit
clone NanmiCoder/dsh-agent-teams dsh-agent-teams
clone RockwellShah/filekey filekey   # GPL-3.0 Extract-only — do not vendor into Atto
clone Futuresis/replay-agent-recorder replay-agent-recorder
clone Kelvin-Coffee/MettleBench MettleBench
clone Alexyskoutnev/TWIN-ARC-AGI-3 TWIN-ARC-AGI-3

echo "=== SKIP (documented, license-k240-2026-08-17) ==="
echo "usertour / corsair — NOASSERTION, no clone"
echo "dsh-anchored-standard — NOASSERTION; dsh-routing-suite — null SPDX"
echo "Qwen GGUF / Uncensored FP8 — HF weights skip"
echo "claude-cookbooks — Extract notebook pattern only (210MB, no full clone)"
echo "unsloth — skip (Transkribus sole HTR)"
echo "jmagly/aiwg — keep K239 Context, do not re-tier"
echo "daily_stock_analysis — K231 size-hold"
echo "traceway — SIZE-SKIP >500MB"
echo "HackTheBox-All-Cheatsheets — null SPDX, Context only"
echo "ftinj / GAMESS — policy only (CCC K284)"
echo "Do not replace PATH claude-ds with any dsh-desktop / awesome-dsh fork"
echo "=== DONE ==="

NEW=(dshackle dsh-vision-toolkit dsh-agent-teams filekey replay-agent-recorder MettleBench TWIN-ARC-AGI-3)
for d in "${NEW[@]}"; do
  [ -d "$d" ] && du -sh "$d"
done
du -ch "${NEW[@]}" 2>/dev/null | tail -1
