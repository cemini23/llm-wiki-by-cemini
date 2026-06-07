#!/usr/bin/env bash
# Deploy all jackpot probes to librarian + egress (24/7 passive data collection).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DEPLOY="${AGENT_DIR}/deploy/deploy_jackpot_probe_remote.sh"

chmod +x "${DEPLOY}"

"${DEPLOY}" --host cemini-librarian --instance lib-a --creds .arena-credentials.jackpot-lib-a
"${DEPLOY}" --host cemini-egress-fi --instance egr-a --creds .arena-credentials.jackpot-egr-a
"${DEPLOY}" --host cemini-egress-fi --instance egr-b --creds .arena-credentials.jackpot-egr-b

echo ""
echo "✓ Fleet deployed (join OFF, hunt OFF). S2 only — use a competition id that is NOT the qual bot:"
echo "  JACKPOT_27_JOIN_ENABLED=1 JACKPOT_27_COMPETITION_ID=<s2-id> ./scripts/jackpot_probe_fleet_deploy.sh"
