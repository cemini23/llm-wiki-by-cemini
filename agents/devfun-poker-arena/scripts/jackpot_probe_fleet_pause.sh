#!/usr/bin/env bash
# Pause jackpot probe fleet — anti-cheat / collusion safety (Playground S1 qual bot).
# Stops services and clears competition join on librarian + egress.
set -euo pipefail

HOSTS=(cemini-librarian cemini-egress-fi)
INSTANCES=(lib-a egr-a egr-b)
REMOTE_DIR="${JACKPOT_REMOTE_DIR:-/opt/devfun-poker-arena-jackpot}"

for host in "${HOSTS[@]}"; do
  case "${host}" in
    cemini-librarian) ids=(lib-a) ;;
    cemini-egress-fi) ids=(egr-a egr-b) ;;
    *) ids=() ;;
  esac
  for id in "${ids[@]}"; do
    echo "==> Pausing ${host} jackpot-27-probe@${id}"
    ssh "${host}" bash -s <<REMOTE
set -euo pipefail
ENV="${REMOTE_DIR}/instances/${id}.env"
if [[ -f "\${ENV}" ]]; then
  sed -i 's/^JACKPOT_27_JOIN_ENABLED=.*/JACKPOT_27_JOIN_ENABLED=0/' "\${ENV}" || true
  grep -q '^JACKPOT_27_JOIN_ENABLED=' "\${ENV}" || echo 'JACKPOT_27_JOIN_ENABLED=0' >> "\${ENV}"
  sed -i 's/^JACKPOT_27_COMPETITION_ID=.*/JACKPOT_27_COMPETITION_ID=/' "\${ENV}" || true
fi
systemctl stop "jackpot-27-probe@${id}.service" 2>/dev/null || true
systemctl disable "jackpot-27-probe@${id}.service" 2>/dev/null || true
echo "    stopped (join OFF, competition cleared)"
REMOTE
  done
done

echo ""
echo "✓ Probe fleet paused. Re-enable for S2 only (separate competition, hunt ON):"
echo "  JACKPOT_27_JOIN_ENABLED=1 JACKPOT_27_COMPETITION_ID=<s2-id> ./scripts/jackpot_probe_fleet_deploy.sh"
