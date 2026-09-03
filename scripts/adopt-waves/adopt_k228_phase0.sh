#!/usr/bin/env bash
# K228 Phase-0 clones (SPDX via gh api; target << 500MB new)
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
# GuruWatcher Integrate
clone 6551Team/opennews-mcp opennews-mcp
# Cyber lab Extract
clone Cjbuilds/Codex-Orchestration Codex-Orchestration
clone DevCop95/bugbounty-lab101 bugbounty-lab101
# CCC Integrate / Watch
clone earendil-works/pi pi-earendil
clone JCodesMore/ai-website-cloner-template ai-website-cloner-template
clone shift-labs-ai/pi-peer pi-peer

echo "=== sizes ==="
du -sh \
  "$ADOPT/opennews-mcp" \
  "$ADOPT/Codex-Orchestration" \
  "$ADOPT/bugbounty-lab101" \
  "$ADOPT/pi-earendil" \
  "$ADOPT/ai-website-cloner-template" \
  "$ADOPT/pi-peer" 2>/dev/null
echo "K228 skip: pdf-inspector already adopted; godoxy NOASSERTION; FUXA/OctoBot/buzz/RustPython size-skip; kimi-k3-in-c Watch skip this batch"
