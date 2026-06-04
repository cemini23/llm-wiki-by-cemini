#!/usr/bin/env bash
# install_federated_daily_digest.sh — bootstrap daily digest on a sibling wiki repo.
# Usage: bash install_federated_daily_digest.sh /path/to/wiki-repo <wiki-id>
set -euo pipefail

WIKI_ROOT="${1:?wiki repo root required}"
WIKI_ID="${2:?wiki-id required (ccc|seo|image-gen|gambling|cybersec|3d-printing)}"
OSINT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
KIT="$OSINT_ROOT/scripts/federation/daily_digest"

mkdir -p "$WIKI_ROOT/scripts" "$WIKI_ROOT/wiki/sweeps" "$WIKI_ROOT/wiki/meta" "$WIKI_ROOT/research to be indexed"

for f in daily_research_digest_run.py daily_research_fetch.py wiki_source_index.py; do
  if [[ -f "$OSINT_ROOT/scripts/$f" ]]; then
    cp "$OSINT_ROOT/scripts/$f" "$WIKI_ROOT/scripts/$f"
  fi
done

if [[ ! -f "$WIKI_ROOT/scripts/daily_research_config.yaml" ]]; then
  cp "$KIT/daily_research_config.template.yaml" "$WIKI_ROOT/scripts/daily_research_config.yaml"
fi

if [[ ! -f "$WIKI_ROOT/wiki/meta/daily-research-digest-cadence.md" ]]; then
  cat > "$WIKI_ROOT/wiki/meta/daily-research-digest-cadence.md" <<EOF
---
title: Daily research digest cadence ($WIKI_ID)
type: concept
tags: [meta, automation]
maturity: draft
created: $(date +%Y-%m-%d)
updated: $(date +%Y-%m-%d)
---

## Narrative

Federated install from @osint-wiki/concepts/federated-daily-research-digest.md.
Script: \`scripts/daily_research_digest_run.py\`. Report: \`wiki/sweeps/YYYY-MM-DD-daily.md\`.
EOF
fi

mkdir -p "$HOME/.cemini/wiki-paths"
printf '%s\n' "$WIKI_ROOT" > "$HOME/.cemini/wiki-paths/${WIKI_ID}.path"
chmod 600 "$HOME/.cemini/wiki-paths/${WIKI_ID}.path"

echo "Installed digest for $WIKI_ID at $WIKI_ROOT"
echo "Path file: $HOME/.cemini/wiki-paths/${WIKI_ID}.path"
echo "Reload all morning agents:"
echo "  bash \"$OSINT_ROOT/scripts/reinstall_morning_launchagents.sh\""
