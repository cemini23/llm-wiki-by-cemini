#!/usr/bin/env bash
# K148 coaching extract gate — fixture transcript must pass sanitize + produce candidate.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

FIXTURE="tests/fixtures/coaching_transcript_clean.txt"
OUT="reports/coaching-extract/gate-$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$OUT"

echo "==> K148 coaching extract gate (fixture → candidate + sanitize)"
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/coaching_video_extract.py \
    --transcript-file "$FIXTURE" \
    --slug gate-fixture \
    --out-dir "$OUT" \
    --gate \
    --json | tee "${OUT}/manifest.json"
else
  python3 scripts/coaching_video_extract.py \
    --transcript-file "$FIXTURE" \
    --slug gate-fixture \
    --out-dir "$OUT" \
    --gate \
    --json | tee "${OUT}/manifest.json"
fi

echo "COACHING EXTRACT GATE OK → ${OUT}"
