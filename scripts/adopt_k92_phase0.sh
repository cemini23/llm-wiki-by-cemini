#!/usr/bin/env bash
# Idempotent K92 Phase-0 laptop adoptions (2026-06-01).
# GO: claude-trading-skills (subset), obsidian-second-brain, rlcard venv.
# Steal-from: documented on wiki only (WagerBrain, casino-server).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_VAULT="$ROOT/wiki"
PHASE0="${PHASE0:-/tmp/k92-phase0}"
TRADING_REPO="${PHASE0}/claude-trading-skills"
OBSIDIAN_SKILL="$HOME/.claude/skills/obsidian-second-brain"

echo "==> rlcard research venv"
bash "$ROOT/scripts/gambling_research_venv.sh"

echo "==> claude-trading-skills (no-API starter set)"
if [[ ! -d "$TRADING_REPO/skills" ]]; then
  echo "Clone missing: git clone --depth 1 https://github.com/tradermonty/claude-trading-skills.git $TRADING_REPO"
  exit 1
fi
for s in market-breadth-analyzer uptrend-analyzer position-sizer trader-memory-core signal-postmortem; do
  src="$TRADING_REPO/skills/$s"
  dst="$HOME/.claude/skills/trading-$s"
  [[ -d "$src" ]] || { echo "missing skill $s"; exit 1; }
  rm -rf "$dst"
  cp -R "$src" "$dst"
  echo "  $dst"
done

echo "==> obsidian-second-brain (vault=$WIKI_VAULT)"
if [[ ! -d "$OBSIDIAN_SKILL/.git" ]]; then
  git clone --depth 1 https://github.com/eugeniughelbur/obsidian-second-brain.git "$OBSIDIAN_SKILL"
fi
bash "$OBSIDIAN_SKILL/scripts/setup.sh" "$WIKI_VAULT"

echo "==> Cemini policy reminder"
POLICY="$ROOT/.local/obsidian-second-brain-cemini-policy.md"
if [[ ! -f "$POLICY" ]]; then
  mkdir -p "$ROOT/.local"
  cat >"$POLICY" <<EOF
# obsidian-second-brain — Cemini guardrails (K92 adopt)

- **Vault:** \`wiki/\` only (git-tracked). Never point agents at \`cemini-librarian\` synced copy.
- **Background agent:** leave \`OBSIDIAN_BG_AGENT_ENABLED\` unset (PostCompact hook inert).
- **Cron / launchd:** do not enable until operator opts in; proposals under \`/tmp/cemini-osb-proposals/\` first.
- **Research APIs:** optional; keys in \`~/.config/obsidian-second-brain/.env\` only.
- **Next step:** run \`/obsidian-init\` once in Claude Code with vault cwd = wiki/.
EOF
fi

echo "Done. Trading skills: trading-* ; Obsidian: $OBSIDIAN_SKILL ; rlcard: .local/venv-gambling-research"
