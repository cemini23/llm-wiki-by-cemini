#!/usr/bin/env bash
# K195 Phase-0 local adopts (<500MB budget). Idempotent shallow clones.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="$ROOT/.local/adopts"
mkdir -p "$ADOPTS"
clone() {
  local repo="$1" dir="$2"
  if [[ -d "$ADOPTS/$dir/.git" ]]; then
    echo "OK exists $dir"
    return 0
  fi
  git clone --depth 1 "https://github.com/$repo.git" "$ADOPTS/$dir"
}
clone citrolabs/ego-lite ego-lite
clone andrewyng/aisuite aisuite
clone affaan-m/ECC ecc
# omlx already present from K182 — skip reclone
echo "SKIP omlx (K182 present)"
echo "WATCH-only (no clone): CoreBunch/Instatic (~185MB Watch)"
echo "Extract-only (no clone this batch): visa/visa-vulnerability-agentic-harness (Apache-2.0 file; air-gap before any run)"
du -sh "$ADOPTS" "$ADOPTS"/ego-lite "$ADOPTS"/aisuite "$ADOPTS"/ecc "$ADOPTS"/omlx 2>/dev/null || true
