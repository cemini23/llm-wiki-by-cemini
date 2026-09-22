#!/usr/bin/env bash
# OSINT K269 Phase-0 — SPDX-confirmed tiny REFERENCE clones only.
# Dual-ID: OSINT K269 = 22 Sep 2026 inbox. gh api 2026-09-22.
# 0 product Integrate GO. SIZE-SKIP / SPDX-null / skill-evolve / CTF = no clone.
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

clone_ref "jev-lexer" "https://github.com/mizchi/jev-lexer.git" "MIT"
clone_ref "jev-test-filter" "https://github.com/mizchi/jev-test-filter.git" "MIT"
clone_ref "open-jev-typed-decision-engine" "https://github.com/intikhab49/open-jev-typed-decision-engine.git" "Apache-2.0"
clone_ref "jev-search" "https://github.com/superagents-lab/jev-search.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "metaevo-ai/harness-zero Apache-2.0 SIZE-SKIP ~21MB FILE entity; no clone"
echo "ryana/jevify SPDX null NO-GO clone"
echo "mizchi/jev-lint MIT ~3.7MB FILE; no skill/lint auto-evolve; skip clone"
echo "safzanpirani/pi-jev-skill-picker MIT FILE; no skill auto-evolve; skip clone"
echo "ferdinandobons/startup-skill MIT FILE; no skill auto-evolve; skip clone"
echo "mmastrac/djev-spark SPDX null NO-GO"
echo "pst2154/Nemotron_Jev SPDX null NO-GO"
echo "FluidInference/FluidUse Apache SIZE-SKIP ~48MB"
echo "gakonst/nanocodex Apache SIZE-SKIP ~197MB"
echo "vercel-labs/json-render Apache FILE; skip clone ~5.8MB"
echo "dorkitude/webctl MIT FILE HITL; jev-browser already exists; skip clone"
echo "noperator/siftrank MIT FILE; skip clone"
echo "can1357/jegrep MIT FILE; skip clone"
echo "mubix/ai-ctf MIT cyber FILE no PoC; no clone"
echo "jkudish/jev-mcp already WIRE; never npx github"
echo "winnow / laya-mlx / NanoJev / jev-browser already prior waves"
echo "=== DONE ==="
echo "0 product Integrate GO. Transkribus sole HTR. Do not swap /route."
echo "No xsp/pm scp. No LIVE Discord. Never auto-arm. Never auto-evolve skills."
