#!/usr/bin/env bash
# K223 Phase-0 clones (SPDX-verified; total << 500MB)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
clone cloudflare/computer cloudflare-computer
clone addyosmani/agent-skills addyosmani-agent-skills
clone Prism-Shadow/GDPevo GDPevo
clone HMAKT99/UnTouchID UnTouchID
clone WofWca/jumpcutter jumpcutter
du -sh "$ADOPT/cloudflare-computer" "$ADOPT/addyosmani-agent-skills" "$ADOPT/GDPevo" "$ADOPT/UnTouchID" "$ADOPT/jumpcutter"
echo "K223: jumpcutter is AGPL-3.0 isolate; UnTouchID not for vault/prod hosts"
