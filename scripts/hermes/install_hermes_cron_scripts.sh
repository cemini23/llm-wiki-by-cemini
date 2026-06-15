#!/usr/bin/env bash
# Install canonical Hermes cron scripts from repo → ~/.hermes/scripts/
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DEST="${HOME}/.hermes/scripts"
mkdir -p "$DEST"
install -m 755 "$ROOT/scripts/hermes/cemini-wiki-gap-due.sh" "$DEST/"
install -m 755 "$ROOT/scripts/hermes/cemini-daily-digest-due.sh" "$DEST/"
echo "Installed Hermes cron scripts to $DEST"
