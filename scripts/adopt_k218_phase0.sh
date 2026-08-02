#!/usr/bin/env bash
# K218 Phase-0 — optical transfer / PDF inspect / agent memory / last30days refresh
# Total << 500MB. SPDX verified 2026-08-02.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  echo "clone $repo → $dest"
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
clone bashalarmistalt/decimen-optical-transfer decimen-optical-transfer
clone firecrawl/pdf-inspector pdf-inspector
clone TencentCloud/TencentDB-Agent-Memory TencentDB-Agent-Memory
clone mvanhorn/last30days-skill last30days-skill
# Watch-only skipped this batch: antirez/ds4, semantica-agi/semantica (size/priority)
# Skip: AGPL invidious, null-SPDX builds, HF abliterated forks
echo "=== sizes ==="
du -sh "$ADOPT"/decimen-optical-transfer "$ADOPT"/pdf-inspector "$ADOPT"/TencentDB-Agent-Memory "$ADOPT"/last30days-skill 2>/dev/null
du -sh "$ADOPT"
