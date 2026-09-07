#!/usr/bin/env bash
# OSINT K256 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K256 = 7 Sep 2026 inbox (13 arXiv + 2 eval docx + 8 newsletters).
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

clone_ref "magnitude" "https://github.com/magnitudedev/magnitude.git" "Apache-2.0"
clone_ref "refactor-platform" "https://github.com/PiSchool/refactor-platform.git" "MIT"
clone_ref "cve-mcp-server" "https://github.com/mukul975/cve-mcp-server.git" "Apache-2.0"
clone_ref "trailofbits-skills" "https://github.com/trailofbits/skills.git" "CC-BY-SA-4.0"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "hoangcuongnguyen2001/Beyond-Shallow-Alignment — null SPDX"
echo "punkpeye/awesome-mcp-servers — MIT catalog ~215MB; no clone"
echo "radixark/miles — GRPO trainer; skill hard-stop"
echo "ReversecLabs/virtual.attack — EXTRACT-ONLY; no PoC clone"
echo "openai/codex-security — already FILE at .local/adopts/codex-security"
echo "DietrichGebert/ponytail — already K247 REFERENCE"
echo "addyosmani/agent-skills — already FILE"
echo "=== DONE ==="
