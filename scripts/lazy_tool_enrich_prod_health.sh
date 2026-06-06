#!/usr/bin/env bash
# Post-reindex search aliases for prod-mcp health tools (K101 smoke finding).
# Run after: lazy-tool reindex --config .cursor/lazy-tool.yaml
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG="$ROOT/.cursor/lazy-tool.yaml"

lazy-tool --config "$CONFIG" catalog set-summary prod-mcp__get_stream_health \
  "Prod stack health: Redis Streams length, consumer groups, pending/lag per intel:* channel. Aliases: polymarket health, stream health, MCP lag monitoring, intel bus."

lazy-tool --config "$CONFIG" catalog set-summary prod-mcp__get_data_health \
  "Prod data freshness: redis/postgres status, intel:* source ages and TTLs. Aliases: polymarket health, prod health, data health, intel staleness."

echo "lazy-tool prod health search aliases set."
