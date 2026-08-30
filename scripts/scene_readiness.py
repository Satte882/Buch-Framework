#!/usr/bin/env python3
"""Scene Readiness completeness checker for Buch-Framework v0.2.

The checker deliberately does NOT decide literary quality. It verifies that a
scene plan has explicit inputs and closed plot/research/character dependencies
so it can enter the bundled G2 Prose Ready review. Human approval remains
external to the checker.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

FIELD_RE = re.compile(r"^([a-z][a-z0-9_]*)\s*:\s*(.*?)\s*$")


@dataclass(frozen=True)
class ReadinessResult:
    status: str
    scene_id: str
    issues: list[str]
    fields: dict[str, str]


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if str(data.get("version")) != "0.2":
        raise ValueError(f"Unsupported scene-readiness config version: {data.get('version')!r}")
    if not data.get("required_fields"):
        raise ValueError("scene-readiness config requires required_fields")
    return data


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in text.splitlines():
        match = FIELD_RE.match(raw_line.strip())
        if not match:
            continue
        key, value = match.groups()
        fields[key] = value.strip()
    return fields


def _starts_na(value: str, prefixes: list[str]) -> bool:
    folded = value.casefold().strip()
    return any(folded.startswith(prefix.casefold()) for prefix in prefixes)


def _na_with_reason(value: str, prefixes: list[str]) -> bool:
    folded = value.casefold().strip()
    stripped = value.strip()
    for prefix in prefixes:
        p = prefix.casefold()
        if folded.startswith(p):
            reason = stripped[len(prefix):].strip()
            return bool(reason)
    return False


def _contains_placeholder_marker(folded: str, token: str) -> bool:
    marker = token.casefold()
    if marker == "offen":
        return (
            folded == "offen"
            or folded.startswith("offen:")
            or folded.startswith("offen -")
            or folded.startswith("[offen]")
        )
    if marker in {"todo", "tbd", "unklar"}:
        return re.search(rf"(?<!\w){re.escape(marker)}(?!\w)", folded) is not None
    return marker in folded


def _looks_placeholder(value: str, tokens: list[str]) -> bool:
    stripped = value.strip()
    if not stripped:
        return True
    if stripped == "?" or stripped.startswith("<"):
        return True
    folded = stripped.casefold()
    for token in tokens:
        if token in {"<", "?"}:
            continue
        if _contains_placeholder_marker(folded, token):
            return True
    return False


def evaluate(text: str, config: dict[str, Any]) -> ReadinessResult:
    fields = parse_fields(text)
    issues: list[str] = []
    required = list(config["required_fields"])
    allowed_na = set(config.get("allow_not_applicable_with_reason", []))
    na_prefixes = list(config.get("not_applicable_prefixes", []))
    placeholders = list(config.get("placeholder_tokens", []))

    for key in required:
        if key not in fields:
            issues.append(f"missing required field: {key}")
            continue

        value = fields[key]
        if _starts_na(value, na_prefixes):
            if key not in allowed_na:
                issues.append(f"not-applicable value is not allowed for: {key}")
                continue
            if not _na_with_reason(value, na_prefixes):
                issues.append(f"not-applicable value requires reason: {key}")
                continue
            continue

        if _looks_placeholder(value, placeholders):
            issues.append(f"unresolved or placeholder value: {key}")

    for key, allowed in config.get("allowed_values", {}).items():
        if key not in fields:
            continue
        value = fields[key].strip().casefold()
        allowed_folded = {str(item).casefold() for item in allowed}
        if value not in allowed_folded:
            issues.append(f"{key} must be one of {sorted(allowed)}; got {fields[key]!r}")

    # Core prose-readiness invariants remain explicit so malformed configs
    # cannot silently weaken deterministic dependency checks.
    if fields.get("story_decisions_open", "").casefold() != "no":
        issues.append("open story decisions block prose")
    if fields.get("character_state_status", "").casefold() != "ready":
        issues.append("character state is not ready")
    if fields.get("research_status", "").casefold() not in {"ready", "not_applicable"}:
        issues.append("research blockers are not closed")

    unique_issues = list(dict.fromkeys(issues))
    status = "BLOCK" if unique_issues else "READY_FOR_HUMAN_GATE"
    return ReadinessResult(
        status=status,
        scene_id=fields.get("scene_id", "UNKNOWN"),
        issues=unique_issues,
        fields=fields,
    )


def format_text(result: ReadinessResult) -> str:
    lines = [
        "SCENE READINESS",
        "",
        f"Scene: {result.scene_id}",
        f"Status: {result.status}",
    ]
    if result.issues:
        lines.extend(["", "Blocking issues:"])
        lines.extend(f"- {issue}" for issue in result.issues)
    else:
        lines.extend(
            [
                "",
                "Mechanical completeness is satisfied.",
                "This is NOT an approval. The scene may enter the bundled G2 Prose Ready review.",
            ]
        )
    return "\n".join(lines)


def format_json(result: ReadinessResult) -> str:
    return json.dumps(asdict(result), ensure_ascii=False, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check whether a scene plan is mechanically ready for bundled G2 review."
    )
    parser.add_argument("scene_plan", help="Scene plan Markdown file")
    parser.add_argument("--config", default="config/scene_readiness.yml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    text = Path(args.scene_plan).read_text(encoding="utf-8")
    config = load_config(args.config)
    result = evaluate(text, config)
    print(format_json(result) if args.format == "json" else format_text(result))
    return 1 if result.status == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
