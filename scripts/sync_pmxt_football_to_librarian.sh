#!/usr/bin/env bash
# OSINT wrapper — delegates to world-cup-bot pmxt football sync on cemini-librarian.
set -euo pipefail
WC_BOT="${WC_BOT_ROOT:-/Users/claudiobarone/Desktop/projects/world-cup-bot}"
exec bash "$WC_BOT/scripts/shock_backtest/sync_pmxt_football_to_librarian.sh" "$@"
