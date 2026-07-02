#!/usr/bin/env bash
# Stage ICE recorder watch code on cemini-prod (companion to prod brief).
# Brief: briefs/2026-07-02_ice-turnkey-recorder-watch-24x7-cemini-prod.md
#
# Usage:
#   bash scripts/scp_ice_recorder_bundle_to_prod.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="cemini-prod:/opt/cemini/intel/ice-turnkey-recorder"

ssh cemini-prod 'mkdir -p /opt/cemini/intel/ice-turnkey-recorder/{scripts,config,reports}'

scp \
  "$ROOT/scripts/ice_turnkey_recorder_check.py" \
  "$ROOT/scripts/cemini_discord_notify.py" \
  "$ROOT/scripts/run_ice_turnkey_recorder_check.sh" \
  "$DEST/scripts/"

scp "$ROOT/config/ice-turnkey-recorder-sites.yaml" "$DEST/config/"

ssh cemini-prod 'chmod +x /opt/cemini/intel/ice-turnkey-recorder/scripts/*.sh'

echo "Staged to cemini-prod:/opt/cemini/intel/ice-turnkey-recorder/"
