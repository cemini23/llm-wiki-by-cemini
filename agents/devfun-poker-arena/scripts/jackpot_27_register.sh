#!/usr/bin/env bash
# Register jackpot satellite agent — separate creds from prod qualification bot.
#
#   ./scripts/jackpot_27_register.sh
#
# Writes: .arena-credentials.jackpot-27 (never copy to .arena-credentials)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

export ARENA_CREDENTIALS_FILE="${ARENA_CREDENTIALS_FILE:-.arena-credentials.jackpot-probe}"
# Anonymous probe — no operator brand in handle unless you set JACKPOT_27_HANDLE
if [[ -z "${JACKPOT_27_HANDLE:-}" ]]; then
  SUFFIX="$(openssl rand -hex 3 2>/dev/null || echo "$RANDOM")"
  export JACKPOT_27_HANDLE="arena_probe_${SUFFIX}"
fi
HANDLE="${JACKPOT_27_HANDLE}"
NAME="${JACKPOT_27_NAME:-Table Probe}"
QUOTE="${JACKPOT_27_QUOTE:-fold and observe}"

echo "==> Register jackpot satellite (handle=${HANDLE})"
echo "    creds → ${ARENA_CREDENTIALS_FILE}"

uv run python - <<PY
import os
import sys
from pathlib import Path
root = Path("${AGENT_DIR}")
sys.path.insert(0, str(root / "examples"))
from dotenv import load_dotenv
load_dotenv(root / ".env")
os.environ["ARENA_CREDENTIALS_FILE"] = "${ARENA_CREDENTIALS_FILE}"
from arena_client import ArenaClient, DEFAULT_BASE, load_or_register
client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE))
creds = load_or_register(client, "${HANDLE}", "${NAME}", "${QUOTE}")
print("agentId=", creds.get("agentId"))
print("handle=", creds.get("handle") or "${HANDLE}")
client.close()
PY

if [[ -f "${ARENA_CREDENTIALS_FILE}" ]]; then
  AGENT_ID="$(python3 -c "import json; print(json.load(open('${ARENA_CREDENTIALS_FILE}'))['agentId'])")"
  echo "✓ Registered agentId=${AGENT_ID}"
  echo "  Prod creds untouched: .arena-credentials"
else
  echo "ERROR: registration did not create ${ARENA_CREDENTIALS_FILE}" >&2
  exit 1
fi
