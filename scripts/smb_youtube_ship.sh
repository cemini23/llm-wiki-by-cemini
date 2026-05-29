#!/usr/bin/env bash
# smb_youtube_ship.sh — Ship SMB Capital YouTube K79 rolling brief + sync wiki.
#
# Usage (repo root):
#   bash scripts/smb_youtube_ship.sh
#   bash scripts/smb_youtube_ship.sh briefs/2026-05-29_k79-smb-capital-youtube-synthesis-cemini.md
#
# Steps: skill_audit → SCP brief to cemini-prod → sync wiki to librarian (+ kb ingest).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BRIEF="${1:-$ROOT/briefs/2026-05-29_k79-smb-capital-youtube-synthesis-cemini.md}"
PROD_HOST="${CEMINI_PROD_HOST:-cemini-prod}"
PROD_BRIEFS="/opt/cemini/briefs"

if [[ ! -f "$BRIEF" ]]; then
  echo "Brief not found: $BRIEF" >&2
  exit 1
fi

echo "==> skill_audit"
python3 "$ROOT/scripts/skill_audit.py" "$BRIEF"
audit_rc=$?
if [[ $audit_rc -eq 2 ]]; then
  echo "skill_audit REJECT — fix brief before shipping" >&2
  exit 2
fi
if [[ $audit_rc -ne 0 ]]; then
  echo "skill_audit WARN (rc=$audit_rc) — continuing; review output above" >&2
fi

dest_name="$(basename "$BRIEF")"
echo "==> SCP brief → ${PROD_HOST}:${PROD_BRIEFS}/${dest_name}"
scp "$BRIEF" "${PROD_HOST}:${PROD_BRIEFS}/${dest_name}"
ssh "$PROD_HOST" "ls -la ${PROD_BRIEFS}/${dest_name}"

echo "==> sync wiki → librarian + kb ingest"
bash "$ROOT/scripts/sync_wiki_to_librarian.sh"

echo "Done. Brief on prod; wiki synced."
