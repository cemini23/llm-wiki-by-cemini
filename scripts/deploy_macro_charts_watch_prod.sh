#!/usr/bin/env bash
# DEPRECATED — GuruWatcher is the canonical repo.
# Redirects to: ~/Projects/GuruWatcher/scripts/deploy_prod.sh
set -euo pipefail
GW="${GURU_WATCHER_ROOT:-$HOME/Projects/GuruWatcher}"
if [[ ! -f "$GW/scripts/deploy_prod.sh" ]]; then
  echo "GuruWatcher not found at $GW" >&2
  echo "Clone: gh repo clone cemini23/GuruWatcher \"$GW\"" >&2
  exit 1
fi
echo "→ redirecting to GuruWatcher deploy ($GW)"
exec bash "$GW/scripts/deploy_prod.sh" "$@"
