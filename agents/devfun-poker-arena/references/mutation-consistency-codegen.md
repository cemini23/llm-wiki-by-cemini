# Mutation-consistency codegen checks (K235)

When agents rewrite configs, ranges, charts, or codegen helpers: prefer
**mutation-consistency** metamorphic oracles over crash-only fuzz.

## Steal

1. Small, intentional input change → predictable **structural** output change.
2. Example (Arena): flip `CEMINI_TAG_WIDEN` 0→1 must expand BB defend (88 call/raise)
   vs fold-off; do not require EV claims.
3. Name collision: **MCP-Tester** here = Mutation Consistency of Programs — **not**
   Model Context Protocol.

## Do not

- Runtime-wire Zenodo `mcp-tester-transpiler` into lobby / prod
- Treat metamorphic chart checks as multi-regime EV proof

## Sources

- `briefs/2026-08-03_k235-k236-mutation-memory-steal.md`
- CCC `.cursor/rules/cemini-phase1-policy-wires.mdc` (K235)
- REFERENCE clone (optional): OSINT/CCC `.local/adopts/mcp-tester-transpiler`
