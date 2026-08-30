#!/usr/bin/env python3
"""Validate provenance references and block silent downstream drift.

The checker supports two deterministic reference types:

- whole-file Git blob refs
- explicit Markdown slice refs for finer dependency granularity

Status semantics stay unchanged:

- accepted/draft + changed upstream => BLOCK
- stale/invalidated + changed upstream => STALE_OK
- unchanged refs => OK

Slice refs never infer semantic relevance. The manifest author explicitly selects
which deterministic source fragment is relevant.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$")
REF_LINE_RE = re.compile(
    r"`([^`]+)`\s+—\s+(?:blob\s+)?`([0-9a-fA-F]{40})`"
)
SLICE_REF_LINE_RE = re.compile(
    r"`([^`]+)`\s+—\s+slice\s+`([^`]+)`\s+—\s+(?:blob\s+)?`([0-9a-fA-F]{40})`"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
VALID_STATUSES = {"draft", "accepted", "stale", "invalidated"}


@dataclass(frozen=True)
class ProvenanceResult:
    status: str
    mismatches: tuple[str, ...]
    checked_refs: tuple[str, ...]


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = FIELD_RE.match(line.strip())
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("`")
    return fields


def parse_refs(text: str) -> list[tuple[str, str]]:
    return [(path, sha.lower()) for path, sha in REF_LINE_RE.findall(text)]


def parse_slice_refs(text: str) -> list[tuple[str, str, str]]:
    return [
        (path, selector, sha.lower())
        for path, selector, sha in SLICE_REF_LINE_RE.findall(text)
    ]


def _one_match(matches: list[str], selector: str) -> str:
    if not matches:
        raise ValueError(f"slice not found: {selector}")
    if len(matches) > 1:
        raise ValueError(f"slice is ambiguous ({len(matches)} matches): {selector}")
    return matches[0]


def extract_markdown_slice(text: str, selector: str) -> str:
    """Extract one explicitly named deterministic Markdown fragment.

    Supported selectors:
    - table-row:<first cell text>
    - heading:<heading text without #>
    - line-prefix:<prefix after surrounding whitespace is stripped>
    """

    if selector.startswith("table-row:"):
        key = selector[len("table-row:") :].strip()
        matches: list[str] = []
        for raw in text.splitlines():
            line = raw.strip()
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if cells and cells[0] == key:
                matches.append(raw.rstrip() + "\n")
        return _one_match(matches, selector)

    if selector.startswith("heading:"):
        title = selector[len("heading:") :].strip()
        lines = text.splitlines(keepends=True)
        starts: list[tuple[int, int]] = []
        for index, raw in enumerate(lines):
            match = HEADING_RE.match(raw.rstrip("\r\n"))
            if match and match.group(2).strip() == title:
                starts.append((index, len(match.group(1))))
        if not starts:
            raise ValueError(f"slice not found: {selector}")
        if len(starts) > 1:
            raise ValueError(f"slice is ambiguous ({len(starts)} matches): {selector}")
        start, level = starts[0]
        end = len(lines)
        for index in range(start + 1, len(lines)):
            match = HEADING_RE.match(lines[index].rstrip("\r\n"))
            if match and len(match.group(1)) <= level:
                end = index
                break
        fragment = "".join(lines[start:end])
        if fragment and not fragment.endswith("\n"):
            fragment += "\n"
        return fragment

    if selector.startswith("line-prefix:"):
        prefix = selector[len("line-prefix:") :].strip()
        matches = [
            raw.rstrip() + "\n"
            for raw in text.splitlines()
            if raw.strip().startswith(prefix)
        ]
        return _one_match(matches, selector)

    raise ValueError(f"unsupported slice selector: {selector}")


def evaluate_provenance(root: Path, provenance_path: Path) -> ProvenanceResult:
    text = provenance_path.read_text(encoding="utf-8")
    fields = parse_fields(text)
    declared_status = fields.get("status", "").lower()
    if declared_status not in VALID_STATUSES:
        return ProvenanceResult(
            status="BLOCK",
            mismatches=(f"invalid or missing provenance status: {declared_status!r}",),
            checked_refs=(),
        )

    refs = parse_refs(text)
    slice_refs = parse_slice_refs(text)
    artifact = fields.get("artifact")
    artifact_ref = fields.get("artifact_ref", "").lower()
    if artifact and re.fullmatch(r"[0-9a-f]{40}", artifact_ref):
        refs.append((artifact, artifact_ref))

    mismatches: list[str] = []
    checked: list[str] = []
    seen: set[tuple[str, ...]] = set()

    for relative, expected in refs:
        key = ("file", relative, expected)
        if key in seen:
            continue
        seen.add(key)
        path = root / relative
        checked.append(relative)
        if not path.exists():
            mismatches.append(f"missing referenced file: {relative}")
            continue
        actual = git_blob_sha(path.read_bytes())
        if actual != expected:
            mismatches.append(
                f"blob mismatch: {relative} expected {expected} actual {actual}"
            )

    for relative, selector, expected in slice_refs:
        key = ("slice", relative, selector, expected)
        if key in seen:
            continue
        seen.add(key)
        path = root / relative
        label = f"{relative}#slice={selector}"
        checked.append(label)
        if not path.exists():
            mismatches.append(f"missing referenced file: {relative}")
            continue
        try:
            fragment = extract_markdown_slice(path.read_text(encoding="utf-8"), selector)
        except ValueError as exc:
            mismatches.append(f"slice error: {relative} {exc}")
            continue
        actual = git_blob_sha(fragment.encode("utf-8"))
        if actual != expected:
            mismatches.append(
                f"slice mismatch: {relative} selector {selector!r} expected {expected} actual {actual}"
            )

    if mismatches:
        result_status = "STALE_OK" if declared_status in {"stale", "invalidated"} else "BLOCK"
    else:
        result_status = "OK"

    return ProvenanceResult(
        status=result_status,
        mismatches=tuple(mismatches),
        checked_refs=tuple(checked),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Check provenance references for silent invalidation.")
    parser.add_argument("provenance", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    result = evaluate_provenance(args.root.resolve(), args.provenance.resolve())
    print(f"PROVENANCE CHECK: {result.status}")
    for item in result.checked_refs:
        print(f"checked: {item}")
    for item in result.mismatches:
        print(f"mismatch: {item}")
    return 1 if result.status == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
