#!/usr/bin/env bash
# K174 Phase-0 — clones under 500MB (user gate this batch)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
CAP_MB=500
mkdir -p "$ADOPTS"
cd "$ADOPTS"
clone() {
  local repo="$1" dir="$2"
  if [[ -d "$dir/.git" ]]; then echo "exists $dir"; du -sh "$dir"; return; fi
  git clone --depth 1 --single-branch "https://github.com/${repo}.git" "$dir"
  mb=$(du -sm "$dir" | awk '{print $1}')
  if (( mb > CAP_MB )); then echo "FAIL $dir ${mb}MB>$CAP_MB"; exit 1; fi
  du -sh "$dir"
}
clone tirth8205/code-review-graph code-review-graph
clone ayghri/i-have-adhd i-have-adhd
echo "SKIP wigolo (AGPL Pass). SKIP ktransformers re-clone (K173). SKIP voicebox Context. NO weight downloads."
