#!/usr/bin/env python3
"""One-shot patch for cemini-egress-fi pipeline.py — K57 Polymarket copy disclosure."""
from pathlib import Path

PIPELINE = Path("/opt/cemini-ai/cemini_ai/pipeline.py")
MARKER = "POLYMARKET COPY-TRADING (K57)"
OLD = (
    '    "do something outside that set, say so plainly and decline to claim "\n'
    '    "otherwise."\n'
    ")"
)
NEW = (
    '    "do something outside that set, say so plainly and decline to claim "\n'
    '    "otherwise."\n'
    '    "\\n\\nPOLYMARKET COPY-TRADING (K57). Polymarket uses a hybrid CLOB: "\n'
    '    "leader matches are off-chain; followers observe via mempool/settlement, not "\n'
    '    "at match time. Marketing \\"0-block\\" means the same Polygon settlement "\n'
    '    "block as the leader, not zero detection lag. Do not promise sub-block copy "\n'
    '    "parity or HFT-grade mirror-bot latency without measured end-to-end fill "\n'
    '    "latency."\n'
    ")"
)


def main() -> int:
    text = PIPELINE.read_text(encoding="utf-8")
    if MARKER in text:
        print("already patched")
        return 0
    if OLD not in text:
        raise SystemExit("expected CAPABILITY HONESTY closing block not found")
    PIPELINE.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
    print("patched", PIPELINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
