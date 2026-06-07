#!/usr/bin/env bash
# Archive full hand history for jackpot probe fleet (+ legacy test probe).
# Writes to reports/jackpot-27-archive/<competition>/ (gitignored).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPETITION_ID="${1:-cmpy2qy65002ud9ej6b7jjq0l}"
TS="$(date -u +%Y%m%dT%H%M%SZ)"
ARCHIVE="${AGENT_DIR}/reports/jackpot-27-archive/${COMPETITION_ID}/${TS}"

cd "${AGENT_DIR}"

if [[ ! -f .arena-credentials && -z "${ARENA_API_KEY:-}" ]]; then
  echo "ERROR: need .arena-credentials or ARENA_API_KEY" >&2
  exit 1
fi

PY="uv run python"
if ! command -v uv >/dev/null 2>&1; then
  PY="python3"
fi

echo "==> Export probe submissions + replays → ${ARCHIVE}"
${PY} examples/export_agent_hand_history.py \
  --match "${COMPETITION_ID}" \
  --out-dir "${ARCHIVE}" \
  --agent "cmq014ud2cl3pacxgg8z4p6ho:lib-a" \
  --agent "cmq014uwfcl3yacxg8v57iizb:egr-a" \
  --agent "cmq014vhqlzltdo3jm2v5ykd2:egr-b" \
  --agent "cmq0023xv5023acxgag69ynrb:probe-0c59ea"

echo "==> Rsync remote probe logs (dealt.jsonl, journal excerpts)"
mkdir -p "${ARCHIVE}/remote-logs"
for host_instance in "cemini-librarian:lib-a" "cemini-egress-fi:egr-a" "cemini-egress-fi:egr-b"; do
  host="${host_instance%%:*}"
  inst="${host_instance##*:}"
  remote="/opt/devfun-poker-arena-jackpot/reports/jackpot-27/${inst}"
  mkdir -p "${ARCHIVE}/remote-logs/${inst}"
  rsync -avz "${host}:${remote}/" "${ARCHIVE}/remote-logs/${inst}/" 2>/dev/null || true
  ssh "${host}" "journalctl -u jackpot-27-probe@${inst}.service --since '2026-06-04' --no-pager" \
    > "${ARCHIVE}/remote-logs/${inst}/journal.txt" 2>/dev/null || true
done

echo ""
echo "✓ Archive ready: ${ARCHIVE}"
echo "  manifest: ${ARCHIVE}/manifest.json"
echo "  combined: ${ARCHIVE}/all-probes-submissions.jsonl"
wc -l "${ARCHIVE}"/*/submissions.jsonl "${ARCHIVE}/all-probes-submissions.jsonl" 2>/dev/null || true
