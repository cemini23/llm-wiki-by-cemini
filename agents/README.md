# Agents (private implementation)

Production wagering/poker bot code lives here — **not** in public `Gambling-wiki`.

| Path | Role |
|------|------|
| `devfun-poker-arena/` | dev.fun NLHE arena bot (`cemini_decide.py`), HL loop, deploy to cemini-prod |

Public wiki (`Gambling-wiki`) keeps venue docs, generic HL workflow, and poker strategy concepts only.

**Local symlink (optional, from Gambling-wiki root):**

```bash
ln -sf "../../OSINT WORKSPACE/agents/devfun-poker-arena" agents/devfun-poker-arena
```

Credentials (`.arena-credentials`, `.env`) stay gitignored in both repos.
