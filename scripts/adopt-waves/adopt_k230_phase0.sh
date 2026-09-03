#!/usr/bin/env bash
# K230 Phase-0 — budget <500MB new clones
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

clone() {
  local slug="$1" dest="$2"
  if [ -d "$dest/.git" ]; then echo "HAVE $dest"; du -sh "$dest"; return; fi
  echo "CLONE $slug -> $dest"
  git clone --depth 1 "https://github.com/${slug}.git" "$dest"
  du -sh "$dest"
}

clone cathrynlavery/diagram-design diagram-design
clone google-deepmind/weathernext weathernext
clone vitali87/code-graph-rag code-graph-rag
clone pingdotgg/t3code t3code
clone router-for-me/CLIProxyAPI CLIProxyAPI
clone Alfredredbird/tookie-osint tookie-osint

echo "=== SKIP (documented) ==="
echo "LifeOS — already K229 shallow"
echo "EpicStaff — NOASSERTION NO-GO"
echo "RuView/Dopamine/iLEAPP — Watch/Extract size hold this batch"
echo "=== DONE ==="
du -sh diagram-design weathernext code-graph-rag t3code CLIProxyAPI tookie-osint 2>/dev/null
du -ch diagram-design weathernext code-graph-rag t3code CLIProxyAPI tookie-osint 2>/dev/null | tail -1
