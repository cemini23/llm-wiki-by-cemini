"""MCP clients for kb-server and Stash.

kb-server uses the REST API at /api/v1 (X-API-Key auth).
Stash uses CLI subprocess (its HTTP endpoint is metrics-only).
All clients degrade gracefully when the remote is unreachable.
"""

from __future__ import annotations

import json
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# kb-server — wiki RAG via REST API (read-only)
# ---------------------------------------------------------------------------


class KBServerClient:
    """Read-only kb-server client via REST API at /api/v1.

    Authenticates via X-API-Key header using the key from config.
    Falls back to kb CLI on connection failure.
    """

    _KB_BIN = "/usr/bin/kb"

    def __init__(self, base_url: str = "", api_key: str = "", timeout: float = 10.0) -> None:
        self._base_url = base_url.rstrip("/") if base_url else ""
        self._api_key = api_key
        self.timeout = timeout

    # -- public API ----------------------------------------------------------

    def search(self, query: str, max_results: int = 5) -> list[dict[str, Any]]:
        """Full-text search across the wiki vault via REST API."""
        result = self._get("/api/v1/search", params={"q": query, "limit": str(max_results)})
        if result is not None:
            return result.get("results", [])[:max_results]
        return self._kb_search_fallback(query, max_results)

    def smart_search(self, query: str, max_results: int = 10) -> list[dict[str, Any]]:
        """Hybrid semantic + keyword search via REST API."""
        result = self._get("/api/v1/search/smart", params={"q": query, "limit": str(max_results)})
        if result is not None:
            return result.get("results", [])[:max_results]
        return self.search(query, max_results)

    def context(self, topic: str, max_results: int = 15) -> str:
        """Token-efficient topic briefing via REST API."""
        result = self._get("/api/v1/context", params={"q": topic, "limit": str(max_results)})
        if result is not None:
            briefing = result.get("briefing", "")
            if briefing:
                return briefing
        # Fallback: search and format manually
        results = self.search(topic, max_results=5)
        if results:
            return json.dumps(results, indent=2)
        return ""

    def read(self, doc_id: int) -> str:
        """Read full document content by ID via REST API."""
        result = self._get(f"/api/v1/documents/{doc_id}")
        if result is not None:
            return json.dumps(result)
        return ""

    # -- HTTP helpers --------------------------------------------------------

    def _headers(self) -> dict[str, str]:
        h: dict[str, str] = {"Accept": "application/json"}
        if self._api_key:
            h["X-API-Key"] = self._api_key
        return h

    def _get(self, path: str, params: dict[str, str] | None = None) -> dict[str, Any] | None:
        """GET a JSON endpoint. Returns parsed response or None on failure."""
        if not self._base_url:
            return None
        try:
            r = httpx.get(
                f"{self._base_url}{path}",
                params=params,
                headers=self._headers(),
                timeout=self.timeout,
            )
            if r.status_code == 200:
                return r.json()
            logger.warning("kb-server %s returned HTTP %s", path, r.status_code)
            return None
        except Exception as exc:
            logger.warning("kb-server %s error: %s", path, exc)
            return None

    # -- CLI fallback --------------------------------------------------------

    def _kb_search_fallback(
        self, query: str, limit: int = 5
    ) -> list[dict[str, Any]]:
        """Fallback to kb CLI when MCP is unavailable."""
        import subprocess
        try:
            result = subprocess.run(
                [self._KB_BIN, "search", query],
                capture_output=True, text=True,
                timeout=self.timeout,
            )
            if result.returncode == 0:
                return self._parse_cli_search(result.stdout, limit)
            logger.warning("kb CLI search failed: %s", result.stderr.strip())
            return []
        except Exception as exc:
            logger.warning("kb CLI search error: %s", exc)
            return []

    @staticmethod
    def _parse_cli_search(stdout: str, limit: int) -> list[dict[str, Any]]:
        """Parse `kb search` CLI output into structured results."""
        if not stdout.strip():
            return []
        results: list[dict[str, Any]] = []
        current: dict[str, Any] | None = None
        for line in stdout.strip().split("\n"):
            line = line.rstrip()
            import re
            m = re.match(r"^(\d+)\.\s+\[(\w+)\]\s+(.+)", line)
            if m:
                if current:
                    results.append(current)
                current = {"rank": int(m.group(1)), "type": m.group(2),
                           "title": m.group(3), "snippet": ""}
            elif current is not None and line.startswith("   "):
                current["snippet"] += line.strip() + " "
            elif current is not None and line.strip():
                current["snippet"] += line.strip() + " "
        if current:
            results.append(current)
        return results[:limit]


