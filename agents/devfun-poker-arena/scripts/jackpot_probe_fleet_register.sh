#!/usr/bin/env bash
# Register anonymous jackpot hunt probes (separate from prod cemini_wiki_poker).
#
#   ./scripts/jackpot_probe_fleet_register.sh
#   ./scripts/jackpot_probe_fleet_register.sh --only lib-a
#
# Writes gitignored creds:
#   .arena-credentials.jackpot-lib-a
#   .arena-credentials.jackpot-egr-a
#   .arena-credentials.jackpot-egr-b
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

ONLY=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --only) ONLY="$2"; shift 2 ;;
    *) shift ;;
  esac
done

register_one() {
  local id="$1"
  local creds=".arena-credentials.jackpot-${id}"
  if [[ -f "${creds}" ]]; then
    local aid
    aid="$(python3 -c "import json; print(json.load(open('${creds}'))['agentId'])")"
    echo "==> skip ${id} (exists agentId=${aid})"
    return 0
  fi
  local suffix
  suffix="$(openssl rand -hex 3 2>/dev/null || echo "$RANDOM")"
  echo "==> register ${id} → ${creds}"
  ARENA_CREDENTIALS_FILE="${creds}" \
    JACKPOT_27_HANDLE="arena_probe_${id}_${suffix}" \
    JACKPOT_27_NAME="Probe ${id}" \
    ./scripts/jackpot_27_register.sh
}

_probes=(lib-a egr-a egr-b)
if [[ -n "${ONLY}" ]]; then
  _probes=("${ONLY}")
fi

for p in "${_probes[@]}"; do
  if [[ -n "${ONLY}" && "${p}" != "${ONLY}" ]]; then
    continue
  fi
  register_one "${p}"
done

echo ""
echo "✓ Fleet creds ready. Deploy:"
echo "  ./deploy/deploy_jackpot_probe_remote.sh --host cemini-librarian --instance lib-a --creds .arena-credentials.jackpot-lib-a"
echo "  ./deploy/deploy_jackpot_probe_remote.sh --host cemini-egress-fi --instance egr-a --creds .arena-credentials.jackpot-egr-a"
echo "  ./deploy/deploy_jackpot_probe_remote.sh --host cemini-egress-fi --instance egr-b --creds .arena-credentials.jackpot-egr-b"
