#!/usr/bin/env bash
# Step 197 — verify build toolchain before FLOX connector compile (off-prod).
set -euo pipefail
need=(cmake g++ openssl cargo)
missing=()
for c in "${need[@]}"; do
  command -v "$c" >/dev/null 2>&1 || missing+=("$c")
done
if ((${#missing[@]})); then
  echo "MISSING: ${missing[*]}"
  echo "Install on a dev host, not prod VPS, then:"
  echo "  cmake -B build -DFLOX_BUILD_CONNECTORS=ON -DFLOX_ENABLE_POLYMARKET_ORDER_EXECUTOR=OFF"
  exit 1
fi
echo "Toolchain OK for FLOX connectors build (Polymarket executor can stay OFF)."
exit 0
