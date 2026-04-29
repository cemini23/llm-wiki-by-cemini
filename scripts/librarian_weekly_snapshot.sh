#!/usr/bin/env bash
# librarian_weekly_snapshot.sh
#
# LSA Phase 6b: weekly Hetzner Cloud snapshot of cemini-librarian + retention
# rotation (keeps last 4 weeks). Runs FROM cemini-librarian itself (no
# laptop dependency). Uses Hetzner Cloud API directly via curl.
#
# WHY: Hetzner's daily backup feature ($2.80/mo, already enabled) retains
# only 7 days. Weekly snapshots stretch retention to ~28 days for low cost
# (~$1/mo for an 80 GB snapshot at €0.0119/GB-month × 4 snapshots).
#
# ONE-TIME SETUP REQUIRED before cron-enabling this script:
#   1. Generate a Hetzner Cloud API token at:
#      Hetzner Cloud Console → Project → Security → API Tokens → Generate
#      Permission: "Read & Write" (snapshots require write)
#   2. Save the token to /etc/hetzner/api-token on the librarian:
#        ssh cemini-librarian "
#          mkdir -p /etc/hetzner && chmod 700 /etc/hetzner
#          echo 'YOUR_TOKEN_HERE' > /etc/hetzner/api-token
#          chmod 600 /etc/hetzner/api-token
#        "
#   3. Test the script manually:  ssh cemini-librarian /opt/scripts/librarian_weekly_snapshot.sh
#   4. Enable the systemd timer (separate file: librarian-weekly-snapshot.timer)
#
# Exit codes:
#   0 — snapshot created successfully (and old snapshots rotated)
#   1 — API token missing
#   2 — server lookup failed
#   3 — snapshot creation failed
#   4 — rotation cleanup failed (snapshot was created though, non-fatal)

set -uo pipefail

TOKEN_FILE="/etc/hetzner/api-token"
LOGFILE="/var/log/librarian-weekly-snapshot.log"
RETENTION_WEEKS=4
SNAPSHOT_PREFIX="weekly-cemini-librarian"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGFILE" >&2
}

if [[ ! -r "$TOKEN_FILE" ]]; then
  log "ERROR: $TOKEN_FILE missing or unreadable. See script header for setup."
  exit 1
fi

TOKEN=$(cat "$TOKEN_FILE")
HOSTNAME_LOCAL=$(hostname)
DATE_TAG=$(date '+%Y-%m-%d')
SNAPSHOT_NAME="${SNAPSHOT_PREFIX}-${DATE_TAG}"

# 1. Find this server's ID via the Hetzner API
log "Looking up server ID for hostname=$HOSTNAME_LOCAL"
SERVER_ID=$(curl -s -m 10 \
  -H "Authorization: Bearer $TOKEN" \
  "https://api.hetzner.cloud/v1/servers?name=${HOSTNAME_LOCAL}" \
  | grep -oE '"id":[[:space:]]*[0-9]+' | head -1 | grep -oE '[0-9]+')

if [[ -z "$SERVER_ID" ]]; then
  log "ERROR: could not resolve server ID for hostname=$HOSTNAME_LOCAL via API"
  exit 2
fi
log "Server ID: $SERVER_ID"

# 2. Create snapshot via API
log "Creating snapshot $SNAPSHOT_NAME"
SNAP_RESPONSE=$(curl -s -m 30 -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"description\":\"$SNAPSHOT_NAME\",\"type\":\"snapshot\",\"labels\":{\"role\":\"librarian\",\"automated\":\"true\",\"week\":\"$DATE_TAG\"}}" \
  "https://api.hetzner.cloud/v1/servers/${SERVER_ID}/actions/create_image")

SNAP_STATUS=$(echo "$SNAP_RESPONSE" | grep -oE '"status":[[:space:]]*"[^"]+"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')
SNAP_IMAGE_ID=$(echo "$SNAP_RESPONSE" | grep -oE '"image":[[:space:]]*\{[^}]*"id":[[:space:]]*[0-9]+' | grep -oE '[0-9]+$')

if [[ "$SNAP_STATUS" != "running" && "$SNAP_STATUS" != "success" ]]; then
  log "ERROR: snapshot creation failed: $SNAP_RESPONSE"
  exit 3
fi
log "Snapshot creation initiated (image_id=$SNAP_IMAGE_ID, status=$SNAP_STATUS)"

# 3. Retention rotation: list all snapshots matching our prefix; delete those
#    beyond RETENTION_WEEKS
log "Rotating snapshots (keep $RETENTION_WEEKS most recent matching '$SNAPSHOT_PREFIX-*')"
ALL_SNAPSHOTS_JSON=$(curl -s -m 10 \
  -H "Authorization: Bearer $TOKEN" \
  "https://api.hetzner.cloud/v1/images?type=snapshot&sort=created:desc")

# Extract (id, description) pairs for snapshots matching our prefix
# Note: lightweight grep-based parse to avoid jq dependency
MATCHING_IDS=$(echo "$ALL_SNAPSHOTS_JSON" | python3 -c "
import json, sys, re
data = json.load(sys.stdin)
matches = []
for img in data.get('images', []):
    desc = img.get('description', '') or ''
    if desc.startswith('$SNAPSHOT_PREFIX-'):
        matches.append((img['created'], img['id']))
matches.sort(reverse=True)
for created, _id in matches[$RETENTION_WEEKS:]:
    print(_id)
" 2>/dev/null)

DELETED=0
if [[ -n "$MATCHING_IDS" ]]; then
  for img_id in $MATCHING_IDS; do
    DEL_RESPONSE=$(curl -s -m 10 -X DELETE \
      -H "Authorization: Bearer $TOKEN" \
      "https://api.hetzner.cloud/v1/images/${img_id}")
    if [[ -z "$DEL_RESPONSE" ]]; then
      log "  Deleted old snapshot image_id=$img_id"
      DELETED=$((DELETED + 1))
    else
      log "  WARNING: delete failed for image_id=$img_id: $DEL_RESPONSE"
    fi
  done
fi
log "Rotation complete (deleted=$DELETED, retained=$RETENTION_WEEKS)"

exit 0
