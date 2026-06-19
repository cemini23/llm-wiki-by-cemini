#!/usr/bin/env bash
# List live Arena competitions — run daily until researcher HU comp appears.
set -euo pipefail
cd "$(dirname "$0")/.."

CREDS=".arena-credentials"
if [[ ! -f "$CREDS" ]]; then
  echo "ERROR: $CREDS missing — run pokerkit run once or register via arena.md"
  exit 1
fi

ARENA_KEY=$(python3 -c "import json; print(json.load(open('$CREDS'))['apiKey'])")
BASE="https://arena.dev.fun/api/arena"

echo "==> Active competitions"
curl -sS -H "x-arena-api-key: $ARENA_KEY" "$BASE/competition/list-active" | python3 -m json.tool

echo ""
echo "==> Filter: challenge / researcher / heads-up / eval / benchmark"
curl -sS -H "x-arena-api-key: $ARENA_KEY" "$BASE/competition/list-all" | python3 -c "
import json, sys
raw = json.load(sys.stdin)
data = raw.get('data', raw) if isinstance(raw, dict) else raw
if not isinstance(data, list):
    raise SystemExit(f'unexpected list-all payload: {type(data)}')
keys = ('challenge', 'researcher', 'heads', 'head-to', 'bench', 'sandbox', 'eval', 'pve')
for c in data:
    if not isinstance(c, dict):
        continue
    blob = (c.get('name', '') + ' ' + c.get('description', '')).lower()
    if any(k in blob for k in keys):
        print(f\"{c.get('id')}  {c.get('name')}  season={c.get('seasonNumber')}\")
"
