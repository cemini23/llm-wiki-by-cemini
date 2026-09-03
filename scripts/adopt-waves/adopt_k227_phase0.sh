#!/usr/bin/env bash
# K227 Phase-0 clones (SPDX via gh api; target << 500MB new)
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
# CCC Integrate
clone rsmdt/the-startup the-startup
# Atto FIND Extract (sherlock MIT; gosearch GPL isolate)
clone sherlock-project/sherlock sherlock
clone ibnaleem/gosearch gosearch
# Watch REFERENCE (GPL — patterns only)
clone adithya-s-k/omniparse omniparse

echo "=== sizes ==="
du -sh \
  "$ADOPT/the-startup" \
  "$ADOPT/sherlock" \
  "$ADOPT/gosearch" \
  "$ADOPT/omniparse" 2>/dev/null
echo "K227 NO-GO/skip: CyberStrike-OffSec-35B HF model (no GGUF download); gosearch/omniparse GPL isolate; realworld NOASSERTION Pass; flutter_roadmap Pass; UNAVAILABLE URLs skipped"
