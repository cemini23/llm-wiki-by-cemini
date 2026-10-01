#!/usr/bin/env bash
# archive_raw_to_egress.sh — post-ingest raw source archive (federation-wide).
#
# Replaces laptop .local/archives/research/ and sibling raw-sources/ retention.
# Librarian bulk host deleted 2026-06-14; canonical cold store is egress-fi.
#
# Usage:
#   bash scripts/archive_raw_to_egress.sh --wiki-id osint "research to be indexed/foo.pdf"
#   bash scripts/archive_raw_to_egress.sh --wiki-id gambling raw-sources/bar.pdf --keep-local
#
# Remote layout:
#   cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/<basename>
#
# Source page Location field:
#   cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/<basename>
#
# Wiki IDs (federation_paths.yaml): osint, ccc, seo, image-gen, gambling,
# game-dev, cybersec, 3d-printing

set -euo pipefail

EGRESS_HOST="${CEMINI_EGRESS_HOST:-cemini-egress-fi}"
REMOTE_BASE="${CEMINI_EGRESS_BULK:-/opt/cemini-bulk/research}"
KEEP_LOCAL=0
WIKI_ID=""

usage() {
  cat <<'EOF'
Usage: archive_raw_to_egress.sh --wiki-id <id> <local-file> [--keep-local]

  --wiki-id   Federation wiki id (osint, ccc, seo, image-gen, gambling,
              game-dev, cybersec, 3d-printing)
  --keep-local  Do not delete the local file after successful scp

Environment:
  CEMINI_EGRESS_HOST  SSH alias (default: cemini-egress-fi)
  CEMINI_EGRESS_BULK  Remote research root (default: /opt/cemini-bulk/research)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --wiki-id)
      WIKI_ID="${2:?--wiki-id requires a value}"
      shift 2
      ;;
    --keep-local)
      KEEP_LOCAL=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      # Capture the first positional here rather than `break`-ing: the documented
      # usage puts flags AFTER the filename, and breaking made everything past it
      # unreachable -- which silently disabled --keep-local and deleted the file.
      if [[ -z "${LOCAL_FILE:-}" ]]; then
        LOCAL_FILE="$1"
        shift
      else
        echo "Unexpected argument: $1" >&2
        usage >&2
        exit 2
      fi
      ;;
  esac
done

LOCAL_FILE="${LOCAL_FILE:-}"
if [[ -z "$WIKI_ID" || -z "$LOCAL_FILE" ]]; then
  usage >&2
  exit 2
fi

if [[ ! -f "$LOCAL_FILE" ]]; then
  echo "archive_raw_to_egress: file not found: $LOCAL_FILE" >&2
  exit 1
fi

BASENAME="$(basename "$LOCAL_FILE")"
REMOTE_DIR="${REMOTE_BASE}/${WIKI_ID}"
REMOTE_PATH="${REMOTE_DIR}/${BASENAME}"

# --- tailnet preflight (added 2026-10-01) -------------------------------
# The egress host is Tailscale-only; public SSH is UFW-closed. Without this,
# an unreachable host makes each file hang on its own SSH timeout.
if ! ssh -o ConnectTimeout=8 -o BatchMode=yes "$EGRESS_HOST" true 2>/dev/null; then
  echo "ERROR: cannot reach ${EGRESS_HOST} (tailnet down?)" >&2
  echo "  Check: tailscale status   (expect 100.76.73.113 cemi-egress-fi)" >&2
  echo "  Do NOT reopen public SSH as a workaround; bring the tailnet up." >&2
  exit 3
fi

echo "==> Ensure ${EGRESS_HOST}:${REMOTE_DIR}"
ssh "$EGRESS_HOST" "mkdir -p '${REMOTE_DIR}'"

echo "==> scp ${LOCAL_FILE} → ${EGRESS_HOST}:${REMOTE_PATH}"
scp "$LOCAL_FILE" "${EGRESS_HOST}:${REMOTE_PATH}"

echo "==> verify remote size"
REMOTE_SIZE="$(ssh "$EGRESS_HOST" "stat -c%s '${REMOTE_PATH}' 2>/dev/null || stat -f%z '${REMOTE_PATH}'")"
LOCAL_SIZE="$(stat -c%s "$LOCAL_FILE" 2>/dev/null || stat -f%z "$LOCAL_FILE")"
if [[ "$REMOTE_SIZE" != "$LOCAL_SIZE" ]]; then
  echo "archive_raw_to_egress: size mismatch local=${LOCAL_SIZE} remote=${REMOTE_SIZE}" >&2
  exit 1
fi

if [[ "$KEEP_LOCAL" -eq 0 ]]; then
  rm -f "$LOCAL_FILE"
  echo "==> removed local copy: $LOCAL_FILE"
else
  echo "==> kept local copy (--keep-local)"
fi

echo "Canonical: ${EGRESS_HOST}:${REMOTE_PATH}"
