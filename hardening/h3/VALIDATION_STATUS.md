# H3 Validation Status – unabhängiger semantischer Review

status: NOT_YET_VALIDATED
issue: #16
date: 2026-08-30
protocol: `SEMANTIC_REVIEW_PROTOCOL.md`
fresh_context_task: `hardening/h3/FRESH_CONTEXT_TASK.md`
holdout_target_blob: `d4a4225d76b3f8699660683cda26252ed4a2809c`

## Warum noch kein PASS

Der aktuelle Arbeitschat hat:

- SPERRFRIST erzeugt,
- M2 begleitet,
- frühere semantische Befunde gesehen,
- den späteren korrigierten Manuskriptstand gesehen.

Ein Review desselben Modells **in diesem Kontext** wäre deshalb nicht unabhängig und darf H3 nicht validieren.

Diese Grenze wird nicht durch einen simulierten „neuen Reviewer“ innerhalb desselben Kontextes umgangen.

## Was bereits vorbereitet ist

- reproduzierbares Review-Protokoll: vorhanden
- historischer echter Pre-Rework-Holdout: vorhanden als Git-Blob
- erlaubte kanonische Review-Inputs: festgelegt
- bekannte spätere Reviews/Diffs: für den Fresh-Context-Reviewer ausdrücklich gesperrt
- strukturiertes Finding-Schema: festgelegt
- Human-Disposition nach Blind-Abgabe: festgelegt

## Nächster erforderlicher Nachweis

`hardening/h3/FRESH_CONTEXT_TASK.md` in einem **neuen, sauberen Chat** ausführen.

Der Fresh-Context-Reviewer muss:

1. ausschließlich die erlaubten GitHub-Artefakte verwenden,
2. den historischen Blob direkt prüfen,
3. keine früheren Findings oder Diffs lesen,
4. strukturierte Findings ohne Rewrite abgeben.

Erst **nach** dieser Abgabe wird im regulären Kontext gegen die historisch bekannten Korrekturen dispositioniert.

## Mögliche nächste Statuswerte

- `CONTAMINATED` – verbotener Kontext wurde verwendet; Test wiederholen.
- `FAIL` – sauberer Blind-Test liefert für den Zweck keinen ausreichenden Nutzen.
- `PASS_FOR_PILOT` – sauberer Blind-Test findet reale, anschließend bestätigte Fehler bei vertretbarer False-Positive-Last.

`PASS_FOR_PILOT` bedeutet nicht, dass semantische QA allgemein validiert ist. Es reicht nur als Evidenz, den unabhängigen Review kontrolliert im echten Romanlauf einzusetzen.

## Aktuelle Hardening-Lage

- H1 Provenienzgranularität: PASS
- H2 Review-Template: PASS
- H3 unabhängiger semantischer Review: **NOT_YET_VALIDATED**

Issue #16 bleibt daher offen.
