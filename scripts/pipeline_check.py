#!/usr/bin/env python3
"""Validate Buch-Framework v0.2 mechanics from concept through G2 Prose Ready.

The checker validates macro-to-micro artifact completeness, reference coverage,
blocking research dependencies and existing human gate records. It never judges
literary quality and never creates or simulates a human approval.
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
BLOCK_ID_RE = re.compile(r"B\d+", re.IGNORECASE)
EVENT_ID_RE = re.compile(r"E\d+", re.IGNORECASE)
BEAT_ID_RE = re.compile(r"BT\d+", re.IGNORECASE)


@dataclass(frozen=True)
class PipelineResult:
    status: str
    issues: list[str]
    checked_artifacts: list[str]
    active_scenes: list[str]


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if str(data.get("version")) != "0.2":
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


def parse_id_rows(
    text: str,
    id_re: re.Pattern[str],
    min_cells: int,
) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < min_cells or not id_re.fullmatch(cells[0]):
            continue
        row_id = cells[0].upper()
        rows[row_id] = cells
    return rows


def validate_table_values(
    label: str,
    rows: dict[str, list[str]],
    required_columns: list[int],
    placeholders: list[str],
) -> list[str]:
    issues: list[str] = []
    if not rows:
        return [f"{label}: no data rows found"]
    for row_id, cells in rows.items():
        for index in required_columns:
            if index >= len(cells) or looks_placeholder(cells[index], placeholders):
                issues.append(f"{label}: {row_id} has unresolved required table value at column {index + 1}")
    return issues


def parse_research_rows(text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 8 or not RESEARCH_ID_RE.fullmatch(cells[0]):
            continue
        research_id = cells[0].upper()
        rows[research_id] = {
            "question": cells[1],
            "artifacts": cells[2],
            "risk": cells[3].casefold(),
            "status": cells[4].casefold(),
            "source": cells[5],
            "decision": cells[6],
            "blocking_now": cells[7].casefold(),
        }
    return rows


def validate_research_table_shape(text: str) -> list[str]:
    issues: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and RESEARCH_ID_RE.fullmatch(cells[0]) and len(cells) < 8:
            issues.append(
                f"RESEARCH_REGISTER.md: {cells[0].upper()} must include blocking_now column"
            )
    return issues


def validate_research_rows(rows: dict[str, dict[str, str]]) -> list[str]:
    issues: list[str] = []
    for research_id, row in rows.items():
        if row["risk"] not in {"low", "medium", "high"}:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has invalid risk {row['risk']!r}")
        if row["status"] not in {"open", "resolved", "not_applicable"}:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has invalid status {row['status']!r}")
        if row["blocking_now"] not in {"yes", "no"}:
            issues.append(
                f"RESEARCH_REGISTER.md: {research_id} blocking_now must be yes or no; got {row['blocking_now']!r}"
            )
        if not row["question"]:
            issues.append(f"RESEARCH_REGISTER.md: {research_id} has no question")
        if row["status"] == "resolved" and (not row["source"] or not row["decision"]):
            issues.append(f"RESEARCH_REGISTER.md: resolved {research_id} needs source and decision")
        if row["status"] == "open" and row["blocking_now"] == "yes":
            issues.append(f"RESEARCH_REGISTER.md: blocking research {research_id} is still open")
    return issues


def validate_research_refs(
    label: str,
    value: str,
    research_rows: dict[str, dict[str, str]],
) -> list[str]:
    folded = value.casefold().strip()
    if folded in {"none", "n/a", "not_applicable"} or folded.startswith(
        ("none -", "n/a -", "not_applicable -")
    ):
        return []

    refs = [match.upper() for match in RESEARCH_ID_RE.findall(value)]
    if not refs:
        return [f"{label}: research refs contain no valid research ID or explicit none"]
    issues: list[str] = []
    for research_id in refs:
        if research_id not in research_rows:
            issues.append(f"{label}: unknown research ref {research_id}")
    return issues


def validate_gate(
    project_root: Path,
    gate_id: str,
    gate_cfg: dict[str, Any],
    config: dict[str, Any],
    placeholders: list[str],
    extra_required_artifacts: list[str] | None = None,
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

    artifact_tokens = [
        token.replace("\\", "/").strip("/")
        for token in split_refs(fields.get("artifacts", ""))
    ]
    required = list(gate_cfg.get("required_artifacts", []))
    required.extend(extra_required_artifacts or [])
    for item in required:
        normalized = item.replace("\\", "/").strip("/")
        matched = any(
            token == normalized or token.endswith("/" + normalized)
            for token in artifact_tokens
        )
        if not matched:
            issues.append(f"{gate_id}: artifacts must include {item}")
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


def validate_version_links(artifact_fields: dict[str, dict[str, str]]) -> list[str]:
    issues: list[str] = []
    idea = artifact_fields.get("book_idea", {})
    story = artifact_fields.get("story_package", {})
    blocks = artifact_fields.get("story_blocks", {})
    events = artifact_fields.get("events", {})
    characters = artifact_fields.get("characters", {})
    beats = artifact_fields.get("beats", {})

    if idea.get("working_title") and story.get("working_title"):
        if idea["working_title"] != story["working_title"]:
            issues.append("BOOK_IDEA.md and STORY_PACKAGE.md use different working_title values")

    expected_links = [
        ("STORY_BLOCKS.md", blocks.get("story_package_version"), story.get("version"), "STORY_PACKAGE"),
        ("EVENTS.md", events.get("story_blocks_version"), blocks.get("version"), "STORY_BLOCKS"),
        ("CHARACTERS.md", characters.get("story_package_version"), story.get("version"), "STORY_PACKAGE"),
        ("BEATS.md", beats.get("events_version"), events.get("version"), "EVENTS"),
    ]
    for label, actual, expected, upstream in expected_links:
        if actual and expected and actual != expected:
            issues.append(f"{label} references a different {upstream} version")
    return issues


def evaluate_project(
    project_root: str | Path,
    config: dict[str, Any],
    scene_config: dict[str, Any],
) -> PipelineResult:
    root = Path(project_root)
    placeholders = list(config.get("placeholder_tokens", []))
    issues: list[str] = []
    checked: list[str] = []
    artifact_fields: dict[str, dict[str, str]] = {}
    artifact_texts: dict[str, str] = {}
    research_rows: dict[str, dict[str, str]] = {}
    active_scene_paths: list[str] = []

    def finish(status: str = "BLOCK") -> PipelineResult:
        return PipelineResult(
            status=status,
            issues=list(dict.fromkeys(issues)),
            checked_artifacts=list(dict.fromkeys(checked)),
            active_scenes=active_scene_paths,
        )

    def load_artifact(artifact_id: str) -> None:
        nonlocal research_rows
        if artifact_id in artifact_fields or artifact_id in artifact_texts:
            return
        artifact_cfg = config["artifacts"][artifact_id]
        relative = artifact_cfg["path"]
        path = root / relative
        if not path.exists():
            issues.append(f"{artifact_id}: missing artifact {relative}")
            return
        text = path.read_text(encoding="utf-8")
        fields = parse_fields(text)
        artifact_fields[artifact_id] = fields
        artifact_texts[artifact_id] = text
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
            issues.extend(validate_research_table_shape(text))
            research_rows = parse_research_rows(text)
            issues.extend(validate_research_rows(research_rows))

    def validate_gate_phase(gate_id: str, extra: list[str] | None = None) -> None:
        gate_issues, relative = validate_gate(
            root,
            gate_id,
            config["gates"][gate_id],
            config,
            placeholders,
            extra_required_artifacts=extra,
        )
        issues.extend(gate_issues)
        if relative:
            checked.append(relative)

    # G0: concept must be mechanically valid and explicitly human-approved
    # before the checker asks for any downstream architecture.
    load_artifact("book_idea")
    validate_gate_phase("G0")
    if issues:
        return finish()

    # G1: validate the complete story-architecture bundle horizontally.
    for artifact_id in (
        "story_package",
        "story_blocks",
        "events",
        "characters",
        "research_register",
    ):
        load_artifact(artifact_id)

    issues.extend(validate_version_links(artifact_fields))

    blocks = parse_id_rows(artifact_texts.get("story_blocks", ""), BLOCK_ID_RE, 9)
    events = parse_id_rows(artifact_texts.get("events", ""), EVENT_ID_RE, 10)

    if "story_blocks" in artifact_texts:
        issues.extend(
            validate_table_values(
                "STORY_BLOCKS.md", blocks, [1, 2, 3, 4, 5, 6, 7], placeholders
            )
        )
    if "events" in artifact_texts:
        issues.extend(
            validate_table_values(
                "EVENTS.md", events, [1, 3, 4, 5, 6, 7, 8], placeholders
            )
        )

    if "story_blocks" in artifact_texts and "events" in artifact_texts:
        events_by_block: dict[str, set[str]] = {block_id: set() for block_id in blocks}
        for event_id, cells in events.items():
            block_id = cells[1].upper()
            if block_id not in blocks:
                issues.append(f"EVENTS.md: {event_id} references unknown block {block_id}")
            else:
                events_by_block[block_id].add(event_id)
            issues.extend(
                validate_research_refs(f"EVENTS.md: {event_id}", cells[9], research_rows)
            )
        for block_id, event_ids in events_by_block.items():
            if not event_ids:
                issues.append(f"STORY_BLOCKS.md: {block_id} has no event coverage")
            issues.extend(
                validate_research_refs(
                    f"STORY_BLOCKS.md: {block_id}", blocks[block_id][8], research_rows
                )
            )

    validate_gate_phase("G1")
    if issues:
        return finish()

    # G2: only after a valid human G1 record do beats, scenes and character
    # states become required. This avoids reporting future-phase noise at G1.
    load_artifact("beats")
    issues.extend(validate_version_links(artifact_fields))
    beats = parse_id_rows(artifact_texts.get("beats", ""), BEAT_ID_RE, 11)

    if "beats" in artifact_texts:
        issues.extend(
            validate_table_values(
                "BEATS.md", beats, [1, 2, 3, 4, 5, 6, 7, 8, 9], placeholders
            )
        )

    beats_by_scene: dict[str, set[str]] = {}
    if "events" in artifact_texts and "beats" in artifact_texts:
        beats_by_event: dict[str, set[str]] = {event_id: set() for event_id in events}
        for beat_id, cells in beats.items():
            event_id = cells[1].upper()
            scene_id = cells[2]
            if event_id not in events:
                issues.append(f"BEATS.md: {beat_id} references unknown event {event_id}")
            else:
                beats_by_event[event_id].add(beat_id)
            beats_by_scene.setdefault(scene_id, set()).add(beat_id)
            issues.extend(
                validate_research_refs(f"BEATS.md: {beat_id}", cells[10], research_rows)
            )
        for event_id, beat_ids in beats_by_event.items():
            if not beat_ids:
                issues.append(f"EVENTS.md: {event_id} has no beat coverage")

    scene_dir = root / "scenes"
    scene_files_by_id: dict[str, Path] = {}
    duplicate_scene_ids: set[str] = set()
    if scene_dir.exists():
        for path in sorted(scene_dir.glob("*.md")):
            fields = parse_fields(path.read_text(encoding="utf-8"))
            scene_id = fields.get("scene_id")
            if not scene_id:
                continue
            if scene_id in scene_files_by_id:
                duplicate_scene_ids.add(scene_id)
            else:
                scene_files_by_id[scene_id] = path
    for scene_id in sorted(duplicate_scene_ids):
        issues.append(f"scenes: duplicate scene_id {scene_id}")

    g2_dynamic_artifacts: list[str] = []
    referenced_state_paths: set[str] = set()

    for scene_id in sorted(beats_by_scene):
        expected_beat_ids = beats_by_scene[scene_id]
        scene_path = scene_files_by_id.get(scene_id)
        if scene_path is None:
            issues.append(f"BEATS.md: planned scene {scene_id} has no matching scene plan")
            continue

        relative_scene = scene_path.relative_to(root).as_posix()
        active_scene_paths.append(relative_scene)
        checked.append(relative_scene)
        g2_dynamic_artifacts.append(relative_scene)

        scene_text = scene_path.read_text(encoding="utf-8")
        scene_result = scene_readiness.evaluate(scene_text, scene_config)
        issues.extend(f"{relative_scene}: {item}" for item in scene_result.issues)
        scene_fields = scene_result.fields

        actual_beat_ids = {ref.upper() for ref in split_refs(scene_fields.get("beat_refs", ""))}
        unknown_beat_ids = actual_beat_ids - set(beats)
        for beat_id in sorted(unknown_beat_ids):
            issues.append(f"{relative_scene}: unknown beat ref {beat_id}")

        wrong_scene_beat_ids = {
            beat_id
            for beat_id in actual_beat_ids & set(beats)
            if beats[beat_id][2] != scene_id
        }
        for beat_id in sorted(wrong_scene_beat_ids):
            issues.append(
                f"{relative_scene}: beat {beat_id} is planned for scene {beats[beat_id][2]}, not {scene_id}"
            )

        if actual_beat_ids != expected_beat_ids:
            missing = sorted(expected_beat_ids - actual_beat_ids)
            extra = sorted(actual_beat_ids - expected_beat_ids)
            if missing:
                issues.append(f"{relative_scene}: beat_refs missing planned beats {missing}")
            if extra:
                issues.append(f"{relative_scene}: beat_refs include non-planned beats {extra}")

        state_refs = split_refs(scene_fields.get("character_state_refs", ""))
        if not state_refs:
            issues.append(f"{relative_scene}: character_state_refs is empty")
        for ref in state_refs:
            state_path = safe_project_path(root, ref)
            if state_path is None:
                issues.append(f"{relative_scene}: character_state_refs escapes project root: {ref}")
                continue
            issues.extend(validate_character_state(state_path, scene_id, config, placeholders))
            if state_path.exists():
                relative_state = state_path.relative_to(root.resolve()).as_posix()
                checked.append(relative_state)
                referenced_state_paths.add(relative_state)

        issues.extend(
            validate_research_refs(
                f"{relative_scene}: research_refs",
                scene_fields.get("research_refs", ""),
                research_rows,
            )
        )

    g2_dynamic_artifacts.extend(sorted(referenced_state_paths))
    validate_gate_phase("G2", g2_dynamic_artifacts)
    if issues:
        return finish()

    return finish("READY_FOR_PROSE")


def format_text(result: PipelineResult) -> str:
    lines = ["FRAMEWORK PIPELINE v0.2", "", f"Status: {result.status}"]
    if result.active_scenes:
        lines.extend(["", "Active v0.2 scenes:"])
        lines.extend(f"- {item}" for item in result.active_scenes)
    lines.extend(["", "Checked artifacts:"])
    lines.extend(f"- {item}" for item in result.checked_artifacts)

    if result.issues:
        lines.extend(["", "Blocking issues:"])
        lines.extend(f"- {item}" for item in result.issues)
    else:
        lines.extend(
            [
                "",
                "Macro-to-micro contracts, reference coverage and G0-G2 human records are mechanically consistent.",
                "This is NOT a human approval and does not judge story quality.",
            ]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Buch-Framework v0.2 mechanics from BOOK_IDEA through G2 Prose Ready."
    )
    parser.add_argument("project_root", help="Project directory containing BOOK_IDEA.md etc.")
    parser.add_argument("--config", default="config/pipeline_contract.yml")
    parser.add_argument("--scene-config", default="config/scene_readiness.yml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    scene_config = scene_readiness.load_config(args.scene_config)
    result = evaluate_project(args.project_root, config, scene_config)
    if args.format == "json":
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print(format_text(result))
    return 1 if result.status == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
