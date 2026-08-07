#!/usr/bin/env bash
# K226 Phase-0 clones (SPDX-verified via gh api; target << 500MB new)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  echo "cloning $repo -> $dest"
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
# Atto Integrate
clone semantica-agi/semantica semantica
# Cyber / local-abliterated-lab Integrate + Extract
clone PrimeIntellect-ai/prime-agent prime-agent
clone chenyme/grok2api grok2api
clone denoland/celld celld
# GuruWatcher Extract (AGPL — patterns REFERENCE only; no proprietary fork)
clone 666ghj/MiroFish MiroFish
# CCC / harness Watch + Context
clone mindsdb/anton anton
clone google/skills google-skills
# OSINT Context
clone K2SOsint/Legendary_OSINT Legendary_OSINT

echo "=== sizes ==="
du -sh \
  "$ADOPT/semantica" \
  "$ADOPT/prime-agent" \
  "$ADOPT/grok2api" \
  "$ADOPT/celld" \
  "$ADOPT/MiroFish" \
  "$ADOPT/anton" \
  "$ADOPT/google-skills" \
  "$ADOPT/Legendary_OSINT" 2>/dev/null
echo "K226 NO-GO clone: nduckmink/arkon NOASSERTION; unclebob/swarm-forge NULL; mehrshad-sdtn/CircuitSteer NULL; Significant-Gravitas/AutoGPT NOASSERTION+size; jdx/mise size-skip (~85MB Context-only); marketingskills/witr/sie/pi-llm-wiki already have entities or K225 clones"
