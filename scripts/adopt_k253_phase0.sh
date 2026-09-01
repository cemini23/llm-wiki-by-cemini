#!/usr/bin/env bash
# OSINT K253 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K253 = 1 Sep 2026 inbox (8 arXiv + 8 newsletters).
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone_ref() {
  local dir="$1" repo="$2"
  if [[ -d "$dir/.git" ]]; then
    echo "SKIP clone (exists): $dir"
    return 0
  fi
  echo "==> clone $repo -> $dir"
  git clone --depth 1 "$repo" "$dir"
}

# AutoSciRub — MIT, ~2.5MB (arXiv 2608.31076)
clone_ref AutoSciRub https://github.com/zjunlp/AutoSciRub.git

echo "=== SKIP (documented) ==="
echo "2608.31100 S3Gym — no public SPDX repo at Phase-0"
echo "2608.31111 Aspire — no public SPDX repo at Phase-0"
echo "2608.31128 DIASENTINEL — clinical OOD; auditable MAS pattern only; wont_wire runtime"
echo "2608.29025 deep hedging — quant paper only"
echo "2608.30867 neural calibration — quant paper only"
echo "2608.29806/29807 physics — OOD stub only"
echo "=== DONE — 1 REFERENCE clone (AutoSciRub MIT) ==="
