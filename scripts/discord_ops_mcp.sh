#!/usr/bin/env bash
# Cursor MCP entrypoint for discord-ops — sources local secrets then exec.
# Cursor.app does not inherit ~/.zprofile; do not rely on ${VAR} in mcp.json.
set -euo pipefail
ENV_FILE="${HOME}/.cemini/discord-ops.env"
if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi
export DISCORD_OPS_TOKEN_ENV="${DISCORD_OPS_TOKEN_ENV:-YOURATTO_DISCORD_BOT_TOKEN}"
export DISCORD_OPS_DRY_RUN="${DISCORD_OPS_DRY_RUN:-true}"

# CLI subcommands (health/validate/setup) — no MCP --tools flag
case "${1:-}" in
  health|validate|setup|listen|serve)
    exec npx -y discord-ops@latest "$@"
    ;;
esac

TOOLS="${DISCORD_OPS_TOOLS:-create_channel,delete_channel,edit_channel,get_channel,list_channels,set_slowmode,create_webhook,delete_webhook,edit_webhook,execute_webhook,get_webhook,list_webhooks,health_check,list_guilds,get_guild,assign_role,list_members,list_roles,create_invite,get_invites,send_message}"
exec npx -y discord-ops@latest --tools "$TOOLS" "$@"
