#!/usr/bin/env bash
# OSINT K270 Phase-0 — one SPDX-confirmed REFERENCE clone only.
# Dual-ID: OSINT K270 = 23 Sep 2026 inbox. gh api 2026-09-23.
# 0 product Integrate GO. SPDX-null / size-skip / 404 = no clone.
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone_ref() {
  local name="$1" url="$2" lic="$3"
  if [[ -d "$name" ]]; then
    echo "SKIP exists: $name"
    return 0
  fi
  echo "=== REFERENCE clone: $name ($lic) ==="
  git clone --depth 1 "$url" "$name"
}

clone_ref "cliffcompaction" "https://github.com/nguyenvuthientrang/cliffcompaction.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "modelun SPDX null ~21MB SIZE-SKIP NO-GO; no clone"
echo "agensh GitHub 404 on 2026-09-23; no license to verify; no clone"
echo "airo-mono no clone"
echo "pi no clone"
echo "Kimi-K3 no clone"
echo "=== DONE ==="
echo "0 product Integrate GO. FILE only. Do not swap /route."
echo "No weight download. Never auto-evolve skills. Never npx github:."
echo "No xsp/pm scp. No LIVE Discord. Never auto-arm."
