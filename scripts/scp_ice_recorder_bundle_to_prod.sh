#!/usr/bin/env bash
# Stage ICE recorder watch code on cemini-prod.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="cemini-prod:/opt/cemini/intel/ice-turnkey-recorder"

ssh cemini-prod 'mkdir -p /opt/cemini/intel/ice-turnkey-recorder/{scripts,config/theses/ice-turnkey,reports}'

scp \
  "$ROOT/scripts/__init__.py" \
  "$ROOT/scripts/cemini_discord_notify.py" \
  "$DEST/scripts/"

scp -r "$ROOT/scripts/intel" "$DEST/scripts/"

scp "$ROOT/scripts/run_ice_turnkey_recorder_check.sh" "$DEST/scripts/"

scp "$ROOT/config/theses/ice-turnkey/recorder-sites.yaml" "$DEST/config/theses/ice-turnkey/"

ssh cemini-prod 'chmod +x /opt/cemini/intel/ice-turnkey-recorder/scripts/*.sh'

echo "Staged to cemini-prod:/opt/cemini/intel/ice-turnkey-recorder/"
