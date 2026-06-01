---
title: Wiki Dashboard
type: meta
tags: [dashboard, dataview, navigation]
created: 2026-04-26
updated: 2026-06-01
---

# Wiki Dashboard

Live in-editor views over the wiki frontmatter. Companion to `index.md` (catalog), `log.md` (chronological), and `_CLAUDE.md` (agent vault manual for `/obsidian-*` commands); this page gives **dynamic**, sortable tables that update automatically as pages change.

**Setup** (one-time, ~30 seconds):
1. Obsidian → Settings (`⌘,`) → Community plugins → Browse → search **Dataview** → Install + Enable
2. Settings → Community plugins → **Dataview** → toggle on **"Enable JavaScript queries"** (needed for the cited-unread query, which scans `related:` arrays across all pages)
3. Reload (`⌘R`) — every codeblock below should render as a live table

This page is excluded from `wiki_lint.py` orphan / bidir / dangling checks (same exemption as `index.md` and `log.md`).

**Path-scoping note**: queries below assume the Obsidian vault is the **workspace root** (where `.obsidian/` lives) and the wiki is at `wiki/`. If you re-opened Obsidian with `wiki/` itself as the vault root, change every `"wiki/..."` path below to drop the `wiki/` prefix (e.g. `FROM "sources"` → `FROM "sources"`).

---

## 0. Sanity check — Dataview is alive

If this block renders as a one-row table showing the vault name and a `.md` file count, Dataview is wired correctly and you can keep reading. If it renders as raw code, the Dataview plugin isn't actually enabled (Settings → Community plugins → make sure Dataview is toggled on, not just installed).

```dataviewjs
const allMd = dv.pages();
const sources = dv.pages('"sources"');
const concepts = dv.pages('"concepts"');
const entities = dv.pages('"entities"');
dv.table(
  ["Vault", "Total .md", "sources/", "entities/", "concepts/", "Dataview"],
  [[dv.app.vault.getName(), allMd.length, sources.length, entities.length, concepts.length, "running"]]
);
```

---

## 1. Cited-unread queue (live equivalent of `wiki_lint.py` output #5)

The next-deep-read priority list. Sources with `read_status: unread-stub` (or no `read_status` field on a `draft` source), ranked by how many other pages list them in `related:`. This is the live version of the J / K progression: J resolved the 13-inbound stub, K resolved the 12-inbound stub, K2 resolved an irony-grade hidden one — top of this table is the next candidate.

```dataviewjs
const sources = dv.pages('"sources"');
const inbound = {};
for (const p of dv.pages()) {
  const rel = p.related || [];
  for (const r of rel) {
    const target = String(r).replace(/\.md$/, "").replace(/^.*\//, "");
    inbound[target] = (inbound[target] || 0) + 1;
  }
}
const stubs = sources.where(p =>
  p.read_status === "unread-stub" ||
  (p.maturity === "draft" && p.read_status !== "validated")
);
const rows = stubs.array()
  .map(p => ({
    name: p.file.name,
    link: p.file.link,
    inbound: inbound[p.file.name] || 0,
    cluster: (p.clusters && p.clusters[0]) || "—",
    updated: p.updated || "—"
  }))
  .filter(r => r.inbound > 0)
  .sort((a, b) => b.inbound - a.inbound)
  .slice(0, 25);
dv.table(
  ["Source", "Inbound", "Primary cluster", "Updated"],
  rows.map(r => [r.link, r.inbound, r.cluster, r.updated])
);
```

---

## 2. Recently-updated pages (last 25)

What's been touched lately, across all wiki types. Useful right after a session to confirm everything intended got an `updated:` bump.

```dataview
TABLE updated, type, maturity
WHERE updated AND file.name != "dashboard"
SORT updated DESC
LIMIT 25
```

---

## 3. Draft pages by staleness (oldest first)

Drafts that haven't been touched in a while — staleness signal. If a draft has been sitting > 30 days, it probably wants either promotion to `validated` or a deliberate decision to leave it.

