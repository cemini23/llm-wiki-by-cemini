"""Cost-ceiling telemetry recorder for reviewer-agent invocations.

Per spec Requirement "Cost-ceiling telemetry": the system MUST record
the tool name, the trigger bucket, the input-token count, and the
output-token count for each reviewer-agent invocation. Recording is
buffered (batched flush) to keep the reviewer-agent call site fast —
strict-async (asyncio / background thread) would add complexity without
clear benefit at expected review volumes.

Storage format: append-only NDJSON (one JSON object per line) at the
configured path. Each record:

    {"ts": "ISO-8601 UTC", "tool": "...", "bucket": "...",
     "in_tokens": int, "out_tokens": int}

This raw log feeds :mod:`conductor.reviewer.cost_aggregator` for the
daily roll-up + monthly spend estimate (Task 3.2 / 3.3).

Spec: openspec/changes/reviewer-agent-selective-trigger/specs/reviewer-agent-selective-trigger/spec.md
Tasks: openspec/changes/reviewer-agent-selective-trigger/tasks.md (3.1)
"""

from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Union

from conductor.reviewer.trigger_policy import Bucket

# Default NDJSON log path. Operators override per-deployment; tests use
# a tempfile path. The directory is created lazily on first flush.
DEFAULT_TELEMETRY_PATH = Path.home() / ".cemini" / "reviewer_telemetry.ndjson"


class TelemetryWriter:
    """Buffered NDJSON telemetry writer.

    Each :meth:`record` appends an entry to an in-memory buffer. The
    buffer is flushed to disk when:

      * ``buffer_size`` records have accumulated (auto-flush)
      * :meth:`flush` is called explicitly
      * The instance is used as a context manager and ``__exit__`` runs

    Thread-safe: a mutex guards the buffer + flush so concurrent
    ``record`` callers from different threads don't interleave writes.

    Flush is atomic at the line level: we open the file in append mode
    and write each JSON line in a single ``write`` call. NDJSON is
    crash-resilient — a partial last line on disk crash truncates one
    record at worst.
    """

    def __init__(
        self,
        path: Union[str, Path] = DEFAULT_TELEMETRY_PATH,
        buffer_size: int = 100,
    ) -> None:
        """
        Args:
            path: NDJSON log path. Parent directory is created lazily.
            buffer_size: Flush threshold; default 100. Use ``1`` for
                tests or sites that want immediate durability.
        """
        if buffer_size < 1:
            raise ValueError(f"buffer_size must be >= 1, got {buffer_size}")
        self.path = Path(path)
        self.buffer_size = buffer_size
        self._buffer: List[dict] = []
        self._lock = threading.Lock()

    def record(
        self,
        tool_name: str,
        bucket: Bucket,
        input_tokens: int,
        output_tokens: int,
        *,
        ts: Optional[datetime] = None,
    ) -> None:
        """Record one reviewer-agent invocation.

        Typically the caller only emits records for calls that the
        reviewer actually saw — i.e., the trigger-policy classified
        them as ``ALWAYS_REVIEW`` (terminal). Calls that skip review
        consume no reviewer tokens and don't belong in the cost log.
        The caller decides; this function does not filter.

        Args:
            tool_name: Tool whose call triggered review.
            bucket: Originating policy bucket. (Stored verbatim for the
                aggregator; matches ``Bucket.value``, e.g.
                ``"always-review"``.)
            input_tokens: Reviewer-agent input token count.
            output_tokens: Reviewer-agent output token count.
            ts: Timestamp override; default is ``datetime.now(UTC)``.
        """
        entry = {
            "ts": (ts or datetime.now(timezone.utc)).isoformat(),
            "tool": tool_name,
            "bucket": bucket.value,
            "in_tokens": int(input_tokens),
            "out_tokens": int(output_tokens),
        }
        with self._lock:
            self._buffer.append(entry)
            if len(self._buffer) >= self.buffer_size:
                self._flush_locked()

    def flush(self) -> int:
        """Flush buffered records to disk.

        Returns:
            Number of records flushed (zero if buffer is empty).
        """
        with self._lock:
            return self._flush_locked()

    def _flush_locked(self) -> int:
        """Flush helper. The caller MUST already hold ``self._lock``."""
        if not self._buffer:
            return 0
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            for entry in self._buffer:
                # ``separators`` produces a compact one-line JSON object —
                # keeps the NDJSON one-record-per-line invariant.
                fh.write(json.dumps(entry, separators=(",", ":")) + "\n")
        flushed = len(self._buffer)
        self._buffer.clear()
        return flushed

    def __enter__(self) -> "TelemetryWriter":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.flush()


def record(
    tool_name: str,
    bucket: Bucket,
    input_tokens: int,
    output_tokens: int,
    *,
    path: Union[str, Path] = DEFAULT_TELEMETRY_PATH,
) -> None:
    """One-shot convenience wrapper for sites that don't manage a writer.

    Opens a :class:`TelemetryWriter` with ``buffer_size=1``, records,
    flushes, closes. Less efficient than reusing a writer across a
    burst of calls; appropriate for sparse / one-off invocations.

    Args:
        tool_name: Tool whose call triggered review.
        bucket: Originating policy bucket.
        input_tokens: Reviewer-agent input token count.
        output_tokens: Reviewer-agent output token count.
        path: NDJSON log path (default :data:`DEFAULT_TELEMETRY_PATH`).
    """
    with TelemetryWriter(path=path, buffer_size=1) as writer:
        writer.record(tool_name, bucket, input_tokens, output_tokens)
