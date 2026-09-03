#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
REPORT="${ROOT}/.local/reports/k190-phase0-$(date +%Y-%m-%d).md"
mkdir -p "$(dirname "$REPORT")"
SIZE_MB=$(du -sm "$ADOPTS" | awk '{print $1}')
cat >"$REPORT" <<R
# K190 Phase-0 — $(date +%Y-%m-%d)

## Integrate GO (cloned)
- genea-app (MIT)
- claude-family-history-research-skill (MIT)
- ancestry-tools (Apache-2.0)
- autoresearch-genealogy reinforce (MIT)

## Extract GO (cloned)
- wikitree-dynamic-tree, lineage, yorkeccak-history, pure-genealogy, go-geni

## Overturned Watch
- betty GPL-3.0; Open-Genealogy CC-BY-NC-SA-4.0; KekuleHtml AGPL-3.0
- Skip large: keifu, danactive/history, wikitree-sourcer

**Disk:** ~${SIZE_MB} MB (cap 500).
R
echo "Wrote $REPORT (${SIZE_MB} MB)"
du -sh "$ADOPTS"/*/ | sort -h | tail -15
