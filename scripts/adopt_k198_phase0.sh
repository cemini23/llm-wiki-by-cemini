#!/usr/bin/env bash
# K198 Phase-0 shallow adopts (<500MB): book-to-skill, agent-governance-toolkit, GeoLibre
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dir="$2"
  if [[ -d "$ADOPT/$dir/.git" ]]; then
    echo "skip $dir (exists)"
    return 0
  fi
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dir"
  du -sh "$ADOPT/$dir"
}
clone virgiliojr94/book-to-skill book-to-skill
clone microsoft/agent-governance-toolkit agent-governance-toolkit
clone opengeos/GeoLibre GeoLibre
echo "K198 Phase-0 done. aisuite already at .local/adopts/aisuite (K195)."