```dataview
TABLE updated, type, length(related) AS "out-edges"
WHERE maturity = "draft" AND type != "meta"
SORT updated ASC
LIMIT 30
```

---

## 4. Source-cluster distribution

Where the corpus weight actually lives. Confirms the heavy clusters (rl-marl ~108, llm-agents ~60) and surfaces under-covered ones.

```dataviewjs
const sources = dv.pages('"sources"');
const counts = {};
for (const p of sources) {
  const cl = (p.clusters && p.clusters[0]) || "—";
  counts[cl] = (counts[cl] || 0) + 1;
}
const rows = Object.entries(counts).sort((a, b) => b[1] - a[1]);
dv.table(["Primary cluster", "Source count"], rows);
```

---

## 5. Tickers by category + maturity

Watchlist-companion view. Should match `entities/ticker-watchlist.md` and the server's `tickers.json` categories. Indexed = page exists at `entities/tickers/<symbol>.md`; pending = stub or not yet ingested.

```dataview
TABLE category, ticker, maturity, updated
FROM "entities/tickers"
SORT category, ticker
```

---

## 6. Concept hubs by outbound count

The cluster-hub topology D / D′ built out — concept pages that aggregate many sources. Top of this list should be the corpus-index hubs (`rl-marl-research`, `llm-agent-systems`, plus the tickers / kalshi / kelly-cvar secondary hubs).

```dataview
TABLE length(related) AS "outbound-edges", maturity
FROM "concepts"
WHERE related
SORT length(related) DESC
LIMIT 20
```

Plus entity hubs (ticker-watchlist, kelly-cvar-risk-engine, kalshi, langgraph, etc.):

```dataview
TABLE length(related) AS "outbound-edges", type, maturity
FROM "entities"
WHERE length(related) >= 5
SORT length(related) DESC
LIMIT 20
```

---

## 7. Maturity × type matrix

Pipeline view. Mostly-`draft` rows mean the column needs deep-read investment; mostly-`validated` rows mean the column is healthy.

```dataviewjs
const all = dv.pages().where(p => p.type && p.type !== "meta");
const matrix = {};
for (const p of all) {
  const t = p.type || "—";
  const m = p.maturity || "—";
  matrix[t] = matrix[t] || {};
  matrix[t][m] = (matrix[t][m] || 0) + 1;
}
const allMaturities = ["draft", "validated", "core", "retracted"];
const rows = Object.entries(matrix).map(([t, ms]) => [
  t,
  ...allMaturities.map(m => ms[m] || 0),
  Object.values(ms).reduce((a, b) => a + b, 0)
]);
dv.table(
  ["Type", ...allMaturities, "Total"],
  rows.sort((a, b) => b[5] - a[5])
);
```

---

## 8. Validated reads — the deep-read trail

Every source that's been promoted to `read_status: validated` (the J / K / K2 progression). Builds the deep-read history at a glance.

```dataview
TABLE updated, length(related) AS "out-edges", clusters
FROM "sources"
WHERE read_status = "validated"
SORT updated DESC
```

---

## Notes for future query authors

- **Frontmatter access**: any YAML field is accessible as `p.fieldname` in dataviewjs, or referenced bare in a dataview query (`WHERE maturity = "draft"`).
- **`related:` is a list**: use `length(related)` for outbound-count, or iterate it for inbound-count (see queries 1 + 4).
- **Path scoping**: `FROM "sources"` = `wiki/sources/**` (when vault root = `wiki/`); omit `FROM` entirely or use `FROM ""` to scan the whole vault. Don't use `FROM "wiki"` — that resolves to `wiki/wiki/` and matches nothing in our setup.
- **`file.link` renders as a clickable Obsidian link** in dataviewjs `dv.table` rows.
- **Refresh a single query**: hover over its codeblock and click the refresh icon in the top-right.
- **Performance**: dataviewjs queries scan all pages on render; at our scale (333 pages) this is instant, but if the corpus grows past ~2000 pages, scope the `dv.pages()` calls more tightly.
