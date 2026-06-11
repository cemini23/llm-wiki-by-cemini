#!/usr/bin/env bash
# Deploy read-only Arena harvest workers to librarian + egress (shard 1 & 2).
# Prod (shard 0) uses existing /opt/devfun-poker-arena — update via normal deploy.
#
# Usage:
#   bash scripts/export_harvest_fleet_deploy.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DEPLOY="${AGENT_DIR}/deploy/deploy_export_harvest_remote.sh"

chmod +x "${DEPLOY}" "${AGENT_DIR}/scripts/run_export_harvest_worker.sh"

"${DEPLOY}" --host cemini-librarian --shard-index 1 --label librarian
"${DEPLOY}" --host cemini-egress-fi --shard-index 2 --label egress

echo ""
echo "✓ Harvest fleet workers deployed (shard 1 librarian, shard 2 egress)."
echo "  Prod shard 0: set CEMINI_EXPORT_SHARD_COUNT=3 on existing export timers."
echo "  Run fleet: bash scripts/run_export_harvest_fleet.sh"
