#!/usr/bin/env python3
"""Validate the thin Buch-Framework pipeline from G0 through a G3-ready scene.

The checker validates explicit artifact completeness, human gate records and
cross-file dependencies. It never judges literary quality and never creates or
simulates a human approval.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import scene_readiness

FIELD_RE = re.compile(r"^([a-z][a-z0-9_]*)\s*:\s*(.*?)\s*$")
RESEARCH_ID_RE = re.compile(r"\bR-\d+\b", re.IGNORECASE)


@dataclass(frozen=True)
class PipelineResult:
    status: str
    issues: list[str]
    checked_artifacts: list[str]
    scene: str | None


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if str(data.get("version")) != "0.1":
        raise ValueError(f"Unsupported pipeline contract version: {data.get('version')!r}")
    return data


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in text.splitlines():
        match = FIELD_RE.match(raw_line.strip())
        if match:
            key, value = match.groups()
            fields[key] = value.strip()
    return fields


def contains_placeholder_marker(folded: str, token: str) -> bool:
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


def looks_placeholder(value: str, tokens: list[str]) -> bool:
    stripped = value.strip()
    if not stripped or stripped == "?" or stripped.startswith("<"):
        return True
    folded = stripped.casefold()
    for token in tokens:
        if token in {"<", "?"}:
            continue
        if contains_placeholder_marker(folded, token):
            return True
    return False


def validate_fields(
    label: str,
    fields: dict[str, str],
    required: list[str],
    allowed_values: dict[str, list[str]],
    placeholders: list[str],
) -> list[str]:
    issues: list[str] = []
    for key in required:
        if key not in fields:
            issues.append(f"{label}: missing required field: {key}")
            continue
        if looks_placeholder(fields[key], placeholders):
            issues.append(f"{label}: unresolved or placeholder value: {key}")

    for key, allowed in allowed_values.items():
        if key not in fields:
            continue
        folded = fields[key].strip().casefold()
        allowed_folded = {str(item).casefold() for item in allowed}
        if folded not in allowed_folded:
            issues.append(f"{label}: {key} must be one of {allowed}; got {fields[key]!r}")
    return issues


def parse_research_rows(text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 5 or not RESEARCH_ID_RE.fullmatch(cells[0]):
            continue
        research_id = cells[0].upper()
        rows[research_id] = {
            "question": cells[1],
            "scenes": cells[2],
            "risk": cells[3].casefold(),
            "status": cells[4].casefold(),
            "source": cells[5] if len(cells) > 5 else "",
            "decision": cells[6] if len(cells) > 6 else "",
        }
    return rows


def validate_research_rows(rows: dict[str, dict[str, str]]) -> list[str]:
    issues: list[str] = []
    for research_id, row in rows.items():
        if row["risk"] not in {"low", "medium", "high"}:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has invalid risk {row['risk']!r}")
        if row["status"] not in {"open", "resolved", "not_applicable"}:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has invalid status {row['status']!r}")
        if not row["question"]:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has no question")
        if row["status"] == "resolved" and (not row["source"] or not row["decision"]):
            issues.append(f"RESEARCH_REGISTER.md: resolved {research_id} needs source and decision")
    return issues


def split_refs(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[;,]", value) if part.strip()]


def safe_project_path(project_root: Path, relative: str) -> Path | None:
    candidate = (project_root / relative).resolve()
    root = project_root.resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate


def validate_gate(
    project_root: Path,
    gate_id: str,
    gate_cfg: dict[str, Any],
    config: dict[str, Any],
    placeholders: list[str],
) -> tuple[list[str], str | None]:
    relative = gate_cfg["path"]
    path = project_root / relative
    if not path.exists():
        return [f"{gate_id}: missing human gate record {relative}"], None

    fields = parse_fields(path.read_text(encoding="utf-8"))
    issues = validate_fields(
        gate_id,
        fields,
        list(config["gate_required_fields"]),
        dict(config.get("gate_allowed_values", {})),
        placeholders,
    )
    if fields.get("gate_id") != gate_id:
        issues.append(f"{gate_id}: gate_id must equal {gate_id!r}")

    artifact_tokens = split_refs(fields.get("artifacts", ""))
    artifact_names = {Path(token).name for token in artifact_tokens}
    for required in gate_cfg.get("required_artifacts", []):
        if Path(required).name not in artifact_names:
            issues.append(f"{gate_id}: artifacts must include {required}")
    return issues, relative


def validate_character_state(
    path: Path,
    expected_scene_id: str,
    config: dict[str, Any],
    placeholders: list[str],
) -> list[str]:
    label = str(path)
    if not path.exists():
        return [f"character state missing: {label}"]
    fields = parse_fields(path.read_text(encoding="utf-8"))
    issues = validate_fields(
        label,
        fields,
        list(config["character_state_required_fields"]),
        dict(config.get("character_state_allowed_values", {})),
        placeholders,
    )
    if fields.get("scene_id") != expected_scene_id:
        issues.append(
            f"{label}: scene_id {fields.get('scene_id')!r} does not match scene {expected_scene_id!r}"
        )
    return issues


def evaluate_project(
    project_root: str | Path,
    config: dict[str, Any],
    scene_config: dict[str, Any],
    scene_relative: str | None = None,
) -> PipelineResult:
    root = Path(project_root)
    placeholders = list(config.get("placeholder_tokens", []))
    issues: list[str] = []
    checked: list[str] = []
    artifact_fields: dict[str, dict[str, str]] = {}
    research_rows: dict[str, dict[str, str]] = {}

    for artifact_id, artifact_cfg in config["artifacts"].items():
        relative = artifact_cfg["path"]
        path = root / relative
        if not path.exists():
            issues.append(f"{artifact_id}: missing artifact {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        fields = parse_fields(text)
        artifact_fields[artifact_id] = fields
        checked.append(relative)
        issues.extend(
            validate_fields(
                relative,
                fields,
                list(artifact_cfg["required_fields"]),
                dict(artifact_cfg.get("allowed_values", {})),
                placeholders,
            )
        )
        if artifact_id == "research_register":
            research_rows = parse_research_rows(text)
            issues.extend(validate_research_rows(research_rows))

    idea = artifact_fields.get("book_idea", {})
    story = artifact_fields.get("story_package", {})
    characters = artifact_fields.get("characters", {})
    if idea.get("working_title") and story.get("working_title"):
        if idea["working_title"] != story["working_title"]:
            issues.append("BOOK_IDEA.md and STORY_PACKAGE.md use different working_title values")
    if story.get("version") and characters.get("story_package_version"):
        if story["version"] != characters["story_package_version"]:
            issues.append("CHARACTERS.md references a different STORY_PACKAGE version")

    for gate_id in ("G0", "G1", "G2"):
        gate_issues, relative = validate_gate(
            root, gate_id, config["gates"][gate_id], config, placeholders
        )
        issues.extend(gate_issues)
        if relative:
            checked.append(relative)

    scene_label: str | None = None
    if scene_relative:
        scene_label = scene_relative
        scene_path = safe_project_path(root, scene_relative)
        if scene_path is None:
            issues.append(f"scene path escapes project root: {scene_relative}")
        elif not scene_path.exists():
            issues.append(f"scene missing: {scene_relative}")
        else:
            checked.append(scene_relative)
            scene_text = scene_path.read_text(encoding="utf-8")
            scene_result = scene_readiness.evaluate(scene_text, scene_config)
            issues.extend(f"{scene_relative}: {issue}" for issue in scene_result.issues)
            scene_fields = scene_result.fields
            scene_id = scene_fields.get("scene_id", "UNKNOWN")

            refs_value = scene_fields.get("character_state_refs", "")
            for ref in split_refs(refs_value):
                state_path = safe_project_path(root, ref)
                if state_path is None:
                    issues.append(f"character_state_refs escapes project root: {ref}")
                    continue
                issues.extend(
                    validate_character_state(state_path, scene_id, config, placeholders)
                )
                if state_path.exists():
                    checked.append(str(state_path.relative_to(root.resolve())))

            research_value = scene_fields.get("research_refs", "")
            folded_research = research_value.casefold().strip()
            is_reasoned_none = any(
                folded_research.startswith(prefix)
                and bool(research_value[len(prefix):].strip())
                for prefix in ("none -", "n/a -", "not_applicable -")
            )
            if not is_reasoned_none:
                refs = [match.upper() for match in RESEARCH_ID_RE.findall(research_value)]
                if not refs:
                    issues.append(f"{scene_relative}: research_refs contains no valid research ID")
                for research_id in refs:
                    row = research_rows.get(research_id)
                    if row is None:
                        issues.append(f"{scene_relative}: unknown research ref {research_id}")
                    elif row["status"] not in {"resolved", "not_applicable"}:
                        issues.append(
                            f"{scene_relative}: research ref {research_id} is still {row['status']}"
                        )

    unique_issues = list(dict.fromkeys(issues))
    if unique_issues:
        status = "BLOCK"
    elif scene_relative:
        status = "READY_FOR_G3"
    else:
        status = "READY_FOR_SCENE_PLANNING"

    return PipelineResult(
        status=status,
        issues=unique_issues,
        checked_artifacts=list(dict.fromkeys(checked)),
        scene=scene_label,
    )


def format_text(result: PipelineResult) -> str:
    lines = ["FRAMEWORK PIPELINE", "", f"Status: {result.status}"]
    if result.scene:
        lines.append(f"Scene: {result.scene}")
    lines.extend(["", "Checked artifacts:"])
    lines.extend(f"- {item}" for item in result.checked_artifacts)
    if result.issues:
        lines.extend(["", "Blocking issues:"])
        lines.extend(f"- {item}" for item in result.issues)
    elif result.status == "READY_FOR_G3":
        lines.extend(
            [
                "",
                "Upstream contracts and scene dependencies are mechanically complete.",
                "This is NOT a G3 approval. A human must still decide APPROVE/REWORK/STOP.",
            ]
        )
    else:
        lines.extend(
            [
                "",
                "G0-G2 are mechanically consistent and human-approved.",
                "Scene planning may begin; no G3 decision has been made.",
            ]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Buch-Framework artifacts from G0 through a G3-ready scene."
    )
    parser.add_argument("project_root", help="Project directory containing BOOK_IDEA.md etc.")
    parser.add_argument("--scene", help="Scene path relative to project_root")
    parser.add_argument("--config", default="config/pipeline_contract.yml")
    parser.add_argument("--scene-config", default="config/scene_readiness.yml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    scene_config = scene_readiness.load_config(args.scene_config)
    result = evaluate_project(args.project_root, config, scene_config, args.scene)
    if args.format == "json":
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print(format_text(result))
    return 1 if result.status == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
