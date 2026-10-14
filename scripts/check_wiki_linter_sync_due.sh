#!/usr/bin/env bash
# Exit 0 when the eight federation wiki linters have DIVERGED — action needed.
# Exit 1 when they are identical.
#
# The exit code mirrors the other cadence checks, where 0 means "prompt the
# operator". Here the thing being asked about is divergence, not elapsed time:
# the eight copies drifted for about five months before anyone noticed, so the
# question is "have they drifted again", asked cheaply on every session start.
#
# Fix a divergence with:
#   python3 scripts/wiki_linter_sync.py sync
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if ! python3 "$ROOT/scripts/wiki_linter_sync.py" check >/tmp/.linter-sync-check.$$ 2>&1; then
  cat /tmp/.linter-sync-check.$$
  rm -f /tmp/.linter-sync-check.$$
  echo "wiki-linter-sync DIVERGED"
  exit 0
fi
rm -f /tmp/.linter-sync-check.$$
echo "wiki-linter-sync ok (all eight identical)"
exit 1
