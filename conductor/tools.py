"""Stage 4 — Tool orchestrator.

Selects and invokes external tools based on the query's taxonomy class.
Results are injected as structured context into the model prompt.
"""

from __future__ import annotations

import logging
from typing import Any

from conductor.mcp_client import KBServerClient, StashClient
from conductor.models import Query, TaxonomyClass

logger = logging.getLogger(__name__)


class ToolOrchestrator:
    """Deterministic tool selection driven by taxonomy → tool map in config."""

    def __init__(
        self,
        config: dict[str, Any],
        kb_client: KBServerClient,
        stash_client: StashClient,
    ) -> None:
        self._kb = kb_client
        self._stash = stash_client
        self._tool_map: dict[str, list[str]] = {}
        for class_id, entry in config.get("tool_orchestration", {}).items():
            self._tool_map[class_id] = list(entry.get("tools", []))
        self._default_tools: list[str] = ["kb_search"]

    def orchestrate(
        self, query: Query, taxonomy: TaxonomyClass
    ) -> list[dict[str, Any]]:
        """Run configured tools for the query's taxonomy class. Returns tool results."""
        tools = self._tool_map.get(taxonomy.name, self._default_tools)
        results: list[dict[str, Any]] = []
        for tool in tools:
            try:
                result = self._invoke(tool, query)
                if result:
                    results.append(result)
            except Exception as exc:
                logger.warning("Tool %s failed: %s", tool, exc)
        return results

    # -- tool dispatch -------------------------------------------------------

    def _invoke(self, tool: str, query: Query) -> dict[str, Any] | None:
        if tool == "kb_search":
            return self._run_kb_search(query)
        if tool == "stash_recall":
            return self._run_stash_recall(query)
        logger.warning("Unknown tool: %s", tool)
        return None

    def _run_kb_search(self, query: Query) -> dict[str, Any]:
        hits = self._kb.search(query.text, max_results=5)
        return {
            "tool": "kb_search",
            "query": query.text,
            "results": hits,
            "count": len(hits),
        }

    def _run_stash_recall(self, query: Query) -> dict[str, Any]:
        facts = self._stash.query_facts(query.text, limit=5)
        return {
            "tool": "stash_recall",
            "query": query.text,
            "results": facts,
            "count": len(facts),
        }

    # -- context assembly (used by orchestrator to build final prompt) -------

    def assemble_context(self, tool_results: list[dict[str, Any]]) -> str:
        """Turn tool results into a compact context string for the model prompt."""
        if not tool_results:
            return ""

        parts: list[str] = []
        for tr in tool_results:
            tool_name = tr.get("tool", "unknown")
            results = tr.get("results", [])
            if not results:
                continue
            if tool_name == "kb_search":
                parts.append("## Wiki Search Results\n")
                for r in results[:5]:
                    if isinstance(r, dict):
                        title = r.get("title", r.get("path", "—"))
                        snippet = r.get("snippet", r.get("content", ""))[:300]
                        parts.append(f"- **{title}**: {snippet}")
            elif tool_name == "stash_recall":
                parts.append("## Memory Recall\n")
                for r in results[:5]:
                    if isinstance(r, dict):
                        content = r.get("content", str(r))[:300]
                        parts.append(f"- {content}")

        return "\n".join(parts)
