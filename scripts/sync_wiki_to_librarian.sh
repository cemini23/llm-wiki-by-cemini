#!/usr/bin/env bash
# sync_wiki_to_librarian.sh
#
# LSA Phase 5: hourly wiki sync from laptop → cemini-librarian + post-rsync
# kb-server reindex. Designed to be safe to run frequently (rsync is idempotent;
# kb-server's incremental ingest skips unchanged files).
#
# Usage:
#   - Manual:  ./scripts/sync_wiki_to_librarian.sh
#   - Cron:    0 * * * * /Users/claudiobarone/Desktop/OSINT\ WORKSPACE/scripts/sync_wiki_to_librarian.sh
#
# Exit codes:
#   0 — success (rsync + kb ingest both succeeded)
#   1 — rsync failed (network, ssh auth, disk full, etc.)
#   2 — kb ingest failed (kb-server down, librarian disk full, etc.)
#   3 — workspace dir missing

set -uo pipefail

WORKSPACE="/Users/claudiobarone/Desktop/OSINT WORKSPACE"
LIBRARIAN_HOST="cemini-librarian"
LIBRARIAN_WIKI_PATH="/opt/cemini-wiki/wiki/"
LOGFILE="$HOME/Library/Logs/cemini-wiki-sync.log"

# Ensure log dir exists (macOS user logs)
mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOGFILE"
}

# Pre-flight: workspace exists?
if [[ ! -d "$WORKSPACE/wiki" ]]; then
  log "ERROR: workspace wiki/ not found at $WORKSPACE/wiki — aborting"
  exit 3
fi

cd "$WORKSPACE" || { log "ERROR: cd to workspace failed"; exit 3; }

# Step 1: rsync wiki → librarian
log "rsync starting: wiki/ → $LIBRARIAN_HOST:$LIBRARIAN_WIKI_PATH"
rsync_output=$(rsync -avz --delete \
  --exclude '.DS_Store' \
  --exclude '.obsidian' \
  --exclude '.smart-env' \
  wiki/ "$LIBRARIAN_HOST:$LIBRARIAN_WIKI_PATH" 2>&1)
rsync_exit=$?

if [[ $rsync_exit -ne 0 ]]; then
  log "ERROR: rsync failed with exit $rsync_exit"
  log "rsync output: $rsync_output"
  exit 1
fi

# Count changed files for logging (rsync output mentions changed files individually)
files_changed=$(echo "$rsync_output" | grep -cE '^[a-z]' || true)
log "rsync OK ($files_changed file paths in output; speedup ratio in trailer)"

# Skip kb ingest entirely if zero meaningful changes (avoids unnecessary load)
if [[ $files_changed -le 1 ]]; then
  log "no wiki changes, skipping kb ingest"
  exit 0
fi

# Step 2: post-rsync kb-server reindex on librarian
log "kb ingest triggering on $LIBRARIAN_HOST"
kb_output=$(ssh "$LIBRARIAN_HOST" \
  "chown -R root:root /opt/cemini-wiki/ 2>/dev/null; kb ingest /opt/cemini-wiki/wiki" 2>&1)
kb_exit=$?

if [[ $kb_exit -ne 0 ]]; then
  log "ERROR: kb ingest failed with exit $kb_exit"
  log "kb output: $kb_output"
  exit 2
fi

# kb output looks like: "Ingesting directory: ... / Ingested: N / Skipped: M"
ingested=$(echo "$kb_output" | grep -oE 'Ingested:[[:space:]]+[0-9]+' | grep -oE '[0-9]+' || echo "?")
skipped=$(echo "$kb_output"  | grep -oE 'Skipped:[[:space:]]+[0-9]+'  | grep -oE '[0-9]+' || echo "?")
log "kb ingest OK (ingested=$ingested skipped=$skipped)"

exit 0
