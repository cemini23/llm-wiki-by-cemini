#!/usr/bin/env bash
# K206 Phase-0 — agent-security-lab (SHarD artifacts) CONDITIONAL-GO Extract
# MIT · ~944KB · no Atto wire · shard (~52MB) deferred
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.local/adopts/agent-security-lab"
mkdir -p "$ROOT/.local/adopts"
if [[ -d "$DEST/.git" ]]; then
  echo "already present: $DEST"
  du -sh "$DEST"
  exit 0
fi
git clone --depth 1 https://github.com/wrgore/agent-security-lab.git "$DEST"
du -sh "$DEST"
echo "OK — Extract only. See wiki/entities/tools/agent-security-lab.md"
