---
name: searchos-progress
description: >-
  Steal SearchOS explicit search-progress blackboard: coverage map, stop
  conditions, citation-backed evidence cells. Use for multi-step OSINT /
  wiki research when agents risk fail-loops or budget waste.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---
# SearchOS progress pattern (K173 Extract)

Clone + venv: `.local/adopts/SearchOS` · `.local/venvs/searchos`

## Agent must

When doing open-domain research with tools (Exa, fetch, web):

1. Write an explicit **coverage map** (questions / facets still empty).
2. Dispatch tool calls only for empty cells.
3. Store each evidence cell with source URL.
4. Stop when map is filled or budget hit — do not retry the same failed query.

## Optional full TUI

```bash
source .local/venvs/searchos/bin/activate
# see SearchOS README — needs API keys for search backends
```
