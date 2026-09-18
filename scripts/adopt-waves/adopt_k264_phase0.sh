#!/usr/bin/env bash
# OSINT K264 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K264 = 18 Sep 2026 inbox (1 eval + 9 arXiv/PDF + 6 newsletters; eval (1) folded).
# 0 product Integrate GO. NOASSERTION / AGPL / GPL / SPDX-null / TLS-unknown = no clone.
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

clone_ref "pi-subagents" "https://github.com/nicobailon/pi-subagents.git" "MIT"
clone_ref "tradingview-optimizer" "https://github.com/Roboquant-AI/tradingview-optimizer.git" "MIT"
clone_ref "fast-jev-compaction" "https://github.com/tamaratran/fast-jev-compaction.git" "MIT"
clone_ref "C2C" "https://github.com/thu-nics/C2C.git" "Apache-2.0"
clone_ref "jev-browser" "https://github.com/jkudish/jev-browser.git" "MIT"

echo "=== SKIP (documented) — no product Integrate GO ==="
echo "jkudish/jev-mcp — already cloned; laptop MCP WIRE (operator OK); never npx github"
echo "browser-use/jev-ultrafast — already cloned; FILE HITL"
echo "tradesdontlie/tradingview-mcp — already entity; eval Integrate OVERRIDE FILE"
echo "jkudish/jev-browser — MIT confirmed by live gh api 2026-09-18; cloned; HITL cassette only"
echo "JustExecution/HTF_indicator — GPL-3.0 EXTRACT-ONLY; never vendor"
echo "mouteee/autonomous-offensive-llm-handbook — NOASSERTION; NO-GO clone; no PoC"
echo "seyimusibau-cyber/hardenerAi — SPDX null; NO-GO clone"
echo "fhshaik/typesafe-mario — SPDX null; NO-GO clone"
echo "dbreunig/building-with-jev-skill — SPDX null; do not copy into ~/.cursor/skills"
echo "koala73/worldmonitor — AGPL skip until SPDX MIT confirmed"
echo "=== DONE ==="
