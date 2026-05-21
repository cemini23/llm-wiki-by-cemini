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
LIBRARIAN_ROOT="/opt/cemini-wiki"
LOGFILE="$HOME/Library/Logs/cemini-wiki-sync.log"

# Wiki definitions: "LOCAL_PATH|REMOTE_SUBPATH"
# REMOTE_SUBPATH is relative to LIBRARIAN_ROOT and becomes the project tag in kb-server.
WIKIS=(
  "$WORKSPACE/wiki/|wiki/"
  "/Users/claudiobarone/Desktop/projects/Cemini claude code CCC/wiki/|ccc-wiki/wiki/"
  "/Users/claudiobarone/Desktop/projects/Image gen/wiki/|image-gen-wiki/wiki/"
  "/Users/claudiobarone/Desktop/projects/3d printing/wiki/|3d-printing-wiki/wiki/"
  "/Users/claudiobarone/Desktop/projects/SEO:GEO B&M Business/wiki/|seo-geo-wiki/wiki/"
  "/Users/claudiobarone/Desktop/projects/Cybersecurity wiki/wiki/|cybersecurity-wiki/wiki/"
)

# Ensure log dir exists (macOS user logs)
mkdir -p "$(dirname "$LOGFILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOGFILE"
}

# Pre-flight: OSINT workspace exists (primary anchor)
if [[ ! -d "$WORKSPACE/wiki" ]]; then
  log "ERROR: OSINT workspace wiki/ not found at $WORKSPACE/wiki — aborting"
  exit 3
fi

# Single-run lock. The sync fires from two triggers — the git post-commit
# hook (instant, on every wiki commit) and the hourly cron backstop (catches
# sibling-wiki commits + uncommitted drift). An atomic mkdir lock keeps
# overlapping runs from piling up; a stale lock (>15 min) is reclaimed.
LOCKDIR="/tmp/cemini-wiki-sync.lock"
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  if [[ -n "$(find "$LOCKDIR" -maxdepth 0 -mmin +15 2>/dev/null)" ]]; then
    log "stale lock (>15 min) — reclaiming"
    rmdir "$LOCKDIR" 2>/dev/null && mkdir "$LOCKDIR" 2>/dev/null || { log "could not reclaim lock — aborting"; exit 0; }
  else
    log "another sync is already running — skipping this run"
    exit 0
  fi
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT

# Step 1: rsync each wiki to its librarian subpath
total_changes=0
synced_wikis=0
for wiki_def in "${WIKIS[@]}"; do
  local_path="${wiki_def%%|*}"
  remote_subpath="${wiki_def##*|}"
  remote_path="${LIBRARIAN_ROOT}/${remote_subpath}"

  if [[ ! -d "$local_path" ]]; then
    log "skip: $local_path not present locally"
    continue
  fi

  # Ensure remote parent exists (first sync for a new wiki alias)
  ssh "$LIBRARIAN_HOST" "mkdir -p $(dirname "$remote_path")" 2>/dev/null || true

  log "rsync starting: $local_path → $LIBRARIAN_HOST:$remote_path"
  rsync_output=$(rsync -avz --delete \
    --exclude '.DS_Store' \
    --exclude '.obsidian' \
    --exclude '.smart-env' \
    "$local_path" "$LIBRARIAN_HOST:$remote_path" 2>&1)
  rsync_exit=$?

  if [[ $rsync_exit -ne 0 ]]; then
    log "ERROR: rsync $local_path failed with exit $rsync_exit"
    log "rsync output: $rsync_output"
    exit 1
  fi

  changes=$(echo "$rsync_output" | grep -cE '^[a-z]' || true)
  total_changes=$((total_changes + changes))
  synced_wikis=$((synced_wikis + 1))
  log "rsync OK ($remote_subpath: $changes file paths)"
done

# Skip reindex if zero meaningful changes (each rsync emits ~1 trailer line)
if [[ $total_changes -le $synced_wikis ]]; then
  log "no wiki changes across $synced_wikis wikis, skipping kb reindex"
  exit 0
fi

# Step 2: post-rsync kb-server vault reindex (with semantic embeddings)
# NOTE: switched from `kb ingest` (no embeddings, dedupes by basename, accumulates orphans)
# to `kb vault reindex --embeddings` (proper UPSERT via vault_files, generates embeddings
# for semantic search). paths.js loads /opt/kb-server/.env automatically.
log "kb vault reindex (--embeddings) triggering on $LIBRARIAN_HOST"
kb_output=$(ssh "$LIBRARIAN_HOST" \
  "chown -R root:root /opt/cemini-wiki/ 2>/dev/null; kb vault reindex --embeddings" 2>&1)
kb_exit=$?

if [[ $kb_exit -ne 0 ]]; then
  log "ERROR: kb vault reindex failed with exit $kb_exit"
  log "kb output: $kb_output"
  exit 2
fi

# kb output looks like: "Done: N indexed, M unchanged, K removed, L embedded"
indexed=$(echo "$kb_output"  | grep -oE '[0-9]+ indexed'   | grep -oE '[0-9]+' || echo "?")
unchanged=$(echo "$kb_output"| grep -oE '[0-9]+ unchanged' | grep -oE '[0-9]+' || echo "?")
removed=$(echo "$kb_output"  | grep -oE '[0-9]+ removed'   | grep -oE '[0-9]+' || echo "?")
embedded=$(echo "$kb_output" | grep -oE '[0-9]+ embedded'  | grep -oE '[0-9]+' || echo "0")
log "kb vault reindex OK (indexed=$indexed unchanged=$unchanged removed=$removed embedded=$embedded)"

exit 0
