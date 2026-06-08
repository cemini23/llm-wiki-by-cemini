#!/usr/bin/env bash
# Fail deploy if prod ARENA_LOBBY_COMPETITION_ID ≠ expected (Lucid-scan guardrail).
#
# Usage (sourced or run before rsync):
#   ARENA_LOBBY_COMPETITION_ID=cmq57o53r0bhw18g23qkydb08 ./scripts/cemini_deploy_comp_check.sh
#
# Bypass: CEMINI_SKIP_COMP_CHECK=1
set -euo pipefail

if [[ "${CEMINI_SKIP_COMP_CHECK:-0}" == "1" ]]; then
  echo "    SKIP comp check (CEMINI_SKIP_COMP_CHECK=1)"
  exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"

# Expected: explicit env → local .env → S2 playground default
EXPECTED="${ARENA_LOBBY_COMPETITION_ID:-}"
if [[ -z "${EXPECTED}" && -f "${AGENT_DIR}/.env" ]]; then
  EXPECTED="$(grep -E '^ARENA_LOBBY_COMPETITION_ID=' "${AGENT_DIR}/.env" | head -1 | cut -d= -f2- | tr -d '"' || true)"
fi
EXPECTED="${EXPECTED:-cmq57o53r0bhw18g23qkydb08}"

PROD="$(ssh -q "${HOST}" "grep -E '^ARENA_LOBBY_COMPETITION_ID=' '${REMOTE_DIR}/.env' 2>/dev/null | head -1 | cut -d= -f2-" || true)"
PROD="${PROD//$'\r'/}"

if [[ -z "${PROD}" ]]; then
  echo "WARN: could not read prod ARENA_LOBBY_COMPETITION_ID — continuing (no .env on host?)" >&2
  exit 0
fi

if [[ "${PROD}" != "${EXPECTED}" ]]; then
  echo "ERROR: prod competition mismatch — prod=${PROD} expected=${EXPECTED}" >&2
  echo "  Fix: ssh ${HOST} sed -i 's/^ARENA_LOBBY_COMPETITION_ID=.*/ARENA_LOBBY_COMPETITION_ID=${EXPECTED}/' ${REMOTE_DIR}/.env" >&2
  echo "  Or: ./scripts/s2_prod_apply.sh" >&2
  echo "  Bypass: CEMINI_SKIP_COMP_CHECK=1" >&2
  exit 1
fi

echo "    comp check OK: ${EXPECTED}"