# ---------------------------------------------------------------------------
# Stash — episodic memory (read + write)
# ---------------------------------------------------------------------------


class StashClient:
    """Stash episodic memory client.

    Uses the stash CLI directly (the HTTP :9090 endpoint is metrics/health only).
    Reads env vars from /opt/stash/.env for database + ollama connectivity.
    """

    _ENV_FILE = "/opt/stash/.env"
    _BINARY = "/opt/stash/stash-linux-x86_64"

    def __init__(self, http_url: str = "", mcp_url: str = "", timeout: float = 10.0) -> None:
        self.timeout = timeout
        self._namespace = "/cemini/conductor"
        self._env = self._load_env()
        self._ns_ready = False

    def _load_env(self) -> dict[str, str]:
        env = {}
        try:
            with open(self._ENV_FILE) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        env[k.strip()] = v.strip()
        except FileNotFoundError:
            logger.warning("Stash env file not found: %s", self._ENV_FILE)
        return env

    # -- write ---------------------------------------------------------------

    def _ensure_namespace(self) -> None:
        """Create the Conductor namespace if it doesn't exist."""
        if self._ns_ready:
            return
        import subprocess
        try:
            subprocess.run(
                [self._BINARY, "namespace", "create", self._namespace],
                capture_output=True, text=True,
                timeout=self.timeout,
                env={**self._env},
            )
        except Exception:
            pass
        self._ns_ready = True

    def store_episode(
        self, content: str, metadata: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Store a routing decision as an episode via stash CLI."""
        self._ensure_namespace()
        import subprocess
        try:
            result = subprocess.run(
                [self._BINARY, "remember", "-n", self._namespace, content],
                capture_output=True, text=True,
                timeout=self.timeout,
                env={**self._env},
            )
            if result.returncode == 0:
                return {"status": "ok", "stdout": result.stdout.strip()}
            logger.warning("Stash remember failed: %s", result.stderr.strip())
            return None
        except Exception as exc:
            logger.warning("Stash remember error: %s", exc)
            return None

    def store_fact(
        self, fact: str, confidence: float = 1.0, metadata: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Store a fact via stash CLI."""
        return self.store_episode(fact, metadata)

    # -- read ----------------------------------------------------------------

    def query_facts(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        """Query Stash for relevant facts/episodes via stash CLI recall."""
        if not query.strip():
            return []
        import subprocess
        try:
            result = subprocess.run(
                [self._BINARY, "recall", "-n", self._namespace, "--limit", str(limit), query],
                capture_output=True, text=True,
                timeout=self.timeout,
                env={**self._env},
            )
            if result.returncode == 0:
                return self._parse_recall(result.stdout)
            logger.warning("Stash recall failed: %s", result.stderr.strip())
            return []
        except Exception as exc:
            logger.warning("Stash recall error: %s", exc)
            return []

    def query_episodes(
        self, namespace: str | None = None, limit: int = 50
    ) -> list[dict[str, Any]]:
        """Query recent episodes. Stash recall requires a query, so we use a broad
        wildcard that matches routing_decision episodes."""
        return self.query_facts("routing_decision", limit=limit)

    @staticmethod
    def _parse_recall(stdout: str) -> list[dict[str, Any]]:
        """Parse stash recall JSON output into structured results."""
        if not stdout.strip():
            return []
        try:
            parsed = json.loads(stdout)
            if isinstance(parsed, list):
                return parsed
            return [parsed]
        except json.JSONDecodeError:
            # Fallback: plain-text lines
            return [{"content": line.strip()} for line in stdout.strip().split("\n") if line.strip()]
