#!/usr/bin/env bash
# K146 pilot — prepare topology pack + optional Gemma-class reviewer.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
  esac
done

echo "==> prepare substrate reviewer pack"
uv run python scripts/prepare_substrate_reviewer_pack.py

echo "==> substrate reviewer pilot"
if [[ "$DRY_RUN" -eq 1 ]]; then
  uv run python scripts/run_substrate_reviewer_pilot.py --dry-run
else
  uv run python scripts/run_substrate_reviewer_pilot.py || uv run python scripts/run_substrate_reviewer_pilot.py --dry-run
fi

echo "PILOT OK"
