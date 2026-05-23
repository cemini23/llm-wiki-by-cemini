#!/usr/bin/env bash
# Step 197 Phase 1b — Polymarket WS ingest benchmark (FLOX vs Python).
# Run on Linux host with network (cemini-librarian recommended).
set -euo pipefail

ROOT="${FLOX_REPO:-/tmp/flox-phase1-build}"
DURATION="${FLOX_PM_DURATION_SEC:-60}"
OUT_DIR="${1:-/opt/cemini-bulk/research/cemini-handoff/briefs}"
mkdir -p "$OUT_DIR"

TOKEN="${FLOX_PM_TOKEN_ID:-}"
if [[ -z "$TOKEN" ]]; then
  TOKEN=$(curl -fsS -H "User-Agent: CeminiOSINT/1.0" \
    "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=1&order=volume24hr&ascending=false" \
    | python3 -c "import sys,json; m=json.load(sys.stdin)[0]; ids=json.loads(m['clobTokenIds']); print(ids[0])")
fi
[[ -n "$TOKEN" ]] || { echo "Could not resolve token id"; exit 1; }
export FLOX_PM_TOKEN_ID="$TOKEN"
export FLOX_PM_DURATION_SEC="$DURATION"

echo "Token: ${TOKEN:0:20}... duration=${DURATION}s"

# Artifact sizes (Phase 1a)
FLOX_LIB="$ROOT/build/connectors/libflox-connectors.a"
FLOX_CORE="$ROOT/build/libflox.a"
{
  echo "libflox_connectors_bytes=$(stat -c%s "$FLOX_LIB" 2>/dev/null || stat -f%z "$FLOX_LIB")"
  echo "libflox_core_bytes=$(stat -c%s "$FLOX_CORE" 2>/dev/null || stat -f%z "$FLOX_CORE")"
} > "$OUT_DIR/flox_phase1b_artifacts.txt"

# Python baseline
PY="$OUT_DIR/flox_phase1b_python.json"
PYBIN=python3
if ! python3 -c "import websockets" 2>/dev/null; then
  if ! apt-get install -y -qq python3-websockets 2>/dev/null; then
    VENV="$OUT_DIR/.flox_phase1b_venv"
    python3 -m venv "$VENV"
    PYBIN="$VENV/bin/python"
    "$PYBIN" -m pip install -q websockets
  fi
fi
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$PYBIN" "$SCRIPT_DIR/flox_phase1b_polymarket_ws_baseline.py" \
  --token-id "$TOKEN" --duration "$DURATION" --out "$PY" || true

ITEST_SRC="$ROOT/connectors/tests/flox_phase1b_integration_test_polymarket.cpp"
if [[ ! -f "$ITEST_SRC" ]]; then
  echo "Missing $ITEST_SRC — copy flox_phase1b_integration_test_polymarket.cpp into connectors/tests/"
  exit 1
fi
ITEST_BIN="flox_phase1b_integration_test_polymarket"

apt-get install -y -qq libgtest-dev libgmock-dev 2>/dev/null || true

cd "$ROOT"
cmake -B build \
  -DFLOX_BUILD_CONNECTORS=ON \
  -DFLOX_ENABLE_POLYMARKET_ORDER_EXECUTOR=OFF \
  -DFLOX_BUILD_TESTS=ON \
  -DFLOX_BUILD_CONNECTOR_INTEGRATION_TESTS=ON 2>&1 | tail -3

cmake --build build --target "$ITEST_BIN" -j2 2>&1 | tail -8

BIN="$ROOT/build/connectors/tests/$ITEST_BIN"
FLOX_JSON="$OUT_DIR/flox_phase1b_flox.json"

export FLOX_PHASE1B_SKIP_STOP=1
timeout "$((DURATION + 30))" /usr/bin/time -f "max_rss_kb=%M elapsed_sec=%e" -o "$OUT_DIR/flox_phase1b_time.txt" \
  "$BIN" --gtest_filter=PolymarketExchangeConnectorIntegrationTest.ReceivesBookUpdates \
  2>&1 | tee "$OUT_DIR/flox_phase1b_flox.log" || true
unset FLOX_PHASE1B_SKIP_STOP

grep '^FLOX_PHASE1B_JSON=' "$OUT_DIR/flox_phase1b_flox.log" \
  | sed 's/^FLOX_PHASE1B_JSON=//' > "$FLOX_JSON" || echo '{}' > "$FLOX_JSON"

python3 - <<PY
import json
from pathlib import Path
out = Path("$OUT_DIR")
py = json.loads((out / "flox_phase1b_python.json").read_text())
fx = json.loads((out / "flox_phase1b_flox.json").read_text() or "{}")
summary = {
  "token_id_prefix": "$TOKEN"[:24],
  "duration_sec": int("$DURATION"),
  "python": py,
  "flox": fx,
  "verdict": "PASS" if py.get("book_updates",0)>0 and fx.get("book_updates",0)>0 else "PARTIAL",
}
(out / "flox_phase1b_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
print(json.dumps(summary, indent=2))
PY

echo "Wrote $OUT_DIR/flox_phase1b_summary.json"
