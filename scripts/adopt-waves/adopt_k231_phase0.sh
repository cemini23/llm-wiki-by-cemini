#!/usr/bin/env bash
# K231 Phase-0 — budget <500MB new clones (shallow)
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

# Integrate
clone antvis/Infographic Infographic
clone tzachbon/smart-ralph smart-ralph
clone browserbase/stagehand stagehand

# Extract
clone oil-oil/oil-motion oil-motion
clone quickemu-project/quickemu quickemu
clone CyberSunil/LLMVault LLMVault
clone microsoft/flint-chart flint-chart
clone haloydev/haloy haloy
clone duolahypercho/codex-router codex-router
clone holaboss-ai/holaOS holaOS
clone beenuar/AiSOC AiSOC

# Watch shallow (small)
clone neural-maze/realtime-phone-agents-course realtime-phone-agents-course

echo "=== SKIP (documented) ==="
echo "Kernel-Exploit-Dojo — NO_LICENSE + ~1.8GB"
echo "OptMem — NO_LICENSE"
echo "harvey-labs — SIZE-SKIP ~2.1GB"
echo "manim / daily_stock_analysis — size-hold / no near-term fit"
echo "diagram-design — already K230"
echo "=== DONE ==="
du -sh Infographic smart-ralph stagehand oil-motion quickemu LLMVault flint-chart haloy codex-router holaOS AiSOC realtime-phone-agents-course 2>/dev/null
du -ch Infographic smart-ralph stagehand oil-motion quickemu LLMVault flint-chart haloy codex-router holaOS AiSOC realtime-phone-agents-course 2>/dev/null | tail -1
