#!/usr/bin/env python3
"""Dependency-free prose audit for Buch-Framework v0.1.

The scanner is deliberately conservative:
- FAIL is reserved for deterministic configured violations.
- REVIEW marks structural candidates; it never rewrites prose.
- INFO reports descriptive signals whose thresholds are not empirically mature.
- No LLM/API call happens here or in CI.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

WORD_RE = re.compile(r"\b[\wÄÖÜäöüß'-]+\b", re.UNICODE)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
DIALOGUE_STARTS = ("„", "»", '"')
VALID_SCOPES = {"core", "prose_profile", "series_profile", "book"}
VALID_SEVERITIES = {"FAIL", "REVIEW", "INFO"}


@dataclass(frozen=True)
class Paragraph:
    chapter: str
    index: int
    start_line: int
    end_line: int
    text: str

    @property
    def word_count(self) -> int:
        return len(words(self.text))

    @property
    def is_dialogue(self) -> bool:
        return self.text.lstrip().startswith(DIALOGUE_STARTS)


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    chapter: str
    start_line: int
    end_line: int
    message: str
    excerpt: str
    scope: str
    evidence_status: str


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def load_config(path: str | Path) -> dict[str, Any]:
    """Load config/prosa_rules.yml.

    v0.1 intentionally stores JSON syntax in the .yml file. JSON is valid YAML
    1.2 and avoids adding PyYAML to a small solo-author tool.
    """
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if str(data.get("version")) != "0.1":
        raise ValueError(f"Unsupported config version: {data.get('version')!r}")
    validate_config(data)
    return data


def validate_config(data: dict[str, Any]) -> None:
    rules = data.get("rules")
    if not isinstance(rules, dict) or not rules:
        raise ValueError("Config must contain at least one rule")

    for rule_id, rule in rules.items():
        scope = rule.get("scope")
        severity = rule.get("severity")
        rule_type = rule.get("type")

        if scope not in VALID_SCOPES:
            raise ValueError(f"{rule_id}: invalid scope {scope!r}")
        if severity not in VALID_SEVERITIES:
            raise ValueError(f"{rule_id}: invalid severity {severity!r}")
        if severity == "FAIL" and rule_type != "deterministic":
            raise ValueError(f"{rule_id}: FAIL is allowed only for deterministic rules")
        if rule.get("auto_rewrite") is not False:
            raise ValueError(f"{rule_id}: v0.1 rules must set auto_rewrite=false")

        for exception in rule.get("exceptions", []):
            if not isinstance(exception, dict):
                raise ValueError(f"{rule_id}: exceptions must be objects with match and reason")
            if not str(exception.get("match", "")).strip():
                raise ValueError(f"{rule_id}: exception match must not be empty")
            if not str(exception.get("reason", "")).strip():
                raise ValueError(f"{rule_id}: exception reason must not be empty")


def parse_paragraphs(text: str) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    chapter = "Vorspann"
    buffer: list[str] = []
    start_line = 1
    para_index = 0

    def flush(end_line: int) -> None:
        nonlocal buffer, para_index, start_line
        if not buffer:
            return
        raw = "\n".join(buffer).strip()
        buffer = []
        if not raw:
            return
        para_index += 1
        paragraphs.append(
            Paragraph(
                chapter=chapter,
                index=para_index,
                start_line=start_line,
                end_line=end_line,
                text=raw,
            )
        )

    lines = text.splitlines()
    for lineno, line in enumerate(lines, start=1):
        heading = HEADING_RE.match(line.strip())
        if heading:
            flush(lineno - 1)
            chapter = heading.group(1).strip()
            para_index = 0
            continue
        if not line.strip():
            flush(lineno - 1)
            continue
        if not buffer:
            start_line = lineno
        buffer.append(line)
    flush(len(lines))
    return paragraphs


def excerpt(text: str, limit: int = 180) -> str:
    flat = re.sub(r"\s+", " ", text).strip()
    return flat if len(flat) <= limit else flat[: limit - 1].rstrip() + "…"


def _regex_flags(names: Iterable[str]) -> int:
    result = 0
    for name in names:
        if name == "IGNORECASE":
            result |= re.IGNORECASE
        elif name == "MULTILINE":
            result |= re.MULTILINE
        else:
            raise ValueError(f"Unsupported regex flag: {name}")
    return result


def _exception_matches(line: str, exceptions: list[Any]) -> bool:
    for item in exceptions:
        match = item.get("match") if isinstance(item, dict) else item
        if match and str(match) in line:
            return True
    return False


def scan_forbidden(text: str, paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    pattern = re.compile(rule["pattern"], _regex_flags(rule.get("flags", [])))
    exceptions = rule.get("exceptions", [])
    findings: list[Finding] = []
    chapter_by_line: dict[int, str] = {}
    for paragraph in paragraphs:
        for line in range(paragraph.start_line, paragraph.end_line + 1):
            chapter_by_line[line] = paragraph.chapter

    for line_no, line in enumerate(text.splitlines(), start=1):
        if _exception_matches(line, exceptions):
            continue
        for match in pattern.finditer(line):
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=rule["severity"],
                    chapter=chapter_by_line.get(line_no, "Vorspann"),
                    start_line=line_no,
                    end_line=line_no,
                    message=f"Forbidden pattern found: {match.group(0)!r}",
                    excerpt=excerpt(line),
                    scope=rule["scope"],
                    evidence_status=rule["evidence_status"],
                )
            )
    return findings


def _normalized_start(text: str) -> str:
    value = text.lstrip()
    value = re.sub(r"^[>*_\s]+", "", value)
    value = value.lstrip("„»\"'(")
    return value.casefold()


def scan_negation_sequences(paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    starters = tuple(item.casefold() for item in rule["starters"])
    min_run = int(rule["min_run"])
    max_words = int(rule["max_words_per_paragraph"])
    findings: list[Finding] = []
    run: list[Paragraph] = []

    def qualifies(paragraph: Paragraph) -> bool:
        start = _normalized_start(paragraph.text)
        return paragraph.word_count <= max_words and any(
            start == starter or start.startswith(starter + " ") or start.startswith(starter + ".")
            for starter in starters
        )

    def flush() -> None:
        nonlocal run
        if len(run) >= min_run:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=rule["severity"],
                    chapter=run[0].chapter,
                    start_line=run[0].start_line,
                    end_line=run[-1].end_line,
                    message=f"{len(run)} consecutive short negation paragraphs",
                    excerpt=excerpt(" / ".join(item.text for item in run)),
                    scope=rule["scope"],
                    evidence_status=rule["evidence_status"],
                )
            )
        run = []

    previous: Paragraph | None = None
    for paragraph in paragraphs:
        contiguous = previous is not None and paragraph.chapter == previous.chapter and paragraph.index == previous.index + 1
        if qualifies(paragraph):
            if run and not contiguous:
                flush()
            run.append(paragraph)
        else:
            flush()
        previous = paragraph
    flush()
    return findings


def scan_staccato_sequences(paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    min_run = int(rule["min_run"])
    max_words = int(rule["max_words_per_paragraph"])
    exclude_dialogue = bool(rule.get("exclude_dialogue", True))
    findings: list[Finding] = []
    run: list[Paragraph] = []

    def qualifies(paragraph: Paragraph) -> bool:
        if exclude_dialogue and paragraph.is_dialogue:
            return False
        return 0 < paragraph.word_count <= max_words

    def flush() -> None:
        nonlocal run
        if len(run) >= min_run:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=rule["severity"],
                    chapter=run[0].chapter,
                    start_line=run[0].start_line,
                    end_line=run[-1].end_line,
                    message=f"{len(run)} consecutive very short narrative paragraphs",
                    excerpt=excerpt(" / ".join(item.text for item in run)),
                    scope=rule["scope"],
                    evidence_status=rule["evidence_status"],
                )
            )
        run = []

    previous: Paragraph | None = None
    for paragraph in paragraphs:
        contiguous = previous is not None and paragraph.chapter == previous.chapter and paragraph.index == previous.index + 1
        if qualifies(paragraph):
            if run and not contiguous:
                flush()
            run.append(paragraph)
        else:
            flush()
        previous = paragraph
    flush()
    return findings


def scan_dialogue_pingpong(paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    min_run = int(rule["min_run"])
    max_words = int(rule["max_words_per_paragraph"])
    findings: list[Finding] = []
    run: list[Paragraph] = []

    def qualifies(paragraph: Paragraph) -> bool:
        return paragraph.is_dialogue and 0 < paragraph.word_count <= max_words

    def flush() -> None:
        nonlocal run
        if len(run) >= min_run:
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=rule["severity"],
                    chapter=run[0].chapter,
                    start_line=run[0].start_line,
                    end_line=run[-1].end_line,
                    message=f"{len(run)} consecutive short dialogue paragraphs",
                    excerpt=excerpt(" / ".join(item.text for item in run)),
                    scope=rule["scope"],
                    evidence_status=rule["evidence_status"],
                )
            )
        run = []

    previous: Paragraph | None = None
    for paragraph in paragraphs:
        contiguous = previous is not None and paragraph.chapter == previous.chapter and paragraph.index == previous.index + 1
        if qualifies(paragraph):
            if run and not contiguous:
                flush()
            run.append(paragraph)
        else:
            flush()
        previous = paragraph
    flush()
    return findings


def scan_softener_density(paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    terms = {item.casefold() for item in rule["terms"]}
    window_words = int(rule["window_words"])
    floor = int(rule["reporting_floor"])
    max_reports = int(rule.get("max_reports", 12))
    candidates: list[tuple[int, Finding]] = []
    by_chapter: dict[str, list[Paragraph]] = {}
    for paragraph in paragraphs:
        by_chapter.setdefault(paragraph.chapter, []).append(paragraph)

    for chapter, chapter_paragraphs in by_chapter.items():
        token_rows: list[tuple[str, Paragraph]] = []
        for paragraph in chapter_paragraphs:
            token_rows.extend((word.casefold(), paragraph) for word in words(paragraph.text))
        if not token_rows:
            continue

        hits: list[tuple[int, int]] = []
        for start in range(len(token_rows)):
            end = min(len(token_rows), start + window_words)
            count = sum(1 for token, _ in token_rows[start:end] if token in terms)
            if count >= floor:
                hits.append((count, start))
        if not hits:
            continue

        hits.sort(reverse=True)
        used_ranges: list[tuple[int, int]] = []
        for count, start in hits:
            end = min(len(token_rows), start + window_words)
            overlaps = any(
                max(start, left) < min(end, right)
                and (min(end, right) - max(start, left)) > window_words // 2
                for left, right in used_ranges
            )
            if overlaps:
                continue
            used_ranges.append((start, end))
            first_paragraph = token_rows[start][1]
            last_paragraph = token_rows[end - 1][1]
            window_excerpt = " ".join(token for token, _ in token_rows[start:end])
            candidates.append(
                (
                    count,
                    Finding(
                        rule_id=rule_id,
                        severity=rule["severity"],
                        chapter=chapter,
                        start_line=first_paragraph.start_line,
                        end_line=last_paragraph.end_line,
                        message=(
                            f"{count} configured softener terms in a {window_words}-word reporting window; "
                            "INFO only, not a quality threshold"
                        ),
                        excerpt=excerpt(window_excerpt),
                        scope=rule["scope"],
                        evidence_status=rule["evidence_status"],
                    ),
                )
            )

    candidates.sort(key=lambda item: (-item[0], item[1].chapter, item[1].start_line))
    return [finding for _, finding in candidates[:max_reports]]


def scan_filter_terms(paragraphs: list[Paragraph], rule_id: str, rule: dict[str, Any]) -> list[Finding]:
    terms = [item.casefold() for item in rule["terms"]]
    floor = int(rule["reporting_floor_per_chapter"])
    by_chapter: dict[str, list[Paragraph]] = {}
    for paragraph in paragraphs:
        by_chapter.setdefault(paragraph.chapter, []).append(paragraph)

    findings: list[Finding] = []
    for chapter, chapter_paragraphs in by_chapter.items():
        combined = "\n".join(item.text for item in chapter_paragraphs)
        chapter_words = [word.casefold() for word in words(combined)]
        token_counts = {term: chapter_words.count(term) for term in terms if chapter_words.count(term) >= floor}
        if token_counts:
            first, last = chapter_paragraphs[0], chapter_paragraphs[-1]
            summary = ", ".join(f"{term}={count}" for term, count in sorted(token_counts.items()))
            findings.append(
                Finding(
                    rule_id=rule_id,
                    severity=rule["severity"],
                    chapter=chapter,
                    start_line=first.start_line,
                    end_line=last.end_line,
                    message=f"Configured filter-term counts: {summary}",
                    excerpt=excerpt(combined),
                    scope=rule["scope"],
                    evidence_status=rule["evidence_status"],
                )
            )
    return findings


def audit_text(text: str, config: dict[str, Any]) -> list[Finding]:
    paragraphs = parse_paragraphs(text)
    findings: list[Finding] = []

    for rule_id, rule in config["rules"].items():
        rule_type = rule["type"]
        if rule_type == "deterministic":
            findings.extend(scan_forbidden(text, paragraphs, rule_id, rule))
        elif rule_id == "softener_density":
            findings.extend(scan_softener_density(paragraphs, rule_id, rule))
        elif rule_id == "negation_sequence":
            findings.extend(scan_negation_sequences(paragraphs, rule_id, rule))
        elif rule_id == "staccato_sequence":
            findings.extend(scan_staccato_sequences(paragraphs, rule_id, rule))
        elif rule_id == "dialogue_pingpong":
            findings.extend(scan_dialogue_pingpong(paragraphs, rule_id, rule))
        elif rule_id == "filter_terms":
            findings.extend(scan_filter_terms(paragraphs, rule_id, rule))
        else:
            raise ValueError(f"Unsupported configured rule: {rule_id} ({rule_type})")

    severity_rank = {"FAIL": 0, "REVIEW": 1, "INFO": 2}
    return sorted(findings, key=lambda item: (severity_rank.get(item.severity, 99), item.chapter, item.start_line, item.rule_id))


def counts(findings: list[Finding]) -> dict[str, int]:
    result = {"FAIL": 0, "REVIEW": 0, "INFO": 0}
    for finding in findings:
        result[finding.severity] = result.get(finding.severity, 0) + 1
    return result


def format_text(findings: list[Finding]) -> str:
    totals = counts(findings)
    lines = [
        "PROSA AUDIT",
        "",
        f"FAIL: {totals.get('FAIL', 0)}",
        f"REVIEW: {totals.get('REVIEW', 0)}",
        f"INFO: {totals.get('INFO', 0)}",
    ]
    for finding in findings:
        lines.extend(
            [
                "",
                f"[{finding.severity}] {finding.rule_id}",
                f"Kapitel: {finding.chapter} | Zeilen: {finding.start_line}-{finding.end_line}",
                finding.message,
                f"Kontext: {finding.excerpt}",
                f"Scope: {finding.scope} | Evidenz: {finding.evidence_status}",
            ]
        )
    return "\n".join(lines)


def format_json(findings: list[Finding]) -> str:
    return json.dumps(
        {"counts": counts(findings), "findings": [asdict(item) for item in findings]},
        ensure_ascii=False,
        indent=2,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit German prose without rewriting it.")
    parser.add_argument("manuscript", help="Markdown/text manuscript to audit")
    parser.add_argument("--config", default="config/prosa_rules.yml", help="Rule config (JSON syntax, valid YAML 1.2)")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", help="Optional report file; stdout if omitted")
    args = parser.parse_args(argv)

    text = Path(args.manuscript).read_text(encoding="utf-8")
    config = load_config(args.config)
    findings = audit_text(text, config)
    rendered = format_json(findings) if args.format == "json" else format_text(findings)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    return 1 if any(item.severity == "FAIL" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
