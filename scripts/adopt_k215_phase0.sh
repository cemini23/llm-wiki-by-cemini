#!/usr/bin/env bash
# K215 Phase-0 — MIT PII-redaction Extracts <<500MB. No AGPL/GPL/NOASSERTION giants.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.local/adopts"
mkdir -p "$DEST"
clone() {
  local repo="$1" name="$2"
  if [[ -d "$DEST/$name/.git" ]]; then echo "ok $name"; du -sh "$DEST/$name"; return; fi
  echo "==> $repo"
  git clone --depth 1 "https://github.com/$repo.git" "$DEST/$name"
  du -sh "$DEST/$name"
}
clone OpenPipe/pii-redaction pii-redaction
clone packyme/privacy-filter privacy-filter
clone sam247/openredaction openredaction
clone Zeno-wistom/vibe-upgrader vibe-upgrader
# Watch Apache (small enough): skip phileas ~38MB for now — optional
echo "BATCH:"
du -sh "$DEST"/pii-redaction "$DEST"/privacy-filter "$DEST"/openredaction "$DEST"/vibe-upgrader
clone Coral-Protocol/AgentRadio agentradio
