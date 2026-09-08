#!/usr/bin/env bash
# OSINT K257 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K257 = 8 Sep 2026 inbox (3 eval + 1 NFL dossier + 4 newsletters).
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

clone_ref "markitdown" "https://github.com/microsoft/markitdown.git" "MIT"

echo "=== SKIP (documented) — no Integrate GO ==="
echo "cathrynlavery/diagram-design — already K241 FILE Extract+HITL deferred"
echo "multica-ai/andrej-karpathy-skills — SPDX null; NO-GO clone"
echo "BenBrostoff/draftfast — SPDX null; keep CONDITIONAL-GO"
echo "Randdalf/fplcache — Unlicense ~715MB SIZE-SKIP"
echo "heygen-com/hyperframes — Apache-2.0 ~402MB SIZE-SKIP (image-gen brief)"
echo "NityaGehlot/nfl-data — MIT ~172MB SIZE-SKIP"
echo "api-evangelist/sportsbook-api — SPDX null; no clone"
echo "The-Swarm-Corporation/AutoHedge — MIT Watch; no clone"
echo "=== DONE ==="
