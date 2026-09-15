#!/usr/bin/env bash
# OSINT K261 Phase-0 — SPDX-confirmed REFERENCE set only (shallow, --depth 1).
# Dual-ID: OSINT K261 = 15 Sep 2026 inbox (1 eval + 9 newsletters).
# 0 Integrate GO. AGPL/GPL/NOASSERTION = no clone.
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

clone_ref "power-pwn" "https://github.com/mbrg/power-pwn.git" "MIT"
clone_ref "agentic-inbox" "https://github.com/cloudflare/agentic-inbox.git" "Apache-2.0"
clone_ref "mcp-sports-hub" "https://github.com/lacausecrypto/mcp-sports-hub.git" "MIT"
clone_ref "arsenal-ng" "https://github.com/halilkirazkaya/arsenal-ng.git" "MIT"
clone_ref "m3e-canvas" "https://github.com/lnkiai/m3e-canvas.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "koala73/worldmonitor — AGPL-3.0 Watch reaffirm; no re-clone"
echo "hypit-ai/hypit — NOASSERTION; NO-GO clone"
echo "Lakr233/vphone-cli — already present; no new clone"
echo "nicocha30/ligolo-ng — GPL-3.0 EXTRACT-ONLY; no vendor; no clone"
echo "debpalash/VoiceStudio — AGPL-3.0 skip; no clone"
echo "Dogacel/auto-gpu-kernel — Watch; no clone"
echo "DefiLeoo/YOINK — FILE wiki-only; no pm scp; skip clone"
echo "LLMQuant/awesome-trading-agents — awesome-list; no clone"
echo "=== DONE ==="
