#!/usr/bin/env python3
"""K146 AST projection CLI — topological map without full implementation dumps.

Inspired by arXiv 2607.02389 (~200 LoC docs CLI pattern).

Usage:
  uv run python scripts/docs_cli.py module examples/cemini_decide.py
  uv run python scripts/docs_cli.py symbol examples/cemini_decide.py decide
  uv run python scripts/docs_cli.py audit [--gate] [--out-dir DIR]
"""
from __future__ import annotations

import argparse
import ast
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Sandbox submit surface — projection + substrate checks only on these paths.
DEFAULT_AUDIT_PATHS = (
    "examples/cemini_decide.py",
    "examples/cemini_trajectory_bound.py",
    "examples/harness_sandbox_agent.py",
    "examples/agent.py",
    "harness/strategy.py",
)

FORBIDDEN_CALLS = frozenset({"eval", "exec", "__import__"})
FORBIDDEN_ATTRS = frozenset({"system", "popen", "spawn"})  # os.system, subprocess.Popen, etc.


@dataclass
class SymbolInfo:
    kind: str
    name: str
    lineno: int
    signature: str
    doc: str


def _read_source(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _first_doc_line(node: ast.AST) -> str:
    doc = ast.get_docstring(node) or ""
    return doc.strip().split("\n")[0] if doc.strip() else ""


def _signature(node: ast.AST) -> str:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = [a.arg for a in node.args.args]
        return f"({', '.join(args)})"
    if isinstance(node, ast.ClassDef):
        return ""
    return ""


def _parse_module(path: Path) -> ast.Module:
    src = _read_source(path)
    return ast.parse(src, filename=str(path))


def cmd_module(path: Path) -> int:
    tree = _parse_module(path)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            print(f"def {node.name}{_signature(node)}  # L{node.lineno}  {_first_doc_line(node)}")
        elif isinstance(node, ast.ClassDef):
            print(f"class {node.name}  # L{node.lineno}  {_first_doc_line(node)}")
    return 0


def cmd_symbol(path: Path, name: str) -> int:
    tree = _parse_module(path)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name == name:
                print(f"{type(node).__name__.replace('Def', '').lower()} {name}{_signature(node)}")
                print(f"file: {path}:{node.lineno}")
                doc = ast.get_docstring(node) or "(no docstring)"
                print(doc)
                return 0
    print(f"symbol not found: {name}", file=sys.stderr)
    return 1


def _collect_symbols(path: Path) -> list[SymbolInfo]:
    tree = _parse_module(path)
    out: list[SymbolInfo] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.append(
                SymbolInfo(
                    "function",
                    node.name,
                    node.lineno,
                    _signature(node),
                    _first_doc_line(node),
                )
            )
        elif isinstance(node, ast.ClassDef):
            out.append(
                SymbolInfo(
                    "class",
                    node.name,
                    node.lineno,
                    "",
                    _first_doc_line(node),
                )
            )
    return out


def _find_forbidden_calls(path: Path) -> list[str]:
    tree = _parse_module(path)
    hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in FORBIDDEN_CALLS:
                hits.append(f"{path}:{node.lineno}: call {func.id}()")
            if isinstance(func, ast.Attribute) and func.attr in FORBIDDEN_ATTRS:
                hits.append(f"{path}:{node.lineno}: call .{func.attr}()")
    return hits


def _require_symbols(path: Path, names: frozenset[str]) -> list[str]:
    tree = _parse_module(path)
    found = {
        n.name
        for n in tree.body
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }
    return [f"missing required symbol {name} in {path}" for name in names if name not in found]


def _run_ruff(paths: list[Path]) -> tuple[bool, str]:
    ruff = shutil.which("ruff")
    if not ruff:
        return True, "ruff not installed — skipped (install ruff for stricter substrate)"
    cmd = [ruff, "check", "--select", "E9,F63,F7,F82", *[str(p) for p in paths]]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0, out.strip() or "(clean)"


def cmd_audit(*, gate: bool, out_dir: Path | None) -> int:
    missing_files: list[str] = []
    forbidden: list[str] = []
    topology: dict[str, list[dict]] = {}
    checked: list[str] = []

    for rel in DEFAULT_AUDIT_PATHS:
        path = ROOT / rel
        if not path.is_file():
            missing_files.append(rel)
            continue
        checked.append(rel)
        topology[rel] = [asdict(s) for s in _collect_symbols(path)]
        forbidden.extend(_find_forbidden_calls(path))

    decide = ROOT / "examples/cemini_decide.py"
    if decide.is_file():
        forbidden.extend(_require_symbols(decide, frozenset({"decide"})))

    ruff_ok, ruff_out = _run_ruff([ROOT / p for p in checked])

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checked": checked,
        "missing_files": missing_files,
        "forbidden_calls": forbidden,
        "ruff_ok": ruff_ok,
        "ruff_output": ruff_out,
        "topology": topology,
        "gate_pass": not missing_files and not forbidden and ruff_ok,
    }

    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "substrate_audit.json").write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )
        lines = [
            "K146 substrate audit",
            f"checked: {len(checked)} files",
            f"missing: {missing_files or 'none'}",
            f"forbidden: {forbidden or 'none'}",
            f"ruff: {'PASS' if ruff_ok else 'FAIL'}",
            "",
            "Topology (first-line docstrings):",
        ]
        for rel, syms in topology.items():
            lines.append(f"\n## {rel}")
            for s in syms[:40]:
                lines.append(f"  {s['kind']} {s['name']}{s['signature']}  L{s['lineno']}  {s['doc']}")
            if len(syms) > 40:
                lines.append(f"  ... +{len(syms) - 40} more")
        lines.extend(["", "ruff:", ruff_out])
        (out_dir / "substrate_topology.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({k: v for k, v in report.items() if k != "topology"}, indent=2))
    if gate and not report["gate_pass"]:
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="K146 docs CLI — AST projection for sandbox audit")
    sub = p.add_subparsers(dest="cmd", required=True)

    pm = sub.add_parser("module", help="List top-level symbols with doc first lines")
    pm.add_argument("path", type=Path)

    ps = sub.add_parser("symbol", help="Show one symbol docstring + signature")
    ps.add_argument("path", type=Path)
    ps.add_argument("name")

    pa = sub.add_parser("audit", help="Substrate audit for sandbox submit paths")
    pa.add_argument("--gate", action="store_true", help="Exit 1 on violations")
    pa.add_argument("--out-dir", type=Path, default=None)

    args = p.parse_args(argv)
    if args.cmd == "module":
        path = args.path if args.path.is_absolute() else ROOT / args.path
        return cmd_module(path)
    if args.cmd == "symbol":
        path = args.path if args.path.is_absolute() else ROOT / args.path
        return cmd_symbol(path, args.name)
    return cmd_audit(gate=args.gate, out_dir=args.out_dir)


if __name__ == "__main__":
    raise SystemExit(main())
