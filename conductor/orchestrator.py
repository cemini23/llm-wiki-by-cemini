"""Cemini Conductor — main pipeline.

Wires stages 1-4 together: taxonomy → pool → cascade → tools → response.
"""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime, timezone
from typing import Any

from conductor.api import DeepSeekClient
from conductor.calibration import CalibrationLogger
from conductor.cascade import CascadeRouter
from conductor.mcp_client import KBServerClient, StashClient
from conductor.models import ConductorResponse, Query, RoutingDecision
from conductor.pool import ModelPoolSelector
from conductor.taxonomy import TaxonomyClassifier
from conductor.tools import ToolOrchestrator

logger = logging.getLogger(__name__)


class Conductor:
    """Lightweight multi-model orchestrator.

    Usage:
        c = Conductor("conductor/config.yaml")
        resp = c.route("What is NVDA's IV rank?")
        print(resp.content)
    """

    def __init__(self, config_path: str) -> None:
        import yaml

        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        infra = self.config.get("infrastructure", {})
        self.api = DeepSeekClient(self.config)
        self.taxonomy = TaxonomyClassifier(self.config, self.api)
        self.pool_selector = ModelPoolSelector(self.config)
        self.cascade = CascadeRouter(self.config, self.api)
        kb_cfg = infra.get("kb_server", {})
        self.kb_client = KBServerClient(
            base_url=kb_cfg.get("url", ""),
            api_key=kb_cfg.get("api_key") or os.environ.get("LIBRARIAN_API_KEY", ""),
        )
        self.stash_client = StashClient()
        self.tools = ToolOrchestrator(self.config, self.kb_client, self.stash_client)
        self.calibration = CalibrationLogger(self.config, self.stash_client, api=self.api)

    def route(
        self, query_text: str, *, session_id: str = "default", source: str = "cli"
    ) -> ConductorResponse:
        """Route a single query through the full pipeline."""
        query = Query(
            text=query_text,
            source=source,
            session_id=session_id,
            timestamp=datetime.now(timezone.utc),
        )
        t0 = time.monotonic()

        # Stage 1 — classify
        taxonomy = self.taxonomy.classify(query)

        # Stage 2 — select model pool
        pool = self.pool_selector.select(taxonomy)

        # Stage 3 — tool orchestration (BEFORE cascade so context is pre-injected)
        tool_results = self.tools.orchestrate(query, taxonomy)

        # Pre-inject tool context into the query so the cascade gets it for free
        tool_ctx = self.tools.assemble_context(tool_results)
        augmented_query = query
        if tool_ctx:
            augmented_query = Query(
                text=f"Context from tools:\n{tool_ctx}\n\nUser query: {query.text}",
                source=query.source,
                session_id=query.session_id,
                timestamp=query.timestamp,
            )

        # Stage 4 — cascade route with confidence gate (returns content)
        routing, content, meta = self.cascade.route(augmented_query, pool)
        routing.taxonomy = taxonomy
        routing.query = query  # store original query, not augmented
        routing.selected_model = pool.models[0] if pool.models else pool.default_model
        routing.tool_calls = [tr.get("tool", "") for tr in tool_results]

        routing.cost_estimate = float(meta.get("cost_usd", 0.0))
        routing.latency_ms = (time.monotonic() - t0) * 1000

        # Log calibration data
        try:
            self.calibration.log(routing)
        except Exception as exc:
            logger.warning("Calibration log failed: %s", exc)

        return ConductorResponse(
            query=query,
            routing=routing,
            content=content,
            sources=[tr.get("tool", "") for tr in tool_results],
            tool_results=tool_results,
        )
