#!/usr/bin/env python3
"""Build reviewer-agent passive-injection context bundle from manifest.yaml.

Offline only — not on the reviewer critical path. Fails closed when any
manifest entry is missing or a requested section/heading is absent.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

CORPUS_DIR = Path(__file__).resolve().parent
REVIEWER_DIR = CORPUS_DIR.parent
WORKSPACE_ROOT = REVIEWER_DIR.parent.parent
MANIFEST_PATH = CORPUS_DIR / "manifest.yaml"

# Federation wiki roots (laptop canonical paths; first match wins).
_WIKI_SUFFIXES: dict[str, tuple[str, ...]] = {
    "osint": ("wiki",),
    "ccc": ("Cemini claude code CCC", "wiki"),
    "cybersec": ("Cybersecurity wiki", "wiki"),
    "gambling": ("Gambling wiki", "wiki"),
}
_WIKI_SEARCH_BASES = (
    WORKSPACE_ROOT.parent / "projects",
    Path.home() / "Projects",
    Path.home() / "Desktop/projects",
)


@dataclass(frozen=True)
class ManifestEntry:
    id: str
    type: str
    path: str
    wiki: str = "osint"
    mode: str = "extract"
    sections: tuple[str, ...] = ()
    narrative_headings: tuple[str, ...] = ()
    rationale: str = ""


def _wiki_root(alias: str) -> Path:
    if alias not in _WIKI_SUFFIXES:
        raise ValueError(f"unknown wiki alias: {alias!r}")
    if alias == "osint":
        local = WORKSPACE_ROOT / "wiki"
        if local.is_dir():
            return local
    parts = _WIKI_SUFFIXES[alias]
    for base in _WIKI_SEARCH_BASES:
        candidate = base.joinpath(*parts)
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(
        f"wiki root for {alias!r} not found under {_WIKI_SEARCH_BASES}",
    )


def _wiki_alias_label(alias: str) -> str:
    return {
        "osint": "osint-wiki",
        "ccc": "ccc-wiki",
        "cybersec": "cybersec-wiki",
        "gambling": "gambling-wiki",
    }.get(alias, alias)


def _load_manifest(path: Path) -> tuple[str, list[ManifestEntry]]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    entries: list[ManifestEntry] = []
    for item in raw["entries"]:
        sections = tuple(item.get("sections") or ())
        headings = tuple(item.get("narrative_headings") or ())
        entries.append(
            ManifestEntry(
                id=item["id"],
                type=item["type"],
                path=item["path"],
                wiki=item.get("wiki", "osint"),
                mode=item.get("mode", "extract"),
                sections=sections,
                narrative_headings=headings,
                rationale=item.get("rationale", ""),
            )
        )
    return raw["bundle_output"], entries


def _split_sections(body: str) -> dict[str, str]:
    parts: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            parts[current] = []
            continue
        if current is not None:
            parts[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in parts.items()}


def _extract_heading_blocks(text: str, headings: tuple[str, ...]) -> str:
    if not headings:
        return text.strip()
    blocks: list[str] = []
    lines = text.splitlines()
    wanted = {h.removeprefix("### ").strip() for h in headings}
    i = 0
    while i < len(lines):
        if lines[i].startswith("### "):
            title = lines[i][4:].strip()
            if title in wanted:
                chunk = [lines[i]]
                i += 1
                while i < len(lines) and not lines[i].startswith("### "):
                    chunk.append(lines[i])
                    i += 1
                blocks.append("\n".join(chunk).strip())
                continue
        i += 1
    if len(blocks) != len(headings):
        found = {b.splitlines()[0][4:].strip() for b in blocks}
        missing = wanted - found
        raise ValueError(f"missing narrative headings: {sorted(missing)}")
    return "\n\n".join(blocks)


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def _extract_wiki(path: Path, entry: ManifestEntry) -> str:
    text = path.read_text(encoding="utf-8")
    body = _strip_frontmatter(text)
    sections = _split_sections(body)
    chunks: list[str] = []
    for section in entry.sections:
        if section not in sections:
            raise ValueError(f"missing ## {section} in {path}")
        content = sections[section]
        if section == "Narrative" and entry.narrative_headings:
            content = _extract_heading_blocks(content, entry.narrative_headings)
        if not content.strip():
            raise ValueError(f"empty ## {section} in {path}")
        chunks.append(f"## {section}\n\n{content.strip()}")
    return "\n\n".join(chunks)


def _resolve_path(entry: ManifestEntry) -> Path:
    if entry.type == "wiki":
        return _wiki_root(entry.wiki) / entry.path
    if entry.type == "file":
        return (CORPUS_DIR / entry.path).resolve()
    raise ValueError(f"unknown entry type: {entry.type}")


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_bundle(manifest_path: Path = MANIFEST_PATH) -> str:
    bundle_name, entries = _load_manifest(manifest_path)
    out_parts: list[str] = [
        "# Conductor reviewer — passive injection context bundle",
        "",
        f"> Generated {date.today().isoformat()} from `{manifest_path.relative_to(WORKSPACE_ROOT)}`.",
        "> Do not edit by hand — run `bash scripts/build_reviewer_context.sh`.",
        "",
        "This bundle is injected into the K37 reviewer-agent prompt at invocation time.",
        "It is **not** retrieved via kb_search. Sprint 5 prod wiring is DEFERRED.",
        "",
        "---",
        "",
    ]
    manifest_hash_inputs: list[str] = []

    for entry in entries:
        src = _resolve_path(entry)
        if not src.is_file():
            raise FileNotFoundError(f"[{entry.id}] missing source: {src}")

        if entry.type == "file" and entry.mode == "verbatim":
            content = src.read_text(encoding="utf-8").strip()
            header = f"## [{entry.id}] {src.name} (verbatim)"
        else:
            content = _extract_wiki(src, entry)
            header = f"## [{entry.id}] @{_wiki_alias_label(entry.wiki)}/{entry.path}"

        manifest_hash_inputs.append(entry.id + content)
        out_parts.extend([header, "", content, "", "---", ""])

    bundle = "\n".join(out_parts).rstrip() + "\n"
    bundle_digest = _sha256("".join(manifest_hash_inputs))
    banner = (
        f"<!-- bundle_sha256_prefix: {bundle_digest} | entries: {len(entries)} -->\n"
    )
    return banner + bundle, bundle_name


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MANIFEST_PATH,
        help="Path to manifest.yaml",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print bundle to stdout instead of writing file",
    )
    args = parser.parse_args(argv)

    try:
        bundle, bundle_name = build_bundle(args.manifest)
    except (FileNotFoundError, ValueError) as exc:
        print(f"build_context_bundle: ERROR: {exc}", file=sys.stderr)
        return 1

    if args.stdout:
        sys.stdout.write(bundle)
        return 0

    out_path = CORPUS_DIR / bundle_name
    out_path.write_text(bundle, encoding="utf-8")
    print(f"Wrote {out_path} ({len(bundle)} bytes, {bundle.count(chr(10))} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
