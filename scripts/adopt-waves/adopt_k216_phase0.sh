#!/usr/bin/env bash
# K216 Phase-0 clones (SPDX-verified Extract/Integrate; total << 500MB)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
clone tmcw/gedcom gedcom
clone sodejm/AncestryLLM AncestryLLM
clone davidondrej/skills davidondrej-skills
clone google/magika magika
clone FamilySearch/gedcomx gedcomx
clone FamilySearch/GEDCOM FamilySearch-GEDCOM
clone github/gh-stack gh-stack
clone bootandy/dust dust
clone bensadeh/tailspin tailspin
clone wavetermdev/waveterm waveterm
clone openaddresses/openaddresses openaddresses
du -sh "$ADOPT"/*

clone rclone/rclone rclone
clone APIs-guru/openapi-directory openapi-directory
# PastPaths skipped: null SPDX + ~869MB
du -sh "$ADOPT"/*
