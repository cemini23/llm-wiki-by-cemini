#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "Clone: ${ROOT}/.local/adopts/code-review-graph"
echo "Docs:  ${ROOT}/.local/adopts/code-review-graph/docs/USAGE.md"
echo "Typical: cd repo && pip install code-review-graph && code-review-graph --help"
echo "MCP: see upstream README for Cursor/Claude MCP server config"
