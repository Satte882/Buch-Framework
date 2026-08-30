#!/usr/bin/env python3
"""Validate Git-blob provenance references and block silent downstream drift.

The checker is intentionally small. It reads the Markdown provenance format used
by the framework, compares referenced 40-char Git blob SHAs with current local
files and enforces the status rule from SOURCE_OF_TRUTH.md:

- accepted/draft + changed upstream => BLOCK
- stale/invalidated + changed upstream => STALE_OK
- unchanged refs => OK

It does not mutate provenance or infer semantic dependencies.
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
    artifact = fields.get("artifact")
    artifact_ref = fields.get("artifact_ref", "").lower()
    if artifact and re.fullmatch(r"[0-9a-f]{40}", artifact_ref):
        refs.append((artifact, artifact_ref))

    mismatches: list[str] = []
    checked: list[str] = []
    seen: set[tuple[str, str]] = set()

    for relative, expected in refs:
        key = (relative, expected)
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
    parser = argparse.ArgumentParser(description="Check provenance Git-blob references for silent invalidation.")
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
