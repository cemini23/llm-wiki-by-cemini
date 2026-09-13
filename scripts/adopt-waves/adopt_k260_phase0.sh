#!/usr/bin/env bash
# OSINT K260 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K260 = 13 Sep 2026 inbox (2 eval + 4 arXiv + Jane Street + 9 newsletters).
# 0 Integrate GO. SPDX-confirmed REFERENCE set only.
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

clone_ref "COBRA-Skills" "https://github.com/Jerry-LuP/COBRA-Skills.git" "Apache-2.0"
clone_ref "pentagi" "https://github.com/vxcontrol/pentagi.git" "MIT"
clone_ref "DeskcommCRM" "https://github.com/melgarafael/DeskcommCRM.git" "MIT"
clone_ref "aimap" "https://github.com/BishopFox/aimap.git" "MIT"
clone_ref "OpenResearch" "https://github.com/alphaXiv/OpenResearch.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "cuiyu-ai/Ecdysis — SPDX null; NO-GO clone"
echo "sparkyniner/Netryx-Astra-V2-Geolocation-Tool — SPDX null; NO-GO clone"
echo "JustVugg/colibri — already Watch; no new clone"
echo "SnailSploit/Claude-Red — already present; no new clone"
echo "ever-co/ever-gauzy — AGPL-3.0 SIZE-SKIP"
echo "tonhowtf/omniget — GPL-3.0 EXTRACT-ONLY; no vendor"
echo "DFS eval 18/20 UNAVAILABLE/404; Krool + mrbusche SPDX null — no clone"
echo "=== DONE ==="
